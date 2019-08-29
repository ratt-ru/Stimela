import utils
import os
import sys
import logging
import Crasa.Crasa as crasa

sys.path.append("/scratch/stimela")

CONFIG = os.environ["CONFIG"]
INPUT = os.environ["INPUT"]
OUTPUT = os.environ["OUTPUT"]
MSDIR = os.environ["MSDIR"]

cab = utils.readJson(CONFIG)

args = {}
for param in cab['parameters']:
    name = param['name']
    value = param['value']

    if value is None:
        continue

    args[name] = value

task = crasa.CasaTask(cab["binary"], crash_on_severe=True, **args)
task.run()
