"""A collection of function for doing my project."""

def rotate(inner, middle, outer, inner_rotation, middle_rotation):
    inner_copy = inner.copy()
    middle_copy = middle.copy()
    outer_copy = outer.copy()
    
    inner_copy.insert(0, inner_copy.pop())
    new_inner = inner_copy
    inner_rotation += 1
    
    if(inner_rotation == 26):
        middle_copy.insert(0, middle_copy.pop())
        new_middle = middle_copy
        middle_rotation += 1
        inner_rotattion = 0;
            
    if(middle_rotation == 26):
        outer_copy.insert(0, outer_copy.pop())
        new_outer = outer_copy
        middle_rotation = 0
        
    return inner_copy, middle_copy, outer_copy, inner_rotation, middle_rotation


def initial_setup(enigma_module, key_inner=0, key_middle=0, key_outer=0):
    inner_setup = enigma_module.inner.copy()
    middle_setup = enigma_module.middle.copy()
    outer_setup = enigma_module.outer.copy()
    
    rotors = [inner_setup, middle_setup, outer_setup]
    keys = [key_inner, key_middle, key_outer]
    
    for rotor, key in zip(rotors, keys):
        for i in range(key):
            rotor.insert(0, rotor.pop())
    
    return inner_setup, middle_setup, outer_setup
    

def encrypt(input_text, enigma_module, key_inner=0, key_middle=0, key_outer=0):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    encrypted_output = ''
    
    inner_rotor, middle_rotor, outer_rotor = initial_setup(enigma_module, key_inner, key_middle, key_outer)
    inner_rotate = 0
    middle_rotate = 0
    
    for letter in input_text:
        if letter not in alphabet:
            encrypted_output += letter
            continue
        else:
            index = inner_rotor.index(letter)
            char = outer_rotor[index]
            
            index = middle_rotor.index(char)
            char = outer_rotor[index]
            
            encrypted_output += char
            inner_rotor, middle_rotor, outer_rotor, inner_rotate, middle_rotate = rotate(inner_rotor, middle_rotor, outer_rotor, inner_rotate, middle_rotate)
    
    return encrypted_output


def decrypt(input_text, enigma_module, key_inner=0, key_middle=0, key_outer=0):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    decrypted_output = ''
    
    inner_rotor, middle_rotor, outer_rotor = initial_setup(enigma_module, key_inner, key_middle, key_outer)
    inner_rotate = 0
    middle_rotate = 0
        
    for letter in input_text:
        if letter not in alphabet:
            decrypted_output += letter
            continue
        else:
            index = outer_rotor.index(letter)
            char = middle_rotor[index]
            
            index = outer_rotor.index(char)
            char = inner_rotor[index]

            decrypted_output += char
            inner_rotor, middle_rotor, outer_rotor, inner_rotate, middle_rotate = rotate(inner_rotor, middle_rotor, outer_rotor, inner_rotate, middle_rotate)
            
    return decrypted_output

