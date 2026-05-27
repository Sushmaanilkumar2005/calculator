'''The included code stub will read an integer, , from STDIN.
Without using any string methods, try to print the following:
Note that "" represents the consecutive values in between.

Example
n = 5
Print the string 1234'''

n = int(input())
for i in range(1,n+1):
    print(i, end="")