#include <iostream>
#include <utility>

using namespace std;

/*
	INPUT : 9 rows of numbers which represent the sudoku, NO SPACES
	OUTPUT : if solution exists outputs 9 rows of numbers ---> SOlved sudoku
			else prints out -1
*/

int grid[9][9];


bool in_box(int row, int col , int num){
	/*
		Parameters:	row --> row in which num might potentially be placed
					col --> coloumn in which num might potentially be placed
		As per rules of sudoku this function checks:
			---> If the number num exists in the box that the (a,b) is in
		if above happens num must not be placed in (a,b)
			---> returns false
		otherwise
			---> returns true
	*/

	int row_start_box = 0;
	int col_start_box = 0;
	
	if(row>=3) row_start_box = 3;
	if(row>=6) row_start_box = 6;
	
	if(col>=3) col_start_box = 3;
	if(col>=6) col_start_box = 6;
	
	for(int i = 0;i<3;i++){
		for(int j = 0;j<3;j++){
			if(grid[row_start_box+i][col_start_box+j] == num)
				return false;
		}
	}
	
	return true;
}

bool in_rowcol(int row , int col , int num){
	/*
		Parameters:	row --> row in which num might potentially be placed
					col --> coloumn in which num might potentially be placed
		As per rules of sudoku this function checks:
			---> If the number num exists in given row
			---> If the number num exists in given column
		if any of the above happens num must not be placed in (a,b)
			---> returns false
		otherwise
			---> returns true
	*/

	for(int i = 0;i<9;i++){
		if(grid[row][i] == num)
			return false;
	}
	
	for(int i = 0;i<9;i++){
		if(grid[i][col] == num){
			return false;
		}
	}
	
	return true;
}

pair<int,int> findzero(){
	/*
		Finds first zero in the grid array and returns a pair indicating its position
		if no zero exists it returns {-1,-1}
	*/

	for(int i = 0;i<9;i++){
		for(int j =0; j <9;j++)
			if(grid[i][j] == 0)
				return {i,j};
	}
	return {-1,-1};
}


bool findans(){
	/*
		Fills the grid array with a possible solution and returns true.
		If no solution exists, keeps grid array as is and returns false
	*/

	pair<int,int> coordinate = findzero();
	pair<int,int> nozeros = {-1,-1};
	if(coordinate == nozeros)
		return true;
	
	int row = coordinate.first;
	int col = coordinate.second;
	//bool found = false;
	
	for(int i = 1;i<=9;i++){
		if(!in_box(row,col,i))
			continue;
		if(!in_rowcol(row,col,i))
			continue;
		
		//found = true;
		grid[row][col] = i;
		if(findans())
			return true;
		grid[row][col] = 0;
	}
	
	return false;
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	//Taking input, we assuming there are no spaces in between
	string sudoku[9];
	for(int i = 0;i<9;i++){
		cin>>sudoku[i];
	}
	
	//parsing the input into a 2D array, which represents the sudoku
	for(int i = 0;i<9;i++){
		for(int j = 0;j<9;j++){
			grid[i][j] = sudoku[i][j] - '0';
		}
	}
	
	//fills the zeros in grid[][] and returns false if answer not found
	bool answer_found = findans();

	if(!answer_found){
		//No possible solution exists
		cout<<-1<<endl;
		return 0;
	}
	
	//output the final answer
	for(int i = 0;i<9;i++){
		for(int j = 0;j < 9; j++){
			cout<<(grid[i][j]);
		}
		cout<<endl;
	}

	
	return 0;
}
