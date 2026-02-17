import tkinter as tk
from tkinter import ttk
import pyautogui
import threading
import time
from datetime import datetime
import pyperclip as pp


pyautogui.FAILSAFE = True 

class target_20:
    def __init__(self, root):
        self.root = root
        self.root.title("파이썬 대장장이 - 24시간 풀가동")
        self.root.geometry("300x250")

        self.is_running = False
        self.macro_thread = None

        self.create_widgets()
      
    def create_widgets(self):
        self.status_label = ttk.Label(self.root, text="상태: 대기 중", font=("Malgun Gothic", 20, "bold"))
        self.status_label.pack(pady=20)

        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=20)

        self.start_btn = ttk.Button(btn_frame, text="강화 시작", command=self.start_macro)
        self.start_btn.pack(side="left", padx=10)

        self.stop_btn = ttk.Button(btn_frame, text="강화 중지", command=self.stop_macro)
        self.stop_btn.pack(side="right", padx=10)
        self.stop_btn.config(state="disabled") # 초기엔 비활성화

        self.log_text = tk.Text(self.root, height=8, width=40, state='disabled')
        self.log_text.pack(padx=10, pady=10)

    def log(self, message):
        current_time = datetime.now().strftime("%H:%M:%S")
        formatted_message = f"[{current_time}] {message}"
        
        self.log_text.config(state='normal')
        self.log_text.insert(tk.END, formatted_message + "\n")
        self.log_text.see(tk.END) 
        self.log_text.config(state='disabled')

    def start_macro(self):
        if self.is_running:
            return
        
        self.is_running = True
        self.status_label.config(text="상태: 강화 중", foreground="green")
        self.start_btn.config(state="disabled")
        self.stop_btn.config(state="normal")
        self.log(">>> 20강 가자!")

        self.macro_thread = threading.Thread(target=self.run_logic)
        self.macro_thread.daemon = True 
        self.macro_thread.start()

    def stop_macro(self):
        if not self.is_running:
            return
        
        self.is_running = False
        self.status_label.config(text="상태: 중지됨", foreground="red")
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self.log(">>> 일단 휴식")
        

    def run_logic(self):
        while self.is_running:
            try:
                try:
                    target_pos = pyautogui.locateOnScreen('upgrade.png', confidence=0.8)
                except:
                    target_pos = None

                if target_pos:
                    center_x, center_y = pyautogui.center(target_pos)
                    pyautogui.click(center_x, center_y)
                    self.log(f"⚔️ 강화 가즈아!!!!")
                    time.sleep(2.0) 
                else:
                    target_x = 346
                    target_y = 743

                    pyautogui.click(target_x, target_y)
                    self.log(f"직접 입력으로 강화 시도...")
                    
                    time.sleep(1.0) 

                    input_text = "/강화" 
                    pp.copy(input_text)
                    pyautogui.hotkey('command', 'v') # 윈도우는 ctrl로 변경

                    time.sleep(0.5)
                    
                    pyautogui.press('enter') 
                    time.sleep(1.0) 
                    pyautogui.press('enter') 
                    
                    # 너무 자주 반복되면 안 되니까 2초 정도 쉼
                    time.sleep(2.0)

                    self.log(f"⚔️ 강화 가즈아!!!!")
                    pass

                time.sleep(1.0) 

            except pyautogui.FailSafeException:
                self.stop_macro()
                self.log("!!! 안전장치 발동 (마우스 코너 감지) !!!")
                break
            except Exception as e:
                self.log(f"에러 발생: {e}")
                # 에러가 나도 멈추지 않게 하려면 아래 break를 지우세요
                # self.stop_macro() 
                # break
                time.sleep(1) # 에러 났을 땐 1초 쉬고 다시 시도

if __name__ == "__main__":
    root = tk.Tk()
    app  = target_20(root)
    root.mainloop()
