from linkedbst import LinkedBST
import random
import time
from linkedbst import LinkedBST

def reaf_file(path):
    file_ = open(path, 'r')
    words_list = []
    for line in file_.readlines():
        line = line.strip()
        line = line.replace('\n', '8')
        words_list.append(line)
    words_random = random.sample(words_list, 10000)
    return words_list, words_random


def search_list(path):
    words_list, words_random = reaf_file(path)
    start = time.time()
    for i in words_random:
        searh_index = words_list.index(i)
    return time.time() - start

def search_tree(path):
    words_list, words_random = reaf_file(path)
    tree_1 = LinkedBST()
    for i in words_list:
        tree_1.add(i)
    start = time.time()
    for i in words_random:
        search_word = tree_1.find(i)
    variant_1 = time.time() - start
    #-------------------------------
    random.shuffle(words_list)
    tree_2 = LinkedBST()
    for i in words_list:
        tree_2.add(i)
    start = time.time()
    for i in words_random:
        search_word = tree_2.find(i)
    variant_2 = time.time() - start
    #-------------------------------
    tree_2.rebalance()
    start = time.time()
    for i in words_random:
        search_word = tree_2.find(i)
    variant_3 = time.time() - start
    return variant_1, variant_2, variant_3

if __name__ == "__main__":
    path = 'C:/Users/kleso/Desktop/words.txt'
    print("Time of searching with list methods is {}, in tree - {}, in random tree - {}, in rebalanced tree - {} ".format(
        search_list(path), search_tree(path)[0], search_tree(path)[1], search_tree(path)[-1]
    ))
