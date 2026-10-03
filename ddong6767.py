import streamlit as st
import random
import time
from ai_helper import ask_ai

st.set_page_config(page_title="똥 피하기", layout="centered", initial_sidebar_state="collapsed")

st.title("💩 똥 피하기 🐔")
st.info("⌨️ **A/D** 또는 **← →** 키를 눌러 닭을 이동하세요!")

# 게임 설정
game_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            margin: 0;
            padding: 20px;
            text-align: center;
            font-family: Arial, sans-serif;
            background: #f0f0f0;
        }
        canvas {
            border: 4px solid #333;
            background: linear-gradient(180deg, #87ceeb 0%, #e0f6ff 100%);
            display: block;
            margin: 20px auto;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        .info {
            font-size: 18px;
            margin-top: 15px;
            font-weight: bold;
        }
        .score { color: #2196F3; }
        .buff { color: #ff9800; }
        .gameover { color: #f44336; }
    </style>
</head>
<body>
    <canvas id="gameCanvas" width="500" height="750"></canvas>
    <div class="info">
        <div class="score">점수: <span id="score">0</span></div>
        <div id="buff" class="buff" style="display:none;"></div>
        <div id="gameover" class="gameover" style="display:none;"></div>
    </div>

    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');

        // 게임 상수
        const GAME_WIDTH = 10;
        const GAME_HEIGHT = 15;
        const CELL_SIZE = 50;
        const SPAWN_RATE = 0.08;
        const GOLDEN_RATE = 0.1;

        // 게임 상태
        let playerX = Math.floor(GAME_WIDTH / 2);
        let poops = [];
        let score = 0;
        let gameOver = false;
        let buffActive = false;
        let buffMessage = '';
        let buffTime = 0;
        let keys = {};

        // 게임 초기화
        function resetGame() {
            playerX = Math.floor(GAME_WIDTH / 2);
            poops = [];
            score = 0;
            gameOver = false;
            buffActive = false;
            buffMessage = '';
            buffTime = 0;
            document.getElementById('gameover').style.display = 'none';
            document.getElementById('buff').style.display = 'none';
        }

        // 키 입력 처리
        document.addEventListener('keydown', (e) => {
            const key = e.key.toLowerCase();
            if (key === 'a' || e.key === 'ArrowLeft') {
                if (playerX > 0) playerX--;
                e.preventDefault();
            } else if (key === 'd' || e.key === 'ArrowRight') {
                if (playerX < GAME_WIDTH - 1) playerX++;
                e.preventDefault();
            } else if (key === 'r') {
                resetGame();
                e.preventDefault();
            }
        });

        // 똥 생성
        function spawnPoop() {
            if (Math.random() < SPAWN_RATE && !gameOver) {
                const isGolden = Math.random() < GOLDEN_RATE;
                poops.push({
                    x: Math.floor(Math.random() * GAME_WIDTH),
                    y: 0,
                    isGolden: isGolden
                });
            }
        }

        // 게임 업데이트
        function update() {
            if (gameOver) return;

            spawnPoop();

            // 똥 이동
            for (let i = poops.length - 1; i >= 0; i--) {
                poops[i].y++;

                // 충돌 감지
                if (poops[i].y === GAME_HEIGHT - 1) {
                    if (poops[i].x === playerX) {
                        if (poops[i].isGolden) {
                            score += 5;
                            buffActive = true;
                            buffTime = 120;
                            buffMessage = '✨ 황금똥 먹음! 행운이 따르자!';
                        } else {
                            gameOver = true;
                            document.getElementById('gameover').style.display = 'block';
                            document.getElementById('gameover').textContent = '💀 게임 오버! 최종 점수: ' + score;
                        }
                    } else if (poops[i].y > GAME_HEIGHT - 1) {
                        if (!poops[i].isGolden) {
                            score++;
                        }
                    }
                }

                // 화면 아래로 나간 것 제거
                if (poops[i].y > GAME_HEIGHT) {
                    poops.splice(i, 1);
                }
            }

            // 버프 시간 감소
            if (buffActive) {
                buffTime--;
                if (buffTime <= 0) {
                    buffActive = false;
                    buffMessage = '';
                    document.getElementById('buff').style.display = 'none';
                }
            }
        }

        // 게임 그리기
        function draw() {
            // 배경
            ctx.fillStyle = '#87ceeb';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // 하늘 그라데이션
            const gradient = ctx.createLinearGradient(0, 0, 0, canvas.height);
            gradient.addColorStop(0, '#87ceeb');
            gradient.addColorStop(1, '#e0f6ff');
            ctx.fillStyle = gradient;
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // 그리드
            ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
            ctx.lineWidth = 1;
            for (let i = 0; i <= GAME_WIDTH; i++) {
                ctx.beginPath();
                ctx.moveTo(i * CELL_SIZE, 0);
                ctx.lineTo(i * CELL_SIZE, canvas.height);
                ctx.stroke();
            }
            for (let i = 0; i <= GAME_HEIGHT; i++) {
                ctx.beginPath();
                ctx.moveTo(0, i * CELL_SIZE);
                ctx.lineTo(canvas.width, i * CELL_SIZE);
                ctx.stroke();
            }

            // 똥 그리기
            ctx.font = 'bold 40px Arial';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            for (let poop of poops) {
                const x = poop.x * CELL_SIZE + CELL_SIZE / 2;
                const y = poop.y * CELL_SIZE + CELL_SIZE / 2;
                ctx.fillText(poop.isGolden ? '💛' : '💩', x, y);
            }

            // 플레이어(닭) 그리기
            ctx.font = 'bold 45px Arial';
            const playerXPos = playerX * CELL_SIZE + CELL_SIZE / 2;
            const playerYPos = (GAME_HEIGHT - 1) * CELL_SIZE + CELL_SIZE / 2;
            ctx.fillText('🐔', playerXPos, playerYPos);

            // 점수 업데이트
            document.getElementById('score').textContent = score;

            // 버프 메시지
            if (buffActive) {
                document.getElementById('buff').style.display = 'block';
                document.getElementById('buff').textContent = buffMessage + ' (' + Math.ceil(buffTime / 60) + 's)';
            }
        }

        // 게임 루프
        function gameLoop() {
            update();
            draw();
            setTimeout(gameLoop, 50);
        }

        gameLoop();
    </script>
</body>
</html>
"""

st.components.v1.html(game_html, height=800)

# 게임 설명
with st.expander("📖 게임 설명"):
    st.markdown("""
    - **목표**: 하늘에서 떨어지는 💩를 피하기
    - **조작**: **A/D** 또는 **← →** 키로 닭을 이동
    - **규칙**:
        - 💩을 피하면 **1점** 획득
        - 💛(황금똥, 10% 확률)을 먹으면 **5점** + 특별 메시지
        - 💩에 맞으면 게임 오버
    """)
