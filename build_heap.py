# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    length = len(data)
    lastIndex = length//2-1

    def helper(i):
        i1 = 2*i+1
        i2 = 2*i+2
        if data[i] > data[i1] or (i2 < length and data[i] > data[i2]):
            if i2 < length and data[i2] < data[i1]:
                i3 = i2
            else:
                i3 = i1
            data[i], data[i3] = data[i3], data[i]
            swaps.append((i, i3))
            if i3 <= lastIndex:
                helper(i3)

    for i in range(lastIndex, -1, -1):
        helper(i)

    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    inputType = input()
    if inputType and inputType[0] == "I":
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
    elif inputType and inputType[0] == "F":
        # input from file
        file = open("tests/" + input(), "r").readlines()
        n = int(file[0])
        data = list(map(int, file[1].split()))
    else:
        return

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n
    
    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
