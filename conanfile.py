from conans import ConanFile, CMake, tools
import os

class Conan2488(ConanFile):
    name = "Conan2488"
    version = "0.1"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "tests": [True, False]}
    generators = "cmake"

    default_options = (
        "shared=False",
        "tests=False"
    )

    def source(self):
        self.run("git clone https://github.com/JavierJF/Conan2488.git")
        self.run("cd Conan2488 && git checkout develop")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="Conan2488")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include/Conan2488", src="Conan2488/include")
        self.copy("*Conan2488.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["Conan2488"]
