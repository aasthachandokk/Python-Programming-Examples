l = [1,2,3,4,5,6,7,8]

even_list = list(filter(lambda x: x%2 ==0, l))
result = list(map(lambda x : x **3, even_list))
print('List containing cube of even numbers:{}'.format(result))
