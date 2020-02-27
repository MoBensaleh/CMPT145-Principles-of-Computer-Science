import test_queue as unit

all_of_em = [
        unit.test_0,
        unit.test_1,
        unit.test_2,
        unit.test_3,
        unit.test_4,
        unit.test_5,
        unit.test_6,
        unit.test_7,
        unit.test_8,
        unit.test_9,
        unit.test_10,
        unit.test_11,
        unit.test_12,
        unit.test_13,
        unit.test_14,
        unit.test_15,
        unit.test_16,
        unit.test_17,
        unit.test_18,
        unit.test_19,
        unit.test_20,
        unit.test_21,
        unit.test_22,
        unit.test_23,
        unit.test_24,
        unit.test_25,
        unit.test_26,
        unit.test_27,
        unit.test_28,
        unit.test_29,
        unit.test_30,
        unit.test_31,
        unit.test_32,
        unit.test_33,
        unit.test_34,
    ]

count = 0
failed = 0
for t in reversed(all_of_em):
    count += 1
    try: 
        t()
    except Exception as e:
        print("Test failure in function:", t.__name__)
        print(e)
        print()
        failed += 1


print('Passed', count - failed, 'out of total', count, 'tests')
if failed > 2:
    print('***Note***\nThe tests were executed in reverse order, so you can\nmore easily see the first test failures.')
