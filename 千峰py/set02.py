# coding:utf-8

# 差集 -/difference
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1-s2)                           # {1, 2}
print(s1.difference(s2))               # {1, 2}

# 交集 &/intersection
print(s1&s2)                           # {3, 4}
print(s1.intersection(s2))             # {3, 4}

# 并集 |/union
print(s1|s2)                           # {1, 2, 3, 4, 5, 6}
print(s1.union(s2))                    # {1, 2, 3, 4, 5, 6}

'''
已知两个列表:
l1 = [5,1,2,9,0,3]
l2 = [7,2,5,7,9]

找出两个列表不同元素
找出两个列表共同元素
'''

l1 = [5,1,2,9,0,3]
l2 = [7,2,5,7,9]

# 共同元素 交集 &
set1 = set(l1)
set2 = set(l2)
set_intersection = set1&set2
print(set_intersection)           # {9, 2, 5}

# 不同元素
set_union = set1 | set2
set_difference = set_union - set_intersection
print(set_difference)             # {0, 1, 3, 7}