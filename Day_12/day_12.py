
input_data = open('input.txt','r') 
data = input_data.read().strip().split('\n')
#print(data)
new_data=list()
for direction in data:
    new_data += list((direction[0],direction[1:]))
print(new_data)
