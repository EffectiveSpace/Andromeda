
class Game():
    def __init__(self):
        self.maps = [1, 2, 3,
                4, 5, 6,
                7, 8, 9]
        self.win_variant = [[0, 1, 2],
                    [3, 4, 5],
                    [6, 7, 8],
                    [0, 3, 6],
                    [1, 4, 7],
                    [2, 5, 8],
                    [0, 4, 8],
                    [2, 4, 6]]

    def print_maps(self):
        print(self.maps[0], end = ' ')
        print(self.maps[1], end = ' ')
        print(self.maps[2])
        
        print(self.maps[3], end = ' ')
        print(self.maps[4], end = ' ')
        print(self.maps[5])
        
        print(self.maps[6], end = ' ')
        print(self.maps[7], end = ' ')
        print(self.maps[8])

    def user_step(self, step, symbol):
        self.ind = self.maps.index(step)
        self.maps[self.ind] = symbol

    def get_result(self):
        self.win = ''
        
        for i in self.win_variant:
            if self.maps[i[0]] == 'X' and self.maps[i[1]] == 'X' and self.maps[i[2]] == 'X':
                self.win = 'X'
            if self.maps[i[0]] == 'O' and self.maps[i[1]] == 'O' and self.maps[i[2]] == 'O':
                self.win = 'O'
        return self.win