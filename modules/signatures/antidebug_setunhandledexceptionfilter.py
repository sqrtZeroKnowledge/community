# CAPE - Config And Payload Extraction
# Copyright(C) 2018 redsand (redsand@redsand.net)
#
# This program is free software : you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.If not, see <http://www.gnu.org/licenses/>.

from lib.cuckoo.common.abstracts import Signature


class antidebug_setunhandledexceptionfilter(Signature):
    name = "antidebug_setunhandledexceptionfilter"
    description = "SetUnhandledExceptionFilter detected (possible anti-debug)"
    severity = 1
    categories = ["anti-debug"]
    authors = ["redsand"]
    minimum = "1.3"
    evented = True
    ttps = ["T1106"]  # MITRE v6,7,8
    ttps += ["U0108"]  # Unprotect
    mbcs = ["OB0001", "B0001", "B0001.030"]

    filter_apinames = set(["SetUnhandledExceptionFilter"])

    def on_call(self, call, process):
        if call["api"] == "SetUnhandledExceptionFilter":
            if self.pid:
                self.mark_call()
            return True
