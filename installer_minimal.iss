; Minimal Inno Setup Script for testing

[Setup]
AppName=File Management Software Minimal
AppVersion=1.0
DefaultDirName={autopf}\File Management Software Minimal
OutputDir=.\installer_output_minimal
OutputBaseFilename=FileManagementSoftware_Minimal_Installer

[Files]
Source: "dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion

