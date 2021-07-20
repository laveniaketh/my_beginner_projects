print('hello world!!')

ans = input('Are you ready to play (yes/no): ')
score = 0
total_q = 4

if ans.lower() == 'yes':
    ans = input('1. What is my name? ')
    if ans.lower() == 'keth':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input('2. How old am I? ')
    if ans == '17':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input('3. What grade am I? ')
    if ans in ('Grade 11', 'G11', 'G-11', 'g11', 'grade 11', 'g-11'):
        score += 1
        print('Correct')
    else:
        print('Incorrect')


if ans.lower() == "no":
    print("ok edi wag bye")
else:
    ans = input('Are you ready to play (yes/no): ')
    score = 0
    total_q = 4