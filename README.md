_____________________________________ Python Version _____________________________________

It is necessary to use any version 3.x

________________________________________ Solution ________________________________________

The solution is procedural with three functions
solving the request in the problem.

The function:
	-- changeOrientation:
			permits to chnage the direction of the move
	-- move:
			permits to manage the command M, then move of 1 unit in the direction
	-- calcFinalPos:
			iterates on the sequence of the command to reach the final position.
			There are some checks to control the data and the result.

________________________________________ Testing ________________________________________

There are unit testing for all the functions and paths in the code. In order to run the
unit testing, it is possible to use the command
	-- python -m unittest discover -p "*_test.py"