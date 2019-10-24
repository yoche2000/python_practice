# The Gril Group Info System was design by Bbangddok's Kimbab
# It is a practice of using dictionary

print("歡迎使用女團輸入系統")
team = input("請輸入團體名稱: ")
print("請在下面開始輸入 %s 的成員資料\n" % team)
izone = []

theflag = True
while theflag:
    info = {}
    name = input("輸入新增成員名稱: ")
    newbd = input("輸入該成員出生年: ")
    position = input("輸入該成員位置  : ")
    info['姓名'] = name
    info['生日'] = newbd
    info['位置'] = position
    print("新增第%d位成員資料為:" % (len(izone)+1), end=' ')
    print(info)

    flag = input("是否確定存入? [y/n]: ")
    if flag == 'y':
        izone.append(info)
        print("資料已存入")
    else:
        print("資料沒有存入")

    repeat = input("是否繼續增加成員資料? [y/n]: ")
    print("\n")
    if repeat != 'y':
        theflag = False

print ("\n女團 %s 的 %d位成員資料為: " % (team, len(izone)))
length = 0
for info in izone:
    if len(info['姓名'])>length:
        length = len(info['姓名'])

if length <=6:
    print("  %-6.2s %-4s %s" % ('姓名','生日', '位置'))
    print("--")
elif length <=8:
    print("  %-8.2s %-4s %s" % ('姓名', '生日', '位置'))
    print("--")
elif length <=10:
    print("  %-10.2s %-4s %s" % ('姓名', '生日', '位置'))
    print("--")
elif length <=12:
    print("  %-12.2s %-4s %s" % ('姓名', '生日', '位置'))
    print("--")
else:
    print("  %-15.2s %-4s %s" % ('姓名', '生日', '位置'))
    print("--")

for info in izone:
    if length <=6:
        print("  %-8s %-6s %s" % (info['姓名'], info['生日'], info['位置']))
    elif length <=8:
        print("  %-10s %-6s %s" % (info['姓名'], info['生日'], info['位置']))
    elif length <=10:
        print("  %-12s %-6s %s" % (info['姓名'], info['生日'], info['位置']))
    elif length <=12:
        print("  %-14s %-6s %s" % (info['姓名'], info['生日'], info['位置']))
    else:
        print("  %-17s %-4s %s" % (info['姓名'], info['生日'], info['位置']))
