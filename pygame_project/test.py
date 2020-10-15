
lst = [[1,2],[3,4],[5,6]]

new_lst = [[ i[0] , i[1]+1 ] for i in lst if i[1] > 2 ]

print(new_lst)