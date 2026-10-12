<?php
declare(strict_types=1);

/*
 * Mszana.info — aggregate page-view counter
 * Counts endpoint calls only. It deliberately stores neither IP address,
 * User-Agent, cookie nor any other visitor identifier.
 */
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store, no-cache, must-revalidate, max-age=0');
header('Pragma: no-cache');
header('X-Content-Type-Options: nosniff');

if (($_SERVER['REQUEST_METHOD'] ?? 'GET') !== 'GET') {
    http_response_code(405);
    header('Allow: GET');
    echo json_encode(['error' => 'method_not_allowed'], JSON_UNESCAPED_UNICODE);
    exit;
}

$dataDir = __DIR__ . DIRECTORY_SEPARATOR . 'dane';
$dataFile = $dataDir . DIRECTORY_SEPARATOR . 'licznik.json';

if (!is_dir($dataDir) && !mkdir($dataDir, 0775, true) && !is_dir($dataDir)) {
    http_response_code(500);
    echo json_encode(['error' => 'counter_storage_unavailable'], JSON_UNESCAPED_UNICODE);
    exit;
}

$handle = fopen($dataFile, 'c+');
if ($handle === false || !flock($handle, LOCK_EX)) {
    if (is_resource($handle)) {
        fclose($handle);
    }
    http_response_code(500);
    echo json_encode(['error' => 'counter_storage_unavailable'], JSON_UNESCAPED_UNICODE);
    exit;
}

rewind($handle);
$raw = stream_get_contents($handle);
$stored = is_string($raw) ? json_decode($raw, true) : null;
$views = (is_array($stored) && isset($stored['views']) && is_numeric($stored['views'])) ? (int) $stored['views'] : 0;
$views = max(0, $views) + 1;

rewind($handle);
ftruncate($handle, 0);
fwrite($handle, json_encode(['views' => $views], JSON_UNESCAPED_UNICODE));
fflush($handle);
flock($handle, LOCK_UN);
fclose($handle);

echo json_encode(['views' => $views], JSON_UNESCAPED_UNICODE);
