# Placement Arena — Single-Server Startup Script (Windows PowerShell)
# Run this from the PlacementArena root directory.

$ErrorActionPreference = "Stop"
$ROOT = Split-Path -Parent $MyInvocation.MyCommand.Path
$BACKEND = Join-Path $ROOT "backend"

Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "  Placement Arena — Starting Dev Environment  " -ForegroundColor Cyan
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

# Create today's exam if it doesn't exist
Write-Host "[1/2] Checking today's exam..." -ForegroundColor Green
Push-Location $BACKEND
python manage.py create_daily_exam
Pop-Location

# Check if Django server is already running
$existing = Get-NetTCPConnection -LocalPort 8000 -State Listen -ErrorAction SilentlyContinue
if ($existing) {
    Write-Host "[INFO] Django server already running on http://127.0.0.1:8000" -ForegroundColor Yellow
} else {
    Write-Host ""
    Write-Host "[2/2] Starting Django backend & frontend server on http://127.0.0.1:8000 ..." -ForegroundColor Green
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$BACKEND'; python manage.py runserver 8000"
    Start-Sleep -Seconds 2
}

Write-Host ""
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "  Placement Arena is READY!" -ForegroundColor Green
Write-Host ""
Write-Host "  Login Portal:     http://127.0.0.1:8000/login/index.html" -ForegroundColor White
Write-Host "  App Admin Panel:  http://127.0.0.1:8000/panel/index.html" -ForegroundColor White
Write-Host "  Django DB Admin:  http://127.0.0.1:8000/admin/" -ForegroundColor White
Write-Host "  API Root:         http://127.0.0.1:8000/api/" -ForegroundColor White
Write-Host ""
Write-Host "  Credentials:" -ForegroundColor Gray
Write-Host "    Admin:       admin1 / admin@123" -ForegroundColor Gray
Write-Host "    Candidate 1: candidate1 / candidate@123" -ForegroundColor Gray
Write-Host "    Candidate 2: candidate2 / candidate@123" -ForegroundColor Gray
Write-Host "===============================================" -ForegroundColor Cyan
