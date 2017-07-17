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

class Script():
    
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions
        
    def __str__(self):
        return '\n'.join(self.instructions)
        
    def __repr__(self):
        return 'Script name: {name}\nCommands:\n{instructions}'\
                            .format(
                                    name = self.name,
                                    instructions = '\n'.join(self.instructions)
                                    )
    