def get_valid_int(prompt, min_value, max_value):
    while True:
        raw = input(prompt).strip()
        if not raw:
            print("⚠️ 입력이 비어 있습니다. 다시 입력해주세요.")
            continue
        if not raw.isdecimal():
            print("⚠️ 숫자만 입력해주세요.")
            continue
        value = int(raw)
        if value < min_value or value > max_value:
            print(f"⚠️ {min_value}-{max_value} 사이의 숫자를 입력하세요.")
            continue
        return value


def get_valid_text(prompt):
    while True:
        text = input(prompt).strip()
        if not text:
            print("⚠️ 입력이 비어 있습니다. 다시 입력해주세요.")
            continue
        return text
