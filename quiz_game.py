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
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
            return

        total = len(self.quizzes)
        correct_count = 0

        print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)")

        for i, quiz in enumerate(self.quizzes, start=1):
            print("-" * 40)
            print(f"[문제 {i}]")
            quiz.show()
            user_answer = get_valid_int("\n정답 입력: ", 1, len(quiz.choices))
            if quiz.check_answer(user_answer):
                print("✅ 정답입니다!\n")
                correct_count += 1
            else:
                print(f"❌ 오답입니다. (정답: {quiz.answer}번)\n")

        score = round(correct_count / total * 100)
        print("=" * 40)
        print(f"🏆 결과: {total}문제 중 {correct_count}문제 정답! ({score}점)")
        if score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")
        print("=" * 40)

    def add_quiz(self):
        print("(퀴즈 추가 기능은 다음 단계에서 구현 예정)")

    def list_quizzes(self):
        print("(목록 보기 기능은 다음 단계에서 구현 예정)")

    def show_best_score(self):
        print("(점수 확인 기능은 다음 단계에서 구현 예정)")
