import os
import sys

sys.path.append("/utils")
import utils

CONFIG = os.environ["CONFIG"]
INPUT = os.environ["INPUT"]
OUTPUT = os.environ["OUTPUT"]
MSDIR = os.environ["MSDIR"]

options = utils.readJson(CONFIG)
vis = options.pop("msname")
options["vis"] = MSDIR + "/" + vis

gains = options.pop("gaintable", [])

for i,item in enumerate(gains):
    gains[i] = utils.substitute_globals(item) or INPUT+"/"+item

options["gaintable"] = gains
print gains
sys.exit(0)

utils.icasa("applycal", **options)
