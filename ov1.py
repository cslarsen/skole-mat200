import math

class P3:
    @staticmethod
    def g(x,y):
        return x*y-math.pi/4

    @staticmethod
    def F_x(x,y):
        g = P3.g(x,y)
        return 2*y*(y-x)*math.sin(2*g)-2*math.sin(g)**2

    @staticmethod
    def F_y(x,y):
        g = P3.g(x,y)
        return 2*math.sin(g)**2 + x*math.sin(2*g)*(2*y-2*x)

    @staticmethod
    def F(x,y):
        g = P3.g(x,y)
        return 2*(y-x)*math.sin(g)**2

def tangent(f, fd, x, a):
    return f(a) + fd(a)*(x-a)

def L(x, y, x0, y0):
    """Linear approximation of P3.F(x,y) from a chosen point x0, y0"""
    return P3.F(x0,y0) + P3.F_x(x0,y0)*(x-x0) + P3.F_y(x0,y0)*(y-y0)

def y1(x,y):
    u = x*y-math.pi/4
    return ((-2*y**2*math.sin(2*u)+2*x*y*math.sin(2*y)+math.cos(2*u))
            /(2*x**2*math.sin(2*u)+2*x*y*math.sin(2*u)+math.cos(2*u)))

def y2(x,y):
    g = x*y-math.pi/4
    return ((-2*y*(y-x)*math.sin(2*g)+2*math.sin(g)**2)
            /(2*math.sin(g)**2 + x*math.sin(2*g)*(2*y-2*x)))


if __name__ == "__main__":
    answer = P3.F(-1.05, 0.02)
    x0, y0 = -1, 0
    approximation = L(-1.05, 0.02, x0, y0)
    print("Answer: %f" % answer)
    print("Approximation: %f" % approximation)
    print("Absolute difference: %f" % abs(answer-approximation))
