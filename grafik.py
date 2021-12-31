import matplotlib.pyplot as plt
import numpy as np



# plot config
MAX = 7
MIN = -4


# eşitsizlik config
inequal = [[5, -1, -6, -1],
         [3, 3, -8, -1],
         [-2, 8, -1, -1],
         [1, 2, -2, -1],
         [2, 2, 0, 1],
         [3, 0, 0, 1]]
Z = [5, 4]




def graph(a: list, b: list) -> list:
  
    for i, j in enumerate(inequal):
        x = j[0]
        y = j[1]
        z = j[2]
        de = j[3]
        if i == 0:
            if de == -1:
                res = x*a + y*b + z < 0
            else:
                res = x*a + y*b + z > 0
        else:
            if de == -1:
                res = res & (x*a + y*b + z < 0)
            else:
                res = res & (x*a + y*b + z > 0)
    return res.astype(int)



def line(a: list):
  
    for i, j in enumerate(inequal):
        x = j[0]
        y = j[1]
        z = j[2]
        if y != 0:
            _b = (-z-x*a)/y
            plt.plot(a, _b)
        else:
            _b = a
            sub_a = np.ones(len(a)) * (-z/x)
            plt.plot(sub_a, _b)




def init():
    
    t = np.linspace(-2, 16, 300)
    a, b = np.meshgrid(t, t)

    mesh_vals = graph(a, b)
    extent = (a.min(), a.max(), b.min(), b.max())

    plt.imshow(mesh_vals, extent=extent, origin="lower", cmap="Purples", alpha=0.5)

    a = np.linspace(MIN, MAX)
    line(a)
    plt.xlim((MIN, MAX))
    plt.ylim((MIN, MAX))
    plt.grid()
    plt.show()


def equality(equal1: list, equal2: list) -> tuple:
   
    X = np.array([[equal1[0], equal1[1]], [equal2[0], equal2[1]]])
    y = np.array([-equal1[2], -equal2[2]])
    res = []
    try:
        res = np.linalg.inv(X) @ y
    except np.linalg.LinAlgError as e:
        if 'Singular matrix' in str(e):
            res = []
        else:
            raise
    return tuple(res)


def is_validation(inequal: list, points: tuple) -> bool:
 
    res = inequal[0]*points[0] + inequal[1]*points[1] + inequal[2]
    if inequal[3] == -1:
        return res <= 0
    else:
        return res >= 0


def validation(p: list) -> list:
 
    true_points = []
    for point in p:
        valid = True
        for j in inequal:
            if len(point) == 0:
                valid = False
            elif not is_validation(j, point):
                valid = False
        if valid and point not in true_points:
            true_points.append(point)
    return true_points


def find_p() -> list:
   
    points = []
    for i in range(len(inequal)):
        for j in range(i+1, len(inequal)):
            if inequal[i] != inequal[j]:
                point = equality(inequal[i], inequal[j])
                points.append(point)
    true_points = validation(points)
    return true_points


def find_s(true_points):
    solutions = []
    for point in true_points:
        z = point[0]*Z[0] + point[1]*Z[1]
        solutions.append(z)
    return solutions


def find_o(solv: list) -> tuple:
  

    max_optimum = max(solv)
    min_optimum = min(solv)

    return max_optimum, min_optimum


points = find_p()
sols = find_s(points)
max_optimum, min_optimum = find_o(sols)

print("Sistemin Bütün çözüm noktaları:")
print(points)
print("\nSistemin Bütün çözümleri:")
print(sols)
print(f"\nMaximum Sonuç: {max_optimum}\nMinimum Sonuç: {min_optimum}")

init()



