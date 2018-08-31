# ----------------------------------------------------------------------------------#
# //////////////////////////////////////////////////////////////////////////////////#
# ----------------------------------------------------------------------------------#
#
#  Copyright (C) 2017, StepToSky
#  All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  1.Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#  2.Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and / or other materials provided with the distribution.
#  3.Neither the name of StepToSky nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  DISCLAIMED.IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
#  ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#  ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#  Contacts: www.steptosky.com
#
# ----------------------------------------------------------------------------------#
# //////////////////////////////////////////////////////////////////////////////////#
# ----------------------------------------------------------------------------------#

import os
from conans import ConanFile, tools
from distutils.version import StrictVersion


class Sdk3DsMaxConan(ConanFile):
    name = 'PKG_NAME'
    version = 'last'
    description = "Conan recipe for 3DsMax SDK."
    url = 'https://github.com/Pancir/conan-3dsmax-sdk-recipes'

    max_sdk = os.getenv("MAX_SDK_DIR")
    data_dir = 'data'

    def package(self):
        self.copy(pattern='*',
                  dst=os.path.join(self.data_dir, "include"),
                  src=os.path.join(self.max_sdk, "include"),
                  keep_path=True)
        self.copy(pattern='*',
                  dst=os.path.join(self.data_dir, "x64"),
                  src=os.path.join(self.max_sdk, "x64"),
                  keep_path=True)
        self.copy(pattern='*',
                  dst=os.path.join(self.data_dir, "lib"),
                  src=os.path.join(self.max_sdk, "lib"),
                  keep_path=True)

    def package_info(self):
        lib_dir = os.path.join(self.package_folder, self.data_dir, self.get_lib_dir())
        self.cpp_info.libdirs = [lib_dir]
        self.cpp_info.includedirs = [os.path.join(self.data_dir, 'include')]
        self.cpp_info.libs = tools.collect_libs(self, lib_dir)
        if len(self.cpp_info.libs) == 0:
            raise Exception('3DsMax Sdk libraries are not found, probably there is a mistake in the recipe.')
        if StrictVersion('SDK_VERSION') > StrictVersion('14.0'):
            self.cpp_info.defines = ['_UNICODE', 'UNICODE']
            self.cpp_info.cflags = ['-D_UNICODE', '-DUNICODE']
            self.cpp_info.cppflags = ['-D_UNICODE', '-DUNICODE']

    @staticmethod
    def get_lib_dir():
        lib_dir = os.path.join('x64', 'lib')
        if StrictVersion('SDK_VERSION') > StrictVersion('15.0'):
            lib_dir = os.path.join('lib', 'x64', 'Release')
        return lib_dir

# ----------------------------------------------------------------------------------#
# //////////////////////////////////////////////////////////////////////////////////#
# ----------------------------------------------------------------------------------#
