# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.26

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/nsasurveillancevan/Téléchargements/CLion-2023.2.2/clion-2023.2.2/bin/cmake/linux/x64/bin/cmake

# The command to remove a file.
RM = /home/nsasurveillancevan/Téléchargements/CLion-2023.2.2/clion-2023.2.2/bin/cmake/linux/x64/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/nsasurveillancevan/Documents/RTerminal

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/nsasurveillancevan/Documents/RTerminal/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/RTerminal.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/RTerminal.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/RTerminal.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/RTerminal.dir/flags.make

CMakeFiles/RTerminal.dir/Bots/level_4/admin_panel.c.o: CMakeFiles/RTerminal.dir/flags.make
CMakeFiles/RTerminal.dir/Bots/level_4/admin_panel.c.o: /home/nsasurveillancevan/Documents/RTerminal/Bots/level_4/admin_panel.c
CMakeFiles/RTerminal.dir/Bots/level_4/admin_panel.c.o: CMakeFiles/RTerminal.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/nsasurveillancevan/Documents/RTerminal/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/RTerminal.dir/Bots/level_4/admin_panel.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/RTerminal.dir/Bots/level_4/admin_panel.c.o -MF CMakeFiles/RTerminal.dir/Bots/level_4/admin_panel.c.o.d -o CMakeFiles/RTerminal.dir/Bots/level_4/admin_panel.c.o -c /home/nsasurveillancevan/Documents/RTerminal/Bots/level_4/admin_panel.c

CMakeFiles/RTerminal.dir/Bots/level_4/admin_panel.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/RTerminal.dir/Bots/level_4/admin_panel.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/nsasurveillancevan/Documents/RTerminal/Bots/level_4/admin_panel.c > CMakeFiles/RTerminal.dir/Bots/level_4/admin_panel.c.i

CMakeFiles/RTerminal.dir/Bots/level_4/admin_panel.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/RTerminal.dir/Bots/level_4/admin_panel.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/nsasurveillancevan/Documents/RTerminal/Bots/level_4/admin_panel.c -o CMakeFiles/RTerminal.dir/Bots/level_4/admin_panel.c.s

# Object files for target RTerminal
RTerminal_OBJECTS = \
"CMakeFiles/RTerminal.dir/Bots/level_4/admin_panel.c.o"

# External object files for target RTerminal
RTerminal_EXTERNAL_OBJECTS =

RTerminal: CMakeFiles/RTerminal.dir/Bots/level_4/admin_panel.c.o
RTerminal: CMakeFiles/RTerminal.dir/build.make
RTerminal: CMakeFiles/RTerminal.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/nsasurveillancevan/Documents/RTerminal/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable RTerminal"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/RTerminal.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/RTerminal.dir/build: RTerminal
.PHONY : CMakeFiles/RTerminal.dir/build

CMakeFiles/RTerminal.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/RTerminal.dir/cmake_clean.cmake
.PHONY : CMakeFiles/RTerminal.dir/clean

CMakeFiles/RTerminal.dir/depend:
	cd /home/nsasurveillancevan/Documents/RTerminal/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/nsasurveillancevan/Documents/RTerminal /home/nsasurveillancevan/Documents/RTerminal /home/nsasurveillancevan/Documents/RTerminal/cmake-build-debug /home/nsasurveillancevan/Documents/RTerminal/cmake-build-debug /home/nsasurveillancevan/Documents/RTerminal/cmake-build-debug/CMakeFiles/RTerminal.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/RTerminal.dir/depend

