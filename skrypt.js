/* Mszana.info — licznik, czcionka, kontrast, menu mobilne, modal RODO, formularze */

(function(){
  "use strict";
  var store = {
    get:function(k){ try{ return window.localStorage ? localStorage.getItem(k) : null; }catch(e){ return null; } },
    set:function(k,v){ try{ if(window.localStorage) localStorage.setItem(k,v); }catch(e){} }
  };

  /* ---------- Rok w stopce ---------- */
  var y = document.getElementById('year');
  if(y){ y.textContent = new Date().getFullYear(); }

  /* ---------- Zwiększanie / zmniejszanie czcionki ---------- */
  var FS_KEY = 'mszana_font_step', step = parseInt(store.get(FS_KEY) || '0', 10) || 0;
  function applyFont(){
    step = Math.max(-2, Math.min(4, step));
    document.documentElement.style.fontSize = (100 + step * 10) + '%';
    store.set(FS_KEY, String(step));
  }
  applyFont();
  var fMinus = document.getElementById('fontMinus'),
      fReset = document.getElementById('fontReset'),
      fPlus  = document.getElementById('fontPlus');
  if(fMinus){ fMinus.addEventListener('click', function(){ step--; applyFont(); announce('Czcionka zmniejszona.'); }); }
  if(fReset){ fReset.addEventListener('click', function(){ step = 0; applyFont(); announce('Przywrócono domyślną wielkość czcionki.'); }); }
  if(fPlus ){ fPlus .addEventListener('click', function(){ step++; applyFont(); announce('Czcionka zwiększona.'); }); }

  /* ---------- Tryb wysokiego kontrastu ---------- */
  var HC_KEY = 'mszana_hc', hcBtn = document.getElementById('hcToggle');
  function applyHC(on){
    document.documentElement.classList.toggle('hc', on);
    if(hcBtn){ hcBtn.setAttribute('aria-pressed', on ? 'true' : 'false'); }
    store.set(HC_KEY, on ? '1' : '0');
  }
  applyHC(store.get(HC_KEY) === '1');
  if(hcBtn){ hcBtn.addEventListener('click', function(){
    var on = !document.documentElement.classList.contains('hc');
    applyHC(on); announce(on ? 'Włączono tryb wysokiego kontrastu.' : 'Wyłączono tryb wysokiego kontrastu.');
  }); }

  /* ---------- Menu mobilne ---------- */
  var burger = document.getElementById('burger'), nav = document.getElementById('navMain');
  if(burger && nav){
    burger.addEventListener('click', function(){
      var open = nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      burger.textContent = open ? '✕ Zamknij' : '☰ Menu';
    });
    nav.addEventListener('click', function(e){
      if(e.target.tagName === 'A' && window.innerWidth <= 820){
        nav.classList.remove('open'); burger.setAttribute('aria-expanded','false'); burger.textContent = '☰ Menu';
      }
    });
  }


  /* ---------- Rozwijane menu „O nas” ---------- */
  var submenuToggles = document.querySelectorAll('.submenu-toggle');
  submenuToggles.forEach(function(toggle){
    var holder = toggle.closest ? toggle.closest('.has-submenu') : toggle.parentNode;
    if(!holder){ return; }
    toggle.addEventListener('click', function(e){
      e.preventDefault();
      var open = holder.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  document.addEventListener('click', function(e){
    submenuToggles.forEach(function(toggle){
      var holder = toggle.closest ? toggle.closest('.has-submenu') : toggle.parentNode;
      if(holder && !holder.contains(e.target)){
        holder.classList.remove('open');
        toggle.setAttribute('aria-expanded','false');
      }
    });
  });
  document.addEventListener('keydown', function(e){
    if(e.key !== 'Escape'){ return; }
    submenuToggles.forEach(function(toggle){
      var holder = toggle.closest ? toggle.closest('.has-submenu') : toggle.parentNode;
      if(holder){ holder.classList.remove('open'); toggle.setAttribute('aria-expanded','false'); }
    });
  });

  /* ---------- Modal RODO ---------- */
  var modal = document.getElementById('rodoModal'), lastFocus = null;
  function openRodo(e){
    if(e){ e.preventDefault(); }
    if(!modal){ return; }
    lastFocus = document.activeElement;
    modal.hidden = false;
    document.body.style.overflow = 'hidden';
    var closeBtn = document.getElementById('rodoClose');
    if(closeBtn){ closeBtn.focus(); }
  }
  function closeRodo(){
    if(!modal){ return; }
    modal.hidden = true;
    document.body.style.overflow = '';
    if(lastFocus && lastFocus.focus){ lastFocus.focus(); }
  }
  ['rodoOpenTop','rodoOpenFooter','rodoLinkInline','rodoLinkForm'].forEach(function(id){
    var el = document.getElementById(id);
    if(el){ el.addEventListener('click', openRodo); }
  });
  ['rodoClose','rodoClose2','rodoToReg'].forEach(function(id){
    var el = document.getElementById(id);
    if(el){ el.addEventListener('click', closeRodo); }
  });
  if(modal){
    modal.addEventListener('click', function(e){ if(e.target === modal){ closeRodo(); } });
  }
  document.addEventListener('keydown', function(e){
    if(e.key === 'Escape' && modal && !modal.hidden){ closeRodo(); }
    /* Pułapka fokusu w modalu */
    if(e.key === 'Tab' && modal && !modal.hidden){
      var f = modal.querySelectorAll('a[href], button, input, [tabindex]:not([tabindex="-1"])');
      if(!f.length){ return; }
      var first = f[0], last = f[f.length - 1];
      if(e.shiftKey && document.activeElement === first){ e.preventDefault(); last.focus(); }
      else if(!e.shiftKey && document.activeElement === last){ e.preventDefault(); first.focus(); }
    }
  });

  /* ---------- Formularze: walidacja + komunikat ---------- */
  function announce(msg){
    var box = document.getElementById('formMsg');
    if(box && msg){ box.textContent = msg; }
  }
  function handleForm(formId, okMsg, requireCheckbox){
    var form = document.getElementById(formId);
    if(!form){ return; }
    form.addEventListener('submit', function(e){
      var msg = document.getElementById('formMsg');
      var email = form.querySelector('input[type="email"]');
      var text  = form.querySelector('textarea[required]');
      var box   = form.querySelector('input[type="checkbox"][required]');
      function bad(text_, field){
        e.preventDefault();
        if(msg){ msg.textContent = text_; msg.classList.add('show'); }
        if(field && field.focus){ field.focus(); }
      }
      if(email && (!email.value || email.value.indexOf('@') < 1)){ return bad('Podaj poprawny adres e-mail, żebyśmy mogli odpowiedzieć.', email); }
      if(text && text.value.trim().length < 10){ return bad('Uzupełnij treść wiadomości (minimum kilka słów).', text); }
      if(requireCheckbox && box && !box.checked){ return bad('Zaznacz zgodę na przetwarzanie danych (klauzula RODO).', box); }
      if(msg){ msg.textContent = okMsg; msg.classList.add('show'); }
      /* Formularz działa przez klienta poczty użytkownika (action="mailto:...") */
    });
  }
  handleForm('contactForm', 'Trwa przekazywanie wiadomości…', true);
  handleForm('correctionForm', 'Dziękujemy! Sprostowanie zostanie przekazane na kontakt@mszana.info i potraktowane priorytetowo zgodnie z Regulaminem.', false);

  /* ---------- Google Apps Script: formularz i zbiorczy licznik ---------- */
  function appsScriptUrl(){
    var cfg = window.MSZANA_CONFIG || {};
    var url = typeof cfg.APPS_SCRIPT_URL === 'string' ? cfg.APPS_SCRIPT_URL.trim() : '';
    return /^https:\/\/script\.google\.com\/macros\/s\/[A-Za-z0-9_-]+\/exec$/.test(url) ? url : '';
  }
  function setFormMessage(message, isError){
    var msg = document.getElementById('formMsg');
    if(!msg){ return; }
    msg.textContent = message;
    msg.classList.add('show');
    msg.classList.toggle('error', !!isError);
  }
  function initContactDelivery(){
    var form = document.getElementById('contactForm');
    if(!form){ return; }
    var startedAt = document.getElementById('formStartedAt');
    if(startedAt){ startedAt.value = String(Date.now()); }
    var endpoint = appsScriptUrl();
    var frame = document.getElementById('contactTransport');
    var sent = false;
    if(!endpoint){
      form.addEventListener('submit', function(e){
        if(e.defaultPrevented){ return; }
        e.preventDefault();
        setFormMessage('Formularz wymaga jeszcze adresu wdrożonego Google Apps Script. Administrator powinien uzupełnić plik config.js.', true);
      });
      return;
    }
    form.action = endpoint;
    form.method = 'post';
    form.enctype = 'application/x-www-form-urlencoded';
    form.target = 'contactTransport';
    form.addEventListener('submit', function(e){
      if(e.defaultPrevented){ return; }
      sent = true;
      setFormMessage('Wiadomość jest wysyłana…', false);
    });
    if(frame){
      frame.addEventListener('load', function(){
        if(!sent){ return; }
        sent = false;
        form.reset();
        setFormMessage('Wiadomość została przekazana na adres kontaktowy. Odpowiemy możliwie szybko.', false);
      });
    }
  }
  function initViewCounter(){
    var fields = document.querySelectorAll('[data-view-counter]');
    var button = document.querySelector('[data-view-counter-consent]');
    var note = document.querySelector('[data-view-counter-note]');
    var endpoint = appsScriptUrl();
    var requested = false;
    function setFields(value){ fields.forEach(function(field){ field.textContent = value; }); }
    function setNote(value){ if(note){ note.textContent = value; } }
    function requestCounter(){
      if(requested || !endpoint){ return; }
      requested = true;
      setFields('…');
      var callback = 'mszanaCounterCallback_' + Date.now() + '_' + Math.floor(Math.random()*100000);
      window[callback] = function(data){
        var views = data && typeof data.views === 'number' ? data.views : null;
        setFields(views === null ? '—' : new Intl.NumberFormat('pl-PL').format(views));
        setNote(views === null ? 'Nie udało się pobrać licznika.' : 'łączna liczba odsłon serwisu');
        if(button){ button.hidden = true; }
        delete window[callback];
      };
      var script = document.createElement('script');
      script.src = endpoint + '?action=count&callback=' + encodeURIComponent(callback) + '&_=' + Date.now();
      script.async = true;
      script.onerror = function(){
        setFields('—'); setNote('Nie udało się pobrać licznika.');
        delete window[callback];
      };
      document.head.appendChild(script);
    }
    if(!fields.length){ return; }
    if(!endpoint){
      setFields('—');
      setNote('licznik zostanie uruchomiony po konfiguracji serwisu');
      if(button){ button.hidden = true; }
      return;
    }
    if(button){ button.hidden = true; }
    requestCounter();
  }
  initContactDelivery();
  initViewCounter();
})();

/* =========================================================
   Dekoder zapasowy adresow e-mail
   Cloudflare podmienia adresy skryptem email-decode.min.js.
   Gdy strona jest serwowana poza Cloudflare (github.io, podglad
   lokalny), ten dekoder robi to samo w przegladarce. Jesli
   Cloudflare juz podmienil adresy, petle ponizej nic nie znajduja.
   ========================================================= */
(function(){
  "use strict";
  function dekoduj(hex){
    if(typeof hex !== "string" || hex.length < 4 || /[^0-9a-fA-F]/.test(hex)){ return ""; }
    var klucz = parseInt(hex.substr(0, 2), 16), out = "";
    for(var i = 2; i + 1 < hex.length; i += 2){
      out += String.fromCharCode(parseInt(hex.substr(i, 2), 16) ^ klucz);
    }
    return out;
  }
  function poprawny(a){ return typeof a === "string" && a.indexOf("@") > 0 && a.indexOf(" ") < 0; }
  function napraw(){
    var i, el, adres, link;
    var znaczniki = document.querySelectorAll("[data-cfemail]");
    for(i = 0; i < znaczniki.length; i++){
      el = znaczniki[i];
      adres = dekoduj(el.getAttribute("data-cfemail"));
      if(!poprawny(adres)){ continue; }
      el.textContent = adres;
      if(el.classList){ el.classList.remove("__cf_email__"); }
      el.removeAttribute("data-cfemail");
      link = el.tagName === "A" ? el : (el.parentNode && el.parentNode.tagName === "A" ? el.parentNode : null);
      if(link && (link.getAttribute("href") || "").indexOf("/cdn-cgi/l/email-protection") === 0){
        link.setAttribute("href", "mailto:" + adres);
      }
    }
    var linki = document.querySelectorAll('a[href^="/cdn-cgi/l/email-protection"]');
    for(i = 0; i < linki.length; i++){
      link = linki[i];
      adres = dekoduj(link.getAttribute("href").split("#")[1] || "");
      if(!poprawny(adres)){ continue; }
      link.setAttribute("href", "mailto:" + adres);
      if(link.textContent.indexOf("[email") > -1){ link.textContent = adres; }
    }
  }
  if(document.readyState === "loading"){ document.addEventListener("DOMContentLoaded", napraw); }
  else { napraw(); }
  window.addEventListener("load", napraw);
})();
