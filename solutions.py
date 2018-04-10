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
        self.edges.append(AB_edge)

        # BA_edge = Edge(new_edge_val, node_B, node_A)
        # node_A.edges.append(BA_edge)
        # self.edges.append(BA_edge)

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
    # Build the graph
    setup = Graph()
    for node in G:
        for tuple in G[node]:
            nodeA = node
            nodeB = tuple[0]
            value = tuple[1]
            setup.insert_edge(value, nodeA, nodeB)

    adjacency_list = {}
    # Select a random node, probably the first one
    # See all available edges and pick the one with the least value
    # Move to that new node and list all untaken edges with the nodes selected so far
    nodes = setup.nodes
    nodes[0].edges
    # nodes[0].edges[0]
    # nodes[0].edges[1]
    return adjacency_list

G = {
        'A': [('B', 2)],
        'B': [('A', 2), ('C', 5)],
        'C': [('B', 5)]
    }


# print question3(G)


# Question 4
# Find the least common ancestor between two nodes on a binary search tree.
# The least common ancestor is the farthest node from the root that is an
# ancestor of both nodes. For example, the root is a common ancestor of all
# nodes on the tree, but if both nodes are descendents of the root's
# left child, then that left child might be the lowest common ancestor.
# You can assume that both nodes are in the tree, and the tree itself adheres
# to all BST properties.

# The function definition should look like question4(T, r, n1, n2), where T is
# the tree represented as a matrix, where the index of the list is equal to the
# integer stored in that node and a 1 represents a child node, r is a
# non-negative integer representing the root, and n1 and n2 are non-negative
# integers representing the two nodes in no particular order. For example,
# one test case might be

# question4([[0, 1, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [1, 0, 0, 0, 1],
#            [0, 0, 0, 0, 0]],
#           3,
#           1,
#           4)
# and the answer would be 3.

def traverse(T, r, n1, n2, data):
    if sum(T[r]) == 0:
        print "ENTER"
        return False
    else:
        # Check to see if there are children
        for index, child in enumerate(T[r]):
            # If there's children, check the value to see if it matches either
            if child:
                if index is n1:
                    data[n1][0] = True
                    data[n1].append(r)
                elif index is n2:
                    data[n2][0] = True
                    data[n2].append(r)
                # Continue going deeper into the tree
                else:
                    if data[n1][0] is False:
                        data[n1].append(r)
                    if data[n2][0] is False:
                        data[n2].append(r)
                    traverse(T, index, n1, n2, data)
                    return data
        return data


def find_ancestor(data, n1, n2):
    extract_n1 = data[n1][1:]
    extract_n2 = data[n2][1:]

    for i in reversed(extract_n1):
        for j in reversed(extract_n2):
            if i is j:
                return i


def question4(T, r, n1, n2):
    # Find the root node
    try:
        data = {
            n1: [False],
            n2: [False]
        }
        # Check for children
        traverse(T, r, n1, n2, data)
        return find_ancestor(data, n1, n2)
    except TypeError:
        print "Check your parameter inputs to see if they're valid"


# # Should be 3
# print question4([[0, 1, 0, 0, 0],
#                  [0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0],
#                  [1, 0, 0, 0, 1],
#                  [0, 0, 0, 0, 0]],
#                 3,
#                 1,
#                 4)
#
# # Should be 0
# print question4([[0, 1, 1, 0, 0],
#                  [0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0],
#                  [1, 0, 0, 0, 1],
#                  [0, 0, 0, 0, 0]],
#                 3,
#                 1,
#                 2)
#
# # Should be 0
# print question4([[0, 1, 1, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 1],
#                  [1, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 1, 0]],
#                 3,
#                 1,
#                 4)
#
# # Should throw an error
# print question4("", "", "", "")

# Question 5
# Find the element in a singly linked list that's m elements from the end.
# For example, if a linked list has 5 elements, the 3rd element from the end is
# the 3rd element. The function definition should look like question5(ll, m),
# where ll is the first node of a linked list and m is the
# "mth number from the end". You should copy/paste the Node class below to use
# as a representation of a node in the linked list.
# Return the value of the node at that position.


class List_Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert(self, new_element, position):
        upper_bound = self.get_position(position)
        lower_bound = self.get_position(position - 1)

        lower_bound.next = new_element
        new_element.next = upper_bound

    def get_position(self, position):
        element = self.head
        if self.head:
            while position > 1:
                element = element.next
                position -= 1
            return element
        else:
            return None

    def list_count(self):
        count = 0
        element = self.head
        if self.head:
            count = 1
            while element.next is not None:
                count += 1
                element = element.next
            return count
        else:
            return count


def test_ll(start, end):
    ll = LinkedList()
    for value in range(start, end):
        element = List_Node(value)
        ll.append(element)
    return ll


def question5(ll, m):
    length = ll.list_count()
    if m > length:
        return None
    elif m == 0:
        return None
    return ll.get_position(length - m + 1).value


# # Should return 3
# ll = test_ll(1, 7)
# m = 3
# print question5(ll, m)
# # Should return 5
# ll = test_ll(1, 8)
# m = 3
# print question5(ll, m)
# # Should return None
# ll = test_ll(1, 7)
# m = 10
# print question5(ll, m)
# # Should return None
# ll = test_ll(1, 7)
# m = 0
# print question5(ll, m)
