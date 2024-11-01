def power(FirstNum,SecondNum):

    if SecondNum == 0:
        return 1

    return FirstNum * power(FirstNum, SecondNum - 1)




FirstNum = int(input())
SecondNum = int(input())

print(power(FirstNum, SecondNum))
