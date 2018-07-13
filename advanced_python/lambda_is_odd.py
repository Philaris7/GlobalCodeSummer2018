#! usr/bin/python3

num_list = [4,3,5,2,34,5,4,3,54]
is_odd = list(filter(lambda x : not  x % 2 == 0, num_list))
print(is_odd)
