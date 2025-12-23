import random

def find_mean(data):
    sum_num = 0
    n = len(data)
    for num in data:
        sum_num += num
    
    average = sum_num / n
    return average

def find_median(data):
    n = len(data)
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1,len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i],data[min_idx] = data[min_idx],data[i]
    
    print("Sorted Data:")
    print(data)
    if n % 2 == 0:
        return (data[int((n-1)/2) + 1] + data[int((n-1)/2)])/2
    else:
        return data[int((n-1)/2)]
    
def find_mode(data):
    hash_map = {}
    for num in data:
        if num in hash_map:
            hash_map[num] += 1
        else:
            hash_map[num] = 1
    
    max_count = max(hash_map.values())
    result = []
    for key in hash_map:
        if hash_map[key] == max_count:
            result.append(key)
    return result

data = random.sample(range(100),4)
print("Data:")
print(data)
print("Average:",find_mean(data))
print("Median:",find_median(data))
print("Mode:",find_mode(data))
