<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>WBPC GLOBAL HR SYSTEM</title>
    <style>
        /* 어제 약속드린 WBPC 전용 스타일 시트 */
        body { background-color: #0d1117; color: #c9d1d9; font-family: 'Segoe UI', Tahoma, sans-serif; margin: 0; padding: 40px; display: flex; justify-content: center; }
        .dashboard { max-width: 900px; width: 100%; border: 1px solid #30363d; border-radius: 15px; padding: 40px; background: linear-gradient(145deg, #161b22, #0d1117); box-shadow: 0 20px 50px rgba(0,0,0,0.6); }
        .header { border-bottom: 3px solid #58a6ff; padding-bottom: 20px; margin-bottom: 30px; text-align: center; }
        h1 { color: #58a6ff; margin: 0; font-size: 28px; letter-spacing: 3px; text-transform: uppercase; }
        .logic-card { background: rgba(255, 255, 255, 0.05); border-left: 5px solid #f0883e; padding: 20px; margin-bottom: 20px; border-radius: 8px; transition: 0.3s; }
        .logic-card:hover { background: rgba(255, 255, 255, 0.1); transform: translateX(10px); }
        .logic-title { color: #f0883e; font-weight: bold; font-size: 1.3em; margin-bottom: 10px; display: block; }
        .logic-content { font-size: 1.1em; line-height: 1.6; color: #8b949e; }
        .weather-alert { color: #ff7b72; font-weight: bold; animation: blink 2s infinite; }
        @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.5; } 100% { opacity: 1; } }
    </style>
</head>
<body>
    <div class="dashboard">
        <div class="header"><h1>WBPC GLOBAL HR CONTROL</h1></div>
        <div class="logic-card">
            <span class="logic-title">🛡️ 01. SMART GATE (S0)</span>
            <div class="logic-content">기기 인식 기반 출입 통제 및 <span class="weather-alert">실시간 기상(-1°C, 대설)</span> 데이터 연동 가동 중</div>
        </div>
        <div class="logic-card">
            <span class="logic-title">🎭 02. DYNAMIC CHARACTER (S1)</span>
            <div class="logic-content">중앙 등장 연출 및 기후 맞춤 복장 자동 전환 로직 최적화 완료</div>
        </div>
        <div class="logic-card">
            <span class="logic-title">🛰️ 03. MEDICAL GUARDIAN</span>
            <div class="logic-content">광주 전남대/조선대 병원 응급실 DB 실시간 감시: 환자 수용 [가능]</div>
        </div>
    </div>
</body>
</html>
