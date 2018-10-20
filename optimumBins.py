# import libraries
import math
import itertools
import sys

def print_bins(freq, ls, output_file):
    fd = open(output_file, "w")

    # The values present between the indices "start" and "end-1" are printed in separate lines
    start = 0
    for bin_size in freq:
        end = start + bin_size
        for ele in ls[start:end]: fd.write(str(ele) + " ")
        fd.write("\n")
        start = end

def optimal_partition(bins, ls):
    ls.sort()

    # frequency of each unique element
    freq = [len(list(v)) for k, v in itertools.groupby(ls)]

    # merge until the length of list "freq" equals number of bins required
    while len(freq) > bins:
        min = math.inf
        # indices to keep track of minimum size pairs
        index_1, index_2 = 0, 0

        # check the sum of all possible adjacent pairs of elements
        for idx in range(len(freq) - 1):
            sum = freq[idx] + freq[idx + 1]
            if sum < min:
                min, index_1, index_2 = sum, idx, idx + 1

        freq[index_1] += freq[index_2]  # merge the pairs
        freq.pop(index_2)

    return freq


def main():
    """
    Contract/Assumptions:
        1. The elements assumed to be spread across all the bins and no Non-overlapping bins will be present
        2. The required number of bins is assumed to be lesser or equal to number of unique elements
        3. The input elements are of positive integers
    """

    if len(sys.argv) != 3:
        print("Please provide valid input")
        exit()

    _, input_file, output_file = sys.argv
    fd = open(input_file, "r")

    # strings in each line are type-casted to int and stored in a list
    data = [int(x) for x in fd.read().splitlines() if x != ""]
    fd.close()

    bins, ls = data[0], data[1:]  # initialize bin and input list

    freq = optimal_partition(bins, ls)  # optimally partition the elements into each bin

    print_bins(freq, ls, output_file)  # write the items in each bin into a file


if __name__ == '__main__':
    main()
