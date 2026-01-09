<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>WBPC GLOBAL WORK CARE AI SYSTEM</title>
    <style>
        body, html { margin: 0; padding: 0; width: 100%; height: 100%; background: #000; overflow: hidden; font-family: 'Arial', sans-serif; }
        
        /* 우주 배경 효과 */
        #universe { position: fixed; width: 100vw; height: 100vh; background: radial-gradient(circle, #1a1a1a 0%, #000 100%); z-index: 1; transition: transform 2s ease-in; }

        /* 중앙 회전 로고 */
        .logo-container { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 10; text-align: center; }
        .main-logo { width: 300px; height: auto; animation: rotateLogo 15s linear infinite; transition: all 1.5s ease-in; filter: drop-shadow(0 0 20px rgba(255,215,0,0.5)); }
        
        @keyframes rotateLogo { from { transform: rotateY(0deg); } to { transform: rotateY(360deg); } }

        /* 오른쪽 상단 국가 선택 박스 */
        .select-box { position: absolute; top: 40px; right: 40px; z-index: 100; }
        select { background: rgba(255,255,255,0.1); color: #ffd700; border: 1px solid #ffd700; padding: 10px 20px; font-size: 16px; cursor: pointer; border-radius: 5px; outline: none; }

        /* 왼쪽 하단 특허 문구 */
        .patent-info { position: absolute; bottom: 20px; left: 20px; color: rgba(255,255,255,0.5); font-size: 12px; z-index: 10; letter-spacing: 1px; }

        /* 우주로 날아가는 애니메이션 효과 */
        .warp-speed { transform: scale(50); opacity: 0; transition: 2.5s all ease-in; }
    </style>
</head>
<body>

<div id="universe">
    <div class="logo-container" id="logoContainer">
        <img src="logo.png" alt="WBPC LOGO" class="main-logo" id="mainLogo">
        <h1 style="color:#ffd700; margin-top:20px; letter-spacing:5px;">WBPC GLOBAL</h1>
    </div>

    <div class="select-box">
        <select id="countrySelect" onchange="startSystem()">
            <option value="">SELECT COUNTRY</option>
            <option value="TH">THAILAND (태국)</option>
            <option value="LA">LAOS (라오스)</option>
            <option value="MM">MYANMAR (미얀마)</option>
            <option value="KH">CAMBODIA (캄보디아)</option>
        </select>
    </div>

    <div class="patent-info">
        [특허출원 완료] 본 시스템의 디자인 및 로직 무단 복제는 법으로 엄격히 금지되어 있습니다.
    </div>
</div>

<script>
    function startSystem() {
        const logo = document.getElementById('mainLogo');
        const universe = document.getElementById('universe');
        
        // 1. 로고 회전 정지
        logo.style.animation = 'none';
        
        // 2. 우주로 날아가는 느낌 연출 (화면 확대 및 소멸)
        setTimeout(() => {
            universe.classList.add('warp-speed');
            
            // 3. 2.5초 후 메인 시스템 화면으로 전환 (현재는 예시로 알림창)
            setTimeout(() => {
                alert("본사 메인 시스템으로 진입합니다.");
                // window.location.href = 'main.html'; // 실제 메인화면 파일로 연결
            }, 2000);
        }, 100);
    }
</script>

</body>
</html>
