s = input()
new = s.split()
for i in range(len(new)):
    sad = new[i][::-1]
    print(sad, end=" ")