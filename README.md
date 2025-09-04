# Gauss-Jordan-Calculator
Conducting Gauss-Jordan elimination, yet without approaching row echelon form. This version only works for n ⨉ (n + 1) matrix. For the sake of a simpler algorithm, the matrix is solved by the column, instead of row, direction from left to right to get the identity form on the left side. The matrix component a(n,n) of column n is divided by itself and returns 1, along with the rest of the components of row n. While the remaining components of the column, along with its entire row, are added or subtracted with the corresponding component of row n to make it 0.

<img width="2662" height="1806" alt="workflow" src="https://github.com/user-attachments/assets/dc290ef0-a861-4336-909f-ad7c92997e2d" />

This algorithm is still being tested and improved for a better workflow. Even though it is found succesful for some common Gauss-Jordan sample problems, it is still not ready to work on unsolved example like homogenous linear equations.

For any error found in the result or steps of this calculator, or simply for any suggestion, please do not hesitate to raise an issue.
