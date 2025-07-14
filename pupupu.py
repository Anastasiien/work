def mag(x):
    k = bin(x)[-3:]
    l = int(k, 2)
    return l

def sevenсс(x):
    a = ''
    if x == 0:
        return '0'
    digits = ''
    while x > 0:
        digits = str(x % 7) + digits
        x //=7
    return digits

f = [int(i) for i in open('17.txt')]
minn = min(f)
maxx = max(f)
count = 0
sums = []
proiz = minn * maxx
magg = mag(proiz)
for i in range (len(f) - 2):
    arr = [f[i], f[i+1], f[i+2]]
    arr.sort()
    if arr[0] + 2 == arr[1] + 1 == arr[2] and sum(arr) > magg:
        count += 1
        sums.append(sum(arr))
print(sevenсс(count), sevenсс(max(sums)))

