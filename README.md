# hello

파이썬 스러운 코드로 작성하는 과정

성적처리프로그램의 알고리즘은 아래의 순서도를 참고하세요.

graph TD;
    A[프로그램 시작] --> B[학생 이름 리스트 초기화]
    B --> C[Classroom 객체 생성]
    C --> D[calculate_student_scores 호출]
    D --> E[assign_student_ranks 호출]
    E --> F[print_student_scores 호출]
    F --> G[반의 총점 및 과목별 총점 계산 - calculate_class_totals 호출]
    G --> H[반 평균 및 과목별 평균 계산 - calculate_class_averages 호출]
    H --> I[반 평균 및 과목별 평균 출력 - print_class_averages 호출]
    I --> J[프로그램 종료]
