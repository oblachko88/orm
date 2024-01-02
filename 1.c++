#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

using namespace std;

const int rows = 5;
const int cols = 5;

class Maze {
public:
    Maze() {
        srand(time(nullptr));
        initializeMaze();
        placeObstacles();
        placeExit();
    }

    void displayMaze() {
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                cout << maze[i][j] << " ";
            }
            cout << endl;
        }
    }

    bool movePlayer(int row, int col) {
        if (row < 0 || row >= rows || col < 0 || col >= cols || maze[row][col] == 'X') {
            cout << "Invalid move! Try again." << endl;
            return false;
        }

        if (maze[row][col] == 'E') {
            cout << "Congratulations! You found the exit." << endl;
            return true;
        }

        cout << "Moved to row " << row << ", col " << col << endl;
        playerRow = row;
        playerCol = col;
        return false;
    }

private:
    vector<vector<char>> maze;
    int playerRow;
    int playerCol;

    void initializeMaze() {
        maze.resize(rows, vector<char>(cols, '.'));
        playerRow = 0;
        playerCol = 0;
        maze[playerRow][playerCol] = 'P';
    }

    void placeObstacles() {
        for (int i = 0; i < 5; ++i) {
            int obstacleRow = rand() % rows;
            int obstacleCol = rand() % cols;
            maze[obstacleRow][obstacleCol] = 'X';
        }
    }

    void placeExit() {
        int exitRow, exitCol;
        do {
            exitRow = rand() % rows;
            exitCol = rand() % cols;
        } while (maze[exitRow][exitCol] == 'X' || (exitRow == playerRow && exitCol == playerCol));

        maze[exitRow][exitCol] = 'E';
    }
};

int main() {
    Maze mazeGame;

    cout << "Welcome to the Maze Game!" << endl;
    cout << "Legend: P - Player, X - Obstacle, E - Exit" << endl;

    while (true) {
        mazeGame.displayMaze();

        cout << "Enter your move (W - Up, A - Left, S - Down, D - Right): ";
        char move;
        cin >> move;

        switch (move) {
            case 'W':
                if (mazeGame.movePlayer(mazeGame.playerRow - 1, mazeGame.playerCol))
                    return 0;
                break;
            case 'A':
                if (mazeGame.movePlayer(mazeGame.playerRow, mazeGame.playerCol - 1))
                    return 0;
                break;
            case 'S':
                if (mazeGame.movePlayer(mazeGame.playerRow + 1, mazeGame.playerCol))
                    return 0;
                break;
            case 'D':
                if (mazeGame.movePlayer(mazeGame.playerRow, mazeGame.playerCol + 1))
                    return 0;
                break;
            default:
                cout << "Invalid move! Try again." << endl;
        }
    }

    return 0;
}
