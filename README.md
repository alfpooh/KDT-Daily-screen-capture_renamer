# Screenshot Class Period Renamer

KDT 온라인 과정에서 매일 강의 시작과 종료 시점의 화상 강의 화면을 캡처해 출석 증빙 자료로 활용할 수 있도록 돕는 도구입니다.
Est AI 서비스 기획과정을 위해 만들어졌습니다. 맥OS를 기준으로 만들어졌습니다.

This script renames macOS screenshot files based on predefined school class periods.  
It detects whether the screenshot was taken at the **start** (within the first 5 minutes) or **end** (within the last 10 minutes) of a school period, and renames the file accordingly.

---

## 🕒 Class Periods Definition

| Period | Time Range      |
|--------|-----------------|
| 1st    | 09:00 - 09:50   |
| 2nd    | 10:00 - 10:50   |
| 3rd    | 11:00 - 11:50   |
| 4th    | 13:00 - 13:50   |
| 5th    | 14:00 - 14:50   |
| 6th    | 15:00 - 15:50   |
| 7th    | 16:00 - 16:50   |
| 8th    | 17:00 - 17:50   |

---

## 🚀 Usage

### 1. Rename screenshots in the current directory
```bash
python daterenamer.py
```

### 2. Rename screenshots in a specific directory
```bash
python daterenamer.py --dir "/path/to/screenshots"
```

### 3. Simulate renaming without making changes
```bash
python daterenamer.py --dry-run
```

### 4. Simulate renaming in a specific directory
```bash
python daterenamer.py --dir "/path/to/screenshots" --dry-run
```

---

## 🧠 Logic

- Files must follow the macOS Korean screenshot filename format:
  ```
  스크린샷 YYYY-MM-DD HH.MM.SS.png
  ```
- Only files captured within the defined start (HH:00–HH:05) or end (HH:40–HH:55) windows are renamed.
- If multiple files match the same period and type (start or end), a suffix `_2`, `_3`, etc. is added.
- The script outputs any **missing class periods** or screenshots not matching start/end patterns.

---

## 🗣 Korean 설명

이 스크립트는 macOS에서 저장된 스크린샷 파일을 교시 시간 기준으로 자동으로 리네이밍합니다.

### 🕒 교시 시간 정의

| 교시 | 시간 범위        |
|------|------------------|
| 1교시 | 09:00 - 09:50   |
| 2교시 | 10:00 - 10:50   |
| 3교시 | 11:00 - 11:50   |
| 4교시 | 13:00 - 13:50   |
| 5교시 | 14:00 - 14:50   |
| 6교시 | 15:00 - 15:50   |
| 7교시 | 16:00 - 16:50   |
| 8교시 | 17:00 - 17:50   |

### ✅ 기능 요약

- 시작(00~05분) 또는 종료(40~55분)에 찍힌 스크린샷만 대상으로 함
- 리네이밍 형식:  
  `2025-05-20-1교시 시작.png` / `2025-05-20-1교시 종료.png`
- 중복된 경우 `_2`, `_3` 등의 번호가 붙음
- 누락된 교시에 대해 경고 출력

### 💻 사용법 예시

#### 현재 폴더에서 실행
```bash
python daterenamer.py
```

#### 특정 폴더에서 실행
```bash
python daterenamer.py --dir "/Users/yourname/Desktop/screenshots"
```

#### 실제 파일 변경 없이 시뮬레이션만
```bash
python daterenamer.py --dry-run
```

#### 특정 폴더에서 시뮬레이션
```bash
python daterenamer.py --dir "/Users/yourname/Desktop/screenshots" --dry-run
```

---

## 🧩 기타

- macOS에서 저장되는 한글 파일명을 정확히 처리하기 위해 유니코드 정규화(NFC)를 적용함
- `.png` 확장자를 기준으로 작동하며, 필요시 다른 확장자 지원도 추가 가능함

## Creator
- Donghoon Alf Bae 배동훈 2025 All rights reserved.