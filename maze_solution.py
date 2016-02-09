
class MazeRunner():
    VISITED = 2
    WALL = 1
    FREE = 0
    PATH = 4
    START = 8
    END = 16

    def __init__(self, filename = 'input.txt'):
        self._board, self._start_point, self._end_point = self.read_data(filename)

    def find_way_out(self):
        "Depth First search algorithm using manhattan distance as a\
        heuristic for the 'best' child"
        current_point = self._start_point
        self._path = [self._start_point]
        self.mark_visited(current_point)
        while current_point != self._end_point:
            next_points = self.next_steps_from(current_point)
            if not next_points:
                self._path.pop()
                current_point = self._path[-1] # backtrack current point to the previous step
            else:
                current_point = self.find_closest(next_points, self._end_point)
                self.mark_visited(current_point)
                self._path.append(current_point)

    def print_path(self):
        for p in self._path:
            self._board[p[0]][p[1]] = MazeRunner.PATH
        self._board[self._start_point[0]][self._start_point[1]] = MazeRunner.START
        self._board[self._end_point[0]][self._end_point[1]] = MazeRunner.END
                                       
        for row in self._board:
            print ''.join(map(MazeRunner.to_symbol, row))
    
    def mark_visited(self, point):
        row, col = point[0], point[1]
        self._board[row][col] = MazeRunner.VISITED
        
    def read_data(self, filename):
        f = open(filename)
        
        size_str = f.readline() # read size of the maze
        h,w = map(int, size_str.strip('\n').split(' '))

        start_str = f.readline() # read starting point
        starting_point = tuple(map(int, start_str.strip('\n').split(' ')))

        end_str = f.readline()  # read ending point
        ending_point = tuple(map(int, end_str.strip('\n').split(' ')))

        board = [0]*h
        for i in range(h):
            board[i] = map(int, f.readline().strip('\n').split(' '))

        f.close()
        return(board, starting_point, ending_point)

    def print_board(self):
        for row in self._board:
            print row
    
    def next_steps_from(self, point):
        steps = []
        r, c = point[0], point[1]
        if self._board[r-1][c] == MazeRunner.FREE:
            steps.append((r-1, c))
        if self._board[r+1][c] == MazeRunner.FREE:
            steps.append((r+1, c))
        if self._board[r][c-1] == MazeRunner.FREE:
            steps.append((r, c-1))
        if self._board[r][c+1] == MazeRunner.FREE:
            steps.append((r, c+1))
        return steps

    @staticmethod
    def to_symbol(n):
        if n == MazeRunner.WALL:
            return '#'
        elif n == MazeRunner.PATH:
            return 'X'
        elif n == MazeRunner.START:
            return 'S'
        elif n == MazeRunner.END:
            return 'E'
        else:
            return ' '
        
    @staticmethod
    def distance(pointA, pointB):
        "Manhattan distance"
        return abs(pointA[0] - pointB[0]) + abs(pointA[1]-pointB[1])

    @staticmethod        
    def find_closest(points, end_point):
        distances = [MazeRunner.distance(p, end_point) for p in points]
        i = distances.index(min(distances))
        return points[i]

# Test files:
# input.txt, large_input.txt, medium_input.txt, small.txt, sparse_medium.txt

maze_runner = MazeRunner('sparse_medium.txt')
maze_runner.print_board()
maze_runner.find_way_out()
maze_runner.print_path()
