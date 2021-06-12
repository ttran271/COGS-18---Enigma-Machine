"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import rotate, encrypt, decrypt, initial_setup
from classes import EnigmaMachine
##
##

def test_encrypt_decrypt():
    assert callable(encrypt)
    assert callable(decrypt)
    
    test_machine = EnigmaMachine()
    test_machine.create_rotors()
    input1 = "HELLO"
    input2 = "PYTHON"
    output1 = encrypt(input1, test_machine)
    output2 = encrypt(input2, test_machine)
    
    assert encrypt(input1, test_machine) != input1
    assert encrypt(input2, test_machine) != input2
    assert input1 == decrypt(output1, test_machine)
    assert input2 == decrypt(output2, test_machine)
    assert isinstance(output1, str)
    assert isinstance(output2, str)
    
    
    
def test_rotate_setup():
    assert callable(rotate)
    assert callable(initial_setup)
    
    test_machine = EnigmaMachine()
    test_machine.create_rotors()
    
    assert initial_setup(test_machine) != initial_setup(test_machine, 12, 4, 8)
    assert (test_machine.inner, test_machine.middle, test_machine.outer) == initial_setup(test_machine)
    
    
