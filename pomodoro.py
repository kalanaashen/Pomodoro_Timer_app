import customtkinter as ctk
from typing import Tuple
from PIL import Image
ctk.set_appearance_mode("Light")



class App(ctk.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.title("Pomodoro Application")
        self.geometry("450x600")
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.rowconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)
        self.rowconfigure(3,weight=1)
        self.columnconfigure(3,weight=1)
        self.loading_wdigets()
        self.is_working=True
        self.array=[{"status":"Work","time":25*60},
                    {"status":"Break","time":5*60},
                    {"status":"Work","time":25*60},
                    {"status":"Break","time":5*60},
                    {"status":"Work","time":25*60},
                    {"status":"Break","time":5*60},
                    {"status":"Work","time":25*60},
                    {"status":"Long Break","time":30*60}]
        self.current_index=0
        self.count=1
        self.correct_sign_="✔️"


    def loading_wdigets(self):
        self.work_break_label=ctk.CTkLabel(self,text="")
        image_tom = Image.open("tomato.png")
        play_pause_image=Image.open("play.png")
        pause_image=Image.open("pause-button.png")
        self.pause_image_last=ctk.CTkImage(light_image=pause_image,dark_image=pause_image,size=(50,50))
        self.play_image=ctk.CTkImage(light_image=play_pause_image,dark_image=play_pause_image,size=(50,50))
        tomato_image=ctk.CTkImage (light_image=image_tom,dark_image=image_tom,size=(400,400))
        self.correct_sign=ctk.CTkLabel(self,text="")
        self.image_label = ctk.CTkLabel(self, image=tomato_image, text="Press Play!", compound="center", font=("Arial", 30, "bold"), text_color="white")
        self.start_pause_button=ctk.CTkButton(self,image=self.play_image,fg_color="transparent",text="",height=20,width=20,corner_radius=0,border_width=0,hover_color="white smoke",command=self.button_logic)
        self.work_break_label.grid(row=0,column=0,sticky="s")
        self.image_label.grid(row=1,column=0)
        self.start_pause_button.grid(row=2,column=0)
        self.correct_sign.grid(row=3,column=0)

    def button_logic(self):


        if self.start_pause_button.cget("image")==self.play_image:
           
           self.start_pause_button.configure(image=self.pause_image_last)
           self.timer()
            
            
        else:
            self.start_pause_button.configure(image=self.play_image)
            self.image_label.configure(text="00:00",font=("Arial",30,"bold"))
            self.work_break_label.configure(text="You Failed All reseted!",font=("Helvetica",40,"bold"))
            self.is_working=False
    

    def timer(self):
        self.is_working=True
        status_obj = self.array[self.current_index]
        self.r_time=status_obj["time"]
        self.status=status_obj["status"]
        self.inside_func()

        
    def inside_func(self):
        if self.r_time >= 0 and self.is_working :
                rest_minutes = self.r_time // 60
                rest_seconds = self.r_time % 60
                time_display = f"{rest_minutes:02}:{rest_seconds:02}"
                self.image_label.configure(text=time_display, font=("Arial", 30,"bold"))
                self.work_break_label.configure(text=self.status,font=("Helvetica",40,"bold"))
                self.r_time -= 1
                self.after(1000, self.inside_func)
        elif self.is_working and self.current_index < len(self.array):
            self.current_index+=1
            if self.status=="Break":
                self.correct_sign.configure(text=f"{self.correct_sign_*self.count}")
                self.count+=1
            self.timer()



app=App()
app.mainloop()



