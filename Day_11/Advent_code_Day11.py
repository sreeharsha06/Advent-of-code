
inputdata = open('input.txt','r')
lines = inputdata.read().strip().split("\n")
data =lambda seats: [[seat for seat in row.replace("L", "#")] for row in seats]
print(data)








#data = list(line for line in lines)
#new_data=[]
#for line in data:
 #   new_data += list(line)
#print(len(new_data))
#for i in range(0,len(new_data)-1):
  #  if (new_data[i] =='L') and ((new_data[i+1] and new_data[i-1]) !='#'):
 #       new_data[i] = '#'
#print(new_data)


