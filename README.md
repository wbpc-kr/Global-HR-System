<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>WBPC Metaverse Onboarding – Full Auto Mode</title>
<style>
    body {
        margin: 0;
        font-family: 'Segoe UI', sans-serif;
        background: #0d1117;
        color: #c9d1d9;
        overflow: hidden;
    }

    .screen {
        display: none;
        width: 100vw;
        height: 100vh;
        padding: 40px;
        box-sizing: border-box;
    }

    .active {
        display: block;
    }

    h1 {
        color: #58a6ff;
        text-transform: uppercase;
        letter-spacing: 3px;
    }

    button {
        padding: 15px 25px;
        margin: 10px;
        border: none;
        border-radius: 8px;
        background: #58a6ff;
        color: #fff;
        font-size: 18px;
        cursor: pointer;
    }

    button:hover {
        background: #1f6feb;
    }

    .center {
        text-align: center;
        margin-top: 20vh;
    }

    .vip-box {
        padding: 30px;
        background: rgba(255,255,255,0.05);
        border-left: 5px solid #f0883e;
        border-radius: 10px;
        width: 60%;
        margin: auto;
        margin-top: 10vh;
    }

</style>
</head>
<body>

<!-- 00. Smart Gate -->
<div id="gate" class="screen active">
    <div class="center">
        <h1>WBPC SMART GATE</h1>
        <p id="gateMessage">기기 인식 중…</p>
        <button onclick="goLobby()">입장하기</button>
        <button onclick="goLobby()">체험하기</button>
    </div>
</div>

<!-- 01. Lobby -->
<div id="lobby" class="screen">
    <div class="center">
        <h1>WBPC LOBBY</h1>
        <p>로비에 오신 것을 환영합니다.</p>
        <button onclick="goElevator()">엘리베이터로 이동</button>
        <button onclick="goDesk()">AI 안내 데스크로 이동</button>
    </div>
</div>

<!-- 01-1 Elevator -->
<div id="elevator" class="screen">
    <div class="center">
        <h1>엘리베이터 보안 인증</h1>
        <p>소속을 선택해 주십시오.</p>
        <button onclick="goAIMeeting()">지자체</button>
        <button onclick="goAIMeeting()">기업</button>
        <button onclick="goAIMeeting()">노동부</button>
    </div>
</div>

<!-- 02. AI Meeting Room -->
<div id="ai" class="screen">
    <div class="center">
        <h1>AI 미팅룸</h1>
        <p id="aiWelcome">안녕하십니까. 저는 AI 엘레나입니다.</p>
        <p>방문 목적을 선택해 주세요.</p>
        <button onclick="goVIP()">상담 / 입점</button>
        <button onclick="goVIP()">업무 / 보고</button>
        <button onclick="goVIP()">교육 / 안전</button>
        <button onclick="goVIP()">기타 문의</button>
    </div>
</div>

<!-- 03. VIP Room -->
<div id="vip" class="screen">
    <div class="vip-box">
        <h1>VIP 미팅룸</h1>
        <p id="vipMessage">이전 상담 기록을 불러오는 중…</p>
        <button onclick="goExit()">상담 종료</button>
    </div>
</div>

<!-- 04. Exit -->
<div id="exit" class="screen">
    <div class="center">
        <h1>감사합니다</h1>
        <p>눈이 많이 내리고 있습니다. 귀가길 안전운전하시길 바랍니다.</p>
        <p>상담 요약본이 모바일로 전송되었습니다.</p>
    </div>
</div>

<script>
    function show(id) {
        document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
        document.getElementById(id).classList.add('active');
    }

    function goLobby() { show('lobby'); }
    function goElevator() { show('elevator'); }
    function goDesk() { show('elevator'); }
    function goAIMeeting() { show('ai'); }
    function goVIP() { show('vip'); }
    function goExit() { show('exit'); }

    // -------------------------
    // 자동 인식 기능 (A안)
    // -------------------------
    const deviceKey = "WBPC_DEVICE_ID";

    function generateDeviceID() {
        return "DEV-" + Math.random().toString(36).substring(2, 12);
    }

    function autoRecognition() {
        let id = localStorage.getItem(deviceKey);

        if (!id) {
            // 신규 방문자
            const newID = generateDeviceID();
            localStorage.setItem(deviceKey, newID);
            document.getElementById("gateMessage").innerText =
                "신규 기기 감지됨. 환영합니다.";
        } else {
            // 재방문자
            document.getElementById("gateMessage").innerText =
                "인증된 기기입니다. 공간을 재구성합니다…";

            setTimeout(() => {
                show("ai");
                document.getElementById("aiWelcome").innerText =
                    "다시 뵙게 되어 영광입니다. 자동 인식이 완료되었습니다.";
            }, 1500);
        }
    }

    // 실행
    autoRecognition();
</script>

</body>
</html>
