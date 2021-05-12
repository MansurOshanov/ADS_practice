class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        '''
        Idea is to traverse strings backwards.
        create helper iterator function
        '''
        def get_character(s):
            skip = 0
            for char in reversed(s):
                if char == "#":
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield char
        
        return all(x == y for x,y in itertools.zip_longest(get_character(s), get_character(t)))
        
        
            
        
        