@echo off
setlocal enabledelayedexpansion
chcp 65001 > nul

:: 1. 設置場所のチェック
set "ffmpegPath=%~dp0bin\ffmpeg.exe"

if not exist "!ffmpegPath!" (
    echo ❌ エラー: 設置場所が間違っているみたい...😱
    echo 「bin」フォルダの中に「ffmpeg.exe」が見つかりませんでした
    echo.
    echo 現在の確認場所: !ffmpegPath!
    echo 正しい場所にバッチファイルを置いてから、もう一度試してください
    pause
    exit /b
)

:: 2. ドロップされたファイルのチェック
if "%~1" == "" (
    echo ⚠️ 文字起こししたいファイルをドロップして起動して下さい ⚠️
    pause
    exit /b
)
set "inputFile=%~1"

:: 3. srtディレクトリの作成
set "srtDir=%~dp0srt"
if not exist "!srtDir!" (
    mkdir "!srtDir!"
)

:: 4. 日時取得
for /f "usebackq" %%i in (`powershell -command "Get-Date -Format 'yyyyMMddHHmmss'"`) do (
    set "timestamp=%%i"
)
set "outputFile=!timestamp!.srt"

:: 5. modelsディレクトリの存在チェック
set "targetDir=%~dp0models"
if not exist "!targetDir!" (
    echo エラー: 「models」ディレクトリがないよ😑
    echo !targetDir! を作成してからもう一度試してね
    pause
    exit /b
)

:: 6. モデル選択
:RETRY
cls
echo 🤖 model選択
echo --------------------------------------------------
echo 場所: !targetDir!
echo.

set count=0
for /f "delims=" %%f in ('dir /b /a-d "!targetDir!\*.bin" 2^>nul') do (
    set /a count+=1
    set "file!count!=%%f"
    echo [!count!] %%f
)

if %count%==0 (
    echo モデルが入ってないよ💦💦 先にモデルをダウンロードしてね
    pause
    exit /b
)

echo.
set /p choice="使用するモデルを選んで番号(1-%count%)を入力してください : "

if not defined file%choice% (
    echo '%choice%'は選択肢にないよ😑 もう一度入力してください🙏
    pause
    goto RETRY
)

set "modelName=!file%choice%!"

:: 7. 最終確認
cls
echo 🚀 準備できました🫡
echo --------------------------------------------------
echo 📹 対象ファイル    : !inputFile!
echo 🤖 モデル          : models/!modelName!
echo 📝 文字起こし結果  : srt/!outputFile!
echo --------------------------------------------------
echo.
echo 🌸 Enterキーを押すと処理を開始します！
pause > nul

echo.
echo 🏃 処理を実行中... しばらくお待ちください
echo --------------------------------------------------

pushd "%~dp0"
"!ffmpegPath!" -itsoffset 01:00:00 -i "!inputFile!" -vn -af "whisper=model=models/!modelName!:queue=20:destination=srt/!outputFile!:format=srt" -f null -
popd

echo --------------------------------------------------
if %errorlevel% equ 0 (
    echo 🎉 正常に完了しました！
    echo 📝 srt/!outputFile!
) else (
    echo ❌ 何かエラーが発生したみたい...😱
)
pause