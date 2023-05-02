num_list = [3,2,5,7,1,6]
sorted_list = []
##num_list.sort()
for i in num_list:
    for k in range(i+1,):
        if i < k:
            sorted_list.append(i)
            temp = i
            i = k
            k = temp

        else:
            print("wrong")
            
print(sorted_list)


print(num_list)
print(sorted_list)
print(len(num_list))