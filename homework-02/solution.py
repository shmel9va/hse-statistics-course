import seaborn as s, matplotlib.pyplot as p
s.kdeplot([*map(float,input().split())]); p.show()