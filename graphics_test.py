# experimenting with matplotlib to draw 'tone clock' notation.
import cmath
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, ConnectionPatch

twelfth_roots = [ cmath.rect(1, k * cmath.pi/6) for k in range(12) ]
complex_clock = twelfth_roots[3::-1] + twelfth_roots[11:3:-1]
clock = [ (z.real, z.imag) for z in complex_clock ]

def create_chord(nums):
    out = []
    for i,j in zip(nums,nums[1:]):
        out.append( ConnectionPatch(clock[i], clock[j], 'data') )
    return out

def create_circle():
    circle = Circle((0,0), radius=1, fill=False)
    return circle

def show_chord(patches):
    ax = plt.gca()
    for patch in patches:
        ax.add_patch(patch)
    ax.add_patch(create_circle())
    plt.axis("scaled")
    plt.show()
