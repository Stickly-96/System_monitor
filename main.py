import monitor

import tkinter as tk




def main():
    window = tk.Tk()
    window.title("System monitor")
    label = tk.Label(
        text = f"{monitor.sysname()}, \n {monitor.temper()}",
        foreground="white",  # Устанавливает белый текст
        background="black",  # Устанавливает черный фон
        width = 37,
        height = 20
    )
    label.pack()

    window.mainloop()



if __name__ == '__main__':
    main()