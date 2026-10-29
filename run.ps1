# Script para iniciar o servidor FastAPI com uvicorn

# Verificar se está no diretório correto
$currentDir = Get-Location
$targetDir = "C:\Users\DELL\Documents"

if ($currentDir -ne $targetDir) {
    Write-Host "Mudando para o diretório do projeto..." -ForegroundColor Cyan
    Set-Location -Path $targetDir
}

Write-Host "Iniciando servidor FastAPI..." -ForegroundColor Green
Write-Host "Acesse: http://127.0.0.1:8000" -ForegroundColor Yellow
Write-Host "Documentação: http://127.0.0.1:8000/docs" -ForegroundColor Yellow
Write-Host "Pressione CTRL+C para parar o servidor." -ForegroundColor Cyan
Write-Host "" -ForegroundColor Gray

python -m uvicorn crud_filmes_e_series:app --reload
