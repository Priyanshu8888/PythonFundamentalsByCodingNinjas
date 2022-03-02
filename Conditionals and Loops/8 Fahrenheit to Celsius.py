# Read input as sepcified in the question
# Print output as specified in the question

S = int(input())
E = int(input())
W = int(input())

for i in range(S, E+1, W):
    ans = (5*(i-32))/9
    print(i, int(ans))