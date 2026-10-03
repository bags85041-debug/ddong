# 🎶 Music DJ - AI 음악 추천 앱

당신의 기분과 취향에 맞는 최고의 곡들을 추천해주는 AI 음악 DJ 앱입니다.

## 📦 설치

### 1. 필수 라이브러리 설치
```bash
pip install -r requirements.txt
```

### 2. 환경 설정
프로젝트 루트에 `.env` 파일을 생성하고 다음 정보를 추가하세요:

```
ANTHROPIC_API_KEY=your_api_key_here
ANTHROPIC_BASE_URL=https://api.anthropic.com
```

**주의**: `.env` 파일은 절대 Git에 커밋하지 마세요!

## 🚀 실행

```bash
streamlit run music_dj_app.py
```

앱이 브라우저에서 자동으로 열립니다. (기본값: `http://localhost:8501`)

## ✨ 주요 기능

- 🎵 상황, 선호 가수, 장르에 맞는 음악 추천
- 🤖 Claude AI를 활용한 맞춤형 추천
- 🎬 YouTube에서 추천곡 바로 검색 가능
- 📋 플레이리스트 분위기 설명

## 📋 프로젝트 구조

```
sample_project_music_dj_app/
├── music_dj_app.py          # 메인 애플리케이션
├── ai_helper.py             # Claude API 헬퍼 함수
├── requirements.txt         # 필수 라이브러리
├── .env                     # 환경변수 (Git 제외)
├── PLAN.md                  # 프로젝트 기획서
├── README.md                # 이 파일
└── .streamlit/
    └── config.toml          # Streamlit 설정
```

## 🔧 주요 함수

- `ask_ai(prompt)` - Claude API를 통해 AI 응답 받기
- `get_music_recommendations()` - 음악 추천 생성
- `render_song_card()` - 추천 곡을 카드 형태로 표시

## 🌐 배포

Streamlit Cloud에 배포되었습니다:
https://fortune-app-32sdxidwdaiukjb7kyc5nx.streamlit.app/

## ⚠️ 중요 사항

- API Key는 절대 공개하지 마세요
- `.env` 파일을 버전 관리에서 제외하세요
- `.gitignore`에 `.env`를 추가하세요
