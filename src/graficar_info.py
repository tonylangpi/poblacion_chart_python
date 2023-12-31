import matplotlib.pyplot as plt

def generate_chart_bars(labels, vals):
    fig, ax = plt.subplots()
    ax.bar(labels, vals)
    plt.show()
    
def generate_chart_pie(labels, vals):
    fig, ax = plt.subplots()
    ax.pie(vals, labels=labels)
    ax.axis('equal')
    plt.show()