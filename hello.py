def complicate_func(a):
    a += 1000
    a *= 0.5
    
    a = 'string'
    a *= 0.1
    return a



if __name__ == '__main__':
    a = 40
    ret = complicate_func(a)