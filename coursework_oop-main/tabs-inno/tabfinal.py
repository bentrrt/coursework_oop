import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tkst
import ttkbootstrap as ttk
from ttkbootstrap import Style
from tkinter import messagebox

import video_library as lib
import font_manager as fonts
import pywhatkit 




def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

def add_text(text_area, content):
    text_area.insert(1.0, content + "\n")

def errorID():
    messagebox.showwarning(title="Invalid ID", message="Please enter a valid ID")

def errorDUP():
    messagebox.showinfo(title="Duplicate found", message="The video has already been added")

def errorNull():
    messagebox.showinfo(title="Playlist Empty", message="womp womp")

def errorOver():
    messagebox.showwarning(title="No more", message="Stop")

def errorReview():
    messagebox.showwarning(title="Invalid Rating", message="Please enter a valid number")


class tabwin:
    def __init__(self, window):
        self.window = window
        self.window.title("tabs")
        self.style = Style(theme='lumen') 
        self.window.resizable(False, False)
        #innit notebook
        self.notebook = ttk.Notebook(window)

        
        #innit tab
        self.tab_check_vid = ttk.Frame(self.notebook)
        self.tab_create_vid_list = ttk.Frame(self.notebook)
        self.tab_update_vid = ttk.Frame(self.notebook)
        self.tab_sort = ttk.Frame(self.notebook)
        self.var1 = tk.IntVar()
        var1 = self.var1
        def night_switch():
           if var1.get() == 1:
               self.style.theme_use("vapor")
           else:
               self.style.theme_use("lumen")
        
        def surprise_me():
            url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 
            pywhatkit.playonyt(url)
        #toggle button
        self.toggle_night_mode = ttk.Checkbutton(bootstyle='success, round-toggle', text="Night Mode" ,variable=var1,command=night_switch)
        self.toggle_night_mode.grid(row=0, column=0, padx=10, pady=10, sticky='ne')
        
        self.btnn = ttk.Button( text="surprise me",command=surprise_me)
        self.btnn.grid(row=1, column=0, padx=10, pady=10, sticky='ne')
        #add tab
        self.notebook.add(self.tab_check_vid, text = "check video")
        self.notebook.add(self.tab_create_vid_list, text = "create video list")
        self.notebook.add(self.tab_update_vid, text = "update video")
        self.notebook.add(self.tab_sort, text = "sort")

        #pack tab
        self.notebook.grid(column=0, row=0, padx=10, pady=10)
        
        #call tab
        self.create_tab_check_vid()
        self.create_tab_update_vid()
        self.create_tab_sort()
        self.create_tab_create_vid_list()
        

        # _________________Add content to tab_check_vid________________
        
    def create_tab_check_vid(self):    
        list_videos_btn = ttk.Button(self.tab_check_vid, text="List All Videos", command=self.list_videos_clicked) 
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = ttk.Label(self.tab_check_vid, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = ttk.Entry(self.tab_check_vid, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_video_btn = ttk.Button(self.tab_check_vid, text="Check Video",command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(self.tab_check_vid, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.video_txt = ttk.Text(self.tab_check_vid, width=24, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = ttk.Label(self.tab_check_vid, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # _________________Add content to tab_create_vid_list_______________
    def create_tab_create_vid_list(self):
        self.videoplaylist=[]
        self.dfplaylist = 0
            #GUI
        listall_button= ttk.Button(self.tab_create_vid_list, text="List All Videos",command = self.listall)
        listall_button.grid(row=0, column=0, padx=10, pady=10)
        
        self.video_box = tkst.ScrolledText(self.tab_create_vid_list, width=48, height=12, wrap="none")
        self.video_box.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)
        
        self.Video_ID = ttk.Label(self.tab_create_vid_list,text="Enter Video ID")
        self.Video_ID.grid(row=0, column=1, padx=10, pady=10)
        
        self.ID_input = ttk.Entry(self.tab_create_vid_list, width=3)
        self.ID_input.grid(row=0, column=2, padx=8, pady=10)
        
        self.Videoinfo_box = tkst.ScrolledText(self.tab_create_vid_list, width=17, height=10, wrap="none")
        self.Videoinfo_box.grid(row=1, column=3, columnspan=3, sticky="W", padx=10, pady=10)
        
        self.check_video = ttk.Button(self.tab_create_vid_list,text="Check Video",command = self.displayinfocreate)
        self.check_video.grid(row=0, column=3, padx=10, pady=10)
        
        self.add_video = ttk.Button(self.tab_create_vid_list,text="Add Video",command=self.add_btn_clicked)
        self.add_video.grid(row=0, column=6, padx=8, pady=10)
        
        self.delete_list = ttk.Button(self.tab_create_vid_list,text="Clear list",command=self.clear_btn_clicked)
        self.delete_list.grid(row=4, column=6, padx=8, pady=10)
        
        self.playlist = tkst.ScrolledText(self.tab_create_vid_list, width=17, height=12, wrap="none")
        self.playlist.grid(row=1, column=6, columnspan=3, sticky="W", padx=10, pady=10)
            
        self.playvideo = ttk.Button(self.tab_create_vid_list,text="Play Video",command=self.PlayVid)
        self.playvideo.grid(row=3, column=6, padx=8, pady=10)
            
        self.next = ttk.Button(self.tab_create_vid_list,text="Next",command=self.Next)
        self.next.grid(row=4, column=7, padx=8, pady=10)
        
        self.prev = ttk.Button(self.tab_create_vid_list,text="Prev",command=self.Prev)
        self.prev.grid(row=4, column=5, padx=8, pady=10)

    
        

    


       # _______________Add content to tab_update_vid____________________________
    def create_tab_update_vid(self):
        self.videoplaylist=[]
        self.ratingdtb=['1','2','3','4','5']
        
        listall_button= ttk.Button(self.tab_update_vid, text="List All Videos",command = self.listallcreate)
        listall_button.grid(row=0, column=0, padx=10, pady=10)
            
        self.video_box2 = tkst.ScrolledText(self.tab_update_vid, width=48, height=12, wrap="none")
        self.video_box2.grid(row=1, column=0, padx=10, pady=10)
                
        self.Video_ID = ttk.Label(self.tab_update_vid,text="Enter Video ID")
        self.Video_ID.grid(row=2, column=0, padx=10, pady=10)
                
        self.ID_input = ttk.Entry(self.tab_update_vid, width=3)
        self.ID_input.grid(row=2, column=1, padx=10, pady=10, sticky='E')

        self.label_rating = ttk.Label(self.tab_update_vid, text="Enter New Rating:")
        self.label_rating.grid(row=4, column=0, padx=10, pady=10)

        self.rating_input = ttk.Entry(self.tab_update_vid, width=3)
        self.rating_input.grid(row=4, column=1, padx=10, pady=10, sticky='E')
            
        self.check_video = ttk.Button(self.tab_update_vid,text="Check Video",command = self.displayinfocupdate)
        self.check_video.grid(row=0, column=3, padx=10, pady=10)
            
        self.Videoinfo_boxupdate = tkst.ScrolledText(self.tab_update_vid, width=38, height=12, wrap="none")
        self.Videoinfo_boxupdate.grid(row=1, column=3, padx=10, pady=10)

        self.update_button = ttk.Button(self.tab_update_vid, text="Update", command=self.displayupdate)
        self.update_button.grid(row=5, column=1, padx=10, pady=10)
        
     # _______________Add content to tab_sort____________________________
    def create_tab_sort(self):
        self.listbox = tk.Listbox(self.tab_sort, width=40, height=10, selectmode='multiple')
        # Inserting the listbox items
        self.listbox.insert(1, "Tom and Jerry")
        self.listbox.insert(2, "Breakfast at Tiffany's")
        self.listbox.insert(3, "Casablanca")
        self.listbox.insert(4, "The Sound of Music")
        self.listbox.insert(5, "Gone with the Wind") 
        self.listbox.grid(row=0, column=3, padx=10, pady=10)
        def selected_item():
     
    # Traverse the tuple returned by
    # curselection method and print
    # corresponding value(s) in the listbox
            for i in self.listbox.curselection():
                print(self.listbox.get(i))

        self.btn=ttk.Button(self.tab_sort, text="Select", command=selected_item)
        self.btn.grid(row=1, column=3, padx=10, pady=10)
   
    

        self.label=ttk.Label(self.tab_sort, text="Sort By:")
    
    # _______________Add content to tab_sort____________________________

        
#_______________________________________________________________________________________from tabcheckvid________________________________________________________
    def check_video_clicked(self):
        key = self.input_txt.get() #Get key from user input
        name = lib.get_name(key)   #Get name from the key from the said input
        if name is not None:
            director = lib.get_director(key) #Get info from the library
            rating = lib.get_rating(key)    #Get info from the library
            play_count = lib.get_play_count(key)    #Get info from the library
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.video_txt, video_details)
        else:
            set_text(self.video_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Check Video button was clicked!")
    def list_videos_clicked(self):
        video_list = lib.list_all() #List all video and info
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")
#_______________________________________________________________________________________from tabcheckvid________________________________________________________
 


#_______________________________________________________________________________________from tabcreatevid________________________________________________________
         
    def listallcreate(self):
        showlistt = lib.list_all()
        set_text(self.video_box2,showlistt)
        
    def DisplayInfocreate(self,key,name,director=None,rating=None,playcount=None):
        director,playcount,rating = self.GetInfo(key)
        info = f"{name}\n{director}\nrating: {rating}\nplays: {playcount}"
        set_text(self.Videoinfo_box,info)
            
    def GetInfo(self,key):
        director = lib.get_director(key)
        playcount = lib.get_play_count(key)
        rating = lib.get_rating(key)
        return(director,playcount,rating)
    
    def GetNameAndKey(self):
        key = self.ID_input.get()
        name = lib.get_name(key)
        return(key,name)
    
    def GetUrl(self,key):
        url = lib.get_url(key)
        return url
    
    #Add a video to the playlist
    def add_btn_clicked(self):
        key , name = self.GetNameAndKey()
        if name is not None:
            if key not in self.videoplaylist:
                self.videoplaylist.append(key)
                addname=f"{name}"
                add_text(self.playlist,addname)
                print(self.videoplaylist)
            else:
                errorDUP()
        else:
            errorID()
        #Clear PLaylist        
    def clear_btn_clicked(self):
        self.playlist.delete("1.0", "end")
        self.videoplaylist.clear()
    #Show All available video
    def listall(self):
        showlist = lib.list_all()
        set_text(self.video_box,showlist)
        
    def displayinfocreate(self):
        key , name =self.GetNameAndKey()
        director,rating,playcount = self.GetInfo(key)
        if name is not None:
            self.DisplayInfocreate( key,name,director,rating,playcount)
        
      #Play Video
    def PlayVid(self):
        if len(self.videoplaylist) == 0:
             errorNull()
        else:
            key = self.videoplaylist[self.dfplaylist]
            lib.increment_play_count(key)
            name = lib.get_name(key)
            self.DisplayInfocreate(key,name)
            url = self.GetUrl(key)
            pywhatkit.playonyt(url)
                
    def Next(self):
        if self.dfplaylist < len(self.videoplaylist)-1:
            self.dfplaylist += 1
        elif self.dfplaylist > len(self.videoplaylist)-1:
            self.dfplaylist = len(self.videoplaylist)-1
            
                
    def Prev(self):
        if self.dfplaylist != 0:
            self.dfplaylist -= 1
        elif self.dfplaylist < 0:
            self.dfplaylist =0
#_____________________________________________________________________________________from tabcreatevid________________________________________________________
    
    
    
#_____________________________________________________________________________________from tabupdatevid________________________________________________________
            


    def listallupdate(self):
        showlist = lib.list_all()
        set_text(self.video_boxupdate,showlist)
 
    def displayinfocupdate(self):
        key , name =self.GetNameAndKey()
        director,rating,playcount = self.GetInfo(key)
        if name is not None:
            info = f"{name}\n{director}\nrating: {rating}\nplays: {playcount}"
            set_text(self.Videoinfo_boxupdate,info)
            

    def displayupdate(self):
        key = self.ID_input.get()
        new_rating = self.rating_input.get()
        if new_rating is not None:
            rating = new_rating
            director = lib.get_director(key)
            playcount = lib.get_play_count(key)
            name = lib.get_name(key)
            info = f"{name}\n{director}\nrating: {rating}\nplays: {playcount}"
            set_text(self.Videoinfo_boxupdate,info)
            
    def DisplayInfoupdate(self,key,name,director=None,rating=None,playcount=None):
            director,playcount,rating = self.GetInfo(key)
            info = f"{name}\n{director}\nrating: {rating}\nplays: {playcount}"
            set_text(self.Videoinfo_box,info)        
            
            
    
            
    def NewRating(self):
        key , name = self.GetNameAndKey()
        newrate = self.rating_input.get()
        if newrate in self.ratingdtb :
            lib.set_rating(key,newrate)
            a = lib.get_rating(key)
            self.DisplayInfocreate(key,name,rating=a)
        else:
            errorReview()
            
            
            
    
#_____________________________________________________________________________________from tabupdatevid________________________________________________________

  

if __name__ == "__main__":
    window = tk.Tk()
    app = tabwin(window)
    window.mainloop()
    