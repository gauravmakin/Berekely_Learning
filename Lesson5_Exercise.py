
# Part 1 – create your data:
# 1. Include a secton line with your name
# 2. Work only with these imports:

# from numpy import matrix, array, random, min, max
# import pylab as plb (... or use matplotlib)

# 3. Cerate a list A of 600 random numbers bound between (0:10)
# 4. Create an array B with 500 elements bound in the range [-3*pi:2*pi]
# 5. Using if, for or while, create a func4on that overwrites every element in A that falls outside of the interval [2:9), and overwrite
# that element with the average between the smallest and largest element in A
# 6. Normalize each list element to be bound between [0:0.1]
# 7. Return the result from the func4on to C
# 8. Cast C as an array
# 9. Add C to B (think of C as noise) and record the result in D ... (watch out: C is of different length. Truncate it)

# Part 2 - ploXng:
# 10. Create a figure, give it a 4tle and specify your own size and dpi
# 11. Plot the sin of D, in the (2,1,1) loca4on of the figure
# 12. Overlay a plot of cos using D, with different color, thickness and type of line
# 13. Create some space on top and boZom of the plot (on the y axis) and show the grid
# 14. Specify the following: 4tle, Y-axis label and legend to fit in the best way
# 15. Plot the tan of D, in loca4on (2,1,2) with grid showing, X-axis label, Y-axis label and legend on top right
# 16. Organize your code: use each line from this HW as a comment line before coding each step


import matplotlib as mp

print("Gaurav Makin")

from numpy import matrix, array, random, min, max
import pylab as plb

A = random.randint(1, 10, 600)
# print(A)
B = random.randint(-3*plb.pi, 2*plb.pi, 500)
# print(B)

def my_overwrite(my_list):
    avg = (my_list.min() + my_list.max())/2
    for item in range(len(my_list)):
        if 2 < my_list[item] < 9:
            continue
        else:
            my_list[item] = avg
    my_list = my_list / (my_list.max()/0.1)
    return my_list

C = array(my_overwrite(A))
# print(C)

D = B + C[:500]
# print(D)

# fig = plb.figure()
fig, axes = plb.subplots(nrows = 2, ncols = 1, figsize = (6, 4), dpi = 100)

axes[0].plot(plb.sin(D), color = 'red', lw = 3, ls = ' -- ', label = 'Sin of D')
axes[0].plot(plb.cos(D), color = 'blue', lw = 2, ls = '-.', label = 'Cos of D')

axes[0].grid()

axes[0].set_ylabel('Y Axis')
axes[0].set_xlabel('X Axis')
axes[0].set_title('Signals')
axes[0].legend(loc = 0)

axes[1].plot(plb.tan(D), label = 'Tan')
axes[1].grid()
axes[1].set_xlabel('X Axis')
axes[1].set_ylabel('Y Axis')
axes[1].legend(loc = 0)

print("Show me the Figure\n")
plb.show()
