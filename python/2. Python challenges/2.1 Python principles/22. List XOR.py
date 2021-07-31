# https://pythonprinciples.com/challenges/List-xor/

def list_xor(n,list1,list2):
    #return (n in list1) XOR (n in list2)
    return (n in list1) ^ (n in list2)
    
    
print(list_xor(1, [1, 2, 3], [4, 5, 6]))


# Solution from site
# smart solution: uses the built-in xor operator ^
def list_xor(n, list1, list2):
    return (n in list1) ^ (n in list2)

# naive solution: check each case at a time
def list_xor(n, list1, list2):
    if n not in list1 and n not in list2:
        return False
    if n in list1 and n in list2:
        return False
    return True

# https://www.w3schools.com/python/gloss_python_bitwise_operators.asp

# Operator      Name                   Description
# & 	        AND	                   Sets each bit to 1 if both bits are 1
# |	            OR	                   Sets each bit to 1 if one of two bits is 1
#  ^	        XOR	                   Sets each bit to 1 if only one of two bits is 1
# ~ 	        NOT	                   Inverts all the bits
# <<	        Zero fill left shift   Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	        Signed right shift	   Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
