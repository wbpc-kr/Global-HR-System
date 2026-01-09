<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>WBPC GLOBAL WORK CARE AI SYSTEM</title>
    <style>
        body, html { margin: 0; padding: 0; width: 100%; height: 100%; background: #000; overflow: hidden; font-family: 'Arial', sans-serif; }
        
        /* 중앙 회전 로고 */
        .logo-container { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 10; text-align: center; }
        .main-logo { width: 350px; height: auto; animation: rotateLogo 15s linear infinite; filter: drop-shadow(0 0 30px rgba(255,215,0,0.6)); }
        
        @keyframes rotateLogo { from { transform: rotateY(0deg); } to { transform: rotateY(360deg); } }

        /* 오른쪽 상단 국가 선택 */
        .select-box { position: absolute; top: 40px; right: 40px; z-index: 100; }
        select { background: rgba(0,0,0,0.7); color: #ffd700; border: 2px solid #ffd700; padding: 12px 25px; font-size: 18px; cursor: pointer; border-radius: 8px; font-weight: bold; }

        /* 왼쪽 하단 특허 문구 */
        .patent-info { position: absolute; bottom: 25px; left: 25px; color: rgba(255,215,0,0.7); font-size: 14px; z-index: 10; border-left: 3px solid #ffd700; padding-left: 10px; }

        /* 우주 워프 효과 */
        #universe { position: fixed; width: 100vw; height: 100vh; background: #000; transition: all 2s ease-in; }
        .warp-speed { transform: scale(100); opacity: 0; filter: brightness(5); }
    </style>
</head>
<body>

<div id="universe">
    <div class="logo-container" id="logo
