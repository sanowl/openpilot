#!/usr/bin/env python3
import subprocess
import sys

from openpilot.common.prefix import OpenpilotPrefix
from security import safe_command


with OpenpilotPrefix():
  ret = safe_command.run(subprocess.call, sys.argv[1:])

exit(ret)
