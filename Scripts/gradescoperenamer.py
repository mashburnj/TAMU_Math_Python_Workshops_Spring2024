import numpy as np
import os
import yaml

section = 532

with open('./submissions/submission_metadata.yml', 'r') as file:
    meta = yaml.safe_load(file)

os.chdir('./submissions/')
for submission in SubmissionList:
    os.rename(submission, str(section) + ' ' + meta[submission][':submitters'][0][':name'] + '.pdf')
os.chdir('..')
