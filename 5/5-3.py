# coding=utf-8
f = open('demo.txt', 'w')
f.write('abc')
f.write('+' * 4094)  # 通常缓冲区是4096

f2 = open('demo2.txt,' 'w', buffering=2048)  # 改变缓冲大小
f3 = open('demo3.txt,' 'w', buffering=1)  # 设置为1就是行缓冲
f4 = open('demo4.txt,' 'w', buffering=0)  # 设置为0就是无缓冲


