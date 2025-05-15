@echo off
setlocal enabledelayedexpansion

:: Set working directory
set "WORKDIR=smcgroup_rebuild"
mkdir "%WORKDIR%"
cd "%WORKDIR%"

:: Define list of URLs
set urls[0]=https://web.archive.org/web/20250117064342/https://smcgroupksa.com/
set urls[1]=https://web.archive.org/web/20250117065734/https://smcgroupksa.com/about-us/
set urls[2]=https://web.archive.org/web/20241204081804/https://smcgroupksa.com/services/
set urls[3]=https://web.archive.org/web/20241204095822/https://smcgroupksa.com/contact-us/

:: Count of URLs
set COUNT=4

:: Loop over URLs
for /L %%i in (0,1,%COUNT%) do (
    call set "url=%%urls[%%i]%%"
    if defined url (
        echo Downloading !url!
        wget ^
            --no-host-directories ^
            --cut-dirs=4 ^
            --directory-prefix=. ^
            --convert-links ^
            --page-requisites ^
            --no-parent ^
            --html-extension ^
            --restrict-file-names=windows ^
            "!url!"
    )
)

:: Rename downloaded HTML files for convenience
ren "index.html" "home.html" 2>nul
ren "about-us.html" "about.html" 2>nul
ren "services.html" "services.html" 2>nul
ren "contact-us.html" "contact.html" 2>nul
ren "home.html" "index.html" 2>nul

echo.
echo ✅ Download complete.
pause
