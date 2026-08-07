# KTW VOCA MASTER CONTEST

강태우어학원 학생용 영어 단어 시험지 제작 프로젝트입니다. 8개 레벨의 A/B형 시험지와 정답지 총 32개 DOCX를 생성합니다.

## 최종 산출물

- `deliverables/KTW VOCA_혼합출제_최종완성본.zip`
- 8개 레벨 × A/B형 × 시험지/정답지 = 32개
- JUPITER B형은 원본 선정 데이터 한계로 96문항

## 시험지 규칙

- 기존 난이도를 유지한 채 `★ → ★★ → ★★★` 순으로 단어를 재배열하고 번호를 새로 부여합니다.
- 홀수 문항: 영어단어 제시 → 빈칸에 한글 뜻 작성
- 짝수 문항: 한글 뜻 제시 → 빈칸에 영어단어 작성
- 문제는 모두 별표 바로 옆 칸에 표시하고, 답안 칸은 항상 비워 둡니다.
- 정답지는 Word와 Meaning을 모두 표시합니다.
- 별표는 전용 칸에 세로 배치하며 행간은 90%입니다.

## 디자인

- 중앙 제목: `KTW VOCA MASTER CONTEST`
- 다음 줄: Class, Name, A/B형
- 안내 박스: `★ Basic / ★★ Challenge / ★★★ Master ...`
- 표와 모든 셀은 가로·세로 중앙정렬
- 표 너비는 페이지 안쪽에 고정되며 긴 내용이 표를 확장하지 않습니다.
- 긴 Word/Meaning은 셀 크기에 맞춰 글자 크기와 줄 간격을 자동 조절합니다.
- 로고는 바닥글 중앙에 고정합니다.

## 재생성

Python 3과 `python-docx`가 필요합니다.

```powershell
pip install python-docx
python scripts/build_all_voca.py BASIC
python scripts/build_all_voca.py PRE-INTERMEDIATE
python scripts/build_all_voca.py INTERMEDIATE
python scripts/build_all_voca.py HIGH
python scripts/build_all_voca.py JUPITER
python scripts/build_all_voca.py SATURN
python scripts/build_all_voca.py URANUS
python scripts/build_all_voca.py NEPTUNE
```

생성 결과는 `generated/KTW VOCA/`에 저장됩니다.

## 검증

```powershell
python scripts/validate_all_voca.py BASIC
```

다른 레벨도 같은 방식으로 검증합니다. 최종 제작 시 레벨별 4개 파일 모두 오류 0개를 확인했습니다.

자세한 요구사항은 [PRD_FINAL.md](PRD_FINAL.md), 변경 과정은 [CHANGELOG.md](CHANGELOG.md)를 참고하세요.
