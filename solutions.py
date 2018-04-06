# Question 1
# Given two strings s and t, determine whether some anagram of t is a substring
# of s. For example: if s = "udacity" and t = "ad", then the function
# returns True. Your function definition should look like: question1(s, t) and
# return a boolean True or False.


def question1(s, t):
    string = {}
    count = 0
    if len(t) == 0:
        return False

    for letter in s:
        string[letter] = s.count(letter, 0, len(s))

    for letter in t:
        for key in string:
            if string.get(letter) is None:
                return False
            else:
                if key == letter:
                    if string[letter] <= 0:
                        return False
                    else:
                        string[letter] -= 1
                        break
    return True


# # Should be True
# s = "udacity"
# t = "uc"
# print question1(s, t)
# # Should be False: insufficient letters
# s = "udacity"
# t = "uu"
# print question1(s, t)
# # Should be False: foreign letter
# s = "udacity"
# t = "az"
# print question1(s, t)
# # Should be False: no string provided
# s = "udacity"
# t = ""
# print question1(s, t)

# Question 2
# Given a string a, find the longest palindromic substring contained in a.
# Your function definition should look like question2(a), and return a string.


def question2(a):
    longest = ""
    current = ""
    data = {}

    for index in range(len(a)):
        check = palindrome(a[index:len(a)])
        if check:
            current = a[index:len(a)]
            if len(current) > len(longest):
                longest = current
        else:
            current = question2(a[index:len(a) - 1])
            if len(current) > len(longest):
                longest = current
    return longest


def palindrome(a):
    if a == "":
        return True
    else:
        if a[0] == a[-1]:
            return palindrome(a[1:-1])
        else:
            return False

# # Should be 'ababa'
# a = "ababa"
# print question2(a)
# # Should be 'ababa'
# a = "ababad"
# print question2(a)
# # Should be 'aba'
# a = "ababda"
# print question2(a)
# # Should be 'rotor'
# a = "rotoring"
# print question2(a)

# Question 3
# Given an undirected graph G, find the minimum spanning tree within G.
# A minimum spanning tree connects all vertices in a graph with the smallest
# possible total weight of edges. Your function should take in and return
# an adjacency list structured like this:
#
# {'A': [('B', 2)],
#  'B': [('A', 2), ('C', 5)],
#  'C': [('B', 5)]}
# Vertices are represented as unique strings.
# The function definition should be question3(G)


class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []


class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_edge(self, new_edge_val, node_A_val, node_B_val):
        node_A = None
        node_B = None
        for node in self.nodes:
            if node_A_val == node.value:
                node_A = node
            if node_B_val == node.value:
                node_B = node
        if node_A is None:
            node_A = Node(node_A_val)
            self.nodes.append(node_A)
        if node_B is None:
            node_B = Node(node_B_val)
            self.nodes.append(node_B)
        AB_edge = Edge(new_edge_val, node_A, node_B)
        node_A.edges.append(AB_edge)
        node_B.edges.append(AB_edge)
        self.edges.append(AB_edge)

        BA_edge = Edge(new_edge_val, node_B, node_A)
        node_A.edges.append(BA_edge)
        node_B.edges.append(BA_edge)
        self.edges.append(BA_edge)

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)

    def get_edge_list(self):
        list = []
        for edge_obj in self.edges:
            edge = [edge_obj.value, edge_obj.node_from.value, edge_obj.node_to.value]
            list.append(edge)
        return list


def question3(G):
    print G.get_edge_list()


G = Graph()
G.insert_edge(2, "A", "B")
G.insert_edge(5, "B", "C")
G.insert_edge(3, "B", "D")
G.insert_edge(1, "C", "D")

print question3(G)





# Question 4
# Find the least common ancestor between two nodes on a binary search tree.
# The least common ancestor is the farthest node from the root that is an
# ancestor of both nodes. For example, the root is a common ancestor of all
# nodes on the tree, but if both nodes are descendents of the root's left child,
# then that left child might be the lowest common ancestor. You can assume that
# both nodes are in the tree, and the tree itself adheres to all BST properties.
# The function definition should look like question4(T, r, n1, n2), where T is
# the tree represented as a matrix, where the index of the list is equal to the
# integer stored in that node and a 1 represents a child node, r is a
# non-negative integer representing the root, and n1 and n2 are non-negative
# integers representing the two nodes in no particular order. For example,
# one test case might be
#
# question4([[0, 1, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [1, 0, 0, 0, 1],
#            [0, 0, 0, 0, 0]],
#           3,
#           1,
#           4)
# and the answer would be 3.


def question4():
    return

# Question 5
# Find the element in a singly linked list that's m elements from the end.
# For example, if a linked list has 5 elements, the 3rd element from the end is
# the 3rd element. The function definition should look like question5(ll, m),
# where ll is the first node of a linked list and m is the
# "mth number from the end". You should copy/paste the Node class below to use
# as a representation of a node in the linked list. Return the value of the node
# at that position.
#
# class Node(object):
#   def __init__(self, data):
#     self.data = data
#     self.next = None


def question5():
    return
