import random
import time
import pyperclip

codes = list(range(1000000))
random.shuffle(codes)

used_codes = set()
index = 0

def has_three_repeat(code):
    for i in range(len(code) - 2):
        if code[i] == code[i+1] == code[i+2]:
            return True
    return False

def safe_copy(text, retries=5, delay=0.1):
    for _ in range(retries):
        try:
            pyperclip.copy(text)
            return True
        except pyperclip.PyperclipWindowsException:
            time.sleep(delay)
    print(f"Warning: Failed to copy {text} to clipboard.")
    return False

while True:
    if index < len(codes):
        num = codes[index]
        index += 1
    else:
        num = random.randint(0, 999999)

    code = f"{num:06}"

    # prevent duplicates
    if code in used_codes:
        continue

    # prevent 3 repeating digits
    if has_three_repeat(code):
        continue

    used_codes.add(code)

    # copy to clipboard safely
    if safe_copy(code):
        print(f"Copied: {code}")
    else:
        print(f"Skipped copying: {code}")

    time.sleep(0.1)  # optional delay to avoid flooding
