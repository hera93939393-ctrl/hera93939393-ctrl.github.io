---
layout: post
title: "ONLY AI=챗GPT??"
date: 2026-07-13
categories: 공부기록
icon: "✌️"
image: "https://github.com/user-attachments/assets/a8344f4f-a69a-43cf-8b34-7d560b190bf2"
thumb: "https://github.com/user-attachments/assets/5a9ac878-1937-4e31-a69b-d1170ffb8700"
banner_large: true
---

<p class="lead">AI 종류는 다양해요!</p>

## 생성형AI의 2가지 Version!

많은 분들이 AI라고 하면 챗GPT를 먼저 떠올립니다!
2022년 가장 먼저 AI 타이틀을 달고 출시되어 큰 화제를 모으면서 AI 챗봇 붐을 이끈 계기가 되었죠! 

그러나 4년여간 AI가 엄청난 속도로 발전해 왔고, 지금은 형태와 종류가 많아졌어요😆

크게는 2가지!<br>
우리가 가장 많이 쓰고 있는 웹브라우저형과 터미널형으로 아래처럼 나눠볼수 있어요.
* <strong>웹브라우저</strong>(챗GPT, Claude 등) = 대화하며 답을 받는 용도 (가장많이 쓰임)
* <strong>DESKTOP-터미널</strong>(Claude Code, Open Code 등) = 내 컴퓨터의 실제 파일과 코드 생성 및 수정 가능
<strong> => 터미널에서 AI를 사용하면 더욱 강력하겠죠! </strong>

<div class="compare-table">
<table>
  <thead>
    <tr><th>구분</th><th>종류</th><th>특징</th></tr>
  </thead>
  <tbody>
    <tr class="group-web">
      <td class="category-cell" rowspan="9">웹브라우저<small>(대화하며 답을 받는 용도)</small></td>
      <td>ChatGPT (OpenAI)</td>
      <td>가장 널리 쓰이는 대화형 AI, 다양한 플러그인·GPT 생태계</td>
    </tr>
    <tr class="group-web"><td>Claude (Anthropic)</td><td>긴 문서 처리와 신중한 답변에 강점, 대화 위주</td></tr>
    <tr class="group-web"><td>Gemini (Google)</td><td>구글 검색·지메일·문서 등과 연동이 잘 됨</td></tr>
    <tr class="group-web"><td>Perplexity</td><td>답변마다 출처 링크를 보여주는 검색형 챗봇</td></tr>
    <tr class="group-web"><td>Grok (xAI)</td><td>X(트위터) 연동, 실시간 트렌드 이슈에 강함</td></tr>
    <tr class="group-web"><td>Copilot (Microsoft)</td><td>오피스·윈도우·엣지에 통합된 챗봇</td></tr>
    <tr class="group-web"><td>Meta AI</td><td>페이스북·인스타그램·왓츠앱에 통합</td></tr>
    <tr class="group-web"><td>DeepSeek</td><td>중국산, 저비용·고성능으로 화제</td></tr>
    <tr class="group-web"><td>Le Chat (Mistral)</td><td>프랑스 AI 기업 미스트랄의 챗봇</td></tr>
    <tr class="group-terminal">
      <td class="category-cell" rowspan="7">터미널<small>(내 컴퓨터의 실제 파일과 코드를 직접 만들고 고치게 시키는 용도)</small></td>
      <td>Claude Code (Anthropic)</td>
      <td>내 컴퓨터에 설치해 파일·코드를 직접 생성/수정</td>
    </tr>
    <tr class="group-terminal"><td>Codex CLI (OpenAI)</td><td>클라우드 코드와 가장 직접적인 경쟁 도구</td></tr>
    <tr class="group-terminal"><td>Gemini CLI (Google)</td><td>제미나이를 터미널에서 쓰는 버전</td></tr>
    <tr class="group-terminal"><td>Cursor / Windsurf</td><td>원래는 편집기(IDE)형, 최근 터미널·에이전트 기능도 강화</td></tr>
    <tr class="group-terminal"><td>Aider</td><td>오픈소스, 초기부터 유명한 터미널 AI 페어 프로그래밍 도구</td></tr>
    <tr class="group-terminal"><td>Amazon Q Developer CLI</td><td>AWS가 내놓은 터미널 코딩 에이전트</td></tr>
    <tr class="group-terminal"><td>OpenCode</td><td>오픈소스 AI 코딩 에이전트, 터미널 전용</td></tr>
  </tbody>
</table>
</div>


## 강력한 AI를 내 컴에서도 써보려면! 😁

아래 4가지 도구는 설치해야 해🗝️

(1) <strong>Claude Code</strong> : 컴퓨터 언어로 번역해 주는 통역기<br>
(2) <strong>터미널</strong> : 통역기의 화면(글자로 명령을 내리는 창)<br>
(3) <strong>Node.js(+ npm)와 uv</strong> : 컴퓨터 언어(자바스크립트-파이썬)가 돌아가게 해주는 엔진<br>
(4) <strong>Git</strong> : 변경 이력을 남기는 장치<br>

### 🎇 AI에게 코딩 시키는 과정, 6단계로 보기

<div class="flow-diagram">
  <div class="flow-step">
    <div class="flow-num">1</div>
    <div class="flow-icon c1">🙋</div>
    <div class="flow-title">나</div>
    <div class="flow-desc">한국어로<br>"이거 만들어줘" 라고 말함</div>
  </div>
  <div class="flow-arrow">→</div>
  <div class="flow-step">
    <div class="flow-num">2</div>
    <div class="flow-icon c2">💻</div>
    <div class="flow-title">터미널</div>
    <div class="flow-desc">그 말이 화면에<br>글자로 나타남</div>
  </div>
  <div class="flow-arrow">→</div>
  <div class="flow-step">
    <div class="flow-num">3</div>
    <div class="flow-icon c3">🌐</div>
    <div class="flow-title">Claude Code</div>
    <div class="flow-desc">한국어를 알아듣고<br>번역해주는 통역가</div>
  </div>
  <div class="flow-arrow">→</div>
  <div class="flow-step">
    <div class="flow-num">4</div>
    <div class="flow-icon c4">🗣️</div>
    <div class="flow-title">JS·Python</div>
    <div class="flow-desc">통역가가 실제로<br>구사하는 언어</div>
  </div>
  <div class="flow-arrow">→</div>
  <div class="flow-step">
    <div class="flow-num">5</div>
    <div class="flow-icon c5">🔧</div>
    <div class="flow-title">Node·uv</div>
    <div class="flow-desc">그 언어가 돌아가게<br>해주는 엔진</div>
  </div>
  <div class="flow-arrow">→</div>
  <div class="flow-step">
    <div class="flow-num">6</div>
    <div class="flow-icon c6">🌍</div>
    <div class="flow-title">컴퓨터</div>
    <div class="flow-desc">진짜로 실행해서<br>결과를 돌려줌</div>
  </div>
</div>
<p class="flow-note">↩ 6번 결과가 다시 1번(나)에게 보여지고, 이상하면 또 말합니다 — 이 반복이 계속됩니다</p>
<p class="flow-git-note">🗃️ Git — 이 전체 과정을 계속 기록해서, 잘못되면 이전 상태로 되돌릴 수 있게 함</p>

## 오늘의 한줄 정리!

내 컴퓨터에 강력한 AI비서가 들어와  파일을 만들고 수정하고 삭제 할 수 있다는 사실이 놀라웠고 흥미로웠다!
꼭 컴퓨터를 엄청 잘하는 직원을 아래에 두고 내가 말로만 지시하는것 같잖아🐱 너무 든든하고 신났다!<br>
무엇이든 다 만들수 있을것 같은 자신감 뿜뿜!!

클라우드 코드 프로그램을 컴퓨터에 다운받고, 위의 프로그램 설치도 부탁하면 READY!!

이제부터가 진짜 시작이당!✌️


