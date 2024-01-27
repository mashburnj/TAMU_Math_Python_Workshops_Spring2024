import numpy as np
import os
from PyPDF2 import PdfWriter, PdfReader

# First, get  the list of submission files.
os.chdir('./Section 532/')
SubmissionList = np.array(os.listdir())
SubmissionList = SubmissionList[ np.char.endswith(SubmissionList, '.pdf') ] # filters the list by names ending in ".pdf"
os.chdir('..')

# Then for each, extract the back page and save to a new file in a separate folder.
for submission in SubmissionList:
    inputpdf = PdfReader(open('./Section 532/' + submission, "rb"))
    output = PdfWriter()
    for pg in inputpdf.pages[1:]:
        output.add_page(pg) # strip first page
    with open('./Section 532 tosharepoint/' + submission, "wb") as outputStream:
        output.write(outputStream)