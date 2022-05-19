## Sum of zero

def sumzero1(l):      ### As two loops so Compexity - O(n square)
    for i in range(len(l)-2):
        c = 0
        for j in range(i+1,len(l)):
            if l[j] + l[i] == 0:
                print(l[j],l[i])
                c += 1
                break
        if c > 0:
            break


def sumzero2(l):
    right_pointer = 0
    left_pointer = len(l)-1
    while right_pointer < left_pointer:
        if l[right_pointer] + l[left_pointer] == 0:
            print(l[right_pointer], l[left_pointer])
            break
        elif l[right_pointer] + l[left_pointer] > 0:
            left_pointer -= 1
        else:
            right_pointer += 1


l = [-5,-4,-3,0,2,4,8,10]


### Bubble sort
# in ranadom and reversed - O(n**2)
#in sorted - O(n)

def bubble_sort(l):
    for i in range(len(l)-1,0,-1):
        swap = 0
        for j in range(i):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
                swap += 1
        if swap == 0:
            break
    return l

sample_list = [10, 50, 50, 100, 100, 100, 20, 30, 40, 20, 30, 90, 40]

print(bubble_sort(sample_list))

