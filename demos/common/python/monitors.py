"""
 Copyright (C) 2020-2024 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

import os
if hasattr(os, "add_dll_directory"):
    for path in os.environ.get("PATH", "").split(";"):
        if os.path.isdir(path):
            os.add_dll_directory(path)
try:
    from monitors_extension import Presenter
except ImportError:
    import logging as log


    class Presenter:
        def __init__(self, keys, yPos=20, graphSize=(150, 60), historySize=20):
            self.yPos = yPos
            self.graphSize = graphSize
            self.graphPadding = 0
            if keys:
                log.warning("monitors_extension wasn't found")

        def handleKey(self, key): pass

        def drawGraphs(self, frame): pass

        def reportMeans(self): return ''
