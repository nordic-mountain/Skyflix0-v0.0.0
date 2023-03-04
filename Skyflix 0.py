# Skyflix 0.py
from tkinter import *
import customtkinter as ctk
from pytube import YouTube
import pathlib
import random
import requests
import re
import os

# Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# App
app = ctk.CTk()
app.geometry("1100x700")
app.title("Skyflix 0")
app.resizable(False, False)

# Main class
class AppMain():
    """Main App Class. Version 4.0.2."""
    
    # Image vars
    SkyflixWord = PhotoImage(file=pathlib.PurePath(r"Images\SkyFlix.png"))
    HomeWord = PhotoImage(file=pathlib.PurePath(r"Images\Home.png"))
    SettingsWord = PhotoImage(file=pathlib.PurePath(r"Images\Settings.png"))
    sideBarImage = PhotoImage(file=pathlib.PurePath(r"Images\Side Bar.png"))
    SettingslogoButton = PhotoImage(file=pathlib.PurePath(r"Images\settings logo.png"))
    ProfilePic = PhotoImage(file=pathlib.PurePath(r"Images\profile pic.png"))
    bgTopImage = PhotoImage(file=pathlib.PurePath(r"Images\Bg.png"))
    
    # Channel lists
    channels = [
                # New Video
                "https://www.youtube.com/@test",
                "https://www.youtube.com/@test",
                "https://www.youtube.com/@test",
                "https://www.youtube.com/@test",
                "https://www.youtube.com/@test",
                
                # Cartoons
                "https://www.youtube.com/@test",
                "https://www.youtube.com/@test",
                "https://www.youtube.com/@test",
                "https://www.youtube.com/@test"
                ]
    
    # tools
    
    def Greating():
        compliments = ["You're a ray of sunshine!",
                       "You have a heart of gold!",
                       "You're a great listener!",
                       "You're amazing and inspiring!",
                       "You're a true gem!",
                       "You're an incredible friend!",
                       "You're a fantastic team player!",
                       "You're so creative and innovative!",
                       "You have an infectious enthusiasm!",
                       "You have a great sense of humor!",
                       "You have a beautiful soul!",
                       "You're a problem-solving genius!",
                       "You're an absolute pleasure to be around!",
                       "You're a natural born leader!",
                       "You're a hard worker and dedicated!",
                       "You always have a positive attitude!",
                       "You have a remarkable talent!",
                       "You inspire others with your actions!",
                       "You're a valuable asset to any team!",
                       "You're a kind and caring individual!"]
        ranComliment = random.choice(compliments)
        Label = ctk.CTkLabel(master=app, text=ranComliment)
        Label.place(x=470, y=650)
    
    def getTitle(url):
        """Get the youtube links title."""
        
        url = url
        Title = YouTube(url=url).title
        return Title       
        
    def downloadVid(url):
        """Download the youtube link."""
        
        YouTube(url).streams.get_highest_resolution().download(pathlib.PurePath(r"video"))
    
    def clear():
        """Clear all th wigets in the screen."""
        
        for widgets in app.winfo_children():
            widgets.destroy()
            
    def playVid(url):
        """Play the video."""

        charters = ["|", "'", "?",
                    ",", ":", "~",
                    "#", "$", "%",
                    "^", "/", '"']

        AppMain.downloadVid(url)
        title = AppMain.getTitle(url=url)
        for x in range(len(charters)):
            title = title.replace(charters[x], "")

        print(title)
        os.startfile(pathlib.PurePath(f"video\{title}.mp4"))
  
    def getLastestVid(channel):
        """Get the lastest video from a youtube channel."""
        
        channel = channel
        html = requests.get(channel + "/videos").text
        url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()

        return url
    
    def showVideoDetails(url, num):
        """Screen that shows the videos info."""

        app.title("Skyflix 0")
        AppMain.clear()
        
        Title = ctk.CTkLabel(master=app, text=YouTube(url).title, font=("Arial", 35))
        DesTitle = ctk.CTkLabel(master=app, text="Description", font=("Arial", 20))
        Decription = ctk.CTkTextbox(master=app, height=300, width=500)
        buttonplay = ctk.CTkButton(master=app, text="Play", width=530, command=num)
        back = ctk.CTkButton(master=app, text="<--", command=AppMain.HomeScreen, width=50)
        
        # Insert Decription
        Decription.insert("0.0", f"""   Description of  "{YouTube(url).title}"   \n\n {YouTube(url).description}""")
        
        # Placement
        Title.pack()
        buttonplay.place(x=530, y=140+230)
        DesTitle.place(x=10, y=140+200)
        Decription.place(x=10, y=170+200)
        back.place(x=10, y=10)
    
    def HomeScreen():
        """Home Screen."""
        
        app.title("Skyflix 0")
        os.system('cls')
        
        def Add0(): AppMain.playVid(AppMain.getLastestVid(AppMain.channels[0]))
        def Add1(): AppMain.playVid(AppMain.getLastestVid(AppMain.channels[1]))
        def Add2(): AppMain.playVid(AppMain.getLastestVid(AppMain.channels[2]))
        def Add3(): AppMain.playVid(AppMain.getLastestVid(AppMain.channels[3]))
        def Add4(): AppMain.playVid(AppMain.getLastestVid(AppMain.channels[4]))
        def Add5(): AppMain.playVid(AppMain.getLastestVid(AppMain.channels[5]))
        def Add6(): AppMain.playVid(AppMain.getLastestVid(AppMain.channels[6]))
        def Add7(): AppMain.playVid(AppMain.getLastestVid(AppMain.channels[7]))
        def Add8(): AppMain.playVid(AppMain.getLastestVid(AppMain.channels[8]))
        
        def ShortenTitle(title):
            """Shorten the title of the video if it is over 41 char."""
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
            
            A = ctk.CTkButton(master=app, text=ShortenTitle(AppMain.getTitle(AppMain.getLastestVid(channel=AppMain.channels[0]))), width= 250, command=lambda: AppMain.showVideoDetails(AppMain.getLastestVid(AppMain.channels[0]), Add0))
            B = ctk.CTkButton(master=app, text=ShortenTitle(AppMain.getTitle(AppMain.getLastestVid(channel=AppMain.channels[1]))), width= 250, command=lambda: AppMain.showVideoDetails(AppMain.getLastestVid(AppMain.channels[1]), Add1))
            C = ctk.CTkButton(master=app, text=ShortenTitle(AppMain.getTitle(AppMain.getLastestVid(channel=AppMain.channels[2]))), width= 250, command=lambda: AppMain.showVideoDetails(AppMain.getLastestVid(AppMain.channels[2]), Add2))
            D = ctk.CTkButton(master=app, text=ShortenTitle(AppMain.getTitle(AppMain.getLastestVid(channel=AppMain.channels[3]))), width= 250, command=lambda: AppMain.showVideoDetails(AppMain.getLastestVid(AppMain.channels[3]), Add3))
            E = ctk.CTkButton(master=app, text=ShortenTitle(AppMain.getTitle(AppMain.getLastestVid(channel=AppMain.channels[4]))), width= 250, command=lambda: AppMain.showVideoDetails(AppMain.getLastestVid(AppMain.channels[4]), Add4))
            
            NewVideosLabel.place(x=70+280*0+100, y=120)
            
            # top row
            A.place(x=70+280*0+100, y=170)
            B.place(x=70+280*1+100, y=170)
            C.place(x=70+280*2+100, y=170)
            
            # middle row
            D.place(x=70+100, y=170+50)
            E.place(x=70+280*2-180, y=170+50)
        
        def CartoonVideos():
            CartoonVideosLabel = ctk.CTkLabel(master=app, text="Cartoon Videos", font=("Arial", 23))
            
            A = ctk.CTkButton(master=app, text=ShortenTitle(AppMain.getTitle(AppMain.getLastestVid(channel=AppMain.channels[5]))), width= 250, command=lambda: AppMain.showVideoDetails(AppMain.getLastestVid(AppMain.channels[5]), Add5))
            B = ctk.CTkButton(master=app, text=ShortenTitle(AppMain.getTitle(AppMain.getLastestVid(channel=AppMain.channels[6]))), width= 250, command=lambda: AppMain.showVideoDetails(AppMain.getLastestVid(AppMain.channels[6]), Add6))
            C = ctk.CTkButton(master=app, text=ShortenTitle(AppMain.getTitle(AppMain.getLastestVid(channel=AppMain.channels[7]))), width= 250, command=lambda: AppMain.showVideoDetails(AppMain.getLastestVid(AppMain.channels[7]), Add7))
            D = ctk.CTkButton(master=app, text=ShortenTitle(AppMain.getTitle(AppMain.getLastestVid(channel=AppMain.channels[8]))), width= 250, command=lambda: AppMain.showVideoDetails(AppMain.getLastestVid(AppMain.channels[8]), Add8))
            
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
        AppMain.Greating()
        
        HomeImage.place(x=350+150, y=40)
    
    def Login():
        """Login Screen."""

        name_var=StringVar()
        passw_var=StringVar()

        def outputSignIn():
            Username=name_var.get()
            Password=passw_var.get()

            if Username and Password == "a":
                In = ctk.CTkLabel(master=app, text=" "*6+"correct")
                In.place(x=350+150, y=480)
                AppMain.clear()
                AppMain.HomeScreen()

            elif Username and Password == "":
                In = ctk.CTkLabel(master=app, text=" "*5+"No Value")
                In.place(x=350+150, y=480)

            else:
                In = ctk.CTkLabel(master=app, text=" "*5+"Incorrect")
                In.place(x=350+150, y=480)

            # Clear the Username and Passwords
            name_var.set("")
            passw_var.set("")
            
            os.system("cls")
            print("Skyflix 0 Launched\nGo to my GitHub: https://github.com/TheTechyKid")
        
        app.title("Skyflix Sign in")
        SkyflixImage = Label(app, image = AppMain.SkyflixWord, bg="#242424")
        UserName = ctk.CTkEntry(master=app, width=300, textvariable=name_var)
        PassWord = ctk.CTkEntry(master=app, width=300, textvariable=passw_var, show = '*')
        SignIn = ctk.CTkButton(master=app, text="Sign In", command=outputSignIn)
        
        # Placement
        SkyflixImage.place(x=300+100,y=70)
        UserName.place(x=300+100,y=350)
        PassWord.place(x=300+100,y=400)
        SignIn.place(x=325+50+100,y=450)

    def __init__(self):
        AppMain.Login()

    
if __name__ == "__main__":
    AppMain()   

# Mainloop
app.mainloop()
