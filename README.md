Gauss-Jordan Calculator

This is a simple Django-based calculator that performs Gauss-Jordan elimination with a unique twist. Instead of following the conventional row echelon form (REF/RREF) reduction, this project introduces a custom column-based algorithm to reduce matrices into identity form. It works specifically for n × (n + 1) matrices, solving them column by column from left to right. Each pivot element a(n,n) is normalized to 1, and the rest of its column is eliminated to 0, continuing until the left side of the matrix becomes an identity matrix. While unconventional, this approach offers a simpler workflow for common examples and demonstrates how an alternative perspective can still solve the problem effectively.

<img width="485" height="357" alt="Gauss-Jordan Demo" src="https://github.com/user-attachments/assets/9bd15d1f-2a1b-4e58-b33a-e218005ef6cf" />

At its current stage, this algorithm is still being tested and improved for better stability. It has been found successful for many common Gauss-Jordan problems, but it is not yet fully reliable for special cases such as homogeneous linear equations. This makes it a work in progress, open for further development and refinement.

If you discover any errors in the results or steps, or if you have suggestions to improve the workflow, please don’t hesitate to raise an issue or contribute. Feedback and collaboration are always welcome.
