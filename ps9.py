"""CS140 PS9
10/29/2019
Authors: Jake Cillay, Ruben Pacheco-Caldera"""
import sys

def optimalBlocks(file_in, file_out):
    in_file = open(file_in, "r")
    permuted_blocks = []
    blocks = in_file.readline()

    for line in in_file:
        newline = line.split()
        length = int(newline[0])
        width = int(newline[1])
        height = int(newline[2])
        # find all permutations of the dimensions of each block
        permuted_blocks.append([length, width, height])
        permuted_blocks.append([height, length, width])
        permuted_blocks.append([height, width, length])
        permuted_blocks.append([width, height, length])
        permuted_blocks.append([width, length, height])
        permuted_blocks.append([length, height, width])

        
    # blocks sorted in decreasing order based on their length
    s_p_b = sorted(permuted_blocks, key=lambda x: x[0])
    # max value table with number of blocks to get the height
    max_vals = []
    
    # going through range of sorted blocks
    for i in range(len(s_p_b) - 1):
        # considering the first block
        num_blocks = 1
        
        # references to the current blocks width,height and length
        cur_len = s_p_b[i][0]
        cur_wid = s_p_b[i][1]
        cur_height = s_p_b[i][2]
        total_height = cur_height

        blocks_used = []
        blocks_used.append([cur_len, cur_height,cur_height])
        # After selecting a block, we will find the next block, decreasing from i,
        # until we run out of blocks
        for j in range(i - 1, 0, -1 ):
            # This checks to make sure the length and width of the potential
            # new block is valid
            if ((s_p_b[j][0]< cur_len) and (s_p_b[j][1] < cur_wid) and not(int(blocks) == num_blocks)):

                # update the length and width to be the length and width of this block
                cur_len = s_p_b[j][0]
                cur_wid = s_p_b[j][1]
                cur_height = s_p_b[j][2]
                # add the blocks height to the current height of the block tower
                total_height += cur_height
                # update block number
                num_blocks += 1
                blocks_used.append([cur_len, cur_height, cur_height])
                
                
        # append the total height received from doing these checks in a pair with the blocks it used
        max_vals.append((total_height, num_blocks, blocks_used))
    # sort the pairs based on the the first element which is the height
    s_max_vals = sorted(max_vals, key=lambda x: x[0], reverse =True)
    max_tower = s_max_vals[0]

    # return the first element which should contain the biggest height possible
    max_height= max_tower[0]
    # returns the blocks used to get that height
    number_blocks = max_tower[1]

    outfile = open(file_out, "w")
    outfile.write(blocks)
    for elts in max_tower[2]:
        block = ""
        for dim in elts:
            block += str(dim) + " "
        outfile.write(block + "\n")
    print("The tallest tower has " + str(number_blocks) + " blocks and a height of " + str(max_height))
    
        
def main():

    optimalBlocks(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
