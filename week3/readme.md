TODO: Reflect on what you learned this week and what is still unclear.

LECTURE
------------------------------------------------------------------------------------------------------------
another_list = [my_dict, my_list]
another_list = [{'taste': 'Delicous', 'name': 'Cake'}, [1, 2, 3, 4, 5]]
another_list[0][taste] gives delicous

CATCHING ERRORS
try:
    do_a_dumb()
except Exception as e:
    print("You did a dumb", e)
finally:
    print("we still love you")

TUTORIAL
------------------------------------------------------------------------------------------------------------
LOOPS
process that keeps repeating
    FOR LOOPS
range
my_list = [34, 11, 69, 99]
for idx in range(5):
    print(idx)
for idx in range(len(my_list)):
    print(idx)
WHILE LOOPS
idx = 0
while idx <= len(my_list)
    print(my_list[idx])
    idx = idx + 1

!= is not equal
