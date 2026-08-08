import json
import random
from datetime import datetime

from input_utils import get_valid_int, get_valid_text
from quiz import Quiz
from quiz_data import DEFAULT_QUIZZES

STATE_FILE = "state.json"
HINT_CREDIT_RATIO = 0.5


class QuizGame:
    def __init__(self):
        self._reset_to_defaults()
        self.load_data()

    def _reset_to_defaults(self):
        self.quizzes = list(DEFAULT_QUIZZES)
        self.best_score = None
        self.score_history = []

    def show_menu(self):
        print("=" * 40)
        print("🎯 나만의 퀴즈 게임 🎯")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 삭제")
        print("4. 목록 보기")
        print("5. 점수 확인")
        print("6. 종료")
        print("=" * 40)

    def run(self):
        try:
            while True:
                self.show_menu()
                choice = get_valid_int("선택: ", 1, 6)
                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.delete_quiz()
                elif choice == 4:
                    self.list_quizzes()
                elif choice == 5:
                    self.show_best_score()
                elif choice == 6:
                    print("게임을 종료합니다.")
                    break
        except (KeyboardInterrupt, EOFError):
            print("\n⚠️ 강제 종료 신호를 감지했습니다. 안전하게 종료합니다.")
        finally:
            self.save_data()

    def play_quiz(self):
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
            return

        total = get_valid_int(
            f"\n풀 문제 수를 입력하세요 (1-{len(self.quizzes)}): ", 1, len(self.quizzes)
        )
        quizzes_to_play = random.sample(self.quizzes, total)
        correct_count = 0
        score_units = 0.0
        hint_used_count = 0

        print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)")

        for i, quiz in enumerate(quizzes_to_play, start=1):
            print("-" * 40)
            print(f"[문제 {i}]")
            quiz.show()
            hint_shown = False
            while True:
                user_answer = get_valid_int(
                    "\n정답 입력 (힌트를 보려면 0): ", 0, len(quiz.choices)
                )
                if user_answer == 0:
                    print(f"💡 힌트: {quiz.hint}")
                    hint_shown = True
                    continue
                break
            if hint_shown:
                hint_used_count += 1
            if quiz.check_answer(user_answer):
                print("✅ 정답입니다!\n")
                correct_count += 1
                score_units += HINT_CREDIT_RATIO if hint_shown else 1
            else:
                print(f"❌ 오답입니다. (정답: {quiz.answer}번)\n")

        score = round(score_units / total * 100)

        print("=" * 40)
        print(f"🏆 결과: {total}문제 중 {correct_count}문제 정답! ({score}점)")
        if hint_used_count > 0:
            print(
                f"💡 {hint_used_count}문제에서 힌트를 사용해 해당 문제는 절반 점수만 인정됩니다."
            )

        self.score_history.append(
            {
                "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "total": total,
                "score": score,
                "hint_used_count": hint_used_count,
            }
        )
        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")
        print("=" * 40)

        self.save_data()

    def add_quiz(self):
        print("\n📌 새로운 퀴즈를 추가합니다.\n")
        question = get_valid_text("문제를 입력하세요: ")
        choices = [get_valid_text(f"선택지 {i}: ") for i in range(1, 5)]
        answer = get_valid_int(f"정답 번호 (1-{len(choices)}): ", 1, len(choices))
        hint = get_valid_text("힌트를 입력하세요: ")

        self.quizzes.append(Quiz(question, choices, answer, hint))
        print("\n✅ 퀴즈가 추가되었습니다!")
        self.save_data()

    def delete_quiz(self):
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return

        self.list_quizzes()
        index = get_valid_int(
            f"\n삭제할 퀴즈 번호를 입력하세요 (1-{len(self.quizzes)}): ",
            1,
            len(self.quizzes),
        )
        removed = self.quizzes.pop(index - 1)
        print(f"\n🗑️ '{removed.question}' 퀴즈가 삭제되었습니다.")
        self.save_data()

    def list_quizzes(self):
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return

        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)\n")
        print("-" * 40)
        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"[{i}] {quiz.question}")
        print("-" * 40)

    def show_best_score(self):
        if self.best_score is None:
            print("⚠️ 아직 퀴즈를 푼 기록이 없습니다.")
            return

        print(f"\n🏆 최고 점수: {self.best_score}점")
        print(f"\n📊 전체 기록 (총 {len(self.score_history)}회)")
        print("-" * 40)
        for i, record in enumerate(self.score_history, start=1):
            hint_note = (
                f", 힌트 {record['hint_used_count']}회"
                if record["hint_used_count"] > 0
                else ""
            )
            print(
                f"{i}회차 [{record['datetime']}] "
                f"{record['total']}문제, {record['score']}점{hint_note}"
            )
        print("-" * 40)

    def load_data(self):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            self._reset_to_defaults()
            return
        except (OSError, json.JSONDecodeError):
            print("⚠️ 저장된 데이터가 손상되어 기본 데이터로 초기화합니다.")
            self._reset_to_defaults()
            return

        try:
            self.quizzes = [
                Quiz(item["question"], item["choices"], item["answer"], item["hint"])
                for item in data["quizzes"]
            ]
            self.best_score = data["best_score"]
            self.score_history = data["score_history"]
        except (KeyError, TypeError):
            print("⚠️ 저장된 데이터 형식이 올바르지 않아 기본 데이터로 초기화합니다.")
            self._reset_to_defaults()
            return

        score_display = (
            f"최고점수 {self.best_score}점"
            if self.best_score is not None
            else "기록 없음"
        )
        print(
            f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, {score_display})"
        )

    def save_data(self):
        data = {
            "quizzes": [
                {
                    "question": q.question,
                    "choices": q.choices,
                    "answer": q.answer,
                    "hint": q.hint,
                }
                for q in self.quizzes
            ],
            "best_score": self.best_score,
            "score_history": self.score_history,
        }
        try:
            with open(STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except OSError as e:
            print(f"⚠️ 데이터 저장 중 오류가 발생했습니다: {e}")
