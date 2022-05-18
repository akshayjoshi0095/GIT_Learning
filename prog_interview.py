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