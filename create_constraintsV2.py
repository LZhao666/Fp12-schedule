
op = []
count = 0
with open("1.txt", "r", encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip('\n')  # 去掉列表中每一个元素的换行符
        count += 1
        op.append(line)
f = open("3.txt","w")

def resource(op): 
    if op[0:3] == 'mdd':
        r = "mdd" + op[34:]   
    elif op[0:3] == 'mud':
        r = "mud" + op[28:]
    elif op[0:3] == 'mld':
        r = "mld" + op[28:]
    elif op[0:3] == 'mrd':
        r = "mrd" + op[28:]
    elif op[0:3] == 'mod':
        r = "mod" + op[22:]
    elif op[0:3] == 'add':
        r = "add" + op[22:] 
    else:
        r = "sub" + op[22:] 
    return r
# 最后得到的是一个二维列表





'''
print(count)
for i in range(0, count):
    # print("i=%d"%i)
    for j in range(0, count):
        # print("j=%d"%j)
        if op[i][4:9] == op[j][10:15] or op[i][4:9] == op[j][16:21]:

     
            f.write("S += "+resource(op[i])+" < "+resource(op[j])+"\n")


                

            #print(resource(op[j])[0:3])
            if (resource(op[j])[0:3] == "mul") and (resource(op[i])[0:3] == "add"):
                f.write("S += "+resource(op[i])+" <= "+resource(op[j])+"\n")



'''

for i in range(0, count):
    # print("i=%d"%i)
    for j in range(0, count):
        # print("j=%d"%j)
        if (
            op[i][4:9] == op[j][10:15]
            or op[i][4:9] == op[j][16:21]
            or op[i][4:9] == op[j][22:27]
            or op[i][4:9] == op[j][28:33]
        ):
            f.write("(""'"+resource(op[i])+"'" "," "'"+resource(op[j])+"'"")"",""\n")











'''

pairs = []

start_points = range(5,48,6)

for start in start_points:
    for offset in range(1,7): 
        pairs.append((f'mul{start}',f'mul{start+offset}'))
        # 直接将pairs列表转换为字符串并写入
for pair in pairs:
    f.write(f"    {pair},\n")
'''



    

