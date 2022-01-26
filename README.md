# 2048-clone

Design principles used:-
1. Each logic function will be designed in such a way that it can be used for both left and right swipes by inverting the matrix and executing left swipe.
2. You may move up by using transposition and then moving left.
3. You may move down by transposing the right-hand movement.

Problems faced while designing the solution:-
To change the stataus of the game. To have the player make the move.

Code walkthrough:-
#![image](https://user-images.githubusercontent.com/65595618/151183578-335711cf-0764-4751-be1a-c407cc9ac1ae.png)
declaring an empty list then
appending 4 list each with four
elements as 0.

#![image](https://user-images.githubusercontent.com/65595618/151183841-f3794784-8a89-41c6-9561-9289ea7dd057.png)
/nchoosing a random index for row and column. add element in a random cell.

Then all function such as reverse, transpose, merge, compress where made doing what the name suggest

After that functions that provide movement where made./n
#![image](https://user-images.githubusercontent.com/65595618/151185069-e821eeea-69f6-45d6-b90d-774cfef5eeac.png)

This gives the current array and also checks if the game is over or not./n
#![image](https://user-images.githubusercontent.com/65595618/151185193-8df87175-c4e2-4439-9021-f42564544a2f.png)

Finally the main function that runs this program.

Scope of making this an 8x8 from 4x4:-
For this mall movement functions has to be modified, also the initial array will be of 8*8.

Change from 2048 to 4096 as end number:-

Change the value to 4096 in the get status function.
