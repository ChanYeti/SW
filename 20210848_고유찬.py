import random

def generate_students(num_students=30):
    students = []
    for _ in range(num_students):
        name = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
        age = random.randint(18, 22)
        score = random.randint(0, 100)
        students.append({"이름": name, "나이": age, "성적": score})
    return students

def selection_sort(data, key, reverse=False):
    for i in range(len(data)):
        target_idx = i
        for j in range(i + 1, len(data)):
            if (data[j][key] > data[target_idx][key] if reverse else data[j][key] < data[target_idx][key]):
                target_idx = j
        data[i], data[target_idx] = data[target_idx], data[i]

def insertion_sort(data, key, reverse=False):
    for i in range(1, len(data)):
        current = data[i]
        j = i - 1
        while j >= 0 and (data[j][key] < current[key] if reverse else data[j][key] > current[key]):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = current

def quick_sort(data, key, reverse=False):
    if len(data) <= 1:
        return data
    pivot = data[0]
    less = [x for x in data[1:] if (x[key] > pivot[key] if reverse else x[key] < pivot[key])]
    greater = [x for x in data[1:] if (x[key] <= pivot[key] if reverse else x[key] >= pivot[key])]
    return quick_sort(less, key, reverse) + [pivot] + quick_sort(greater, key, reverse)

def counting_sort(data, key, exp, reverse):
    n = len(data)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (data[i][key] // exp) % 10
        count[index] += 1

    if reverse:
        for i in range(8, -1, -1):
            count[i] += count[i + 1]
    else:
        for i in range(1, 10):
            count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (data[i][key] // exp) % 10
        output[count[index] - 1] = data[i]
        count[index] -= 1

    for i in range(n):
        data[i] = output[i]

def radix_sort(data, key, reverse=False):
    if not data:
        return data

    max_value = max(data, key=lambda x: x[key])[key]
    exp = 1
    while max_value // exp > 0:
        counting_sort(data, key, exp, reverse)
        exp *= 10
    return data

def sort_students(students, algorithm, key, reverse=False):
    if algorithm == "선택 정렬":
        selection_sort(students, key, reverse)
    elif algorithm == "삽입 정렬":
        insertion_sort(students, key, reverse)
    elif algorithm == "퀵 정렬":
        return quick_sort(students, key, reverse)
    elif algorithm == "기수 정렬" and key == "성적":
        return radix_sort(students, key, reverse)
    else:
        raise ValueError("지원하지 않는 정렬 알고리즘입니다.")
    return students

def display_menu():
    print("\n성적 관리 프로그램:")
    print("1. 이름을 기준으로 정렬")
    print("2. 나이를 기준으로 정렬")
    print("3. 성적을 기준으로 정렬")
    print("4. 프로그램 종료")

def main():
    students = generate_students()
    print("\n생성된 학생 정보:")
    for student in students:
        print(student)

    while True:
        display_menu()
        try:
            choice = input("정렬 기준을 선택하세요 (1, 2, 3, 4): ").strip()
            if not choice:  # 입력이 없으면 기본값 사용
                choice = 4
            else:
                choice = int(choice)
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")
            continue
        except OSError as e:
            print(f"입력 오류 발생: {e}")
            choice = 4  # 기본값으로 프로그램 종료
            break

        if choice == 4:
            print("프로그램을 종료합니다.")
            break

        if choice == 1:
            key = "이름"
        elif choice == 2:
            key = "나이"
        elif choice == 3:
            key = "성적"
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")
            continue

        print("\n정렬 알고리즘:")
        print("1. 선택 정렬")
        print("2. 삽입 정렬")
        print("3. 퀵 정렬")
        if key == "성적":
            print("4. 기수 정렬")
        try:
            algo_choice = input("정렬 알고리즘을 선택하세요 (1, 2, 3): ").strip()
            if not algo_choice:  # 입력이 없으면 기본값 사용
                algo_choice = 1
            else:
                algo_choice = int(algo_choice)
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")
            continue
        except OSError as e:
            print(f"입력 오류 발생: {e}")
            algo_choice = 1  # 기본값으로 선택 정렬 사용

        algorithms = {1: "선택 정렬", 2: "삽입 정렬", 3: "퀵 정렬", 4: "기수 정렬"}
        algorithm = algorithms.get(algo_choice)

        if not algorithm or (algorithm == "기수 정렬" and key != "성적"):
            print("잘못된 선택입니다. 다시 시도하세요.")
            continue

        try:
            reverse_input = input("내림차순으로 정렬하시겠습니까? (y/n): ").strip().lower()
            reverse = reverse_input == "y"
        except OSError as e:
            print(f"입력 오류 발생: {e}")
            reverse = False  # 기본값: 오름차순 정렬

        if algorithm == "기수 정렬":
            sorted_students = sort_students(students, algorithm, key, reverse)
        else:
            sorted_students = sort_students(students[:], algorithm, key, reverse)

        print("\n정렬된 학생 정보:")
        for student in sorted_students:
            print(student)

if __name__ == "__main__":
    main()

