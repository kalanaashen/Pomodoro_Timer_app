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
        pause_image=Image.open("pause-button.png")
        self.pause_image_last=ctk.CTkImage(light_image=pause_image,dark_image=pause_image,size=(50,50))
        self.play_image=ctk.CTkImage(light_image=play_pause_image,dark_image=play_pause_image,size=(50,50))
        tomato_image=ctk.CTkImage (light_image=image_tom,dark_image=image_tom,size=(400,400))

        self.image_label=ctk.CTkLabel(self,image=tomato_image,text="hello world")
        #timer_label=ctk.CTkLabel(self,text="timer here")
        self.start_pause_button=ctk.CTkButton(self,image=self.play_image,fg_color="transparent",text="",height=20,width=20,corner_radius=0,border_width=0,hover_color="#1a1a1a",command=self.button_logic)
        counting_label=ctk.CTkLabel(self,text="Counting label rest here")


        self.image_label.grid(row=0,column=0)
        #timer_label.grid(row=1,column=0)
        self.start_pause_button.grid(row=2,column=0)
        counting_label.grid(row=3,column=0)


    def button_logic(self):
        if self.start_pause_button.cget("image")==self.play_image:
            self.start_pause_button.configure(self,image=self.pause_image_last)
            self.sec_25()
            
        else:
            self.start_pause_button.configure(self,image=self.play_image)
    def sec_25(self):

        self.seconds=10*2
        self.timer()
    def timer(self):

        if self.seconds>=0:
            self.rest_minutes=int(self.seconds/60)
            self.rest_seconds=self.seconds%60
            if self.rest_minutes==0 and self.seconds>=10:
                self.image_label.configure(text=f"{self.rest_seconds}",font=("Arial",30, "bold"))
            elif self.seconds<10 and self.rest_minutes!=0:
                self.image_label.configure(text=f"{self.rest_minutes}:0{self.rest_seconds}",font=("Arial",30, "bold"))
            elif self.seconds<10 and self.rest_minutes==0:
                self.image_label.configure(text=f"{self.rest_seconds}",font=("Arial",30, "bold"))
            self.seconds-=1
            self.after(1000,self.timer)





    def sec_5(self):
        self.seconds_break=5*60
        self.timer()




app=App()
app.mainloop()



