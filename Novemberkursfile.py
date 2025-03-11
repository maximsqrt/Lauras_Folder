# Exkurs Seaborn, gute Lib auch für Darstelleung und Graphen 
# Basiert aber auf Matplotlib, änderungen hätten somit direkt einfluss auf Abhängigkeiten



import numpy
# Alte Methode in der Numpy Lib 
# Angennommen wir haben einen Array
arr = np.array([42])

scalar = np.asscalar(arr)

# numpy == 1.18.5
# Wir wollen aber nicht Global eine veraltete Numpy Version!
# Idee! 
# Wir setzen dafür ein VENV auf, ein virtuelles Environment! 
# In diesem Virtuellen Env stört es dann nicht andere Versionen 
# Dann gibt es keine Verisonskonflikte

"""generell nicht zu empfehlen!"""
# python -m venv --system-site-packages 
# Auch extern Libs mit zu laden.