import os

from conans import ConanFile, CMake, tools


class NanoflannConan(ConanFile):
    name = "nanoflann"
    version = "master"
    license = "BSD"
    url = "https://github.com/J-Light/conan-nanoflann"
    description = ("nanoflann is a C++11 header-only library for building "
                   + "KD-Trees of datasets with different topologies")
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "build_benchmarks": [True, False],
        "build_examples": [True, False],
        "build_tests": [True, False]
    }
    default_options = (
        "shared=False",
        "build_benchmarks=False ",
        "build_examples=False ",
        "build_tests=False")
    generators = "cmake"

    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    def source(self):
        source_url = "https://github.com/jlblancoc/nanoflann"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self.source_subfolder)
        
    def build(self):
        # cmake = CMake(self)
        # cmake.definitions["BUILD_BENCHMARKS"] = self.options.build_benchmarks
        # cmake.definitions["BUILD_EXAMPLES"] = self.options.build_examples
        # cmake.definitions["BUILD_TESTS"] = self.options.build_tests
        # cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        # cmake.configure(build_folder=self.build_subfolder)
        # cmake.build()
        # cmake.install()
        return

    def package(self):
        header_dir = os.path.join(self.source_subfolder, "include")
        self.copy("*.hpp", dst="include", src=header_dir)

    def package_info(self):
        self.info.header_only()
        # self.cpp_info.libs = ["hello"]
        return
