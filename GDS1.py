import random, math, sys
from fractions import Fraction

# 교과목 선택 함수
def select_subject():
    answer = -1
    while answer == -1:
        answer = input_filter(input("\n[단원선택]\n- 학습하고자하는 단원을 선택해주세요.\n'지수' : 1\n'로그' : 2\n'삼각함수' : 3\n'수열' : 4\n입력 : "), start=0, end=4)
    return answer

# 입력 오류 확인 함수 (start~end사이의 정상 값이면 값을, 오류가 나거나 값을 벗어나면 -1을 리턴)
def input_filter(answer, start=0, end=0, isStr=False, isExpression=False):
    if answer == 'help' or answer == '도움': return help()
    if isStr: return answer.replace(' ', '')
    try: 
        if isExpression:
            a, b = map(int, answer.split('/'))
            return round(a/b, 4)
        answer = eval(answer)
    except: return -1
    if isinstance(answer, tuple): return answer
    if start <= answer <= end or start==end: return answer
    else: return -1

# 정답 확인 함수
def result_check(result, answer):
    if result == answer:
        print('정답')
        return 1
    else:
        print('오답')
        return 0

# help 메소드
def help():
    print("\n[도움말]\n- 뒤로가기 : 0\n- 각 챕터마다\n답변 : 숫자\n형태로 주어짐.\n- 기본적으로 5문제 출제됨.\n- 정답이 두개 이상인 경우 괄호로 감싸 제출\n예 : (1, 2)")
    return -1

# 지수 교과목
def exp():
    print("\n[지수]\n- 문제유형 1, 2, 3, 4 총 4가지가 있습니다.\n")
    answer = -1
    while answer == -1:
        answer = input_filter(input("\n[지수]\n- 학습하고자하는 문제 유형을 입력해주세요.\n거듭제곱 : 1\n지수법칙 : 2\n거듭제곱근(실수) : 3\n지수가 실수인 경우 : 4\n입력 : "), start=0, end=4)
    if answer != 0: # 0이라면 바로 종료
        count = 0
        for i in range(1, 6): # 5문제 출제
            count += exp_problem(i, answer)
        print(f'\n[결과]\n- {count}/5 문제 맞음. {count*20}점')


# 문제 출제 함수 (랜덤, 매스, 그래프 등)
# TODO: 마지막 문제 만들기
def exp_problem(index, category):
    print(f'\n[문제{index}]')
    result = 0
    if category == 1: # 거듭제곱
        a = random.randint(1, 20)
        b = random.randint(1, 8)
        result = a ** b
        print(f'{a}의 {b}제곱을 구하시오.')
    elif category == 2: # 지수법칙
        operators = ['*', '/', '^']
        operator = random.choice(operators)
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        if operator == '*':
            print(f'x^{a} * x^{b}')
            result = 'x^' + str(a + b)
        elif operator == '/':
            print(f'x^{a} / x^{b}')
            result = 'x^' + str(a - b) if a-b>0 else '1/x^' + str(b - a)
        else:
            print(f'(x^{a})^{b}')
            result = 'x^' + str(a * b)
    elif category == 3: # 거듭제곱근
        problem_list = [
            [8, 3], [-8, 3],
            [81, 4], [-81, 4],
            [121, 2],
            [64, 3], [-64, 3],
            [27, 3], [-27, 3],
            [64, 3], [-64, 3], 
            [16, 4], [-16, 4]
        ]
        a, b = random.choice(problem_list)
        result = (round(abs(a) ** (1/b)), round(-abs(a) ** (1/b))) if b % 2 == 0 else (round(abs(a) ** (1/b) if a > 0 else round(-abs(a)**(1/b))))
        print(f'{a}의 {b}제곱근을 구하시오.')
    elif category == 4: # 지수가 실수인 경우
        result = 0
        pass

    answer = input_filter(input('정답을 입력해주세요. : '), isStr=True if category==2 else False)
    return result_check(result, answer)

# 로그 교과목
def log():
    print("\n[로그]\n- 문제유형 1, 2, 3, 4 총 4가지가 있습니다.\n")
    answer = -1
    while answer == -1:
        answer = input_filter(input("\n[로그]\n- 학습하고자하는 문제 유형을 입력해주세요.\n로그 값 구하기 : 1\n로그의 밑의 변환 : 2\n상용로그 : 3\n입력 : "), start=0, end=3)
    if answer != 0: # 0이라면 바로 종료
        count = 0
        for i in range(1, 6): # 5문제 출제
            count += log_problem(i, answer)
        print(f'\n[결과]\n- {count}/5 문제 맞음. {count*20}점')

# TODO: 3문제 만들기   
def log_problem(index, category):
    print(f'\n[문제{index}]')
    result = 0
    if category == 1: # 로그 값 구하기 
        num_list = [2, 3, 4, 5, 7, 10]
        num1 = random.choice(num_list)
        num2 = random.choice([num1**i for i in range(5)])
        case = random.randint(1, 4)
        if case == 1:
            print(f'log_{num1} {num2}')
        elif case == 2:
            print(f'log_1/{num1} {num2}')
            num1 = 1/num1
        elif case == 3:
            print(f'log_{num1} 1/{num2}')
            num2 = 1/num2
        else:
            print(f'log_1/{num1} 1/{num2}')
            num1 = 1/num1
            num2 = 1/num2
        result = round(math.log(num2, num1))
        answer = input_filter(input('정답을 입력해주세요. : '))
    elif category == 2: # 로그의 밑의 변환
        problem_list = [
            [8, 16], [9, 27],
            [25, 125], [4, 8],
            [8, 32], [9, 243],
            [4, 2], [8, 2]
        ]
        num1, num2 = random.choice(problem_list)
        print(f'log_{num1} {num2}')
        a = round(math.log(num2, num1), 4)
        result = a
        answer = input_filter(input('정답을 입력해주세요. : '), isExpression=True)
    elif category == 3: # 상용로그
        pass
    return result_check(result, answer)

def trig():
    return 0
def seq():
    return 0

# 프로그램 종료 함수
def exit():
    print("프로그램을 종료합니다.")
    sys.exit()
    
# 메인 함수
def main():
    print("[공돌수1]\n- 공돌수1 프로젝트는 1인 개발 프로젝트입니다.\n- 대한민국 수포자들을 돕기 위해 개발되었습니다.\n- 다양한 문제를 제한 없이 풀어볼 수 있습니다.\n- 도움이 필요하시면 help 혹은 '도움'을 입력해주세요.\n")
    
    # 함수 모음 딕셔너리
    subject_list = {
        0 : exit,
        1 : exp,
        2 : log,
        3 : trig,
        4 : seq
    }
    
    while True:
        answer = select_subject()
        subject_list[answer]()

if __name__ == "__main__":
    main()