# scientific_computing-BIT-2118
JULIA WAMBUI MAINA 
BSCCS262718012
JULIA WAMBUI MAINA 
BSCCS262718012
BIT 2118: SCIENTIFIC COMPUTING 

                                           TASK 2
INSTRUCTION B: INPUT VALUES AND THE MATHEMATICAL OPERATIONS PERFORMED.
•	put: 24 hourly temperatures in °C, stored in one NumPy array.
•	Operations: 
o	mean = (sum of all values) ÷ 24
o	min and max = smallest and largest value
o	F = 1.8C + 32, applied to the whole array at once (vectorization, no loop)
INSTRUCTION C: CHANGE ATLEAST ONE INPUT/ PARAMETER.
1.	Change the 29.4 (the 13:00 reading) to 35.0, simulating a heat spike.
2.	Run again and record the new output: 
o	Mean goes from 23.12 to 23.35.
o	Max goes from 29.40 to 35.00.
o	Min stays 17.50.
3.	Explain: one extreme value raised the maximum by 5.6 °C, but the mean rose by only about 0.23 °C because it is shared across 24 readings. The minimum is unaffected because the changed value was not the smallest.
INSTRUCTION D: THE MEANING OF THE OUTPUT IN WORDS.
The station recorded an average temperature of about 23.1 °C over 24 hours. The coolest hour was 17.5 °C (around 03:00, before sunrise) and the hottest was 29.4 °C (around 12:00 to 13:00, early afternoon). The Fahrenheit values are the same readings expressed on another scale, e.g. 18.5 °C is 65.3 °F. This task has no graph, so no graph interpretation is needed.


TASK 3
INSTRUCTION B: INPUT VALUES AND THE MATHEMATICAL OPERATIONS PERFORMED 
•	Inputs: 
o	1,000,000 latency values, uniformly random between 5 and 250 ms
o	Seed 42, so the data is reproducible
•	Operations: 
o	seconds = ms ÷ 1000 (unit conversion)
o	squared = seconds² (as used in error calculations)
o	The same math is done two ways: a Python for loop that handles one value at a time, and a vectorized NumPy expression that handles the whole array at once.
o	time it measures how long each way takes.
INSTRUCTION C: CHANGE ATLEAST ONE INPUT/ PARAMETER.
1.	Change 1,000,000 to 10,000 and run. Record the speed-up.
2.	Change it to 5,000,000 and run again. Record the speed-up.
Example results to record (yours will vary):
Array size	Loop time	Vectorized time	Speed-up
10,000	~0.003 s	~0.00002 s	~100x
1,000,000	~0.25 s	~0.002 s	~100x
5,000,000	~1.3 s	~0.01 s	~100x
Explanation: The loop time grows in proportion to the data size because Python processes each element one by one with interpreter overhead. NumPy runs the operation in optimized compiled code, so it is much faster. The speed-up stays large (often 50x or more) at every size, and the absolute time saved grows with the data. You can also try changing uniform (5, 250) to uniform (5, 500) and note that the squared values get larger (the maximum squared value goes from about 0.0625 to 0.25) while the timings stay almost the same, because the amount of work hasn’t changed.

INSTRUCTION D: THE MEANING OF THE OUTPUT IN WORDS.
The program converted one million latency measurements from milliseconds to seconds and squared them. The first five squared values (about 0.038, 0.013, 0.046, 0.031 and 0.0008) correspond to latencies of about 195, 113, 215, 176 and 28 ms. The loop took X seconds while the vectorized version took Y seconds, so vectorization was about Z times faster. Both methods give the same numbers, but vectorization is far more efficient, which matters when the network monitor must process millions of readings in real time. This task has no graph.

TASK 4 (Floating-Point Arithmetic and Numerical Errors)
INSTRUCTION B: INPUT VALUES AND THE MATHEMATICAL OPERATIONS PERFORMED.
•	Inputs: 
o	0.1 and 0.2, compared with 0.3
o	True value √2 and the approximation 1.414
o	Small values of x: 1e-4, 1e-8, 1e-12
•	Operations: 
o	Exact equality (==) versus tolerance comparison (np.isclose)
o	Absolute error = |true − approx.|
o	Relative error = absolute error ÷ |true|
o	Two algebraically identical formulas for (√(1+x) − 1)/x: 
	direct: subtracts two nearly equal numbers
	stable: the rationalized form 1/(√(1+x) + 1), which avoids that subtraction
INSTRUCTION C: CHANGE ATLEAST ONE INPUT/ PARAMETER.
Change approx_value = 1.414 to 1.41421. Record:
•	Absolute error drops from about 0.000214 to about 0.0000036.
•	Relative error drops from about 0.0151% to about 0.00025%.
Change the list to [1e-4, 1e-8, 1e-12, 1e-16]. At 1e-16, you get:
•	direct = 0.0, which is completely wrong.
•	stable = 0.5, which is correct.
Explanation to write:
•	More digits in the approximation means a smaller truncation error.
•	In the direct formula, √(1+x) is almost exactly 1 when x is tiny. Subtracting 1 cancels nearly all the significant digits (catastrophic cancellation), and dividing by the tiny x then magnifies what is left. At x = 1e-16, the computer cannot tell 1 + x from 1, so the numerator becomes exactly 0.
•	The stable formula has no subtraction of nearly equal numbers, so it stays accurate for every x. The true limit is 0.5.

INSTRUCTION D: THE MEANING OF THE OUTPUT IN WORDS.
Adding 0.1 and 0.2 gives 0.30000000000000004, not exactly 0.3, because computers store decimals in binary and cannot represent 0.1 or 0.2 exactly. So == returns False, but np.isclose returns True because it allows a tiny tolerance. Approximating √2 as 1.414 gives an absolute error of about 0.000214, which is about 0.0151% of the true value, so the approximation is good to about four significant figures. In the last test, the direct formula loses accuracy as x gets smaller (at 1e-12 it gives about 0.50004 instead of 0.5), while the stable formula stays correct. This shows that how you write a formula matters as much as the formula itself. This task has no graph.

TASK 5 (MATRIX ALGEBRA AND MATRIX OPERATIONS)
INSTRUCTION B: INPUT VALUES AND THE MATHEMATICAL OPERATIONS PERFORMED.
•	Inputs: 
o	4 corner points of a unit square
o	Rotation angle of 45°
o	Scale factors of 2.0 (x direction) and 1.5 (y direction)
•	Operations: 
o	Build a rotation matrix R = [[cos θ, −sin θ], [sin θ, cos θ]]
o	Build a scaling matrix S = diag(2.0, 1.5)
o	Combine them: T = R @ S (scale first, then rotate)
o	Transform all points at once: points @ T.T
o	Compute det(T)

INSTRUCTION C: CHANGE ATLEAST ONE INPUT/ PARAMETER.
Experiment 1: change scale x from 2.0 to 3.0. Record:
•	The determinant becomes 4.5 (3.0 × 1.5).
•	Point (1, 0) moves to about (2.121, 2.121) instead of (1.414, 1.414).
•	Point (1, 1) moves to about (1.061, 3.182).
Experiment 2: change np.deg2rad(45) to np.deg2rad(90). Record:
•	The transformed corners become about (0, 0), (0, 2), (−1.5, 2), (−1.5, 0).
•	The determinant stays 3.0.
Explanation:
•	The determinant equals the factor by which the area changes. The original square has area 1, so the new shape has area equal to the determinant (3.0, then 4.5).
•	Rotation does not change area, so the determinant depends only on the scale factors (2 × 1.5 = 3). That is why Experiment 2 still gives 3.0, while Experiment 1 changes it.
•	A determinant of 0 would mean the shape collapses to a line and the transformation cannot be reversed.
INSTRUCTION D: THE MEANING OF THE OUTPUT IN WORDS.
The program takes a unit square and stretches it by 2 horizontally and 1.5 vertically, then rotates it by 45°. The corner (0, 0) stays at the origin because linear transformations always keep the origin fixed. The other three corners move to (1.41, 1.41), (0.35, 2.47) and (−1.06, 1.06), which form a tilted parallelogram. The determinant of 3.0 means the new shape has three times the area of the original square. This task has no graph, but you can plot the before and after shapes (see the optional tip below) to see the transformation.





TASK 6 (SYSTEMS OF LINEAR EQUATIONS).
INSTRUCTION B: INPUT VALUES AND THE MATHEMATICAL OPERATIONS PERFORMED.
•	Inputs: 
o	Coefficient matrix A = [[4, 2], [8, 12]]. Row 1 is CPU use per server, row 2 is memory use per server.
o	Totals vector b = [20, 72] (total CPU units and total GB memory).
•	Operations: 
o	The two equations are 4x + 2y = 20 (CPU) and 8x + 12y = 72 (memory).
o	np.linalg.solve(A, b) finds x and y so that A·x = b.
o	Verification: multiply A @ solution and compare with b. The residual is b − A·x and should be about 0.

INSTRUCTION C: CHANGE ATLEAST ONE INPUT/ PARAMETER.
Experiment 1: change b to [24.0, 80.0]. Record:
•	Type A = 4 and Type B = 4.
Experiment 2: change b to [20.0, 60.0]. Record:
•	Type A = 3.75 and Type B = 2.5. The printout with :.0f would round these and hide the fact that they are not whole numbers, so change the print lines to :.2f to see them.
Explanation to write:
•	Raising the totals (Experiment 1) means more resources are being used, so more servers must be active. Here the solution is still whole numbers.
•	In Experiment 2 the answer is fractional, so those totals cannot come from a whole number of servers. This tells you the measured totals are inconsistent with the server model, or that the data contains errors.
•	In Experiment 3 the two equations carry the same information, so there is no unique solution. This happens when the determinant is 0. For the original A, det = 4×12 − 2×8 = 32, which is not 0, so a unique solution exists.

INSTRUCTION D: THE MEANING OF THE OUTPUT IN WORDS.
Solving the two resource equations shows that 3 Type A servers and 4 Type B servers are active. Check: the CPU use is 3×4 + 4×2 = 20 units and the memory use is 3×8 + 4×12 = 72 GB, which match the observed totals. The verification line returns [20, 72] and the residual is zero (or about 1e-15), so the solution reproduces the data to machine precision. This task has no graph.

TASK 7 (GAUSSIAN ELIMINATION AND LU DECOMPOSITION)
INSTRUCTION B: INPUT VALUES AND THE MATHEMATICAL OPERATIONS PERFORMED.
•	Inputs: 
o	A 3×3 coefficient matrix A, which stays the same for every run
o	Three different measurement vectors b: [15,10,10], [16,11,9] and [14,12,11]
•	Operations: 
o	lu_factor(A) factors A into PA = LU, where L is lower triangular, U is upper triangular and P records row swaps (pivoting). This is Gaussian elimination stored in reusable form.
o	lu_solve((lu, piv), b) solves Ly = Pb by forward substitution, then Ux = y by back substitution.
o	The residual b − A·x checks the answer.
o	np.linalg.solve is used once to compare.
INSTRUCTION C: CHANGE ATLEAST ONE INPUT/ PARAMETER.
Experiment 1: change the first measurement set to [30.0, 20.0, 20.0] (double the original). Record:
•	Solution = [10, 10, 10], double the original [5, 5, 5].
Experiment 2: add a fourth set, np.array([0.0, 0.0, 0.0]). Record:
•	Solution = [0, 0, 0].
Experiment 3: change A[0,0] from 4.0 to 8.0. Record the new solutions. The first set becomes about [2.31, 3.46, 4.49]. The solution values change because the first equation now has a heavier weight on x.
Explanation:
•	The system is linear, so doubling b doubles x, and a zero b gives a zero solution.
•	Factoring is done once with lu_factor, so each extra measurement vector adds little work. For large matrices, factoring costs roughly n³ operations while each substitution costs only about n², so reuse saves a lot.
•	Changing A forces a new factorization, since L and U depend only on A.

INSTRUCTION D: THE MEANING OF THE OUTPUT IN WORDS.
The program solved the same three-equation system for three different sets of measurements. The first set gives x = y = z = 5, which can be checked by hand: 4(5) − 5 = 15, −5 + 20 − 5 = 10 and −5 + 15 = 10. The other two sets give slightly different values (for example, about 5.32, 5.27 and 4.76 for the second set), showing how the unknowns respond to changes in the measurements. The residual norms are zero or about 1e-15, so every solution reproduces its measurements to machine precision. The direct solver gives the same answer as the LU method for the first set. This task has no graph.

TASK 8 (ITERATIVE METHODS FOR LINEAR SYSTEMS)
•	Inputs: 
o	A 5×5 tridiagonal matrix with 2 on the diagonal and −1 on the neighbouring diagonals
o	Right-hand side b = [100, 0, 0, 0, 20], where 100 °C and 20 °C are the boundary temperatures
o	Starting guess of all zeros
o	Tolerance 1e-8 and a maximum of 500 iterations
•	Operations: 
o	Jacobi: every new value is calculated using only the previous iteration’s values.
o	Gauss-Seidel: each new value uses the latest values already updated in the same sweep.
o	After each iteration, the error is the largest change in any temperature. The loop stops when it falls below the tolerance.
o	The direct solution from np.linalg.solve is the reference answer.

INSTRUCTION C: CHANGE ATLEAST ONE INPUT/ PARAMETER.
Experiment 1: change tol=1e-8 to tol=1e-4 in both function definitions. Record the iteration counts. Both drop to roughly 80 for Jacobi and roughly 40 for Gauss-Seidel. The temperatures are still close to the exact values, but only accurate to about 4 decimal places.
Experiment 2: change b to [100., 0., 0., 0., 100.]. Record:
•	All five temperatures become 100, because both ends are equally hot.
Experiment 3: change the diagonal from 2. to 1.5 in all five rows (keep the -1. entries). Record:
•	The errors grow instead of shrinking, and Jacobi hits the 500-iteration limit without converging. The matrix is no longer diagonally dominant, so convergence is not guaranteed.
•	On the graph, the curves rise instead of falling.
Explanation:
•	A looser tolerance stops earlier, which saves work but gives a less accurate answer.
•	Equal boundary temperatures leave no reason for heat to flow, so the whole rod settles at that temperature.
•	Jacobi and Gauss-Seidel converge when the diagonal entries dominate the off-diagonal entries. Once that condition is broken, the iterations can diverge.
INSTRUCTION D: THE MEANING OF THE OUTPUT IN WORDS.
The program models heat flow along a rod with five interior measuring points, with the left end at 100 °C and the right end at 20 °C. Starting from a guess of 0 °C everywhere, both methods repeatedly improve the guess until it stops changing by more than 1e-8. They end at about 86.7, 73.3, 60.0, 46.7 and 33.3 °C, which matches the direct solution and falls evenly from the hot end to the cold end.
Graph: the x-axis is the iteration number and the y-axis is the largest change in any temperature, on a log scale. Both curves are nearly straight lines going down, which means the error shrinks by a constant factor each iteration. The Gauss-Seidel line is steeper, so it converges faster, in about half the iterations. Both curves cross the 1e-8 level at the end of their runs, where the iteration stops.



TASK 9 (EIGENVALUES AND EIGENVECTORS).
INSTRUCTION B: INPUT VALUES AND THE MATHEMATICAL OPERATIONS PERFORMED.
•	Inputs: 
o	A 4×4 adjacency matrix. A 1 means two nodes are connected and a 0 means they are not.
o	Connections: A–B, A–C, B–C, B–D, C–D. A and D are not directly connected.
o	The matrix is symmetric because the network is undirected.
•	Operations: 
o	np.linalg.eig(A) finds all eigenvalues λ and eigenvectors v satisfying Av = λv.
o	The dominant eigenvalue is the largest one. Its eigenvector is used as the importance measure.
o	np.abs removes the arbitrary sign of the vector.
o	Dividing by the sum scales the scores to add up to 1.
o	The verification checks that Av − λv ≈ 0.
INSTRUCTION C: CHANGE ATLEAST ONE INPUT/ PARAMETER.
Experiment 1: add the missing link between A and D. Change the matrix to:
python
A = np.array([
    [0., 1., 1., 1.],
    [1., 0., 1., 1.],
    [1., 1., 0., 1.],
    [1., 1., 1., 0.]
])
Record:
•	Dominant eigenvalue = 3.0.
•	Every node scores 0.2500.
Experiment 2: go back to the original matrix and remove the B–C link (set A[1,2], A[2,1] to 0). Record:
•	Dominant eigenvalue = 2.0.
•	Every node scores 0.2500. The network is now a square ring (A–B–D–C–A).
Explanation:
•	The dominant eigenvalue grows as the network becomes more connected. It is 2.0 for the ring, about 2.56 for the original, and 3.0 when every node links to every other.
•	In the original network, B and C each have 3 connections while A and D have only 2, so B and C score higher (0.2808 versus 0.2192).
•	When every node has the same number of connections (the ring and the full network), all nodes are equally important, so the scores are equal.
INSTRUCTION D: THE MEANING OF THE OUTPUT IN WORDS.
The program treated a four-node network as a matrix and found its eigenvalues. The largest, about 2.56, describes the overall connectivity of the network. Its eigenvector gives each node an importance score: B and C get 0.281 each, while A and D get 0.219 each. This makes sense because B and C are each linked to three other nodes, while A and D are linked to only two. A node scores highly when it is connected to other well-connected nodes. The verification error is almost zero, so the computed eigenpair satisfies Av = λv. This task has no graph.











TASK 10 (BISECTION AND FIXED-POINT ROOT FINDING)
INSTRUCTION B: INPUT VALUES AND THE MATHEMATICAL OPERATIONS PERFORMED.
•	Inputs: 
o	Heat-balance function f(T) = T − 25 − 10e^(−T/20)
o	Bisection bracket [20, 40], tolerance 1e-10
o	Fixed-point starting guess T₀ = 30, tolerance 1e-10, maximum 100 iterations
•	Operations: 
o	Bisection: f(20) ≈ −8.68 and f(40) ≈ +13.65 have opposite signs, so a root lies between them. Each step takes the midpoint and keeps the half where the sign change remains. The interval halves every time, so reaching 1e-10 takes about 38 steps.
o	Fixed-point iteration: rewrite f(T) = 0 as T = g(T) = 25 + 10e^(−T/20), then repeat Tₙ₊₁ = g(Tₙ) until successive values differ by less than 1e-10.
o	The equilibrium is the temperature at which heat gain equals heat loss.
INSTRUCTION C: CHANGE ATLEAST ONE INPUT/ PARAMETER.
Experiment 1: change the ambient temperature from 25 to 30 in both heat_balance and g. Record:
•	The equilibrium rises to about 32.017 °C.
Experiment 2: change bracket=[20, 40] to bracket=[0, 10]. Record:
•	SciPy raises ValueError: f(a) and f(b) must have different signs. Here f(0) ≈ −35 and f(10) ≈ −21, both negative, so no sign change is guaranteed.
Experiment 3: change the starting guess T = 30.0 to T = 100.0. Record:
•	The same root, 27.525211, but with about 1 to 2 more iterations.
Experiment 4 (optional): change the coefficient 10 to 20 in both functions. Record:
•	The root moves to about 29.56 °C, and the fixed-point method still converges, but in a few more iterations.
Explanation:
•	A higher ambient temperature shifts the whole equilibrium upward.
•	Bisection needs a bracket with a sign change, since it relies on the intermediate value theorem. Without one it cannot start.
•	The root does not depend on the starting guess. The guess only affects how many iterations are needed.
•	Fixed-point iteration converges when |g′(T)| < 1 near the root. Here g′(T) = −0.5e^(−T/20), which is about −0.13 at the root. The error shrinks to roughly 13% of its size each step, which is why it needs far fewer iterations than bisection (about 11 versus 38).
INSTRUCTION D: THE MEANING OF THE OUTPUT IN WORDS.
Both methods find an equilibrium temperature of about 27.53 °C, the point where the heat-balance function equals zero, meaning heat gain equals heat loss. Bisection is slow but guaranteed, taking about 38 halving’s to shrink an interval of width 20 down to 1e-10. Fixed-point iteration is faster here, taking about 11 steps, because each step reduces the error by a factor of about 0.13. Its iterates alternate above and below the root (30, 27.23, 27.56, 27.52, …) while closing in.
Graph: the x-axis is temperature in °C and the y-axis is the value of the heat-balance function. The curve rises steadily from about −8.7 at 20 °C to about +13.6 at 40 °C. It crosses the horizontal line y = 0 at about 27.5 °C, which is where the dashed vertical line sits. Below that temperature the function is negative (heat loss and gain are not balanced one way), and above it the function is positive. The crossing point is the equilibrium.

TASK 11 (NEWTON-RAPHSON AND SECANT METHODS)
INSTRUCTION B: INPUT VALUES AND THE MATHEMATICAL OPERATIONS PERFORMED.
•	Inputs: 
o	Cash flows: −10,000 at year 0, then +3,000, +3,500, +4,000 and +2,500 in years 1 to 4
o	Newton starting guess 10%, with the derivative supplied
o	Secant starting guesses 5% and 20%
o	Tolerance 1e-12
•	Operations: 
o	NPV(r) = Σ cashflow_t ÷ (1 + r)^t
o	The IRR is the rate r where NPV(r) = 0.
o	Newton-Raphson: rₙ₊₁ = rₙ − NPV(rₙ) ÷ NPV′(rₙ), where NPV′ is the exact derivative d_npv.
o	Secant: the same idea, but the slope is estimated from the last two guesses, so no derivative is needed.
INSTRUCTION C: CHANGE ATLEAST ONE INPUT/ PARAMETER.
Experiment 1: change the last cash flow from 2500 to 3500. Record:
•	The IRR rises to about 14.5%.
Experiment 2: change the initial investment from -10000 to -12000. Record:
•	The IRR falls to about 3.3%.
Experiment 3: change the Newton starting guess x0=0.10 to x0=0.30. Record:
•	The same IRR, but possibly one or two more iterations.
Explanation to write:
•	Larger inflows make the project more profitable, so the rate that cancels the investment rises.
•	A larger up-front cost needs a lower discount rate for NPV to reach zero, so the IRR drops.
•	The root does not depend on the starting guess, which only affects the number of iterations.
•	Newton converges quickly because it uses the exact slope, and the number of correct digits roughly doubles each step. The secant method is slightly slower but needs only function values, which is useful when a derivative is hard to write.
INSTRUCTION D: THE MEANING OF THE OUTPUT IN WORDS.
The investment of 10,000 returns 12,000 in total over four years. The program finds the discount rate at which the present value of those returns exactly equals the investment. Both methods give an internal rate of return of about 11.55% per year. The NPV at that rate is essentially zero, which confirms the answer. Newton-Raphson needed fewer iterations than the secant method, but both reached the same result. If the cost of borrowing is below 11.55%, the project adds value, and if it is above 11.55%, the project loses value. This task has no graph.



TASK 12 (POLYNOMIAL AND NONLINEAR EQUATION SOLVING)
INSTRUCTION B: INPUT VALUES AND THE MATHEMATICAL OPERATIONS PERFORMED.
•	Inputs: 
o	Two equations: x² + y² − 4 = 0 (circle of radius 2) and y − (x² − 1) = 0 (parabola)
o	Starting guesses (1, 1) and (−1, 1)
o	Polynomial coefficients [1, −5, 6] for x² − 5x + 6
•	Operations: 
o	equations(z) returns the residuals, which are the left side minus the right side of each equation. A true intersection makes both residuals zero.
o	root(equations, guess) repeatedly adjusts (x, y) until both residuals are close to zero (a Newton-type method for systems).
o	np.roots finds the roots of a polynomial from its coefficients.
o	Check by hand: substituting x² = y + 1 into the circle gives y² + y − 3 = 0, so y = (−1 + √13)/2 ≈ 1.3028 and x = ±√2.3028 ≈ ±1.5176. The other value, y ≈ −2.30, would need x² to be negative, so it has no real intersection.
INSTRUCTION C: CHANGE ATLEAST ONE INPUT/ PARAMETER.
Experiment 1: change the circle radius by replacing - 4 with - 9 (radius 3). Record:
•	The intersections move to about (±1.8365, 2.3723).
Experiment 2: change the parabola to y - (x**2 - 3) and use four guesses: ([1.9, 0.6], [-1.9, 0.6], [1.2, -1.6], [-1.2, -1.6]). Record:
•	Four intersections: about (±1.9021, 0.6180) and (±1.1756, −1.6180).
Experiment 3: go back to the original equations and use the guess [0.0, 3.0]. Record the result. It converges to one of the two original solutions (or reports Converged: False), which shows that the guess affects which solution you reach.
Explanation to write:
•	A bigger circle moves the intersections outwards.
•	Lowering the parabola gives it more crossings with the circle, so a nonlinear system can have several solutions, and a solver finds only the one near its starting guess. This is why the brief says to try more than one initial guess.
•	Always check the residuals and success flag, because a solver may stop without a true solution.

INSTRUCTION D: THE MEANING OF THE OUTPUT IN WORDS.
The program finds where a circle of radius 2 and an upward-opening parabola cross. There are two intersection points, at about (1.52, 1.30) and (−1.52, 1.30), mirror images of each other because both curves are symmetric about the y-axis. The residuals are about 1e-13, so both equations are satisfied to machine precision, and the solver reports that it converged. The two different starting guesses led to the two different solutions. The polynomial x² − 5x + 6 has roots 2 and 3, matching (x − 2)(x − 3) = 0. This task has no graph.

TASK 13 (INTERPOLATION)
INSTRUCTION B: INPUT VALUES AND THE MATHEMATICAL OPERATIONS PERFORMED.
•	Inputs: 
o	7 hourly measurements, from 08:00 to 14:00, rising from 18.0 °C to a peak of 25.5 °C and then easing to 25.0 °C
o	Target times every 10 minutes (1/6 hour), plus a single query at 10:30
•	Operations: 
o	Linear interpolation joins neighbouring points with straight lines. At 10:30 it takes the midpoint of 22.5 and 24.0, which is (22.5 + 24.0) ÷ 2 = 23.25.
o	Cubic spline fits a smooth cubic curve between each pair of points. The pieces join so that the slope and the curvature match at every measurement, which makes the curve smooth.
o	Both functions are built once from the data and then evaluated at any times you choose.


INSTRUCTION C: CHANGE ATLEAST ONE INPUT/ PARAMETER.
Experiment 1: change target_time from 10.5 to 8.5. Record:
•	Linear = 19.00 °C and cubic ≈ 18.81 °C.
Experiment 2: change target_time to 15.0 (an hour after the last measurement). Record:
•	Linear raises ValueError: A value ... in x_new is above the interpolation range.
•	The cubic spline does not raise an error. It extrapolates and gives about 22.9 °C, which falls even though the real temperature might still be about 25 °C.
Experiment 3: change the 13:00 reading from 25.5 to 28.0 in temperature. Record the new curves. The linear plot gains a sharp peak at 13:00, and the cubic curve overshoots, bulging above 28 °C around that point.
Explanation to write:
•	The linear estimate is only as smooth as a set of straight segments. The cubic estimate follows the gently curving trend, so it differs slightly (23.36 vs 23.25).
•	Interpolation is only reliable between measured points. Linear interpolation refuses to guess outside the range. The spline will extrapolate silently, so the number it produces cannot be trusted.
•	Splines can overshoot near a sudden change, so a smoother method is not always more accurate.

INSTRUCTION D: THE MEANING OF THE OUTPUT IN WORDS.
The sensor measured the temperature only once an hour, but the program estimates it every 10 minutes. At 10:30 the straight-line method estimates 23.25 °C, exactly halfway between the 10:00 and 11:00 readings. The cubic spline gives 23.36 °C, slightly higher, because the temperature curve was bending towards a plateau and the spline follows that bend. The two methods differ by only about 0.1 °C, so the choice matters little for smooth data like this.
Graph: the x-axis is the hour of the day and the y-axis is the temperature. The dots are the seven real measurements. The straight line connects them with visible corners at each dot. The cubic curve passes through the same dots but is smooth. Both rise quickly in the morning (about 2 °C per hour), flatten around 12:00 to 13:00 and begin to fall at 14:00. The two lines are almost on top of each other, and the largest gap is between the dots.


TASK 14 (CURVE FITTING AND APPROXIMATION)
INSTRUCTION B: INPUT VALUES AND THE MATHEMATICAL OPERATIONS PERFORMED.
•	Inputs: 
o	7 load levels (50 to 350 concurrent users)
o	7 measured response times (82 to 305 ms)
o	A quadratic model y = ax² + bx + c
•	Operations: 
o	curve_fit finds the a, b and c that minimize the sum of squared residuals Σ(yᵢ − ŷᵢ)² (least squares).
o	Residual = measured value − model prediction.
o	RMSE = √(mean of squared residuals), the typical size of the error in ms.
o	The fitted model is then used to predict the response at 400 users.

INSTRUCTION C: CHANGE ATLEAST ONE INPUT/ PARAMETER.
Experiment 1 (change the model): replace the model with a straight line:
python
def model(x, a, b, c):
    return b*x + c
Record:
•	RMSE jumps to about 18.8 ms, and the prediction at 400 users falls to about 313 ms.
•	Because a no longer appears in the model, its value is not estimated, so you may see a warning about the covariance. This is expected.
Experiment 2 (change the data): change the last response from 305 to 330. Record:
•	RMSE rises noticeably, and the prediction at 400 users rises to about 410 ms.
Experiment 3 (extrapolate): change 400 to 800 in the prediction line. Record:
•	About 1364 ms.
Explanation to write:
•	The data curves upwards, so a straight line misses the shape and leaves large residuals (the line is too low at both ends and too high in the middle). The quadratic follows the bend, so its RMSE is about 12 times smaller.
•	One changed measurement pulls the whole curve, which shows that least squares is sensitive to unusual points.
•	Predictions beyond the measured range (350 users) are extrapolation. A quadratic keeps growing, but a real server may saturate or crash, so treat 800 users as a rough guess at best.

INSTRUCTION D: THE MEANING OF THE OUTPUT IN WORDS.
The program fits a curve to server response times measured at seven user loads. The fitted model is y = 0.002167x² − 0.1345x + 85, so the response time with almost no load is about 85 ms and it grows faster and faster as users are added. The RMSE of about 1.55 ms means the curve is, on average, within about 1.5 ms of each measurement, which is a very good fit. The residuals are small and switch between positive and negative with no strong pattern, which suggests the quadratic is a suitable model. At 400 users the model predicts about 378 ms.
Graph: the x-axis is the number of concurrent users and the y-axis is the response time in ms. The dots are the seven measurements, and the smooth curve passes very close to all of them. The curve rises slowly at first (about 13 ms per 50 users at low load) and then steeply (about 67 ms per 50 users at the high end). It extends beyond the last dot to 400 users, and that final part is a prediction, not data.

TASK 15 (NUMERICAL DIFFERENTIATION)
INSTRUCTION B: INPUT VALUES AND THE MATHEMATICAL OPERATIONS PERFORMED.
•	Inputs: 
o	7 GPS timestamps, 0 to 6 s, one second apart
o	7 positions in metres, from 0 to 38 m
•	Operations: 
o	Forward difference at the first point: v₀ = (x₁ − x₀) ÷ Δt
o	Central difference at interior points: vᵢ = (xᵢ₊₁ − xᵢ₋₁) ÷ (tᵢ₊₁ − tᵢ₋₁)
o	Backward difference at the last point: v = (xₙ − xₙ₋₁) ÷ Δt
o	Central differences use points on both sides, so they are more accurate. The end points can only use one side.
INSTRUCTION C: CHANGE ATLEAST ONE INPUT/ PARAMETER.
Experiment 1 (a GPS glitch): change the position at t = 3 from 16.1 to 17.1. Record:
•	Speed at t=2 becomes 6.15 (was 5.65).
•	Speed at t=3 stays 6.25.
•	Speed at t=4 becomes 6.45 (was 6.95).
Experiment 2 (a wider step): add this after the loop, to estimate the speed at t=3 using points two seconds either side:
python
wide = (position[5] - position[1]) / (time[5] - time[1])
print("Speed at t=3 with wider step:", wide)
Record:
•	6.30 m/s (compared with 6.25 m/s using neighbours one second away).
Experiment 3 (faster sampling): change the time array to np.array([0, 1, 2, 3, 4, 5, 6]) * 0.5, so the same positions are covered in half the time. Record:
•	All speeds double, from 4.8 to 9.6, and from 8.0 to 16.0.
Explanation to write:
•	A central difference at a point ignores that point’s own value, so a glitch there does not change that point’s speed, but it spoils the speeds on both sides. Differentiation amplifies noise, so noisy data should be smoothed first.
•	A wider step averages over a longer time. It gives a smoother estimate but blurs fast changes. A small step follows the changes closely but is more sensitive to measurement error.
•	The speed depends on the time spacing. The same distance in half the time means double the speed, so units and time stamps must be correct.



INSTRUCTION D: THE MEANING OF THE OUTPUT IN WORDS.
The program estimates how fast a vehicle was moving from GPS positions recorded once a second. The speed starts at about 4.8 m/s (17 km/h) and rises steadily to 8.0 m/s (29 km/h) after six seconds, so the vehicle is accelerating. Between t=1 and t=5 the speed rises from 5.1 to 7.65 m/s, which is about 0.64 m/s per second. The speeds at t=0 and t=6 are less reliable because they use only one neighbour.
Graph: the x-axis is time in seconds and the y-axis is the estimated speed in m/s. The line rises from left to right with a slightly increasing slope. The upward trend shows the vehicle speeding up, and the steepening slope shows the acceleration is not quite constant. The last segment is steeper partly because the end-point formula is less accurate.

TASK 16 (NUMERICAL INTEGRATION)
INSTRUCTION B: INPUT VALUES AND THE MATHEMATICAL OPERATIONS PERFORMED.
•	Inputs: 
o	7 smart-meter times, from 0 to 12 hours, every 2 hours
o	7 power readings in kW, from 0.8 up to a peak of 1.8 at 6 hours, then down to 0.9
•	Operations: 
o	Energy (kWh) = ∫ power dt, the area under the power–time curve.
o	Trapezoidal rule: joins the readings with straight lines and adds up the trapezoid areas: Σ (Δt/2)(pᵢ + pᵢ₊₁).
o	Simpson’s rule: fits a parabola through each group of three readings, weighting them 1, 4, 1, which is usually more accurate for smooth curves.
o	Both need the time values (x=time_hours) so the spacing is used correctly.

INSTRUCTION C: CHANGE ATLEAST ONE INPUT/ PARAMETER.
Experiment 1: change the last power reading from 0.9 to 1.5. Record:
•	Trapezoid = 16.300 kWh and Simpson = 16.200 kWh.
Experiment 2 (coarser sampling): use only every second reading:
python
time_hours = np.array([0, 4, 8, 12], dtype=float)
power_kw = np.array([0.8, 1.4, 1.6, 0.9])
Record:
•	Trapezoid = 15.400 kWh (was 15.700). Fewer readings give a rougher estimate.
•	Because there are only 3 intervals (an odd number), Simpson uses a special treatment of the end, so the trapezoid is the cleaner comparison here.
Experiment 3 (sanity check): use constant power of 2 kW for 3 hours:
python
np.trapezoid([2, 2, 2, 2], [0, 1, 2, 3])
Record:
•	6.0 kWh, matching 2 × 3 from the brief.
Explanation to write:
•	A higher reading at the end adds energy in the last interval, and the effect is bigger on the trapezoid rule.
•	Fewer readings mean the program cannot see what happens between them. The peak at 6 hours is partly missed, so the estimate shifts by 0.3 kWh.
•	Constant power gives exactly rate × time, which confirms that the method works. The trapezoid rule is exact for straight lines, and Simpson is exact for quadratics.

INSTRUCTION D: THE MEANING OF THE OUTPUT IN WORDS.
The smart meter recorded the power used by a building every two hours, and the program added up the area under that curve to find the energy consumed. The trapezoidal rule gives 15.7 kWh and Simpson’s rule gives 15.8 kWh, so the building used about 15.7 to 15.8 kWh in 12 hours, an average of 1.31 kW. The two methods differ by only 0.1 kWh (under 1%), so the answer is reliable. Simpson is usually the better estimate for smooth data like this.
Graph: the x-axis is time in hours and the y-axis is power in kW. The line rises from 0.8 kW at the start to a peak of 1.8 kW at 6 hours, then falls to 0.9 kW at 12 hours. The shaded area under the line is the energy used, in kWh. The tall middle part of the shape contributes most of the energy.


TASK 17 (EULER METHOD FOR ODES).
INSTRUCTION B: INPUT VALUES AND THE MATHEMATICAL OPERATIONS PERFORMED.
•	Inputs: 
o	Ambient temperature 25 °C, starting temperature 90 °C
o	Cooling constant k = 0.12 per minute
o	Step size h = 1 minute, end time 30 minutes
•	Operations: 
o	The ODE is dT/dt = −k(T − T_ambient). The object cools faster when it is much hotter than the room.
o	Euler update: Tₙ₊₁ = Tₙ + h × (−k)(Tₙ − T_ambient). Each step moves along the current slope for one time step.
o	Here this is the same as multiplying the temperature difference by (1 − kh) = 0.88 at every step.
o	The exact solution T(t) = 25 + 65e^(−0.12t) is used to measure the error.

INSTRUCTION C: CHANGE ATLEAST ONE INPUT/ PARAMETER.
Experiment 1 (smaller step): change h = 1.0 to h = 0.5. Record:
•	Euler after 30 min is about 26.59 °C, so the error falls to about 0.19 °C, roughly half of the original.
Experiment 2 (larger step): change h to 5.0. Record:
•	Euler after 30 min is about 25.27 °C, and the error grows to about 1.5 °C. The graph shows a coarse staircase-like curve that drops too fast.
Experiment 3 (unstable step): change h to 10.0. Record:
•	The values are 90, 12, 27.6 and 24.48. The temperature undershoots below the 25 °C room temperature and oscillates, which is physically impossible.
Experiment 4: change k = 0.12 to k = 0.25 (with h back to 1.0). Record:
•	The object cools much faster, and after 30 min Euler gives about 25.01 °C, nearly at room temperature.
Explanation to write:
•	The Euler error is roughly proportional to h, so halving the step halves the error, at the cost of twice as many steps.
•	Each Euler step assumes the slope stays constant over the whole step. With a big step the slope has changed a lot by the end, so the error grows.
•	The method becomes unstable when the factor (1 − kh) is below −1, that is when h > 2/k ≈ 16.7 minutes here. Even at h = 10 the factor is −0.2, which gives wrong oscillations.
•	A larger k means faster cooling, which also makes Euler less accurate for the same h, because the temperature changes faster within a step.

INSTRUCTION D: THE MEANING OF THE OUTPUT IN WORDS.
The program predicts how a 90 °C object cools in a 25 °C room. After 30 minutes, Euler’s method gives 26.40 °C, while the exact formula gives 26.78 °C. The error of 0.37 °C is small (about 0.6% of the original temperature difference), so Euler is good enough for this step size. Euler slightly underestimates the temperature because each step uses the slope at the start of the step, which is steeper than the average slope across the step.
Graph: the x-axis is time in minutes and the y-axis is temperature in °C. Both curves start at 90 °C and fall steeply at first (about 8 °C per minute), then flatten as they approach the room temperature of 25 °C. The Euler curve (with dots) lies slightly below the exact curve all the way, and the gap is largest in the first few minutes before the curves flatten out. The object never drops below 25 °C, which matches the physics.


TASK 18 (SOLVING ODES WITH SCIPY)
INSTRUCTION B: INPUT VALUES AND THE MATHEMATICAL OPERATIONS PERFORMED.
•	Inputs: 
o	Supply voltage Vs = 5 V, resistance R = 1000 Ω, capacitance C = 0.001 F
o	Initial capacitor voltage V₀ = 0 V
o	Time interval 0 to 5 s, with 200 output times
o	Tolerances rtol = 1e-9 and atol = 1e-11
•	Operations: 
o	The ODE is dV/dt = (Vs − V)/(RC). The capacitor charges quickly while the voltage gap is large, and more slowly as the gap closes.
o	solve_ivp steps through time using a higher-order Runge-Kutta method (RK45 by default) and adjusts the step size automatically to stay within the tolerances.
o	t_eval asks for the answer at 200 chosen times.
o	The exact solution V(t) = Vs(1 − e^(−t/RC)) is used to check the error.
o	The time constant is RC = 1000 × 0.001 = 1 s.
INSTRUCTION C: CHANGE ATLEAST ONE INPUT/ PARAMETER.
Experiment 1 (larger capacitor): change C = 0.001 to C = 0.002. Record:
•	RC = 2 s, and the voltage at 5 s is 4.5896 V (5(1 − e^(−2.5))).
Experiment 2 (higher supply): change Vs = 5.0 to 12.0. Record:
•	The voltage at 5 s is about 11.919 V.
Experiment 3 (discharging): set Vs = 0.0 and V0 = 5.0. Record:
•	The voltage falls from 5 V to about 0.0337 V at 5 s (5e⁻⁵). The curve decays instead of rising.
Experiment 4 (looser tolerance): change rtol=1e-9, atol=1e-11 to rtol=1e-3, atol=1e-6. Record the new maximum error. It should rise noticeably, but the graph looks the same.
Explanation to write:
•	A larger RC means a longer time constant, so charging is slower. Doubling C doubles RC, so at 5 s the capacitor has reached less of the supply voltage (4.59 V instead of 4.97 V).
•	The final voltage approaches the supply voltage, so a higher Vs scales the whole curve up. The shape stays the same.
•	Setting Vs = 0 turns charging into discharging, with V decaying exponentially toward 0.
•	Tight tolerances make the solver take smaller steps and give a more accurate answer at a higher cost. Loose tolerances run faster but with a larger error.
•	After one time constant (1 s) the capacitor reaches 63.2% of the supply voltage, and after about five time constants it is above 99%.
INSTRUCTION D: THE MEANING OF THE OUTPUT IN WORDS.
The program simulates a capacitor charging through a resistor from a 5 V supply. The solver reports success, and after 5 seconds the capacitor voltage is 4.9663 V, which is 99.3% of the supply voltage. The maximum difference from the exact formula is about 1e-9 V, so the numerical solution is essentially exact. After one time constant (RC = 1 s) the voltage is about 3.16 V, which is the familiar 63.2% rule.
Graph: the x-axis is time in seconds and the y-axis is the capacitor voltage in volts. The curve starts at 0 V and rises steeply at first (the initial slope is Vs/RC = 5 V per second), then flattens as it approaches 5 V. The solid solver curve and the dashed exact curve lie on top of each other, so no difference can be seen. The flattening shows that the charging current falls as the capacitor fills up.


TASK 19 (NUMERICAL OPTIMIZATION)
INSTRUCTION B: INPUT VALUES AND THE MATHEMATICAL OPERATIONS PERFORMED.
•	Inputs: 
o	Cost per unit: A = 12, B = 18
o	Capacity per unit: A = 100, B = 170
o	Required capacity: at least 1000
o	Bounds x ≥ 0 and y ≥ 0
o	Starting guess (5, 3)
•	Operations: 
o	Objective: minimize cost = 12x + 18y.
o	Constraint: 100x + 170y − 1000 ≥ 0. SciPy’s "ineq" means the function must be ≥ 0.
o	minimize with SLSQP searches for the lowest cost that satisfies the constraint and the bounds.
o	The loops then test whole-number combinations and keep the cheapest one that meets the capacity requirement.
INSTRUCTION C: CHANGE ATLEAST ONE INPUT/ PARAMETER.
Experiment 1 (higher demand): change 1000 to 2000 in capacity_constraint, and 1000 in the integer loop’s if capacity >= 1000. Record:
•	Type B = 11.765, Type A = 0, cost = 211.76.
•	The whole-server answer costs 216.
Experiment 2 (B becomes expensive): change the cost of B from 18 to 25 in both cost() and the integer loop. Record:
•	Type A = 10.000, Type B = 0, cost = 120.00.
•	The whole-server answer is (120, 10, 0, 1000).
Experiment 3 (limit on B): change the bounds to [(0, None), (0, 3)], so at most 3 units of B. Record:
•	Type B = 3.000, Type A = 4.900, cost = 112.80.
Explanation to write:
•	Doubling the demand roughly doubles the cost, and the cheapest-per-capacity server is still used.
•	Type B is cheaper per unit of capacity (0.106 against 0.120), so the optimizer uses only B. When B’s cost rises to 25, its cost per capacity (0.147) is higher than A’s (0.120), so the answer switches to only A. The optimum depends on cost per unit of capacity, not on the unit price alone.
•	A limit on B forces the optimizer to use B up to its limit and fill the rest with A, so the cost rises (105.88 to 112.80). Adding a constraint can never make the optimum cheaper.
•	Rounding to whole servers raises the cost (105.88 to 108) because the continuous answer of 5.882 servers is not physically possible. The whole-server answer is always at least as expensive as the continuous one.
INSTRUCTION D: THE MEANING OF THE OUTPUT IN WORDS.
The program finds the cheapest mix of two server types that provides at least 1000 units of processing capacity. The optimizer reports success and recommends using only Type B, about 5.88 units, giving exactly 1000 capacity at a planning cost of 105.88. Type B is the better buy because each unit of capacity costs less (0.106) than Type A (0.120). The constraint is “active”, meaning the optimizer uses exactly the minimum capacity, because extra capacity would only add cost. Because servers come in whole numbers, the practical answer is 6 Type B servers, which gives 1020 capacity at a cost of 108, only 2% above the theoretical minimum. This task has no graph.


TASK 20 (RANDOM NUMBERS AND MONTE CARLO METHODS)
INSTRUCTION B: INPUT VALUES AND THE MATHEMATICAL OPERATIONS PERFORMED.
•	Inputs: 
o	Server capacity 1000 requests, mean demand 850, standard deviation 120
o	N = 100,000 simulated scenarios, random seed 42 (so results can be repeated)
•	Operations: 
o	rng.normal generates N random demand values from a normal distribution.
o	demand > capacity marks each scenario as overloaded (True) or not (False).
o	The mean of those True/False values is the estimated probability: overloaded cases ÷ total cases.
o	The running probability after each simulation shows how the estimate settles as N grows.
INSTRUCTION C: CHANGE ATLEAST ONE INPUT/ PARAMETER.
Experiment 1 (more capacity): change capacity to 1100. Record:
•	Overload probability falls to about 1.9%.
Experiment 2 (less variable demand): change std_demand to 80. Record:
•	Overload probability falls to about 3.0%.
Experiment 3 (higher average demand): change mean_demand to 900. Record:
•	Overload probability rises to about 20%.
Experiment 4 (fewer simulations): change N to 1_000. Record:
•	The estimate becomes noisy, typically anywhere between about 8% and 13%. Run it with a few different seeds (for example default_rng(1), default_rng(2)) to see the spread.
Explanation to write:
•	Extra capacity moves the limit further into the tail of the demand distribution, where few scenarios reach it.
•	Less variability makes extreme demands rarer, so risk falls even though the average is unchanged.
•	Higher average demand pushes the whole distribution towards the limit, so overload becomes much more likely.
•	The accuracy of a Monte Carlo estimate improves only with the square root of N. Ten times more simulations cuts the error by only about 3 times.

INSTRUCTION D: THE MEANING OF THE OUTPUT IN WORDS.
•	The program simulated 100,000 possible days of demand on a server with a capacity of 1000 requests, where demand averages 850 with a spread of 120. In about 10.5% of the simulated days the demand exceeded the capacity, so the server has roughly a 1-in-10 chance of being overloaded. This matches the theoretical value of 10.57% to within the small standard error of about 0.1%.
•	Graph: the x-axis is the number of simulations on a log scale and the y-axis is the estimated overload probability. At the left (10 to 100 simulations) the line jumps around widely, because a few random cases can change the fraction a lot. As the number of simulations grows, the line settles and flattens onto the dashed theoretical line at about 0.106. This shows that Monte Carlo estimates converge as N increases.



