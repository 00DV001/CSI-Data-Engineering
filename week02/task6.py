#task6, https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
from collections import Counter
collection_of_sizes = int(input())
input_sizes = input()
list_input_sizes = input_sizes.split()
no_of_cust = int(input())
sales_total = 0
dict_size_no = dict(Counter(list_input_sizes))

for i in range(no_of_cust):
    selected_size_and_sale_value = input().split()
    search_key = selected_size_and_sale_value[0]
    sale_value = int(selected_size_and_sale_value[1])
    if search_key in dict_size_no:
        if dict_size_no[search_key] != 0:
            sales_total = sales_total + sale_value
            dict_size_no[search_key] -= 1
        else:
            continue

print(sales_total)

