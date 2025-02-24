num_test_cases = int(input())
test_cases = []

for _ in range(num_test_cases):
    n = int(input())
    boys = list(map(int, input().split()))
    girls = list(map(int, input().split()))
    test_cases.append({'n': n, 'boys': boys, 'girls': girls})

def can_arrange_students(num_test_cases, test_cases):
    for i in range(num_test_cases):
        n = test_cases[i]['n']
        boys = sorted(test_cases[i]['boys'])
        girls = sorted(test_cases[i]['girls'])
        
        def is_valid(b_first):
            arrangement = []
            for j in range(n):
                arrangement.append(boys[j] if b_first else girls[j])
                arrangement.append(girls[j] if b_first else boys[j])
            return all(arrangement[k] <= arrangement[k + 1] for k in range(len(arrangement) - 1))
        
        if is_valid(True) or is_valid(False):
            print("YES")
        else:
            print("NO")

can_arrange_students(num_test_cases, test_cases)
