def print_tree(height):
    """To print tree we need 2*n-1 series starting with n=1"""
    # 1, 3, 5, 7, 9..so on i.e. (2*n -1; n starting from 1 onwards)    
    # 2*1 -1 = 1
    # 2*2 -1 = 3
    # 2*3 -1 = 5
    # 2*4 -1 = 7
    # 2*5 -1 = 19
    offset = 100 #some number which roughly corresponds to your output windows's mid point.
    for i in range(1,height+1):
        num_stars = 2*i -1
        temp_offset = offset - int(num_stars/2)        
        for j in range(temp_offset):
            print(" ",end=" ")
        for k in range(num_stars):
            print("*",end=" ")
        print("\n") # move to next line now to again start printing next row of *

if __name__=="__main__":
    print_tree(height=5)