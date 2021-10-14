#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import sys
import os
import wave

import ast

if not os.path.exists("model"):
    print ("Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
    exit (1)

wf = wave.open(sys.argv[1], "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
    exit (1)

model = Model("model")
# You can also specify the possible word list
rec = KaldiRecognizer(model, wf.getframerate(),'["Step 1 Proof yeast set oven to proofing for 5 minutes Step 2  First rise set oven to proofing for one and a half hours Step 3 Second rise set oven to proofing for 45 minutes Step 4 bake bread at 375 for 30 minutes", "[unk]"]')


while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())
#dict_vals = ast.literal_eval(rec.FinalResult())
print(rec.FinalResult())