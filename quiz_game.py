from quiz_data import DEFAULT_QUIZZES


def get_valid_int(prompt, min_value, max_value):
    while True:
        raw = input(prompt).strip()
        if not raw:
            print("⚠️ 입력이 비어 있습니다. 다시 입력해주세요.")
            continue
        if not raw.isdigit():
            print("⚠️ 숫자만 입력해주세요.")
            continue
        value = int(raw)
        if value < min_value or value > max_value:
            print(f"⚠️ {min_value}-{max_value} 사이의 숫자를 입력하세요.")
            continue
        return value


class QuizGame:
    def __init__(self):
        self.quizzes = list(DEFAULT_QUIZZES)
        self.best_score = 0

    def show_menu(self):
        print("=" * 40)
        print("🎯 나만의 퀴즈 게임 🎯")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 목록 보기")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    def run(self):
        try:
            while True:
                self.show_menu()
                choice = get_valid_int("선택: ", 1, 5)
                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.list_quizzes()
                elif choice == 4:
                    self.show_best_score()
                elif choice == 5:
                    print("게임을 종료합니다.")
                    break
        except (KeyboardInterrupt, EOFError):
            print("\n⚠️ 강제 종료 신호를 감지했습니다. 안전하게 종료합니다.")

    def play_quiz(self):
        print("(퀴즈 풀기 기능은 다음 단계에서 구현 예정)")

    def add_quiz(self):
        print("(퀴즈 추가 기능은 다음 단계에서 구현 예정)")

    def list_quizzes(self):
        print("(목록 보기 기능은 다음 단계에서 구현 예정)")

    def show_best_score(self):
        print("(점수 확인 기능은 다음 단계에서 구현 예정)")
