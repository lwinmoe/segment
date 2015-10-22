cmake_minimum_required(VERSION 3.2)
project(segment)

set(EXECUTABLE_NAME "segment")
add_definitions(-std=c99)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

#find_library(foma.a PATHS /usr/local/lib)
find_library(foma.a PATHS ${CMAKE_SYSTEM_LIBRARY_PATH})
find_package( ZLIB REQUIRED )
set(SOURCE_FILES main.c)
add_executable(${EXECUTABLE_NAME} ${SOURCE_FILES})
target_link_libraries(${EXECUTABLE_NAME} libfoma.a ${ZLIB_LIBRARIES})