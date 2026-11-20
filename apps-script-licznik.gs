// ============================================================
// MSZANA.INFO — LICZNIK ODSŁON (Google Apps Script)
// ============================================================
// Wklej CAŁĄ zawartość tego pliku do edytora Apps Script
// (script.google.com → Nowy projekt → Code.gs), a następnie:
//   1. Zapisz (Ctrl+S)
//   2. Wdróż → Nowe wdrożenie → typ: Aplikacja internetowa
//      • Wykonaj jako: JA
//      • Kto ma dostęp: KAŻDY (Anyone)
//   3. Skopiuj adres kończący się na /exec
//   4. Wklej go do config.js w polu APPS_SCRIPT_URL
//
// Licznik trzyma JEDNĄ liczbę w Właściwościach skryptu — nie wymaga
// arkusza, nie zbiera danych osobowych, nie zapisuje IP ani adresów.
// ============================================================

var PROP_KEY = 'MSZANA_VIEWS';
var LOCK_WAIT_MS = 10000;

/**
 * Zwiększa licznik o 1 i zwraca stan w formacie JSONP.
 * Wywołanie:  .../exec?action=count&callback=nazwaFunkcji
 */
function doGet(e) {
  var params = (e && e.parameter) || {};
  var action = String(params.action || '').toLowerCase();
  var callback = String(params.callback || '');
  var views;

  if (action === 'count') {
    views = incrementViews_();
  } else if (action === 'peek') {
    // podgląd bez zwiększania — przydatne do sprawdzenia wdrożenia
    views = getViews_();
  } else {
    return json_({ error: 'unknown_action', views: null }, callback);
  }

  return json_({ views: views, updated: new Date().toISOString() }, callback);
}

function doPost(e) {
  return doGet(e);
}

/** Zwiększa licznik z blokadą, żeby dwa równoczesne wejścia się nie zgubiły. */
function incrementViews_() {
  var lock = LockService.getScriptLock();
  try {
    lock.waitLock(LOCK_WAIT_MS);
  } catch (err) {
    // nie udało się zablokować — zwracamy bieżący stan bez zapisu
    return getViews_();
  }
  try {
    var props = PropertiesService.getScriptProperties();
    var current = parseInt(props.getProperty(PROP_KEY) || '0', 10);
    if (isNaN(current)) { current = 0; }
    current += 1;
    props.setProperty(PROP_KEY, String(current));
    return current;
  } finally {
    lock.releaseLock();
  }
}

function getViews_() {
  var raw = PropertiesService.getScriptProperties().getProperty(PROP_KEY) || '0';
  var n = parseInt(raw, 10);
  return isNaN(n) ? 0 : n;
}

/** Odpowiedź: JSONP, gdy podano callback; w przeciwnym razie czysty JSON. */
function json_(obj, callback) {
  var body = JSON.stringify(obj);
  if (callback && /^[A-Za-z_$][A-Za-z0-9_$]*$/.test(callback)) {
    return ContentService
      .createTextOutput(callback + '(' + body + ');')
      .setMimeType(ContentService.MimeType.JAVASCRIPT);
  }
  return ContentService
    .createTextOutput(body)
    .setMimeType(ContentService.MimeType.JSON);
}

// ============================================================
// NARZĘDZIA — uruchom ręcznie z edytora, jeśli chcesz coś sprawdzić
// ============================================================

/** Uruchom w edytorze: wpisz licznik ręcznie (np. 1500). */
function ustawLicznik(wartosc) {
  PropertiesService.getScriptProperties().setProperty(PROP_KEY, String(Number(wartosc) || 0));
  Logger.log('Licznik ustawiony na: ' + getViews_());
}

/** Uruchom w edytorze: pokaż bieżący stan. */
function pokazLicznik() {
  Logger.log('Odsłony: ' + getViews_());
}

/** Uruchom w edytorze: wyzeruj licznik. */
function wyzerujLicznik() {
  PropertiesService.getScriptProperties().setProperty(PROP_KEY, '0');
  Logger.log('Licznik wyzerowany.');
}
