# Placement Arena — Instant Public Tunnel Script
# Share a free HTTPS link with your friend so both of you can access Placement Arena!

$ROOT = Split-Path -Parent $MyInvocation.MyCommand.Path
$BACKEND = Join-Path $ROOT "backend"

Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "  Placement Arena — Instant Public Sharing    " -ForegroundColor Cyan
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

# Ensure backend server is running
$existing = Get-NetTCPConnection -LocalPort 8000 -State Listen -ErrorAction SilentlyContinue
if (-not $existing) {
    Write-Host "[1/2] Starting local server on http://127.0.0.1:8000 ..." -ForegroundColor Green
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$BACKEND'; python manage.py runserver 8000"
    Start-Sleep -Seconds 3
}

Write-Host "[2/2] Opening free public SSH tunnel via Serveo.net..." -ForegroundColor Green
Write-Host ""
Write-Host "Your friend can use the link printed below from ANY browser or phone!" -ForegroundColor Yellow
Write-Host ""

ssh -R 80:localhost:8000 serveo.net
