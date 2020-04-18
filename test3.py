# 當清單中有需要分隔的東西時...

lines = []
with open('3.txt', 'r', encoding='utf-8-sig')as f:
    for line in f:
        lines.append(line.strip())

for line in lines:
    s = line.split(' ')
    time = s[0][:5] # 清單[0]內有時間與人名，[:5]為[0]之中第0個~第4個
    name = s[0][5:]
    print(name)