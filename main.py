import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

count = 0


# Function to download
def download():
    global count
    try:
        link = YouTube(link_var.get())
        if (filetype_var.get() == filetype_list[0]):
            link.streams.get_audio_only().download(filename+'/')
        elif (filetype_var.get() == filetype_list[1]):
            link.streams.get_highest_resolution().download(filename+'/')
        count += 1
        entry.delete(0, 'end')
        completion_label = tk.Label(
            window, text=f'<{count}> Download Completed as <{filetype_var.get()}>', font='CavierDreams 13', foreground='Maroon2').pack(anchor='w')
    except:
        error_label = tk.Label(
            window, text='Error', font='CavierDreams 13', foreground='Red').pack(anchor='w')


def directory():
    global filename
    while True:
        filename = filedialog.askdirectory()

        # Bug 1
        # The user wont be able to select directory after pressing cancel at first place
        if not filename == '/':
            browse_button.configure(state="disabled", bg="gray", fg="black")
            download_button.configure(state="normal", fg="Lawn Green")
            location = f'Location : {filename}'
            file_label = tk.Label(window, text=location, font='CavierDreams 13',
                                  foreground='Spring Green').pack(anchor="w")
            break


# window
window = tk.Tk()
window.title('Youtube Download')
window.geometry('200x200')

# label


# input field
input_frame = ttk.Frame(master=window)
link_var = tk.StringVar()
entry = ttk.Entry(master=input_frame, textvariable=link_var)

download_button = tk.Button(
    input_frame, text="Download", command=download, state='disabled', bg="gray", fg="black")
browse_button = tk.Button(input_frame, text="Directory",
                          command=directory, fg="Black", )


filetype_list = ['Audio', 'Video']
filetype_var = tk.StringVar(value=filetype_list[0])
filetype_combobox = ttk.Combobox(input_frame, textvariable=filetype_var)

quit_button = tk.Button(input_frame, text='Quit', command=window.quit)


filetype_combobox['value'] = filetype_list

browse_button.pack(anchor="w")
download_button.pack(anchor="w")
entry.pack(anchor="w")
quit_button.pack(anchor="w")
filetype_combobox.pack(anchor='w')


input_frame.pack(pady=5, anchor='w')


# main loop
window.mainloop()
