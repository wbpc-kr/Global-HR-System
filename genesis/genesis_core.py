# genesis_core.py
# 제니시스 AI의 핵심 로직

def detect_intrusion(log_data):
    if "unauthorized_access" in log_data:
        return True
    return False
