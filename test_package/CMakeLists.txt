project(PackageTest CXX)
cmake_minimum_required(VERSION 3.0.0)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(pointcloud_example pointcloud_example.cpp)
target_link_libraries(pointcloud_example ${CONAN_LIBS})
set_property(TARGET pointcloud_example PROPERTY CXX_STANDARD 11)
