"""CS140 PS9
10/29/2019
Authors: Jake Cillay, Ruben Pacheco-Caldera"""
def preprocess(file_in):
    permuted_blocks = []
    blocks = file_in.readline()
    for line in file_in:
        newline = line.split()
        permuted_blocks.append(newline)
        permutation_1 = [newline[2],newline[0], newline[1]]
        permutation_2 = [newline[2], newline[1], newline[0]]
        permutation_3 = [newline[1], newline[2], newline[0]]
        permutation_4 = [newline[1], newline[0], newline[2]]
        permutation_5 = [newline[0], newline[2], newline[1]]
        permuted_blocks.append(permutation_1)

        permuted_blocks.append(permutation_2)
        
        permuted_blocks.append(permutation_3)
        
        permuted_blocks.append(permutation_4)
        
        permuted_blocks.append(permutation_5) 


    new_blocks = []
    for i in permuted_blocks:
        new_list = []
        for elem in i:
            new_list.append(int(elem))
        new_blocks.append(new_list)
        
    #blocks sorted in decreasing order based on their length 
    s_p_b = sorted(new_blocks, key=lambda x: x[0])
    #max value table with number of blocks to get the height
    max_vals = []
    
    #going through range of sorted blocks 
    for i in range(len(s_p_b) - 1):
        #considering the first block
        num_blocks = 1
        
        #references to the current blocks width,height and length
        cur_len = s_p_b[i][0]
        cur_wid = s_p_b[i][1]
        cur_height = s_p_b[i][2]
        #After selecting a block, we will find the next block, decreasing from i, 
        #until we run out of blocks
        for j in range(i - 1, 0, -1 ):
            #This checks to make sure the length and width of the potential
            #new block is valid
            if ((s_p_b[j][0]< cur_len) and (s_p_b[j][1] < cur_wid) and not(int(blocks) == num_blocks)):
                print(blocks, num_blocks)
                #update the length and width to be the length and width of this block 
                cur_len = s_p_b[j][0]
                cur_wid = s_p_b[j][1]
                #add the blocks height to the current height of the block tower
                cur_height += s_p_b[j][2]
                #update block number
                num_blocks += 1
                
                
        #append the total height received from doing these checks in a pair with the blocks it used
        max_vals.append((cur_height, num_blocks))
    #sort the pairs based on the the first element which is the height
    s_max_vals = sorted(max_vals, key=lambda x: x[0], reverse =True)
    #return the first element which should contain the biggest height possible
    max_val = s_max_vals[0][0]
    #returns the blocks used to get that height
    number_blocks = s_max_vals[0][1]
    for elts in max_vals:
        print(elts)
    print("max height = ", max_val, " numb Blocks = ", number_blocks)
    
        
def main():
    file = open("example.txt", "r")
    preprocess(file)

if __name__ == '__main__':
    main()
