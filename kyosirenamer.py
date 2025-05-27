import os
import re
import unicodedata
import argparse
from collections import defaultdict

# ✅ argparse로 디렉토리 인자 받기
parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str, default='.', help='작업할 디렉토리 경로')
args = parser.parse_args()

target_dir = args.dir

def normalize_filename(name):
    return unicodedata.normalize('NFC', name)

# 교시 시간대 매핑
def get_period(hour, minute):
    time = hour * 60 + minute
    periods = {
        1: (9*60, 9*60+50),
        2: (10*60, 10*60+50),
        3: (11*60, 11*60+50),
        4: (13*60, 13*60+50),
        5: (14*60, 14*60+50),
        6: (15*60, 15*60+50),
        7: (16*60, 16*60+50),
        8: (17*60, 17*60+50)
    }
    for period, (start, end) in periods.items():
        if start <= time <= end:
            return period
    return None

# 파일 이름 정규표현식
pattern = re.compile(r".*?(\d{4}-\d{2}-\d{2}) (\d{2})\.(\d{2})\.(\d{2})\.png")

rename_counter = defaultdict(int)
hour_check = defaultdict(set)

for filename in os.listdir(target_dir):
    norm_name = normalize_filename(filename)
    match = pattern.match(norm_name)
    if not match:
        continue

    date_str, hour_str, min_str, sec_str = match.groups()
    hour = int(hour_str)
    minute = int(min_str)

    period = get_period(hour, minute)
    if not period:
        continue

    if 0 <= minute % 60 <= 5:
        tag = "시작"
    elif 40 <= minute % 60 <= 55:
        tag = "종료"
    else:
        continue

    hour_check[period].add(tag)
    base_name = f"{date_str}-{period}교시 {tag}"
    rename_counter[base_name] += 1
    new_filename = f"{base_name}.png" if rename_counter[base_name] == 1 else f"{base_name}_{rename_counter[base_name]}.png"

    src_path = os.path.join(target_dir, filename)
    dst_path = os.path.join(target_dir, new_filename)
    os.rename(src_path, dst_path)
    print(f"✅ {filename} → {new_filename}")

# 요약 출력
print("\n==== 요약 ====")
for i in range(1, 9):
    if i not in hour_check:
        print(f"⚠️ {i}교시 캡처 없음")
    else:
        if "시작" not in hour_check[i]:
            print(f"⚠️ {i}교시 시작 없음")
        if "종료" not in hour_check[i]:
            print(f"⚠️ {i}교시 종료 없음")
print("✅ 리네이밍 작업 완료.")
