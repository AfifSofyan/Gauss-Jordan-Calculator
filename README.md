# Gauss-Jordan-Calculator
Conducting Gauss-Jordan elimination, yet without approaching row echelon form. This version only works for n ⨉ (n + 1) matrix. For the sake of simpler algorithm, the matrix is solved by the column —instead of row, direction from left to right to get the identity form on the left side. The matrix component a(n,n) of columnn is divided by itself and return 1, along with the entire components of row n. While the remaining components of the column, along its entire row, are added or subtracted with the coresponding component of rown to get 0.

This algorithm is still being tested and improved for a better workflow. Even though it is found succesful for some common Gauss-Jordan example problem, it is still not ready to work on unsolved example like homogenous linear equations.

Live demo is available through https://gauss-jordan-calculator-production.up.railway.app/

For any error found in the result or steps of this calculator, or simply for any suggestion, please do not hesitate to raise issue.
