from quiz import Quiz

DEFAULT_QUIZZES = [
    Quiz(
        "파이썬에서 참(True) 또는 거짓(False), 딱 두 가지 값만 가지는 자료형은?",
        ["int", "str", "bool", "list"],
        3,
    ),
    Quiz(
        "파이썬에서 반복 횟수가 정해져 있지 않고, 조건이 참인 동안 계속 반복하고 싶을 때 적합한 문법은?",
        ["while", "for", "if", "def"],
        1,
    ),
    Quiz(
        "파이썬 인스턴스 메서드의 첫 번째 매개변수로 항상 명시적으로 써줘야 하는 것은?",
        ["this", "self", "super", "cls"],
        2,
    ),
    Quiz(
        "파이썬에서 데이터를 저장할 때 흔히 쓰는, 사람도 읽기 쉬운 텍스트 기반 데이터 형식은?",
        ["JSON", "EXE", "ZIP", "ISO"],
        1,
    ),
    Quiz(
        "원격 저장소를 처음 내 컴퓨터로 복제해올 때 쓰는 명령어는?",
        ["git pull", "git clone", "git push", "git fetch"],
        2,
    ),
    Quiz(
        "작업 중이던 브랜치의 변경사항을 main 브랜치에 합칠 때 쓰는 명령어는?",
        ["git branch", "git merge", "git checkout", "git clone"],
        2,
    ),
]
