# README

### 1. What is this?

Example project to test conan issue.

#### Building

In project folder:

For debugging purposes:

1. mkdir build && cd build
3. cmake -G "Visual Studio 15 Win64" -DCMAKE_BUILD_TESTS=ON ..
4. cmake --build . --target ALL_BUILD --config Debug

For building a release version:

1. mkdir build && cd build
3. cmake -G "Visual Studio 15 Win64" -DCMAKE_BUILD_TESTS=ON ..
4. cmake --build . --target ALL_BUILD --config Release
