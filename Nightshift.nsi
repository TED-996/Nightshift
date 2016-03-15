############################################################################################
#      NSIS Installation Script created by NSIS Quick Setup Script Generator v1.09.18
#               Entirely Edited with NullSoft Scriptable Installation System                
#              by Vlasis K. Barkas aka Red Wine red_wine@freemail.gr Sep 2006               
############################################################################################

!define APP_NAME "Nightshift"
!define COMP_NAME "TED96"
!define VERSION "1.00.00.00"
!define COPYRIGHT "TED96"
!define DESCRIPTION "Shift your wallpaper at night!"
!define LICENSE_TXT "LICENSE.txt"
!define INSTALLER_NAME "InstallNightshift.exe"
!define MAIN_APP_EXE "nightshift.exe"
!define SETUP_APP_EXE "nightshift_setup.exe"
!define INSTALL_TYPE "SetShellVarContext current"
!define REG_ROOT "HKCU"
!define REG_APP_PATH "Software\Microsoft\Windows\CurrentVersion\App Paths\${MAIN_APP_EXE}"
!define UNINSTALL_PATH "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}"

!define REG_START_MENU "Start Menu Folder"

var SM_Folder

######################################################################

VIProductVersion  "${VERSION}"
VIAddVersionKey "ProductName"  "${APP_NAME}"
VIAddVersionKey "CompanyName"  "${COMP_NAME}"
VIAddVersionKey "LegalCopyright"  "${COPYRIGHT}"
VIAddVersionKey "FileDescription"  "${DESCRIPTION}"
VIAddVersionKey "FileVersion"  "${VERSION}"

######################################################################

SetCompressor ZLIB
Name "${APP_NAME}"
Caption "${APP_NAME}"
OutFile "${INSTALLER_NAME}"
BrandingText "${APP_NAME}"
XPStyle on
InstallDirRegKey "${REG_ROOT}" "${REG_APP_PATH}" ""
InstallDir "$PROGRAMFILES\Nightshift"

######################################################################

!include "MUI.nsh"
!include "nsProcess.nsh"

!define MUI_ABORTWARNING
!define MUI_UNABORTWARNING

!insertmacro MUI_PAGE_WELCOME

!ifdef LICENSE_TXT
!insertmacro MUI_PAGE_LICENSE "${LICENSE_TXT}"
!endif

!insertmacro MUI_PAGE_DIRECTORY

!ifdef REG_START_MENU
!define MUI_STARTMENUPAGE_DEFAULTFOLDER "Nightshift"
!define MUI_STARTMENUPAGE_REGISTRY_ROOT "${REG_ROOT}"
!define MUI_STARTMENUPAGE_REGISTRY_KEY "${UNINSTALL_PATH}"
!define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "${REG_START_MENU}"
!insertmacro MUI_PAGE_STARTMENU Application $SM_Folder
!endif

!insertmacro MUI_PAGE_INSTFILES

!define MUI_FINISHPAGE_RUN_TEXT "Set up Nightshift"
!define MUI_FINISHPAGE_RUN "$INSTDIR\${SETUP_APP_EXE}"

!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_CONFIRM

!insertmacro MUI_UNPAGE_INSTFILES

!insertmacro MUI_UNPAGE_FINISH

!insertmacro MUI_LANGUAGE "English"

######################################################################

Section -MainProgram
${INSTALL_TYPE}
SetOverwrite ifnewer
SetOutPath "$INSTDIR"
File "dist\*"

CreateShortCut "$SMSTARTUP\Nightshift.lnk" "$INSTDIR\${MAIN_APP_EXE}"

SectionEnd

######################################################################

Section -Icons_Reg
SetOutPath "$INSTDIR"
WriteUninstaller "$INSTDIR\uninstall.exe"

!ifdef REG_START_MENU
!insertmacro MUI_STARTMENU_WRITE_BEGIN Application
CreateDirectory "$SMPROGRAMS\$SM_Folder"
CreateShortCut "$SMPROGRAMS\$SM_Folder\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$SMPROGRAMS\$SM_Folder\Set up Nightshift.lnk" "$INSTDIR\${SETUP_APP_EXE}"
CreateShortCut "$SMPROGRAMS\$SM_Folder\Uninstall Nightshift.lnk" "$INSTDIR\uninstall.exe"
!ifdef WEB_SITE
WriteIniStr "$INSTDIR\${APP_NAME} website.url" "InternetShortcut" "URL" "${WEB_SITE}"
CreateShortCut "$SMPROGRAMS\$SM_Folder\${APP_NAME} Website.lnk" "$INSTDIR\${APP_NAME} website.url"
!endif
!insertmacro MUI_STARTMENU_WRITE_END
!endif

!ifndef REG_START_MENU
CreateDirectory "$SMPROGRAMS\Nightshift"
CreateShortCut "$SMPROGRAMS\Nightshift\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$SMPROGRAMS\Nightshift\Set up Nightshift.lnk" "$INSTDIR\${SETUP_APP_EXE}"
CreateShortCut "$SMPROGRAMS\Nightshift\Uninstall Nightshift.lnk" "$INSTDIR\uninstall.exe"
!ifdef WEB_SITE
WriteIniStr "$INSTDIR\${APP_NAME} website.url" "InternetShortcut" "URL" "${WEB_SITE}"
CreateShortCut "$SMPROGRAMS\Nightshift\${APP_NAME} Website.lnk" "$INSTDIR\${APP_NAME} website.url"
!endif
!endif

WriteRegStr ${REG_ROOT} "${REG_APP_PATH}" "" "$INSTDIR\${MAIN_APP_EXE}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "DisplayName" "${APP_NAME}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "UninstallString" "$INSTDIR\uninstall.exe"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "DisplayIcon" "$INSTDIR\${MAIN_APP_EXE}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "DisplayVersion" "${VERSION}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "Publisher" "${COMP_NAME}"

!ifdef WEB_SITE
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "URLInfoAbout" "${WEB_SITE}"
!endif
SectionEnd

######################################################################

Section Uninstall
${INSTALL_TYPE}


# kill nightshift
${nsProcess::CloseProcess} "${MAIN_APP_EXE}" $R0
${nsProcess::Unload}


Delete "$INSTDIR\bz2.pyd"
Delete "$INSTDIR\CRYPT32.dll"
Delete "$INSTDIR\library.zip"
Delete "$INSTDIR\mfc90.dll"
Delete "$INSTDIR\nightshift.exe"
Delete "$INSTDIR\nightshift_cmd.exe"
Delete "$INSTDIR\nightshift_setup.exe"
Delete "$INSTDIR\PIL._imaging.pyd"
Delete "$INSTDIR\pyexpat.pyd"
Delete "$INSTDIR\python27.dll"
Delete "$INSTDIR\pywintypes27.dll"
Delete "$INSTDIR\select.pyd"
Delete "$INSTDIR\unicodedata.pyd"
Delete "$INSTDIR\win32api.pyd"
Delete "$INSTDIR\win32pipe.pyd"
Delete "$INSTDIR\win32ui.pyd"
Delete "$INSTDIR\_ctypes.pyd"
Delete "$INSTDIR\_hashlib.pyd"
Delete "$INSTDIR\_socket.pyd"
Delete "$INSTDIR\_ssl.pyd"
Delete "$INSTDIR\uninstall.exe"
!ifdef WEB_SITE
Delete "$INSTDIR\${APP_NAME} website.url"
!endif

RmDir "$INSTDIR"
Delete "$SMSTARTUP\Nightshift.lnk"

!ifdef REG_START_MENU
!insertmacro MUI_STARTMENU_GETFOLDER "Application" $SM_Folder
Delete "$SMPROGRAMS\$SM_Folder\${APP_NAME}.lnk"
Delete "$SMPROGRAMS\$SM_Folder\Set up Nightshift.lnk"
Delete "$SMPROGRAMS\$SM_Folder\Uninstall Nightshift.lnk"
!ifdef WEB_SITE
Delete "$SMPROGRAMS\$SM_Folder\${APP_NAME} Website.lnk"
!endif
RmDir "$SMPROGRAMS\$SM_Folder"
!endif

!ifndef REG_START_MENU
Delete "$SMPROGRAMS\Nightshift\${APP_NAME}.lnk"
Delete "$SMPROGRAMS\Nightshift\Set up Nightshift.lnk"
Delete "$SMPROGRAMS\Nightshift\Uninstall Nightshift.lnk"
!ifdef WEB_SITE
Delete "$SMPROGRAMS\Nightshift\${APP_NAME} Website.lnk"
!endif
RmDir "$SMPROGRAMS\Nightshift"
!endif

RMDir /r "$LOCALAPPDATA\Nightshift"

DeleteRegKey ${REG_ROOT} "${REG_APP_PATH}"
DeleteRegKey ${REG_ROOT} "${UNINSTALL_PATH}"

SectionEnd

######################################################################

