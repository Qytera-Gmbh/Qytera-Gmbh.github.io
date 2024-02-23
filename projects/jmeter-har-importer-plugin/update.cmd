IF EXIST ".tmp" (
    RMDIR /S /Q ".tmp"
)
mkdir ".tmp"
git clone --depth 1 https://github.com/Qytera-Gmbh/JMeterHARImporterPlugin.git .tmp
robocopy ".tmp/docs" "docs/docs" /E
move ".tmp\README.md" "docs\index.md"
