---
layout: post
title: "🖥️컴퓨터 용어 정리"
date: 2026-07-10
categories: 공부기록
icon: "👑"
image: "https://github.com/user-attachments/assets/c3914afa-2cdc-40de-9f9a-017da0fc444f"
thumb: "https://github.com/user-attachments/assets/b36098fe-d669-468c-9a1a-aa2eb9f05e8d"
---

<p class="lead">AI 활용을 위한 용어들</p>

## '터미널' 용어

(1) <strong>mkdir</strong> = make directory, 새 폴더를 만드는 명령어<br>
예> mkdir project (project라는 폴더 만들어줘!)<br>
(2) <strong>cd</strong> = 지정한 폴도러 이동하는 명령어<br>
 예> cd project (project 폴더로 이동해줘!)<br>
(3) <strong>pwd</strong> = 현재 위치한 경로를 출력<br>
(4) <strong>touch</strong> = 빈 파일을 새로 만들거나 파일의 수정 시간을 갱신<br>
 예> touch README.md
(5) <strong>echo</strong>= 입력한 내용을 화면에 그대로 출력해줌<br>
(6) <strong>which</strong>= 그 프로그램이 실제로 어느 위치에 있어?<br>
 예> which python (파이썬 어느경로에 있는지 알려줘)<br>
(7) <strong>ls</strong>= 현재 폴더 안의 파일 및 폴더 이름 보여줘<br>
(8) <strong>rm</strong>= 파일 삭제 명령어<br>


##  'GitHub / Git' 용어

(1) <strong>git init</strong> = 현재 폴더를 git 저장소(repository)로 초기화<br>
(2) <strong>clone</strong> = 원격 저장소(remote repository)를 내 컴퓨터로 복제해오는 것<br>
(3) <strong>add</strong> = 변경한 파일을 커밋할 준비 상태(staging area)로 올리는 것. 예: git add<br>
(4) <strong>commit</strong> = staging area에 올린 변경 내용을 하나의 저장 단위(기록)로 남기는 것<br>
(5) <strong>push</strong> = 로컬(내 컴퓨터)의 커밋을 원격 저장소(GitHub)로 업로드<br>
(6) <strong>pull</strong> = 원격 저장소의 최신 내용을 로컬로 가져와서 병합<br>
(7) <strong>branch</strong> = 원본 코드에서 분리된 독립적인 작업 흐름(가지). 기능 개발이나 실험할 때 사용<br>
(8) <strong>merge</strong> = 서로 다른 브랜치의 변경 내용을 하나로 합치는 것<br>
(9) <strong>checkout</strong> = 다른 브랜치나 커밋으로 이동하는 것. 예: git checkout main<br>
(10) <strong>status</strong> = 현재 변경된 파일, staging 상태 등을 확인. 예: git status<br>
(11) <strong>fork</strong> = 다른 사람의 저장소를 내 계정으로 복제해서 독립적으로 관리하는 것 (GitHub 웹 기능)<br>
(12) <strong>pull request (PR)</strong> = 내가 작업한 브랜치를 원본 저장소에 합쳐달라고 요청하는 것<br>

##  '컴퓨터 명령 FLOW' 용어

(1) <strong>터미널(terminal)t</strong> = macOS Terminal, iTerm2, VS Code 내장 터미널 등은 그 장치를 화면 속에서 재현한 "터미널 에뮬레이터"<br>
창을 띄우고 키 입력을 전달할 뿐, 명령의 뜻을 직접 해석하지X<br>
(2) <strong>셸(shell)</strong> = 운영체제의 핵심(커널)을 감싼 "껍데기<br> 
사람이 입력한 명령을 해석해 프로그램을 실행시키고 커널과 이어주는 역할을 해요. bash, zsh 등이 대표적인 셸의 종류임<br>
(3) <strong>커널(kernel)</strong> = "알맹이"라는 뜻<br> CPU·메모리·파일·네트워크 같은 자원을 관리하는 운영체제의 중심부<br>
(4) <strong>프롬프트(prompt)</strong> = "재촉하다"라는 뜻<br> 셸이 "입력 기다리는 중"임을 알리는 화면 표시( $, % 같은 모양)<br>







