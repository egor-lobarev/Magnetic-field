# -*- coding: utf8 -*-
from tkinter import *
from tkinter import messagebox
from math import *
from sys import exit
import time
col=["black","blue","red","orange","green"]
numcol=0
okno=Tk()
okno.geometry("1020x720")
holst=Canvas(okno,width=1020,height=720,bg="white")
holst.pack()
#im=PhotoImage(file='fon.png')
def help():
   help1="1) Нажмите 'Esc', чтобы выйти из пункта меню.\n\n2) Чтобы войти в пункт меню, наведите курсор на нужный пункт\nи нажмите на левую клавишу мыши.\n\n"
   help2="3) Чтобы постваить проводник наведите курсор на поле и нажмите левую или правую клавишу мыши.\n\n4) После установки всех проводников, нажмите 'Enter', чтобы  запустить моделирование."
   help3="\n\n5) Чтобы переместить прводник, наведите курсор на нужный проводник, нажмите и удерживайте левую клавишу мыши, передвиньте проводник движением мыши в нужное место и отпустите левую клавишу мыши."
   help4="\n\n6) Чтобы настроить силу тока в проводнике, наведите курсор на проводник, нажмите левую клавишу мыши, и вращайте колёсико мыши, чтобы увеличить или уменьшить силу тока. \n\n 7) Чтобы удалить проводник, выберете его, нажав левую клавишу мыши, и нажмите клавишу 'Delete' наклавиатуре."
   help5="\n\n8) в программе есть возможность сохренения постороения полей - просто ничего не стирайте, измените проводники и начните построение ещё раз"
   messagebox.showinfo("Помощь",help1+help2+help3+help4+help5)
helpbutton=Button(holst,text=" ? ",command=help,font="Colibry 16")
helpbutton.place(x=0,y=0,anchor="nw")
#возможные_варианты_постановки_проводников
a_m=[[[400,400,10],[620,400,-10]],[[600,200,10],[400,400,10],[700,400,10]],[[400,400,10],[700,400,10]]]
def ex():
   okno.destroy()
   exit()
def back(ev):
   if (ev.x>970)and(ev.x<1020)and(ev.y>1)and(ev.y<50):
        m(ev)
def no(e):
    l=1
def klik(ev):
        ky=ev.y
        if (ky>55)and(ky<125):
          usl()
        elif (ky>145)and(ky<215):
          mod()
        elif (ky>235)and(ky<305):
          z()
        elif (ky>325)and(ky<395):
           ex()
#меню           
def m(e):
    okno.bind('<Escape>',no),okno.bind('<space>',no), holst.bind('<Button-1>',no), holst.bind('<Button-3>',no)
    holst.tag_bind("menu",'<Button-1>',klik)
    holst.delete("all")
    #holst.create_image(0,0,image=im,anchor="nw")
    holst.create_oval(635,55,695,125,fill="lightgreen",outline="lightgreen",tag="menu")
    holst.create_oval(325,55,385,125,fill="lightgreen",outline="lightgreen",tag="menu")
    holst.create_oval(635,145,695,215,fill="lightgreen",outline="lightgreen",tag="menu")
    holst.create_oval(325,145,385,215,fill="lightgreen",outline="lightgreen",tag="menu")
    holst.create_oval(635,235,695,305,fill="lightgreen",outline="lightgreen",tag="menu")
    holst.create_oval(325,235,385,305,fill="lightgreen",outline="lightgreen",tag="menu")
    holst.create_oval(635,325,695,395,fill="red",outline="red",tag="menu")
    holst.create_oval(325,325,385,395,fill="red",outline="red",tag="menu")
    holst.create_polygon(355,55,665,55,665,125,355,125,fill="lightgreen",outline="lightgreen",tag="menu")
    holst.create_polygon(355,145,665,145,665,215,355,215,fill="lightgreen",outline="lightgreen",tag="menu")
    holst.create_polygon(355,235,665,235,665,305,355,305,fill="lightgreen",outline="lightgreen",tag="menu")
    holst.create_polygon(355,325,665,325,665,395,355,395,fill="red",outline="red",tag="menu")
    holst.create_text(505,90,text="Условие", font="Colibry 33",tag="menu")
    holst.create_text(505,360,text="Выход", font="Colibry 33",tag="menu")
    holst.create_text(510,180,text="Моделирование", font="Colibry 28",tag="menu")
    holst.create_text(500,270,text="Заставка", font="Colibry 33",tag="menu")
    holst.create_text(500,700,text="Для входа в пункт меню, наведите курсор на пункт и нажмите левую кнопку мыши", font="Tahoma 16", fill="grey")
    okno.update()
#заствка   
def z():
        okno.bind('<space>',m), holst.tag_bind('menu','<Button-1>',no)
        holst.delete("all")
        #holst.create_image(0,0,image=im,anchor="nw")
        holst.create_text(500,200,text="Лобарев Георгий Романович", font="Colibry 33")
        holst.create_text(500,250,text="10Г, 2019г-2020г", font="Colibry 33")
        holst.create_text(500,400,text="Тема: моделирование линий магнитной индукции проводников", font="Colibry 22")
        holst.create_text(500,650,text="Чтобы пройти в меню, нажмите 'ПРОБЕЛ'", font="Tahoma 18",fill="grey")     
        holst.update()
#условие
def usl():
    okno.bind('<Escape>',m), holst.tag_bind('menu','<Button-1>',no)
    holst.delete("all")
    okno.bind('<Button-1>',back)
    #holst.create_image(0,0,image=im,anchor="nw")
    holst.create_polygon(970,50,1019,50,1019,1,970,1,fill="red",outline="black")
    holst.create_line(970,1,1019,50,width=2)
    holst.create_line(1019,1,970,50,width=2)
    holst.create_text(500,220,text="Условие:",font="colibry 30")
    holst.create_text(55,300,text="Составить программу, моделирующую построение линий магнитной \nиндукции поля, создаваемого тремя и более проводниками с током, \nрасположенными параллельно.",font="Colibry 20",anchor="w")
#моделирование
def mod():
    global act, yprint, check, mzar, numb, check2, numcol, n_a_m, load
    load=None
    n_a_m=-1
    check=1
    check2=1
    holst.delete("all")
    act=0
    mzar=[]
    vec=[]
    numb=[]
    holst.create_oval(50,5,70,25,fill="blue",outline='black')
    holst.create_text(80,15,text="=",font="Colibry 16")
    holst.create_oval(90,5,110,25,width=2)
    holst.create_oval(99,14,101,16,width=3)
    holst.create_oval(50,30,70,50,fill="red",outline='black')
    holst.create_text(80,40,text="=",font="Colibry 16")
    holst.create_oval(90,30,110,50,width=2)
    holst.create_line(96,36,105,45,width=2)
    holst.create_line(105,36,96,45,width=2)
    holst.create_rectangle(48,2,115,53,width=2)
    for i in range(130,1130,25):
       holst.create_line(i,0,i,720,fill="lightgrey")
    for i in range(0,720,25):
       holst.create_line(130,i,1020,i,fill="lightgrey")
    holst.create_line(130,0,130,715,width=2,arrow=LAST)
    holst.create_line(130,5,1010,5,width=2,arrow=LAST)
    holst.create_text(1005,20,text="X",font="Colibri 12")
    holst.create_text(140,700,text="Y",font="Colibri 12")
    holst.create_text(140,15,text="0",font="Colibri 12")
    for i in range(180, 1000, 50):
     holst.create_line(i,5,i,14,width=2)
    holst.create_text(190,15,text="50",font="Colibri 12")
    for i in range (50, 700, 50):
     holst.create_line(130,i,136,i,width=2)
    holst.create_text(140,60,text="50",font="Colibri 12")
    txt=holst.create_text(540,670,text="Нажмите Enter, чтобы перейти к моделированию",font="Tahoma 14")
    yprint=holst.create_text(0,0,text="")
    def m_(e):
        m(e)
        obn.destroy()
        obn3.destroy()
        auto.destroy()
        okno.bind('<Button-3>',no)
    def choose(e):
        def delete(e):
           global act
           if len(mzar)>1 and act!=-1:
              holst.delete(mzar[act][0])
              holst.delete(numb[act][1])
              holst.delete(numb[act][0])
              mzar.pop(act)
              holst.itemconfig(yprint,text="")
              numb.pop(act)
              for i in range(len(numb)):
                 holst.itemconfig(numb[i][1],text="I"+str(i+1)+"="+str(mzar[i][3]))
                 holst.itemconfig(numb[i][0],text=str(i+1))
                 holst.coords(numb[i][1],5,(i+1)*15+250)
              act=-1
              holst.update()
        okno.bind('<Delete>',delete)
        global yprint,act
        if mzar[act][3]>0:
               holst.itemconfig(mzar[act][0],fill="red")
        else:
                holst.itemconfig(mzar[act][0],fill="blue")
        for i in range(len(mzar)):
           if (e.x-mzar[i][1])**2+(e.y-mzar[i][2])**2<15**2:
              if mzar[i][3]<0:
                 holst.itemconfig(mzar[i][0],fill="#003891")
              else:
                  holst.itemconfig(mzar[i][0],fill="#800101")
              act=i
              holst.coords(yprint,mzar[act][1],mzar[act][2]+40)
              holst.itemconfig(yprint,text="y="+str(mzar[act][2])+"\nx="+str(mzar[act][1]-130)+"\nI="+str(mzar[act][3]),font="Colibri 12")
        def zarch(e):
            if fabs(mzar[act][3]+e.delta/10)>60:
                i=1
            else:
                mzar[act][3]+=int(e.delta/12)
            if mzar[act][3]==0:
                mzar[act][3]+=int(e.delta/12)
            if mzar[act][3]>0:
                holst.itemconfig(mzar[act][0],fill="#800101")
            else:
                holst.itemconfig(mzar[act][0],fill="#003891")
            holst.itemconfig(yprint,text="y="+str(mzar[act][2])+"\nx="+str(mzar[act][1]-130)+"\nI="+str(mzar[act][3]))
            holst.itemconfig(numb[act][1],text="I"+str(act+1)+"="+str(mzar[act][3]))
        okno.bind('<MouseWheel>',zarch)
    def obnul():
        global mzar,vec,numb, act, check, load, numcol
        if load is not None:
            holst.delete(load)
        numcol=0
        check=0
        holst.itemconfig(yprint,text="")
        act=-1
        holst.delete("vec")
        holst.delete("ovl")
        holst.delete("numb")
        numb=[]
        mzar=[]
        vec=[]
        pusk()
    def obnpole():
        global vec, check, numcol
        check=0
        numcol=0
        act=-1
        holst.delete("vec")
        vec=[]
        pusk()
    def postr():
     global k,check,check2, load, numcol, load
     if check == 1:
        colour=col[numcol-(numcol//5)*5]
        for f in range(len(mzar)):
            n=[]
            for k in range(1,int(abs(mzar[f][3]/10))+2):
                n.append(-100+(200/(abs(mzar[f][3]/10))*k))
            for h in range(len(n)):
                k1,Lo,count=0,0,0
                k1=10
                k=10
                xn=mzar[f][1]+n[h]
                yn=mzar[f][2]
                x=xn
                y=yn
                lmin1=sqrt((xn-mzar[0][1])**2+(yn-mzar[0][2])**2)
                for i in range(1,len(mzar)):
                       if sqrt((xn-mzar[i][1])**2+(yn-mzar[i][2])**2)<lmin1:
                          lmin1=sqrt((xn-mzar[i][1])**2+(yn-mzar[i][2])**2)
                if lmin1>=40:
                          load=holst.create_text(5,690,text="Построение...",font="Colibry 15",anchor="w", fill="red")
                          while (Lo>30 or count<500) and check == 1:
                            lmin=[]
                            count+=1
                            x1=x
                            y1=y
                            for i in range(len(mzar)):
                              L=sqrt((x-mzar[i][1])**2+(y-mzar[i][2])**2)
                              F=k*(mzar[i][3]/L**2)
                              x=x+((mzar[i][2]-y)/L)*F
                              y=y+((x-mzar[i][1])/L)*F
                              lmin.append(L)
                            Lo=sqrt((x-xn)**2+(y-yn)**2)
                            if min(lmin)>80:
                                k=min(lmin)*4+k1
                            elif min(lmin)<80:
                                k=min(lmin)/4+k1
                            if x<1020 and x>130 and y>0 and y<720:
                             if k>70:
                               if count%350==0:
                                    holst.update()
                                    vec.append(holst.create_line(x1,y1,x,y,arrow=LAST,tag="vec",fill=colour))
                               else:
                                   vec.append(holst.create_line(x1,y1,x,y,tag="vec",fill=colour))
                             else:
                               if count%500==0:
                                    holst.update()
                                    vec.append(holst.create_line(x1,y1,x,y,arrow=LAST,tag="vec",fill=colour))
                               else:
                                   vec.append(holst.create_line(x1,y1,x,y,tag="vec",fill=colour))                 
                if check==1: vec.append(holst.create_line(x,y,xn,yn,tag="vec",fill=colour));holst.delete(load)
        numcol+=1
        pusk()
    def klick1(e):
       dm = -1
       for i in range(0,len(mzar)):
           if dm == -1:
               dm = sqrt((e.x-mzar[i][1])**2+(e.y-mzar[i][2])**2)
           elif sqrt((e.x-mzar[i][1])**2+(e.y-mzar[i][2])**2)<dm:
              dm=sqrt((e.x-mzar[i][1])**2+(e.y-mzar[i][2])**2)
       if 152<e.x<995 and 14<e.y<650 and len(mzar)<35 and (dm>50 or dm == -1): 
         mzar.append([holst.create_oval(e.x-10,e.y-10,e.x+10,e.y+10,fill="red",tag="ovl"),e.x,e.y,10])
         numb.append([holst.create_text(e.x,e.y,text=str(len(mzar)),tag="ovl",fill="white"),holst.create_text(5,len(mzar)*15+250,text="I"+str(len(mzar))+"="+str(mzar[-1][3]),font="Courier 14",anchor="w",tag="numb")])
    def klick2(e):
       dm = -1
       for i in range(0,len(mzar)):
           if dm == -1:
               dm = sqrt((e.x-mzar[i][1])**2+(e.y-mzar[i][2])**2)
           elif sqrt((e.x-mzar[i][1])**2+(e.y-mzar[i][2])**2)<dm:
              dm=sqrt((e.x-mzar[i][1])**2+(e.y-mzar[i][2])**2)
       if 152<e.x<995 and 14<e.y<650 and len(mzar)<35 and (dm>50 or dm == -1):
         mzar.append([holst.create_oval(e.x-10,e.y-10,e.x+10,e.y+10,fill="blue",tag="ovl"),e.x,e.y,-10])
         numb.append([holst.create_text(e.x,e.y,text=str(len(mzar)),tag="ovl",fill="white"),holst.create_text(5,len(mzar)*15+250,text="I"+str(len(mzar))+"="+str(mzar[-1][3]),font="Courier 14",anchor="w",tag="numb")])
    def pusk2(e):
        global check
        if len(mzar)>0:
           check=1
           holst.tag_bind('ovl','<B1-Motion>',no)
           okno.bind('<MouseWheel>',no)
           okno.bind('<Return>',no)
           holst.tag_bind('ovl','<Button-1>',no)
           holst.bind('<Button-1>', no)
           holst.bind('<Button-3>', no)
           holst.itemconfig(txt,text="")
           holst.itemconfig(yprint,text="")
           if mzar[act][3]>0:
                   holst.itemconfig(mzar[act][0],fill="red")
           else:
                   holst.itemconfig(mzar[act][0],fill="blue")
           postr()
        else:
             holst.itemconfig(txt,text="Нет проводников",fill="red")
             holst.update()
             time.sleep(1)
             holst.itemconfig(txt,text="Нажмите Enter, чтобы перейти к моделированию",fill="black")   
           
    def motion(e):
       if 152<e.x<995 and 14<e.y<650:
           mzar[act][1]=e.x
           mzar[act][2]=e.y
           holst.itemconfig(yprint,text="y="+str(mzar[act][2])+"\nx="+str(mzar[act][1]-130)+"\nI="+str(mzar[act][3]))
           holst.coords(mzar[act][0],e.x-10,e.y-10,e.x+10,e.y+10)
           holst.coords(yprint,e.x,e.y+40)
           holst.coords(numb[act][0],e.x,e.y)
           holst.update()
    def pusk():
       global check
       holst.itemconfig(txt,text="Нажмите Enter, чтобы перейти к моделированию",fill="black")
       okno.bind('<Escape>',m_), holst.bind('<Button-3>',klick2), okno.bind('<Return>',pusk2), holst.tag_bind("menu",'<Button-1>',no)
       holst.bind('<Button-1>',klick1)
       holst.tag_bind('ovl','<Button-1>',choose)
       holst.tag_bind('ovl','<B1-Motion>',motion)
       okno.bind('<Return>',pusk2)
    def auto():
       global n_a_m
       obnul()
       if n_a_m+2>len(a_m):
          n_a_m=0
       else:
          n_a_m+=1 
       for j in range(len(a_m[n_a_m])):
            ex=a_m[n_a_m][j][0]
            ey=a_m[n_a_m][j][1]
            q=a_m[n_a_m][j][2]
            if q>0:
               clr="red"
            else:
               clr="blue"
            mzar.append([holst.create_oval(ex-10,ey-10,ex+10,ey+10,fill=clr,tag="ovl"),ex,ey,q])
            numb.append([holst.create_text(ex,ey,text=str(len(mzar)),tag="ovl",fill="white"),holst.create_text(5,len(mzar)*15+250,text="I"+str(len(mzar))+"="+str(mzar[-1][3]),font="Courier 14",anchor="w",tag="numb")])
    obn=Button(holst,text="Сброс",command=obnul,font="Colibry 24",background="#c20827",foreground="white")
    obn.place(x=2,y=85,anchor="w")
    obn3=Button(holst,text="Удалить\nполе",command=obnpole,font="Colibry 14",width=10,background="lightgreen",foreground="white")
    obn3.place(x=2,y=150,anchor="w")
    auto=Button(holst, text="Поставить\nзаряды\nавтоматически", command=auto, font="Colibry 12", background="green",foreground="white")
    auto.place(x=2,y=218,anchor="w")
    pusk()

z()
okno.mainloop()
