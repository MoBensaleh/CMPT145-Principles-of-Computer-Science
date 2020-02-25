# CMPT 145: Computational Complexity
# Defines some empirical experiments to understand computational complexity.
#
# In this script, we run experiments on computation time.
# The experiments use three different computational tasks.
#  - Python's built-in sort() operation
#  - a simple implementation of bubblesort
#  - a simple linear search
# Clearly, the sort() and bubblesort() are doing the same task, and
# the linear search is quite different.
# We can compare the two sort functions to each other, and see that
# bubblesort is worse than Python's sort().
# But it's not just measurably worse, it's a different kind of worse.
# Theoretically, sort() and bubblesort() are in different categories.
# To demonstrate a third category, the linear search is used.
# TL;DR
#   - three different algorithms, each one is a different category
#
# This set of experiments collects the raw time measures.
#
# We take the minimum time seen from a number of trials,
# because we know that random causes will increase the
# amount of time needed; but the experiments below do not
# allow for measurement error in the negative direction!
# (you have to set up the experiment so that this is true)


import Statistics as Stat
import apparatus as apparatus
import matplotlib.pyplot as plt

trials = 50

#
print("Statistics for Python's sort()")
sort_sizes = range(500,5001,500)
sort_times = []
for n in sort_sizes:
    t1 = Stat.create()
    for i in range(trials):
        Stat.add(t1,apparatus.run_sort(n))
    rtime = Stat.minimum(t1)
    print(n, rtime)
    sort_times.append(rtime)


print("Statistics for bubblesort()")
bubblesort_sizes = range(50,501,50)
bubblesort_times = []
for n in bubblesort_sizes:
    t1 = Stat.create()
    for i in range(trials):
        Stat.add(t1,apparatus.run_bubblesort(n))
    rtime = Stat.minimum(t1)
    print(n, rtime)
    bubblesort_times.append(rtime)



print('Statistics for find')
linsearch_sizes = range(5000,50001,5000)
linsearch_times = []
for n in linsearch_sizes:
    t1 = Stat.create()
    t2 = Stat.create()
    for i in range(trials):
        Stat.add(t1,apparatus.run_find(n))
    rtime = Stat.minimum(t1)
    print(n, rtime)
    linsearch_times.append(rtime)

print('Data collection done... Plotting graphs!')

# plot the results
plt.figure(1)
plt.subplot(311)
plt.plot(sort_sizes, sort_times,'ro-',label="Raw times for sort()")
plt.legend()

plt.subplot(312)
plt.plot(bubblesort_sizes, bubblesort_times,'bo-',label="Raw times for bubblesort()")
plt.legend()

plt.subplot(313)
plt.plot(linsearch_sizes, linsearch_times,'go-',label="Raw times for linear search")
plt.legend()

plt.show()
