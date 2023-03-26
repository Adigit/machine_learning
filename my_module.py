def palindrom(a):
    '''this is a function to know if a string is a palindrom 
    or no'''
    if a == a[::-1]:
        return ('yes')
    else:
        return ('no')
    
    
def even_odd(num):
    if num %2 == 0:
        return 'even'
    else:
        return 'odd'
    
if __name__ == '__main__':
    print(palindrom('rotor'))
    print(even_odd(2))