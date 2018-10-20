# nonOverlappingOptimalBins
A solution for non overlapping optimal bins

Given a list of integer items, we want to partition the items into at most N
non-overlapping, consecutive bins, in a way that minimizes the maximum number
of items in any bin.
For example, suppose we are given the items (5, 2, 3, 6, 1, 6), and we want 3
bins. 

We can optimally partition these as follows:
n < 3: 1, 2 (2 items)
3 <= n < 6: 3, 5 (2 items)
6 <= n: 6, 6 (2 items)
Every bin has 2 items, so we can’t do any better than that.


A program to partition a set of input items.

Can be executed with the following command from the source directory.

`python optimumBins.py input.txt output.txt`





