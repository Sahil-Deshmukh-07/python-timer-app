import tkinter as tk
import tim 
import threading

def clock():

    root = tk.Tk()
    root.title("Timer")
    root.geometry("400x400")
    root.resizable(False, False)
    root.configure(bg="#7805FC",border=5,relief="ridge")

    label = tk.Label(root,text="TIMER",bg="#3D0281",fg="#FFFFFF",font=("Times New Roman",24,"bold","underline"),border=5,relief="ridge",padx=10,pady=10,justify="center")
    label.pack(pady=20)

    hours = tk.Entry(root)
    hours.pack(pady=20)
    hours.focus_set()
    hours.configure(bg="#FFFFFF",fg="#000000",font=("Arial",14,"bold"),border=2,relief="solid",justify="center")
    hours.bind("<Return>",func=lambda event:minutes.focus_set())

    minutes = tk.Entry(root)
    minutes.pack(pady=20)
    minutes.configure(bg="#FFFFFF",fg="#000000",font=("Arial",14,"bold"),border=2,relief="solid",justify="center")
    minutes.bind("<Return>",func=lambda event:seconds.focus_set())

    seconds = tk.Entry(root)
    seconds.pack(pady=20)
    seconds.configure(bg="#FFFFFF",fg="#000000",font=("Arial",14,"bold"),border=2,relief="solid",justify="center")
    seconds.bind("<Return>",func=lambda event:on_button_click())

    button = tk.Button(root, text="Start Timer", command=lambda: start_timer())
    button.pack(pady=10)
    button.configure(bg="#3D0281",fg="#FFFFFF",font=("Arial",14,"bold"),border=5,relief="ridge",padx=10,pady=5,justify="center")

    def on_button_click():
        start_timer()

    def start_timer():
        set_time = f"{int(hours.get()):02d}:{int(minutes.get()):02d}:{int(seconds.get()):02d}"
        print(f"Timer set for: {set_time}")
        threading.Thread(target=tim.timer, args=(set_time,), daemon=True).start()

    root.mainloop()

if __name__ == "__main__":
    clock()