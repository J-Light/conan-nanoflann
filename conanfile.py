import os

from conans import ConanFile, CMake, tools


class NanoflannConan(ConanFile):
    name = "nanoflann"
    version = "master"
    description = ("nanoflann is a C++11 header-only library for building "
                   + "KD-Trees of datasets with different topologies")
    url = "https://github.com/J-Light/conan-nanoflann"
    homepage = "https://github.com/jlblancoc/nanoflann"

    license = "BSD"

    exports = ['LICENSE.md']

    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"

    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [True, False],
        "build_benchmarks": [True, False],
        "build_examples": [True, False],
        "build_tests": [True, False]}
    default_options = (
        "shared=False",
        "build_benchmarks=False ",
        "build_examples=False ",
        "build_tests=False")

    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    def source(self):
        source_url = "https://github.com/jlblancoc/nanoflann"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_BENCHMARKS"] = self.options.build_benchmarks
        cmake.definitions["BUILD_EXAMPLES"] = self.options.build_examples
        cmake.definitions["BUILD_TESTS"] = self.options.build_tests
        cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        cmake.configure(build_folder=self.build_subfolder)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.info.header_only()
