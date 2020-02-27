import test_a10q2 as unit

all_of_em = [
            unit.test_0,
            unit.test_1,
            unit.test_2,
            unit.test_4,
            unit.test_5,
            unit.test_6
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
