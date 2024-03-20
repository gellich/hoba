def h1():
    import os
    from PIL import Image
    os.mkdir('kiritinki')
    k=0
    for i in os.listdir('forlab9'):
        img = Image.open(i)
        img = img.resize((img.width // 3, img.height // 3))
        k+=1
        img.save("D:\питон\kiritinki\img" + i + ".jpg")

def h2():
    k=1
    import os
    from PIL import Image
    os.mkdir('kiritinki')
    for i in os.listdir('forlab9'):
        if i.endswith('.jpg') or i.endswith('.png'):
            img = Image.open(i)
            img = img.resize((img.width // 3, img.height // 3))
            img.save("D:\питон\kiritinki\img" + str(k) + ".jpg")
            k+=1

def h3():
    import csv
    itog=0
    print('покупочки:')
    with open('data.csv') as file:
        file = csv.reader(file)
        for i in file:
            name=i[0]
            kolvo=int(i[1])
            cn=int(i[2])
            itog+=kolvo*cn