twelve = 'ABCDEFGHIJKL'
ten = '0123456789'
index = int(input()) - 2013
print(twelve[(index+5)%12] + ten[(index-1)%10])