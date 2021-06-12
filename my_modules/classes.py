"""Classes used throughout project"""
import random

class EnigmaMachine:
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    def __init__(self):
        self.inner = []
        self.middle = []
        self.outer = []
        
        char_A = 65;
        alphabet = [chr(char_A + i) for i in range(26)]
        
    def create_rotors(self):
        rotors = [self.inner, self.middle, self.outer]
        
        for each in rotors:
            length = 0
            duplicate = []
            
            while(length != 26):
                insert = random.choice(self.alphabet)
                if insert in duplicate:
                    continue
                else:
                    each.append(insert)
                    duplicate.append(insert)
                    length += 1
                    
    def show_rotors(self):
        print("Inner rotor is: ", end=' ')
        for letter in self.inner:
            print(letter, end=' ')
        print('\n')
        
        print("Middle rotor is: ", end=' ')
        for letter in self.middle:
            print(letter, end=' ')
        print('\n')
        
        print("Outer rotor is: ", end=' ')
        for letter in self.outer:
            print(letter, end=' ')
        print('\n')
        
    def initial_setup(self, key_inner=0, key_middle=0, key_outer=0):
        rotors = [self.inner, self.middle, self.outer]
        keys = [key_inner, key_middle, key_outer]
        
        for each, key in zip(rotors, keys):
            for i in range(key):
                each.insert(0, each.pop())
  
