# Copyright (C) 2017 Antoine Fourmy <antoine dot fourmy at gmail dot com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
from inspect import stack
from os.path import abspath, dirname
from cx_Freeze import setup, Executable

# prevent python from writing *.pyc files / __pycache__ folders
sys.dont_write_bytecode = True

path_app = dirname(abspath(stack()[0][1]))

if path_app not in sys.path:
    sys.path.append(path_app)
        
build_options = dict(
                     compressed = True,
                     path = sys.path + [path_app]
                     )

setup(
      name = 'pyNMS',
      version = '0.1',
      description = 'pyNMS - a carrier-grade Network Management System',
      options = dict(build_exe=build_options),
      executables = [Executable('main.py')],
      )