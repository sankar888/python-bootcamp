import tkinter as tk
import time

def main():
    root = tk.Tk('sname', 'bname')
    root.title('Hello')

    frame = tk.Frame(root, borderwidth=3, background='blue', padx=3, pady=3)
    # create canvas
    canvas = tk.Canvas(frame,
        height=600,
        width=600,
        bg = 'white'
    )
    id = canvas.create_text(20,20, text="0", fill='brown', font=('Helvetica', 36, 'bold'))
    
    def animate():
        print('animation starts..')
        for i in range(1,10):
            print(f'i => {i}')
            canvas.itemconfig(id, text=str(i))
            canvas.update_idletasks()
            time.sleep(0.5)
        print('animation ends..')
    
    canvas.pack()
    frame.pack()

    root.after(5000, animate)
    root.mainloop()
    print(f'exit!')


if __name__ == '__main__':
    main()