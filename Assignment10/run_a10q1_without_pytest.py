import test_a10q1 as unit

all_of_em = [
            unit.test_0,
            unit.test_1,
            unit.test_2,
            unit.test_3,
            unit.test_3a,
            unit.test_3b,
            unit.test_3c,
            unit.test_00,
            unit.test_01,
            unit.test_02,
            unit.test_03,
            unit.test_04,
            unit.test_04a,
            unit.test_03a,
            unit.test_03b,
            unit.test_03c,
            unit.test_03d,
            unit.test_03e,
            unit.test_03f,
            unit.test_000,
            unit.test_001,
            unit.test_002,
            unit.test_003,
            unit.test_004,
            unit.test_004a,
            unit.test_005,
            unit.test_006,
            unit.test_hint_0,
            unit.test_4,
            unit.test_5,
            unit.test_6,
            unit.test_7,
            unit.test_7b,
            unit.test_7c,
            unit.test_7d,
            unit.test_7e,
            unit.test_7f,
            unit.test_7g,
            unit.test_7h,
            unit.test_8,
            unit.test_9,
            unit.test_10,
            unit.test_11,
            unit.test_12,
            unit.test_13,
            unit.test_14,
            unit.test_15,
            unit.test_12a,
            unit.test_13b,
            unit.test_14b,
            unit.test_15b,
            unit.test_12c,
            unit.test_13c,
            unit.test_14c,
            unit.test_14d,
            unit.test_14e,
            unit.test_14f,
            unit.test_20,
            unit.test_21,
            unit.test_22,
            unit.test_23,
            unit.test_25,
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
