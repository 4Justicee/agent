# -*- coding: utf-8 -*-
'''
This Source Code Form is subject to the terms of the Mozilla
Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
'''
import sys
import monitor
import os

        
if __name__ == "__main__":
    main = monitor.Main()
    main._set_config_base_path(".." + os.sep + "core")
    monitor.Main.set_instance(main)
    main.start("window")
    sys.exit(0)
            


