import tkinter as tk
gameMaster = (1200,800)

players = (600,800)


class Interface(tk.Tk):
    def __init__(self,frameSize):
        super().__init__()
        self.title("Dnd initiative manager")
        self.size = frameSize


        self.config_row_col()
        self.make_frames()
        self.center_window()


    def config_row_col(self):
        self.grid_rowconfigure(0,weight=5)
        self.grid_rowconfigure(1,weight=1)


    def make_frames(self):
        pass

    def center_window(self):
        width_screen = self.winfo_screenwidth()
        height_screen = self.winfo_screenheight()
        self.geometry("{}x{}+{}+{}".format(self.size[0],self.size[1],int(width_screen/2-self.size[0]/2),int(height_screen/2-self.size[1]/2)-40))