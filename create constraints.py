
op = []
count = 0
with open("1.txt", "r", encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip('\n')  # 去掉列表中每一个元素的换行符
        count += 1
        op.append(line)
f = open("2.txt","w")
'''
def resource(op): 
    if op[0:3] == 'mdd':
        r = "mdd" + op[34:]   
    elif op[0:3] == 'mud':
        r = "mud" + op[28:]
    elif op[0:3] == 'mmd':
        r = "mmd" + op[22:]
    elif op[0:3] == 'ypd':
        r = "ypd" + op[22:]
    elif op[0:3] == 'add':
        r = "add" + op[22:] 
    else:
        r = "sub" + op[22:] 
    return r
# 最后得到的是一个二维列表
'''
def resource(op): 
    if op[0:3] == 'mdd':
        r = "mdd[" + op[34:] + "]"
    elif op[0:3] == 'mud':
        r = "mud[" + op[28:] + "]"
    elif op[0:3] == 'mld':
        r = "mld[" + op[28:] + "]"
    elif op[0:3] == 'mrd':
        r = "mrd[" + op[28:] + "]"
    elif op[0:3] == 'mod':
        #print("j=%s"%op)
        r = "mod[" + op[22:] + "]"
    elif op[0:3] == 'add':
        r = "add[" + op[22:] + "]"
    else: 
        r = "sub[" + op[22:] + "]"
    return r

'''
for i in range(0, count):
    for j in range(0, count):
        if (
            op[i][4:9] == op[j][10:15]
            or op[i][4:9] == op[j][16:21]
            or op[i][4:9] == op[j][22:27]
            or op[i][4:9] == op[j][28:33]
        ):
            constraint = f"S += {resource(op[i])} < {resource(op[j])}"
            f.write(constraint + "\n")

'''


for i in range(0, count):
    for j in range(0, count):
        if (
            op[i][4:9] == op[j][10:15]
            or op[i][4:9] == op[j][16:21]
            or op[i][4:9] == op[j][22:27]
            or op[i][4:9] == op[j][28:33]
        ):
            left = resource(op[i])
            right = resource(op[j])
            # 如果左侧是 mdd[...] 且右侧是 add[...]
            if left.startswith("mdd[") and right.startswith("add["):
                constraint = f"S += {left} <= {right}"
            else:
                constraint = f"S += {left} < {right}"
            f.write(constraint + "\n")













'''
print(count)
for i in range(0, count):
    # print("i=%d"%i)
    for j in range(0, count):
        # print("j=%d"%j)
        if op[i][4:9] == op[i][10:15] or op[i][4:9] == op[j][16:21] or op[i][4:9] == op[j][22:27] or op[i][4:9] == op[j][28:32]:
            f.write("S += "+resource(op[i])+" < "+resource(op[j])+"\n")

'''
'''
or resource(op[i])[0:3] == "mod") and (resource(op[j])[0:3] == "add"
                or resource(op[i])[0:3] == "mud") and (resource(op[j])[0:3] == "add"
                or resource(op[i])[0:3] == "mud") and (resource(op[j])[0:3] == "add"
                or resource(op[i])[0:3] == "mud") and (resource(op[j])[0:3] == "add"
'''

            #print(resource(op[j])[0:3])
         
           



    

