cmake_minimum_required(VERSION 3.26)
project(RTerminal C)

set(CMAKE_C_STANDARD 11)
find_package(OpenSSL REQUIRED)

add_executable(RTerminal
        Bots/level_4/admin_panel.c)
