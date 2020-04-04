### Killer Sudoku Solver

To run the solver use the following command: 

``python solver.py sudoku_easy.json``

The argument passed onto the file should be your filename. 

It will initially check if your input is in the correct format and if you haven't made any mistakes. 
When confirmed it will solve the sudoku and display a possible solution. 

The following data structure has been chosen as input for the solver:

```json
[
    {"totalSum": 10, "boxes": [[0, 0], [1, 0]]},
    {"totalSum": 19, "boxes": [[0, 1], [1, 1], [1,2]]}
]
```

The first square in the top right corner has the coordinates (0, 0)

Where the first value represents the row in the sudoku and the second the column. 
So [0, 1] would be the value to the right of the first square and [1, 0] would be the value 
underneath the first square.

#### Method
This solver uses backtracking to solve the puzzle. It will start at the top corner and checks if value n in range(1, 10)
could be placed there without breaking the rules. In case this is possible it will store the value n in the grid
and recursively calls the same solve() function that will continue to solve the second empty box in the sudoku. 
In case there is no possible solution for a certain field with the current state of the grid, it will go back to previous 
decisions and test for other values. 

This method seems very inefficient, and it is, but because of this method there is no need 
to code specific strategies that a human would use when solving a sudoku. 

#### Performance
With the project there are two examples that you can run to test the performance. 
The easy sudoku was solved in 0.8 seconds and tried 313.425 possibilities to find the correct answer. 
The medium sudoku was solved in 16 minutes and 8 seconds and tried 593.457.705 (that's more than 593 million possibility checks) possibilities to find the correct result!