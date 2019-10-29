"""CS140 PS9
10/29/2019
Authors: Jake Cillay, Ruben Pacheco-Caldera"""
from operator import itemgetter
def preprocess(file_in):
    permuted_blocks = []
    file_in.readline()
    for line in file_in:
        newline = line.split()
        permuted_blocks.append(newline)
        permutation_1 = [newline[2],newline[0], newline[1]]
        permutation_2 = [newline[1], newline[2], newline[0]]
        permutation_3 = [newline[2], newline[1], newline[0]]
        permutation_5 = [newline[0], newline[2], newline[1]]
        permuted_blocks.append(permutation_1)

        permuted_blocks.append(permutation_3)

        permuted_blocks.append(permutation_5)

    new_blocks = []
    for i in permuted_blocks:
        new_list = []
        for elem in i:
            new_list.append(int(elem))
        new_blocks.append(new_list)

    sorted_permuted_blocks2 = sorted(new_blocks, key=lambda x: x[0], reverse=True)
    #print(sorted_permuted_blocks)
    print(sorted_permuted_blocks2)
    max_vals = []
    for i in range(len(sorted_permuted_blocks2) - 1):
        for j in range(i - 1, 0, -1 ):
            print(sorted_permuted_blocks2[i], sorted_permuted_blocks2[j])


def main():
    file = open("example.txt", "r")
    preprocess(file)

if __name__ == '__main__':
    main()
