from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import cv2
import matplotlib.pyplot as plt
import time

main_frame=Tk()
width = main_frame.winfo_screenwidth()
height = main_frame.winfo_screenheight()
countdevilangel=0
if width==1366 and height==768:
    main_frame.attributes('-fullscreen',True)
    countdevilangel+=1
else:
    main_frame.geometry("1366x768")
    main_frame.minsize(1366, 768)
    main_frame.maxsize(1366, 768)

darkicon_1= PhotoImage(file=r"image.app\db image\icon\931044ce15604e0302b36b64cdb5a551-modified(1).png")
darkicon_2= PhotoImage(file=r"image.app\db image\icon\anime-boy-whatsapp-dp (1)-modified.png")
darkicon_3= PhotoImage(file=r"image.app\db image\icon\anime-boy-whatsapp-dp (5)-modified.png")
darkicon_4= PhotoImage(file=r"image.app\db image\icon\anime-boy-whatsapp-dp (6)-modified.png")
darkicon_5= PhotoImage(file=r"image.app\db image\icon\anime-boy-whatsapp-dp (10)-modified.png")
darkicon_6= PhotoImage(file=r"image.app\db image\icon\Anime-Girl-WhatsApp-DP-Pictures-modified.png")
darkicon_7= PhotoImage(file=r"image.app\db image\icon\Anime-WhatsApp-DP-23-modified.png")
darkicon_8= PhotoImage(file=r"image.app\db image\icon\Anime-WhatsApp-DP-for-Boys-13-modified.png")
darkicon_9= PhotoImage(file=r"image.app\db image\icon\Anim-Whatsapp-Dp-Images-pictures-photo-free-hd-modified.png")
darkicon_10= PhotoImage(file=r"image.app\db image\icon\cartoon-boy-images-16-1-modified.png")
darkicon_11= PhotoImage(file=r"image.app\db image\icon\cartoon-boy-images-18-modified.png")
darkicon_12= PhotoImage(file=r"image.app\db image\icon\cartoon-girl-images-4-modified.png")
darkicon_13= PhotoImage(file=r"image.app\db image\icon\images-modified.png")

devil_image_1=PhotoImage(file=r"image.app\devil3.png")
devil_image_2=PhotoImage(file=r"image.app\devil6.png")
devil_image_3=PhotoImage(file=r"image.app\devil5.png")

evil1_photo_cover= PhotoImage(file=r"image.app\devil332.png")

devil_house=PhotoImage(file=r"image.app\uploading(1).png")

devil_limet_1=0
devil_limet_2=0
devil_limet_3=0

darksuman=0

devil_col="#303134"

file=open("link.txt","r")
devilfile=file.read()
darkness= PhotoImage(file=devilfile)

def dark_lib_2():
    global devil_buttton_1,devil_buttton_2,devil_buttton_3,devil_buttton_4,devil_buttton_5,devil_angel_count_lib,darksuman,darkdemon,angel2,angel3,angel4,angel5,angel6,angel7,angel8,angel9,angel66,evil1,game1,game5,angel66,devil_button_1,devil_button_2,devil_button_3
    def devilhide():
        demon5.destroy()
    if darksuman==1:
        angel2.destroy(),angel3.destroy(),angel4.destroy(),angel5.destroy(),angel6.destroy(),angel7.destroy(),
        angel8.destroy(),angel9.destroy(),angel66.destroy()
        demon5=Label(main_frame,image=evil1_photo_cover,bd=0,bg="#a8fdff")
        demon5.place(x=0,y=0)
        main_frame.after(5,devilhide)
        darksuman-=1
def dark_lib_1(event):
    dark_lib_2()

def main_indegration(vid):
    try:
        devil_file= "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
        angel_model="frozen_inference_graph.pb"

        model=cv2.dnn_DetectionModel(angel_model,devil_file)

        with open("name.pb","r") as devil_angel:
            devil_name=devil_angel.read().split("\n")

        model.setInputSize(320,320)
        model.setInputScale(1.0/127.5)
        model.setInputMean((127.5,127.5,127.5))
        model.setInputSwapRB(True)

        while(True):
            ret, frame = vid.read()
            classindex_devil,confidece_devil,bbox_devil=model.detect(frame,confThreshold=0.5)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            font_scale=3
            font=cv2.FONT_HERSHEY_PLAIN
            if len(devil_name)!=0:
                for devil_1,devil_2,devil_3 in zip(classindex_devil,confidece_devil,bbox_devil):
                    if devil_1<=80:
                        cv2.rectangle(frame,devil_3,(255,0,0),2)
                        cv2.putText(frame,devil_name[devil_1-1],(devil_3[0]+10,devil_3[1]+40),font,fontScale=font_scale,color=(0,255,0),thickness=3)
                        cv2.imshow("DEVIL",frame)
    except:
        pass
        
def devil_uplode():
    file_name = filedialog.askopenfilename()
    vid = cv2.VideoCapture(file_name)
    main_indegration(vid)
def devil_1_3():
    vid = cv2.VideoCapture(0)
    main_indegration(vid)
def devil_1_4():
    main_frame.destroy()
    
devil_label_1=Label(main_frame,image=devil_image_1,bg=devil_col)
devil_label_1.bind("<Enter>",dark_lib_1)
devil_label_1.place(x=0,y=0)
devil_label_22=Label(main_frame,text="UPLODE YOUR IMAGE BELLOW ",bg=devil_col,fg="#BB5699",font=Font(size=60,family="Freestyle Script",weight="bold"))
devil_label_22.bind("<Enter>",dark_lib_1)
devil_label_22.place(x=310,y=150)
devil_label_33=Label(main_frame,text="PLEASE... ",bg=devil_col,fg="#BB5699",font=Font(size=50,family="Freestyle Script",weight="bold"))
devil_label_33.bind("<Enter>",dark_lib_1)
devil_label_33.place(x=610,y=260)
devil_button_4=Button(main_frame,image=devil_house,bg=devil_col,bd=0,activebackground=devil_col,command=devil_uplode)
devil_button_4.place(x=620,y=400)

def devil_lib_angel():
    global darkangel2,darksuman,angel2,angel3,angel4,angel5,angel6,angel7,angel8,angel9,angel66
    def devil_101():
            angel101.destroy()
    def devil_full_cover():
        global angel101
        angel101=Label(main_frame,image=devil_image_3,bd=0,bg=devil_col)
        angel101.place(x=450,y=250)
    def dark(event):
        global darksuman,angel2,angel3,angel4,angel5,angel6,angel7,angel8,angel9,angel66
        darksuman+=1
        angel2=Button(main_frame,text="",bg="#343538",activebackground="#343538",width=1,bd=0,font=Font(size=466),state="disabled")
        angel2.place(x=0,y=0)
        angel6=Label(main_frame,text="____________________________",bg="#343538",fg="#BB5699",bd=0,font=Font(size=18))
        angel6.place(x=0,y=200)
        class devilbg():
            def darkbg1(event):
                angel3["background"]="#202124"
                angel3["foreground"]="#BB5699"
            def darkfg1(event):
                angel3["background"]="#343538"
                angel3["foreground"]="#BB5699"
            def darkbg2(event):
                angel4["background"]="#202124"
                angel4["foreground"]="#BB5699"
            def darkfg2(event):
                angel4["background"]="#343538"
                angel4["foreground"]="#BB5699"
            def darkbg3(event):
                angel5["background"]="#202124"
                angel5["foreground"]="#BB5699"
            def darkfg3(event):
                angel5["background"]="#343538"
                angel5["foreground"]="#BB5699"
            def darkbg4(event):
                angel66["background"]="#202124"
                angel66["foreground"]="#BB5699"
            def darkfg4(event):
                angel66["background"]="#343538"
                angel66["foreground"]="#BB5699"
        class angel_lib():
                    def devilname():
                        global angel14,angel15,angel16,devilcount,deviltime,devilage,demoncount,devil_limet_1
                        if devil_limet_1==0:
                            devilcount=0
                            deviltime=0
                            devilage=0
                            demoncount=0
                            def devildestroy2():
                                global devilcount,deviltime,devilage,demoncount
                                if demoncount>1:
                                    if devilcount>0:
                                        angel14.destroy()
                            def devildestroy():
                                global angel14,angel15,angel16,devilcount,deviltime,devilage,devil_limet_1
                                devil_full_cover()
                                angel10.destroy(),angel11.destroy(),angel12.destroy(),angel13.destroy(),angelentry.destroy()
                                if devilcount>0:
                                    angel14.destroy()
                                    devilcount=0
                                if deviltime>0:
                                    angel15.destroy()
                                    deviltime=0
                                if devilage>0:
                                    angel16.destroy()
                                    devilage=0
                                main_frame.after(5,devil_101)
                                devil_limet_1-=1
                            def devilget():
                                global angel14,angel15,angel16,devilcount,deviltime,devilage,demoncount
                                get=angelentry.get()
                                getcount=len(get)
                                if get.isalpha():
                                    if getcount<20:
                                        devilcount+=1
                                        demoncount+=1
                                        devildestroy2()
                                        angel14=Label(main_frame,text="NAME HAS CHANGED SUCCESSFULLY",bg="#cf3467",bd=0,fg="white",font=Font(size=14,family="Freestyle Script"))
                                        angel14.place(x=570,y=480)
                                        file4=open("name.txt","w")
                                        devilfile4=file4.write(get)
                                        file4.close()
                                        dark_lib_2()
                                        devil_lib_angel()
                                    else:
                                        if devilage>0:
                                            angel16.destroy()
                                            devilage=0
                                        angel16=Label(main_frame,text="        ERROR IN CHANGING NAME         ",bg="#cf3467",bd=0,fg="white",font=Font(size=14,family="Freestyle Script"))
                                        angel16.place(x=570,y=480)
                                        devilage+=1
                                        demoncount+=1
                                else:
                                    if deviltime>0:
                                        angel15.destroy()
                                        deviltime=0
                                    angel15=Label(main_frame,text="        ERROR IN CHANGING NAME         ",bg="#cf3467",bd=0,fg="white",font=Font(size=14,family="Freestyle Script"))
                                    angel15.place(x=570,y=480)
                                    deviltime+=1
                            angel10=Label(main_frame,image=devil_image_2,bd=0)
                            angel10.bind("<Enter>",dark_lib_1)
                            angel10.place(x=450,y=250)
                            angel11=Button(main_frame,text="x",activebackground="#343538",bg="#343538",bd=0,fg="#BB5699",font=Font(size=15),command=devildestroy)
                            angel11.place(x=900,y=250)
                            angel12=Label(main_frame,text="ENTER YOUR NEW NAME...",bg="#343538",bd=0,fg="#BB5699",font=Font(size=14,family="Freestyle Script",weight="bold"))
                            angel12.place(x=600,y=340)
                            angelentry=Entry(main_frame,bg="#BB5699",bd=0,fg="white",selectbackground="#BB5699",selectforeground="white",font=Font(size=15))
                            angelentry.place(x=580,y=370)
                            angel13=Button(main_frame,text="ENTER",activebackground="#343538",bg="#343538",activeforeground="#BB5699",bd=0,fg="#BB5699",font=Font(size=15,family="Freestyle Script",weight="bold"),command=devilget)
                            angel13.bind('<Return>',devilget)
                            angel13.place(x=660,y=440)
                            devil_limet_1+=1
                    def devilemail():
                        global angel14,angel15,angel16,devilcount,deviltime,devilage,demoncount,devil_limet_2
                        if devil_limet_2==0:
                            devilcount=0
                            deviltime=0
                            devilage=0
                            demoncount=0
                            def devildestroy2():
                                global devilcount,deviltime,devilage,demoncount
                                if demoncount>1:
                                    if devilcount>0:
                                        angel14.destroy()
                            def devildestroy():
                                global angel14,angel15,angel16,devilcount,deviltime,devilage,devil_limet_2
                                devil_full_cover()
                                angel10.destroy(),angel11.destroy(),angel12.destroy(),angel13.destroy(),angelentry.destroy()
                                if devilcount>0:
                                    angel14.destroy()
                                    devilcount=0
                                if deviltime>0:
                                    angel15.destroy()
                                    deviltime=0
                                if devilage>0:
                                    angel16.destroy()
                                    devilage=0
                                main_frame.after(5,devil_101)
                                devil_limet_2-=1
                            def devilget():
                                global angel14,angel15,angel16,devilcount,deviltime,devilage,demoncount
                                get=angelentry.get()
                                getcount=len(get)
                                try:
                                    aa=validate_email(get,verify=True)
                                except:
                                    aa=True
                                if aa==True:
                                    if getcount<28:
                                        devilcount+=1
                                        demoncount+=1
                                        devildestroy2()
                                        angel14=Label(main_frame,text="EMAIL HAS CHANGED SUCCESSFULLY",bg="#cf3467",bd=0,fg="white",font=Font(size=14,family="Freestyle Script"))
                                        angel14.place(x=570,y=480)
                                        file4=open("email.txt","w")
                                        devilfile4=file4.write(get)
                                        file4.close()
                                        dark_lib_2()
                                        devil_lib_angel()
                                    else:
                                        if devilage>0:
                                            angel16.destroy()
                                            devilage=0
                                        angel16=Label(main_frame,text="        ERROR IN CHANGING EMAIL         ",bg="#cf3467",bd=0,fg="white",font=Font(size=14,family="Freestyle Script"))
                                        angel16.place(x=570,y=480)
                                        devilage+=1
                                else:
                                    if deviltime>0:
                                        angel15.destroy()
                                        deviltime=0
                                    angel15=Label(main_frame,text="        ERROR IN CHANGING EMAIL         ",bg="#cf3467",bd=0,fg="white",font=Font(size=14,family="Freestyle Script"))
                                    angel15.place(x=570,y=480)
                                    deviltime+=1
                            angel10=Label(main_frame,image=devil_image_2,bd=0)
                            angel10.bind("<Enter>",dark_lib_1)
                            angel10.place(x=450,y=250)
                            angel11=Button(main_frame,text="x",activebackground="#343538",bg="#343538",bd=0,fg="#BB5699",font=Font(size=15),command=devildestroy)
                            angel11.place(x=900,y=250)
                            angel12=Label(main_frame,text="ENTER YOUR NEW EMAIL...",bg="#343538",bd=0,fg="#BB5699",font=Font(size=14,family="Freestyle Script",weight="bold"))
                            angel12.place(x=600,y=340)
                            angelentry=Entry(main_frame,bg="#BB5699",bd=0,fg="white",selectbackground="#BB5699",selectforeground="white",font=Font(size=15))
                            angelentry.place(x=580,y=370)
                            angel13=Button(main_frame,text="ENTER",activebackground="#343538",bg="#343538",activeforeground="#BB5699",bd=0,fg="#BB5699",font=Font(size=15,family="Freestyle Script",weight="bold"),command=devilget)
                            angel13.bind('<Return>',devilget)
                            angel13.place(x=660,y=440)
                            devil_limet_2+=1
                    def devilphoto():
                        global devil_limet_3
                        if devil_limet_3==0:
                            def darklink(darkdemon):
                                global darkangel2,angel9         
                                filenew=open("link.txt","w")
                                devilfilenew=filenew.write(darkdemon)
                                filenew.close()
                                dark_lib_2()
                                devil_lib_angel()
                            class darkside():
                                def angelink1():
                                    darklink(darkdemon=r"image.app\db image\931044ce15604e0302b36b64cdb5a551-modified(1).png")
                                def angelink2():
                                    darklink(darkdemon=r"image.app\db image\anime-boy-whatsapp-dp (1)-modified.png")
                                def angelink3():
                                    darklink(darkdemon=r"image.app\db image\anime-boy-whatsapp-dp (5)-modified.png")
                                def angelink4():
                                    darklink(darkdemon=r"image.app\db image\anime-boy-whatsapp-dp (6)-modified.png")
                                def angelink5():
                                    darklink(darkdemon=r"image.app\db image\anime-boy-whatsapp-dp (10)-modified.png")
                                def angelink6():
                                    darklink(darkdemon=r"image.app\db image\Anime-Girl-WhatsApp-DP-Pictures-modified.png")
                                def angelink7():
                                    darklink(darkdemon=r"image.app\db image\Anime-WhatsApp-DP-23-modified.png")
                                def angelink8():
                                    darklink(darkdemon=r"image.app\db image\Anime-WhatsApp-DP-for-Boys-13-modified.png")
                                def angelink9():
                                    darklink(darkdemon=r"image.app\db image\Anim-Whatsapp-Dp-Images-pictures-photo-free-hd-modified.png")
                                def angelink10():
                                    darklink(darkdemon=r"image.app\db image\cartoon-boy-images-16-1-modified.png")
                                def angelink11():
                                    darklink(darkdemon=r"image.app\db image\cartoon-boy-images-18-modified.png")
                                def angelink12():
                                    darklink(darkdemon=r"image.app\db image\cartoon-girl-images-4-modified.png")
                                def angelink13():
                                    darklink(darkdemon=r"image.app\db image\images-modified.png")
                            def devildestroy():
                                global devil_limet_3
                                devil_full_cover()
                                angel10.destroy(),angel11.destroy(),angel12.destroy(),angel13.destroy(),angel14.destroy(),angel15.destroy(),angel16.destroy(),angel17.destroy()
                                angel18.destroy(),angel19.destroy(),angel20.destroy(),angel21.destroy(),angel22.destroy(),angel23.destroy(),angel24.destroy(),angel25.destroy()
                                main_frame.after(5,devil_101)
                                devil_limet_3-=1
                            angel10=Label(main_frame,image=devil_image_2,bd=0)
                            angel10.bind("<Enter>",dark_lib_1)
                            angel10.place(x=450,y=250)
                            angel11=Button(main_frame,text="x",activebackground="#343538",bg="#343538",bd=0,fg="#BB5699",font=Font(size=15),command=devildestroy)
                            angel11.place(x=900,y=250)
                            angel25=Label(main_frame,text="SELECT YOU IMAGE...",bg="#343538",bd=0,fg="#BB5699",font=Font(size=14,family="Freestyle Script",weight="bold"))
                            angel25.place(x=610,y=260)   
                            angel12=Button(main_frame,image=darkicon_1,activebackground="#343538",bg="#343538",bd=0,fg="white",command=darkside.angelink1)
                            angel12.place(x=470,y=290)
                            angel13=Button(main_frame,image=darkicon_2,activebackground="#343538",bg="#343538",bd=0,fg="white",command=darkside.angelink2)
                            angel13.place(x=560,y=290)
                            angel14=Button(main_frame,image=darkicon_3,activebackground="#343538",bg="#343538",bd=0,fg="white",command=darkside.angelink3)
                            angel14.place(x=650,y=290)
                            angel15=Button(main_frame,image=darkicon_4,activebackground="#343538",bg="#343538",bd=0,fg="white",command=darkside.angelink4)
                            angel15.place(x=740,y=290)
                            angel16=Button(main_frame,image=darkicon_5,activebackground="#343538",bg="#343538",bd=0,fg="white",command=darkside.angelink5)
                            angel16.place(x=830,y=290)
                            angel17=Button(main_frame,image=darkicon_6,activebackground="#343538",bg="#343538",bd=0,fg="white",command=darkside.angelink6)
                            angel17.place(x=470,y=370)
                            angel18=Button(main_frame,image=darkicon_7,activebackground="#343538",bg="#343538",bd=0,fg="white",command=darkside.angelink7)
                            angel18.place(x=560,y=370)
                            angel19=Button(main_frame,image=darkicon_8,activebackground="#343538",bg="#343538",bd=0,fg="white",command=darkside.angelink8)
                            angel19.place(x=650,y=370)
                            angel20=Button(main_frame,image=darkicon_9,activebackground="#343538",bg="#343538",bd=0,fg="white",command=darkside.angelink9)
                            angel20.place(x=740,y=370)
                            angel21=Button(main_frame,image=darkicon_10,activebackground="#343538",bg="#343538",bd=0,fg="white",command=darkside.angelink10)
                            angel21.place(x=830,y=370)
                            angel22=Button(main_frame,image=darkicon_11,activebackground="#343538",bg="#343538",bd=0,fg="white",command=darkside.angelink11)
                            angel22.place(x=470,y=450)
                            angel23=Button(main_frame,image=darkicon_12,activebackground="#343538",bg="#343538",bd=0,fg="white",command=darkside.angelink12)
                            angel23.place(x=560,y=450)
                            angel24=Button(main_frame,image=darkicon_13,activebackground="#343538",bg="#343538",bd=0,fg="white",command=darkside.angelink13)
                            angel24.place(x=650,y=450)
                            devil_limet_3+=1
                
        file=open("name.txt","r")
        devilfile=file.read()
        file2=open("email.txt","r")
        devilfile2=file2.read()
        
        angel3=Button(main_frame,text="IMAGE",bg="#343538",fg="#BB5699",command=devil_uplode,activebackground="#343538",activeforeground="#BB5699",bd=0,width=60,height=3,font=Font(size=10,family="Freestyle Script",weight="bold"))
        angel3.bind("<Enter>",devilbg.darkbg1)
        angel3.bind("<Leave>",devilbg.darkfg1)
        angel3.place(x=0,y=230)
        angel4=Button(main_frame,text="VIDEOS",bg="#343538",fg="#BB5699",command=devil_uplode,activebackground="#343538",activeforeground="#BB5699",bd=0,width=60,height=3,font=Font(size=10,family="Freestyle Script",weight="bold"))
        angel4.bind("<Enter>",devilbg.darkbg2)
        angel4.bind("<Leave>",devilbg.darkfg2)
        angel4.place(x=0,y=280)
        angel5=Button(main_frame,text="WEB CAMERA",bg="#343538",fg="#BB5699",command=devil_1_3,activebackground="#343538",activeforeground="#BB5699",bd=0,width=60,height=3,font=Font(size=10,family="Freestyle Script",weight="bold"))
        angel5.bind("<Enter>",devilbg.darkbg3)
        angel5.bind("<Leave>",devilbg.darkfg3)
        angel5.place(x=0,y=330) 
        angel66=Button(main_frame,text="EXIT",bg="#343538",fg="#BB5699",command=devil_1_4,activebackground="#343538",activeforeground="#BB5699",bd=0,width=60,height=3,font=Font(size=10,family="Freestyle Script",weight="bold"))
        angel66.bind("<Enter>",devilbg.darkbg4)
        angel66.bind("<Leave>",devilbg.darkfg4)
        angel66.place(x=0,y=380)
        angel7=Button(main_frame,text=devilfile,bg="#343538",fg="#BB5699",activebackground="#343538",height=0,bd=0,font=Font(size=18,family="Freestyle Script",weight="bold"),command=angel_lib.devilname)
        angel7.place(x=140,y=81)
        angel8=Button(main_frame,text=devilfile2,bg="#343538",activebackground="#343538",fg="#BB5699",height=0,bd=0,font=Font(size=18,family="Freestyle Script",weight="bold"),comman=angel_lib.devilemail)
        angel8.place(x=140,y=115)
        angel9=Button(main_frame,image=darkness,activebackground="#343538",bg="#343538",fg="#BB5699",bd=0,command=angel_lib.devilphoto)
        angel9.place(x=2,y=50)
    angel=Button(main_frame,text="|||",bg=devil_col,fg="#BB5699",bd=0,font=Font(size=19))
    angel.bind("<Enter>",dark)
    angel.place(x=0,y=0)
def devil_start():
    devil_lib_angel()
devil_start()
main_frame.mainloop()

