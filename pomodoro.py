import customtkinter as ctk
from typing import Tuple
ctk.set_appearance_mode("Dark")
from PIL import Image



class App(ctk.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.title("Pomodoro Application")
        self.geometry("400x500")
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)
        self.columnconfigure(3,weight=1)
        self.loading_wdigets()
    


    def loading_wdigets(self):
        image_tom = Image.open("tomato.png")
        play_pause_image=Image.open("play.png")
        play_image=ctk.CTkImage(light_image=play_pause_image,dark_image=play_pause_image,size=(200,200))
        tomato_image=ctk.CTkImage (light_image=image_tom,dark_image=image_tom,size=(400,400))
        image_label=ctk.CTkLabel(self,image=tomato_image,text="hello world")
        timer_label=ctk.CTkLabel(self,text="timer here")
        start_pause_button=ctk.CTkButton(self,image=play_image,fg_color="transparent",text="")
        counting_label=ctk.CTkLabel(self,text="Counting label rest here")


        image_label.grid(row=0,column=0)
        timer_label.grid(row=1,column=0)
        start_pause_button.grid(row=2,column=0)
        counting_label.grid(row=3,column=0)







app=App()
app.mainloop()



