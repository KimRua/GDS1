import random
import sympy as sp

# 교과목 선택 함수
def select_subject():
    answer = -1
    while answer == -1:
        answer = error_check(input("\n[단원선택]\n- 학습하고자하는 단원을 선택해주세요.\n'지수' : 1\n'로그' : 2\n'삼각함수' : 3\n'수열' : 4\n입력 : "), 0, 4)
    return answer

# 입력 오류 확인 함수 (start~end사이의 정상 값이면 값을, 오류가 나거나 값을 벗어나면 -1을 리턴)
def error_check(answer, start=0, end=0):
    if answer == 'help' or answer == '도움': return help()
    try: answer = eval(answer)
    except: return -1
    if isinstance(answer, tuple): return answer
    if start <= answer <= end or start==end: return answer
    else: return -1

# help 메소드
def help():
    print("\n[도움말]\n- 뒤로가기 : 0\n- 각 챕터마다\n답변 : 숫자\n형태로 주어짐.\n- 기본적으로 5문제 출제됨.\n- 정답이 두개 이상인 경우 괄호로 감싸 제출\n예 : (1, 2)")
    return -1

# 지수 교과목
def exp():
    print("\n[지수]\n- 문제유형 1, 2, 3, 4 총 4가지가 있습니다.\n")
    answer = -1
    while answer == -1:
        answer = error_check(input("\n[지수]\n- 학습하고자하는 문제 유형을 입력해주세요.\n거듭제곱 : 1\n지수법칙 : 2\n거듭제곱근(실수) : 3\n미정 : 4\n입력 : "), 0, 4)
    if answer != 0: # 0이라면 바로 종료
        count = 0
        for i in range(1, 6): # 5문제 출제
            count += exp_problem(i, answer)
        print(f'\n[결과]\n- {count}/5 문제 맞음. {count*20}점')

# 문제 몇 개 맞았는지, 무슨 문제를 맞고 무슨 문제를 틀렸는지, 원래답은 뭐고 뭐라고 대답했는데 등의 채점 결과

# 문제 출제 함수 (랜덤, 매스, 그래프 등)
def exp_problem(index, category):
    print(f'\n[문제{index}]')
    result = 0
    if category == 1: # 거듭제곱
        a = random.randint(1, 20)
        b = random.randint(1, 8)
        result = a ** b
        print(f'{a}의 {b}제곱을 구하시오.')
    elif category == 2: # 지수법칙
        x = sp.Symbol('x')
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        # *****************수정해야함****************
        pass
    elif category == 3: # 거듭제곱근
        problem_list = [[8, 3], [-8, 3],
                        [81, 4], [-81, 4],
                        [121, 2],
                        [64, 3], [-64, 3],
                        [27, 3], [-27, 3],
                        [64, 3], [-64, 3], 
                        [16, 4], [-16, 4]]
        a, b = random.choice(problem_list)
        result = (round(abs(a) ** (1/b)), round(-abs(a) ** (1/b))) if b % 2 == 0 else (round(abs(a) ** (1/b) if a > 0 else round(-abs(a)**(1/b))))
        print(f'{a}의 {b}제곱근을 구하시오.')

    answer = error_check(input('정답을 입력해주세요. : '))
    if result == answer:
        print('정답')
        return 1
    else:
        print('오답')
        return 0
    

# 지수 부분 완성 후 완성하기
def log():
    return 0
def trig():
    return 0
def seq():
    return 0

# 프로그램 종료 함수
def exit():
    print("프로그램을 종료합니다.")
    global main_switch
    main_switch = False

# 메인 함수
def main():
    print("[공돌수1]\n- 공돌수1 프로젝트는 1인 개발 프로젝트입니다.\n- 대한민국 수포자들을 돕기 위해 개발되었습니다.\n- 다양한 문제를 제한 없이 무료로 풀어볼 수 있습니다.\n- 도움이 필요하시면 -h 혹은 -help 혹은 '도움'을 입력해주세요.\n- 학생 여러분의 열정을 응원합니다.\n")
    
    # 함수 모음 딕셔너리
    subject_list = {
        0 : exit,
        1 : exp,
        2 : log,
        3 : trig,
        4 : seq
    }
    
    while main_switch:
        answer = select_subject()
        subject_list[answer]()
        
# 프로그램 종료 스위치 선언
global main_switch
main_switch = True

if __name__ == "__main__":
    main()