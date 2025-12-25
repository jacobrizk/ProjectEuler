minNum = 1
maxNum = 10
dem = 1
testList = []

while True:
    for num in range(minNum, maxNum + 1):
        print(dem, "/", num)
        if dem % num == 0:
            print("clear")
            testList.append(dem)
        dem += 1

print(testList)