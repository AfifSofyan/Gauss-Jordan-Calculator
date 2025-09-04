This is a simple Django-based calculator that performs Gauss–Jordan elimination with a unique twist. Instead of following the conventional row echelon form (REF/RREF) reduction, this project implements a custom column-based approach to reduce matrices into identity form. It works specifically for n × (n + 1) augmented matrices, processing them column by column from left to right. Each pivot element a(n,n) is normalized to 1, and the rest of its column is eliminated to 0, continuing until the left side becomes an identity matrix. While unconventional, this approach offers a simpler workflow for common examples and shows how an alternative perspective can still solve the problem effectively.

<img width="485" height="357" alt="App screenshot" src="https://github.com/user-attachments/assets/9bd15d1f-2a1b-4e58-b33a-e218005ef6cf" />

From the user’s perspective, the calculator is straightforward to use. You enter the coefficients of your linear system into the grid of input fields that represent an augmented matrix, then click **Run Gauss-Jordan Calculator**. The app runs the column-based Gauss–Jordan routine and displays both the final reduced matrix and the intermediate operations performed at each stage. This makes it easy not only to obtain the solution vector but also to visually follow the logic of normalization and elimination as it progresses.

<img width="303" height="576" alt="generated matrices and the result" src="https://github.com/user-attachments/assets/4dcdc11a-0c97-4c72-bcc9-8389f14ac0cb" />

The first image shows a typical result after computation: the left side has been driven to the identity matrix and the rightmost column contains the solution. This mirrors what you would expect from reduced row echelon form, but achieved through a left-to-right, column-oriented sequence of steps.

<img width="746" height="622" alt="step by step solution" src="https://github.com/user-attachments/assets/14018337-1004-4181-8dfc-e18ba1bb727e" />

The second image shows the step-by-step log. For each pivot column, the calculator normalizes the pivot to 1 and then eliminates all other entries in that column by applying row operations using the current pivot row. The log makes the process transparent, so users can verify each transformation and learn how Gauss–Jordan works in practice.

At its current stage, this algorithm is still being tested and improved for better stability. It has been successful on many common Gauss–Jordan problems, but it is not yet fully reliable for certain cases such as homogeneous linear equations. This is an active work in progress and open to refinement.
