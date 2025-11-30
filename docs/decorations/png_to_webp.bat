@echo off
for %%f in (*.png) do (
    ffmpeg -i "%%f" "%%~nf.webp"
)
