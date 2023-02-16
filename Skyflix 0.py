# Skyflix
from tkinter import *
import customtkinter as ctk
from pytube import YouTube
import requests
import youtube_dl
import re
import os

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("1100x700")
app.title("Skyflix 0")

class AppMain():
    Logo = PhotoImage(file=os.path.join("Images",r"C:\Users\Gianclarence Solas\Desktop\python books\Skyflix\Images\Logo.png"))
    SkyflixWord = PhotoImage(file=os.path.join("Images",r"C:\Users\Gianclarence Solas\Desktop\python books\Skyflix\Images\SkyFlix.png"))
    HomeWord = PhotoImage(file=os.path.join("Images",r"C:\Users\Gianclarence Solas\Desktop\python books\Skyflix\Images\Home.png"))
    SettingsWord = PhotoImage(file=os.path.join("Images",r"C:\Users\Gianclarence Solas\Desktop\python books\Skyflix\Images\Settings.png"))
    sideBarImage = PhotoImage(file=os.path.join("Images",r"C:\Users\Gianclarence Solas\Desktop\python books\Skyflix\Images\Side Bar.png"))
    SettingslogoButton = PhotoImage(file=os.path.join("Images",r"C:\Users\Gianclarence Solas\Desktop\python books\Skyflix\Images\settings logo.png"))
    ProfilePic = PhotoImage(file=os.path.join("Images",r"C:\Users\Gianclarence Solas\Desktop\python books\Skyflix\Images\profile pic.png"))
    bgTopImage = PhotoImage(file=os.path.join("Images",r"C:\Users\Gianclarence Solas\Desktop\python books\Skyflix\Images\Bg.png"))
    
    channels = [
                # New Video
                "https://www.youtube.com/@Danny-Gonzalez",
                "https://www.youtube.com/@ryan",
                "https://www.youtube.com/@NetworkChuck",
                "https://www.youtube.com/user/mrbeast6000",
                "https://www.youtube.com/@DailyDoseOfInternet",
                
                # Cartoons
                "https://www.youtube.com/@cartoonnetworkuk",
                "https://www.youtube.com/user/ElmoreStream",
                "https://www.youtube.com/channel/UCrFslqncMIdjD2WfB6pAcEg",
                "https://www.youtube.com/channel/UCFuU-5B1eKAWaTeLUu3JuyA"
                ]
    
    # tools
    def getTitle(url):
        url = url
        ydl = youtube_dl.YoutubeDL()
        info = ydl.extract_info(url, download=False)
        return info["title"]
        
    def downloadVid(url):
        YouTube(url).streams.get_highest_resolution().download(r"C:\Users\Gianclarence Solas\Desktop\python books\Skyflix\video")
    
    def clear():
        for widgets in app.winfo_children():
            widgets.destroy()
            
    def playVid(url):
        charters = ["|", "'", "?", ",", ":", "~", "#", "$", "%", "^", "/", '"']
        AppMain.downloadVid(url)
        title = AppMain.getTitle(url=url)
        for x in range(len(charters)):
            title = title.replace(charters[x], "")
        print(title)
        os.startfile(f"C:\\Users\\Gianclarence Solas\\Desktop\\python books\\Skyflix\\video\\{title}.mp4")
        
    def getLastestVid(channel):
        channel = channel
        html = requests.get(channel + "/videos").text
        url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()

        return url
    
    def showVideoDetails(url, num):
        AppMain.clear()
        Title = ctk.CTkLabel(master=app, text=YouTube(url).title, font=("Arial", 35))
        DesTitle = ctk.CTkLabel(master=app, text="Description", font=("Arial", 20))
        Decription = ctk.CTkTextbox(master=app, height=300, width=500)
        buttonplay = ctk.CTkButton(master=app, text="Play", width=530, command=num)
        back = ctk.CTkButton(master=app, text="<--", command=AppMain.HomeScreen, width=50)
        bgTop = Label(app, image=AppMain.bgTopImage, bg="#242424")
        
        Decription.insert("0.0", f"""   Description of  "{YouTube(url).title}"   \n\n {YouTube(url).description}""")

        #bgTop.place(x=0, y=-100)
        Title.pack()
        buttonplay.place(x=530, y=140+230)
        DesTitle.place(x=10, y=140+200)
        Decription.place(x=10, y=170+200)
        back.place(x=10, y=10)
    
    def HomeScreen():
        os.system('cls')
        app.iconphoto(False, AppMain.Logo)
        def Add0(): AppMain.playVid(AppMain.getLastestVid(AppMain.channels[0]))
        def Add1(): AppMain.playVid(AppMain.getLastestVid(AppMain.channels[1]))
        def Add2(): AppMain.playVid(AppMain.getLastestVid(AppMain.channels[2]))
        def Add3(): AppMain.playVid(AppMain.getLastestVid(AppMain.channels[3]))
        def Add4(): AppMain.playVid(AppMain.getLastestVid(AppMain.channels[4]))
        def Add5(): AppMain.playVid(AppMain.getLastestVid(AppMain.channels[5]))
        def Add6(): AppMain.playVid(AppMain.getLastestVid(AppMain.channels[6]))
        def Add7(): AppMain.playVid(AppMain.getLastestVid(AppMain.channels[7]))
        def Add8(): AppMain.playVid(AppMain.getLastestVid(AppMain.channels[8]))
        
        def show0(): AppMain.showVideoDetails(AppMain.getLastestVid(AppMain.channels[0]), Add0)
        def show1(): AppMain.showVideoDetails(AppMain.getLastestVid(AppMain.channels[1]), Add1)
        def show2(): AppMain.showVideoDetails(AppMain.getLastestVid(AppMain.channels[2]), Add2)
        def show3(): AppMain.showVideoDetails(AppMain.getLastestVid(AppMain.channels[3]), Add3)
        def show4(): AppMain.showVideoDetails(AppMain.getLastestVid(AppMain.channels[4]), Add4)
        def show5(): AppMain.showVideoDetails(AppMain.getLastestVid(AppMain.channels[5]), Add5)
        def show6(): AppMain.showVideoDetails(AppMain.getLastestVid(AppMain.channels[6]), Add6)
        def show7(): AppMain.showVideoDetails(AppMain.getLastestVid(AppMain.channels[7]), Add7)
        def show8(): AppMain.showVideoDetails(AppMain.getLastestVid(AppMain.channels[8]), Add8)
        
        def ShortenTitle(title):
            if len(title) >= 41:
                short_text = title[0:35]+"..."
                return short_text
            else:
                return title
        
        def sideBar():
            SideBar = Label(app, image = AppMain.sideBarImage, bg="#242424")
            SideBar.place(x=-2, y=-2)
        
        def Icon():
            LabelPic = Label(app, image=AppMain.ProfilePic, bg="#3C3C3C")
            LabelPic.place(x=17, y=10)
        
        def NewVideos():
            NewVideosLabel = ctk.CTkLabel(master=app, text="New Videos", font=("Arial", 25))
            
            Key = ctk.CTkButton(master=app, text=ShortenTitle(AppMain.getTitle(AppMain.getLastestVid(channel=AppMain.channels[0]))), width= 250, command=show0)
            Ard = ctk.CTkButton(master=app, text=ShortenTitle(AppMain.getTitle(AppMain.getLastestVid(channel=AppMain.channels[1]))), width= 250, command=show1)
            Chuck = ctk.CTkButton(master=app, text=ShortenTitle(AppMain.getTitle(AppMain.getLastestVid(channel=AppMain.channels[2]))), width= 250, command=show2)
            Rev = ctk.CTkButton(master=app, text=ShortenTitle(AppMain.getTitle(AppMain.getLastestVid(channel=AppMain.channels[3]))), width= 250, command=show3)
            idid = ctk.CTkButton(master=app, text=ShortenTitle(AppMain.getTitle(AppMain.getLastestVid(channel=AppMain.channels[4]))), width= 250, command=show4)
            
            NewVideosLabel.place(x=70+280*0+100, y=120)
            
            # top row
            Key.place(x=70+280*0+100, y=170)
            Ard.place(x=70+280*1+100, y=170)
            Chuck.place(x=70+280*2+100, y=170)
            
            # middle row
            Rev.place(x=70+100, y=170+50)
            idid.place(x=70+280*2-180, y=170+50)
        
        def CartoonVideos():
            CartoonVideosLabel = ctk.CTkLabel(master=app, text="Cartoon Videos", font=("Arial", 23))
            
            A = ctk.CTkButton(master=app, text=ShortenTitle(AppMain.getTitle(AppMain.getLastestVid(channel=AppMain.channels[5]))), width= 250, command=show5)
            B = ctk.CTkButton(master=app, text=ShortenTitle(AppMain.getTitle(AppMain.getLastestVid(channel=AppMain.channels[6]))), width= 250, command=show6)
            C = ctk.CTkButton(master=app, text=ShortenTitle(AppMain.getTitle(AppMain.getLastestVid(channel=AppMain.channels[7]))), width= 250, command=show7)
            D = ctk.CTkButton(master=app, text=ShortenTitle(AppMain.getTitle(AppMain.getLastestVid(channel=AppMain.channels[8]))), width= 250, command=show8)
            
            # top row
            A.place(x=70+280*0+100, y=170+150)
            B.place(x=70+280*1+100, y=170+150)
            C.place(x=70+280*2+100, y=170+150)
            
            # middle row
            D.place(x=70+100, y=170+50+150)
            
            CartoonVideosLabel.place(x=70+280*0+100, y=270)
        
        sideBar()
        Icon()
        HomeImage = Label(app, image = AppMain.HomeWord, bg="#242424")
        NewVideos()
        CartoonVideos()
        HomeImage.place(x=350+150, y=40)
    
    def Login():
        name_var=StringVar()
        passw_var=StringVar()

        def outputSignIn():
            name=name_var.get()
            password=passw_var.get()
            if name == "a" and password == "a":
                In = ctk.CTkLabel(master=app, text="       correct")
                In.place(x=350+150, y=480)
                AppMain.clear()
                AppMain.HomeScreen()
            elif name == "" and password == "":
                In = ctk.CTkLabel(master=app, text="     No Value")
                In.place(x=350+150, y=480)
            else:
                In = ctk.CTkLabel(master=app, text="     Incorrect")
                In.place(x=350+150, y=480)
            name_var.set("")
            passw_var.set("")
            os.system("cls")
            print("Skyflix 0 Launched")
            print("Go to my GitHub: https://github.com/TheTechyKid")
        
        SkyflixImage = Label(app, image = AppMain.SkyflixWord, bg="#242424")
        UserName = ctk.CTkEntry(master=app, width=300, textvariable=name_var)
        PassWord = ctk.CTkEntry(master=app, width=300, textvariable=passw_var, show = '*')
        SignIn = ctk.CTkButton(master=app, text="Sign In", command=outputSignIn)
        SkyflixImage.place(x=300+100,y=70)
        UserName.place(x=300+100,y=350)
        PassWord.place(x=300+100,y=400)
        SignIn.place(x=325+50+100,y=450)

    def __init__(self):
        AppMain.Login()
    
if __name__ == "__main__":
    try:
        AppMain()
    except:
        pass

app.mainloop() # 172 LINE OF CODE!