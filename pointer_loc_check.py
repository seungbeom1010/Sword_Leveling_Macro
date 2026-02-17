import pyautogui
import time

print("실시간 좌표 확인 중... (종료하려면 Ctrl + C)")

try:
    while True:
        x, y = pyautogui.position()
        print(f"현재 위치 -> X: {x:<5} Y: {y:<5}", end="\r")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\n\n좌표 확인 종료!")