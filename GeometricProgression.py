
def GetGeometricSum(firstValue, ratio, item):
    try:
        sum = firstValue * (1 - ratio**item) / (1 - ratio)
    except ZeroDivisionError:
        print("输入比值不能为1")
        return None
    else:
        return sum

#每次1/4卖出的初值为25(a*1/4)、比值为3/4
while True:
    firstValue = ''
    try:
        firstValue, ratio, item = input("请依次输入等比数列的初值、比值、前几项，以空格分隔。输入 q 退出：").split()
    except Exception as exp:
        #print(exp)
        break
        #if firstValue == 'q':
        #    break
    else:
        firstValue = float(firstValue)
        ratio = float(ratio)
        item = int(item)
        sum = GetGeometricSum(firstValue, ratio, item)
        if sum:
            print("等比数列前" + str(item) + "项和为" + str(sum))
        else:
            pass

