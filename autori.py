import re

txt = input()
upper = [x[0] for x in re.split("-", txt)]
print(''.join(map(str, upper)))