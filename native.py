from os import listdir, path, environ, chdir, system, makedirs
from shutil import rmtree
from glob import glob
import tkinter as tk
from tkinter import messagebox

#  Function definitions


def show_msg():
    messagebox.showinfo("Notification", "Task completed")


def del_cookies():
    chdir(environ['LOCALAPPDATA'])
    rmtree('Microsoft/Windows/History', ignore_errors=True)
    rmtree('Microsoft/Windows/Cookies', ignore_errors=True)
    rmtree('Microsoft/Intern~1', ignore_errors=True)
    rmtree('Microsoft/Windows/Tempor~1', ignore_errors=True)
    show_msg()


def del_temp_files():
    rmtree('C:\Windows\Temp', ignore_errors=True)
    makedirs('C:\Windows\Temp', exist_ok=True)
    chdir(environ['LOCALAPPDATA'])
    rmtree('Temp', ignore_errors=True)
    makedirs('Temp', exist_ok=True)
    show_msg()


def win_activation():
    system('slmgr /skms ushwbmswpz925.one.ad.bms.com:1688')
    system('slmgr.vbs /ipk windows key')
    system('slmgr /ato')
    show_msg()


def office_activation():
    chdir('/program files/microsoft office/office15')
    system('ospprearm.exe')
    system('cscript ospp.vbs /inpkey:office key')
    system('cscript ospp.vbs /act')
    show_msg()


def pwdmgr():
    my_cmd = 'powershell'
     # " -noexit -command cmdkey /list | ForEach-Object{if($_ -like "*Target:*"){cmdkey /del:($_ -replace " ","" -replace "Target:","")}}')
    my_cmd += ' -noexit '
    my_cmd += '-command '
    my_cmd += 'cmdkey /list | ForEach-Object{if($_ -like '
    my_cmd +='"*Target:*")'
    my_cmd +='{cmdkey /del:($_ -replace " ","" -replace "Target:","")}}'
    system(my_cmd)


def cleanup():
    system('cleanmgr /VERYLOWDISK')


def bginfo():
    system('C:\Progra~1\BGInfo\BGInfo.exe C:\Progra~1\BgInfo\BMSBasic.bgi /NOLICPROMPT /TIMER:0 /POPUP')


def internet():
    system('inetcpl.cpl')


def device_mgr():
    system('hdwwiz.cpl')


def wra():
    chdir(environ['LOCALAPPDATA'])
    try:
        remove('RAExpertHistory.xml')
    except OSError:
        print("File not found")
    show_msg()


def about():
    messagebox.showinfo("About this application", "This application has been conceived and implemented by Mario Scarpa "
                                                  "for the Field Service Desk."
                                                  "\n\nIt has been last reviewed and updated on 16th May 2018")


def close_program():
    print("Goodbye")
    answer = messagebox.askquestion("Exit", "Are you sure you want to close this application?", icon='warning')
    print("Answer = {}".format(answer))
    if answer == "yes":
        messagebox.showinfo("Exit", "Remember to restart the computer")
        svd_window.destroy()
    elif answer == "no":
        print("Let's continue")
    else:
        print("else condition")


# def menu_list():
#     messagebox.showinfo("Grazie", "Obrigado")


# WINDOW DESIGN

svd_window = tk.Tk()
svd_window.geometry("400x300")
# svd_window.iconbitmap('favicon.ico')
svd_window.title('Service Desk Utility')
# image1 = tk.PhotoImage(file="background.gif")
svd_window.configure(background='cadetblue2')
# t = tk.Label(svd_window, image=image1)
# t.pack(side='top', fill='both', expand='yes')

# Menu
# menu_bar = tk.Menu(svd_window)
# svd_window.config(menu=menu_bar)
# filemenu = tk.Menu(menu_bar)
# menu_bar.add_cascade(label='Tools', menu=filemenu)
# filemenu.add_command(label='List', command=menu_list)
# filemenu.add_command(label='Exit', command=close_program)

# BUTTONS ACTIONS (left side)

button_cookies = tk.Button(svd_window, text="Delete Browser's data", command=del_cookies, height=1, width=20)
button_cookies.place(x=40, y=50)

button_del_tmp = tk.Button(svd_window, text="Delete temporary files", command=del_temp_files, height=1, width=20)
button_del_tmp.place(x=40, y=80)

button_office = tk.Button(svd_window, text="Activate Office", command=office_activation, height=1, width=20)
button_office.place(x=40, y=110)

button_wra = tk.Button(svd_window, text="Delete WRA history", command=wra, height=1, width=20)
button_wra.place(x=40, y=140)

button_win = tk.Button(svd_window, text="Activate Windows 7", command=win_activation, height=1, width=20)
button_win.place(x=40, y=170)


# BUTTONS ACTIONS (right side)
button_cleanup = tk.Button(svd_window, text="Cleanup Manager", command=cleanup, height=1, width=20)
button_cleanup.place(x=210, y=50)

button_bginfo = tk.Button(svd_window, text="BGInfo", command=bginfo, height=1, width=20)
button_bginfo.place(x=210, y=80)

button_pwd = tk.Button(svd_window, text="Password Manager", command=pwdmgr, height=1, width=20)
button_pwd.place(x=210, y=110)

button_internet = tk.Button(svd_window, text="Internet properties", command=internet, height=1, width=20)
button_internet.place(x=210, y=140)

button_devmgr = tk.Button(svd_window, text="Device Manager", command=device_mgr, height=1, width=20)
button_devmgr.place(x=210, y=170)

# BUTTONS ACTIONS (bottom)
button_info = tk.Button(svd_window, text="About", command=about, height=1, width=10, bg='tan1')
button_info.place(x=70, y=260)

button_exit = tk.Button(svd_window, text="Exit", command=close_program, height=1, width=10, bg='tan1')
button_exit.place(x=240, y=260)


# button_submit = tk.Button(svd_window, text="Submit", command=submit)

# Input fields
# tk.Label(svd_window, text='Name').grid(row=0)
# tk.Label(svd_window, text='Surname').grid(row=1)
# field1 = tk.Entry(svd_window)
# field2 = tk.Entry(svd_window)
#
# field1.grid(row=0, column=1)
# field2.grid(row=1, column=1)

svd_window.mainloop()
