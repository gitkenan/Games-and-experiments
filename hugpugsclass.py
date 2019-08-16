class Tile(object):
    def __init__(self, letter, score):
        self.letter = letter
        self.score = score
    def get_letter(self):
        return self.letter
    def get_score(self):
        return self.score
		
Letter_1 = Tile("A", 30)

print Letter_1.get_score()

class Wildcard(Tile):
    def __init__(self, score):
        super(Wildcard, self).__init__('?', score)
    def set_letter(self, letter):
        self._letter = letter
    def reset(self):
        self._letter = '?'
		
