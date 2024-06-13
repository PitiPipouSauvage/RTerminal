#include "C:\MinGW\include\stdlib.h"
#include <stdio.h>

/// OS {0 -> Windows, 1 -> Apple, 2 -> Linux, 3 -> Not supported}

#ifdef _WIN32
#define OS 0

#elif __APPLE__
#define OS 1

#elif __linux__
#define OS 2

#else
#define OS 3
#endif

int main() {
#ifdef _WIN32
    const char* download_py = (const char*)"curl --output C:\\Windows\\System32\\python_installer.ps1 https://raw.githubusercontent.com/jtmoon79/PythonEmbed4Win/main/PythonEmbed4Win.ps1";
    system(download_py);
    const char* install_py = (const char*)"powershell.exe -noexit \"Start-Process -Verb RunAs powershell .\\python_installer.ps1\"";
    system(install_py);

#elif __linux__
    const char* install_python_linux = (const char*)"sudo apt-get install -y python";
    system(install_python_linux);
    const char* install_pip = (const char*)"sudo apt-get install -y python-pip";
    system(install_pip);

#elif __APPLE__
    const char* install_homebrew = (const char*)"/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)\"";
    system(install_homebrew);
    const char* export = (const char*)"echo \"export PATH=\"/usr/local/opt/python/libexec/bin:$PATH\" >> ~/.profile";
    system(export);
    const char* install_python = (const char*)"brew install python";
    system(install_python);

#endif

    const char* command = (const char*)"pause";
    system(command);
    return 0;    
}