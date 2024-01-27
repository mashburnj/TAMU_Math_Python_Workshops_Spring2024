import sys
import sympy as sp

# This header.txt file should include everything before, but NOT including, "\begin{document}"
with open('header.txt', 'r') as file:
    header = file.read()

# INSERT SYMPY COMPUTATION CODE HERE
# 
# 

# I recommend doing all computations FIRST, then output all results to the .tex file in one batch afterward,
#     since it's bad programming practice to keep a file open longer than necessary.

# Now we open our output file, while changing the stream (for text output) from the console to the file.
with open('output.tex', 'w') as sys.stdout:
    print(header)
    # Insert output using print statements and sp.print_latex() here! Below is an example:
    sp.print_latex(expression) # This prints the LaTeX code needed to write expression to the open .tex file.
    print('\\end{document}')
