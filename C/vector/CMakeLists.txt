cmake_minimum_required(VERSION 3.6)
project(vector)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES
    vector.c
    vector.h)

add_executable(vector ${SOURCE_FILES})