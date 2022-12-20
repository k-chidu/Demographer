from tkinter import *
from tkinter import ttk
import values
import time
import mysql.connector
from datetime import datetime

#window
#=====================================================================
'''
                        ##///Overview:///##
=====================================================================
======================================================================
                                windows:-

1. root - Main window (Gets value of state name, year and population)
2. root3 - Output window (Displayes calculated values inputted by user)
3. root_ - Database button (Login page)
4. root1 - Saved database (user selects the state to view database)
5. root2 - Shows database values of selected Indian_states.
======================================================================
======================================================================

============================================================================
(root):
1. no: of buttons - 4           commands=readme_,dbs,submit,clr
2. no: of Labels - 8 
3. no: of combobox - 3          variables= stringvar(var,var_),intvar(var1)
=============================================================================
(root3):
1. no: of labelframes - 3
2. no: of buttons - 1           command=win_exit.close_root3
3. no: of Labels - 20
4. no: of canvas - 3
==============================================================================
(root_):
1. no: of buttons - 1           command=sub_check
2. no: of Labels - 4
3. no: of entry - 2             variable= stringvar(var3,var4)
==============================================================================
(root1):
1. no: of Label - 1
2. no: of combobox - 1          variable = stringvar(var2)
3. no: of button - 1            command= go_
==============================================================================
(root2)
1. no: of Label - 2
2. no: of button - 2            commands=win_exit.close_root2,graph_.line_graph
3. no: of treeview - 1
===============================================================================
===============================================================================
'''
#=======================================================================

#defining tkinter window
#=============================
values.check()
'''
def start_animation(master,width,height):
        i,j=1,1
        ratio=width/height
        while i< width and j<height:
                if i==width:
                        j=j+10
                elif j==height:
                        i=i+10
                else:
                        i=i+10
                        j=j+10
                master.geometry('{}x{}'.format(i,j))

'''             


root=Tk()
root.title("Demographer")
root.geometry('500x400')
#start_animation(root,500,400)
root.iconbitmap(r"icons\stats.ico")

#Connecting sql server
#============================

conn=mysql.connector.connect(
        host='localhost',
        user='root',
        passwd=values.pass_,
        database='Indian_states'
        )
c=conn.cursor()

#=============================

#tkinter variables  var,var1
#=======================================================

var=StringVar(root)
var.set('-states-')

var1=IntVar(root)
var1.set(2021)

var_=StringVar(root)
var_.set('Total_Population')

#=========================================================

#Gets the present year from os
#========================================================

now=datetime.now()
global present_year
present_year=now.strftime('%Y')

#=======================================================
#defining values for combobox Indian_states,yrs
#======================================================

c.execute("SHOW TABLES")
n=c.fetchall()
Indian_states=[]
for i in range(len(n)):
        Indian_states.append(n[i][0].capitalize())
yrs=[]
for i in range(2021,2071):
        yrs.append(i)
Indian_states.sort()

popu_options=['Total_Population','Male_Population','Female_Population']
#==============================================================================

# funtions for Buttons and other purposes
#=============================================================================


def clr():#Clears the values in root window (sets to default)


        var.set('-Indian_states-')
        var1.set(2021)
        var_.set('Total_Population')
        error.config(text='')

def submit():#Executes the values entered in root window

        x=var.get()
        y=var1.get()
        z=var_.get()
        
        if x=='-Indian_states-':

                error.config(text='Please select a valid input!!')
                error.place(relx=0.31,rely=0.6)
    
        else:
                error.config(text='')

        output()       

def dbs():#database login function
        
        def sub_check():
                if var3.get()=='admin' and var4.get()=='admin':
                        error2.config(text='')
                        error2.place(relx=0.4,rely=0.65)
                        dbs_entry()
                else:
                        error2.config(text='Wrong Credentials!!')
                        error2.place(relx=0.4,rely=0.65)
        global root_
        root_=Tk()
        root_.geometry('300x200')
        root_.title('Login')
        root_.iconbitmap(r'icons\login.ico')

        global var3
        global var4

        var3=StringVar(root_)
        var4=StringVar(root_)
        
        head=Label(root_,text='Login',fg='red',
                        font=('ALGERIAN',14,'bold','underline')).place(relx=0.4,rely=0.01)

        user_name=Label(root_,text='Username:',
                        font=('Courier New',14,'bold')).place(relx=0.02,rely=0.3)

        password=Label(root_,text='Password:',
                        font=('Courier New',14,'bold')).place(relx=0.02,rely=0.5)

        user_entry=Entry(root_,textvariable=var3,
                        font=('Courier New',12)).place(relx=0.4,rely=0.3,height=25,width=150)
        values.pass_entry=Entry(root_,show='*',textvariable=var4,
                        font=('Courier New',12)).place(relx=0.4,rely=0.5,height=25,width=150)

        error2=Label(root_,text='Wrong Credentials!!',fg='red')

        Sub=Button(root_,text='Submit',
                        bg='#BDBDBD',fg='black',
                        font=('Courier New',12,'bold'),command=sub_check).place(relx=0.4,rely=0.8)

        root_.mainloop()
       
def dbs_entry():#selecting state for viewing database 
        global root1

        root_.destroy()
        
        root1=Tk()
        root1.geometry('300x200')
        root1.title('Select State')
        root1.iconbitmap(r'icons\stats.ico')

        
        head=Label(root1,text='DATABASE',
                fg='red',
                font=("ALGERIAN",16,'bold','underline')).place(relx=0.3,rely=0.01)
        
        global var2
        var2=StringVar(root1)
        var2.set('-Indian_states-')

        
        options=ttk.Combobox(root1,width=18,state='readonly',textvariable=var2,values=Indian_states)
        options.place(relx=0.3,rely=0.4)
        options.bind("<<ComboboxSelected>>",lambda e: root1.focus())
          
        
        go=Button(root1,text='go',command=go_).place(relx=0.45,rely=0.55,height=30,width=40)
        
        
        root1.mainloop()
  
def go_():

        

        conn=mysql.connector.connect(
        host='localhost',
        user='root',
        passwd=values.pass_,
        database='Indian_states'
        )
        c=conn.cursor()

        root1.destroy()

        global root2

        root2=Tk()
        root2.geometry('600x500')
        root2.title('Database')
        root2.iconbitmap(r'icons\dbs1.ico')

        c.execute('SELECT * FROM {}'.format(var2.get()))
        fs=c.fetchall()


        tv=ttk.Treeview(root2)

        tv['columns']=('Year','All_Population','Male_Population','Female_Population')

        tv.column('#0',width=0)
        tv.column('Year',anchor=CENTER,width=100,minwidth=50)
        tv.column('All_Population',anchor=CENTER,width=140,minwidth=80)
        tv.column('Male_Population',anchor=CENTER,width=140,minwidth=80)
        tv.column('Female_Population',anchor=CENTER,width=140,minwidth=80)

        tv.heading('#0',text='S.NO',anchor=CENTER)
        tv.heading('Year',text='Year',anchor=W)
        tv.heading('All_Population',text='All_Population',anchor=W)
        tv.heading('Male_Population',text='Male_Population',anchor=W)
        tv.heading('Female_Population',text='Female_Population',anchor=W)
        x=0

        for key in fs:


                tv.insert(parent='',index='end',iid=x,text='',values=key)
                x=x+1

        tv.place(relx=0.1,rely=0.2)

        head=Label(root2,text='DATABASE',
                fg='red',
                font=("ALGERIAN",22,'bold','underline')).place(relx=0.4,rely=0.01)

        

        exit_=Button(root2,text='OK',
                        bg='#BDBDBD',
                        font=('Courier New',14,'bold'),
                        command=win_exit.close_root2).place(relx=0.5,rely=0.8,width=60,height=30)
        
        graph=Button(root2,text='GRAPH',
                        bg='#BDBDBD',
                        font=('Courier New',14,'bold'),
                        command=graph_.line_graph).place(relx=0.3,rely=0.8,width=80,height=30)
        
        lbl_0=Label(root2,text='Multiplying factor = 1000', fg='#0B0B61',
                        font=('Courier New',12,'bold')).place(relx=0.55,rely=0.15)

        conn.commit()
        c.close()
        conn.close()

        #var3.set('Total_population')

        root2.mainloop()

class win_exit:
        def close_root2():
                root2.destroy()
                clr()
        def close_root3():
                root3.destroy()
                clr()

def readme_():#README.pdf file opens
        import webbrowser
        url=r'file:///C:/Users/User/Desktop/DEMOGRAPHER/txt/README.pdf'
        webbrowser.register('edge',None,webbrowser.BackgroundBrowser(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'))
        webbrowser.get('edge').open(url)
        
class graph_():#graphs

        def line_graph():

                import matplotlib.pyplot as plt
                conn=mysql.connector.connect(
                host='localhost',
                user='root',
                passwd=values.pass_,
                database='Indian_states'
                )
                c=conn.cursor()

                q='SELECT total_population,Male_population,Female_population FROM {}'.format(var2.get())
                c.execute(q)
                fe=c.fetchall()
                lst_graph_total=[]
                lst_graph_male=[]
                lst_graph_female=[]
                for key in fe:
                        lst_graph_total.append(key[0])
                        lst_graph_male.append(key[1])
                        lst_graph_female.append(key[2])

                x = [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036]
                plt.plot(x,lst_graph_total)
                plt.plot(x,lst_graph_male)
                plt.plot(x,lst_graph_female)

                plt.xlabel('x - axis (Year)')
                plt.ylabel('y - axis (Population)')

                plt.title('Popultion VS Year Graph')

                plt.show()
                conn.commit()
                c.close()
                conn.close()
        
def output():

        conn=mysql.connector.connect(
                host='localhost',
                user='root',
                passwd=values.pass_,
                database='Indian_states'
        )
        cur=conn.cursor()
        x=var.get()
        y=var1.get()
        z=var_.get()

        query_0='SELECT Total_population from {}'.format(x)  #select population from state name.
        cur.execute(query_0)
        val_1=cur.fetchall()
        lst_total=[]

        for key in val_1:
                lst_total.append(key[0])

        query_1='SELECT Male_population from {}'.format(x)
        cur.execute(query_1)
        val_2=cur.fetchall()
        lst_male=[]

        for key in val_2:
                lst_male.append(key[0])


        #Finds the values for present year.
        query_1='SELECT {}'.format(z)+' FROM {}'.format(x)+' WHERE year= {}'.format(present_year) 
        #select population from state where year=x   for present value

        cur.execute(query_1)
        o=cur.fetchone()


        predicted_total_population = lnr_regression(lst_total) * 1000 #Linear regression function lst01= all values
        predicted_male_population = lnr_regression(lst_male) * 1000
        predicted_female_population = (predicted_total_population - predicted_male_population) 

        if z=='Total_Population':
                predicted_population=predicted_total_population
        elif z=='Male_Population':
                predicted_population=predicted_male_population 
        else:
                predicted_population=predicted_female_population 

        #============================================================================================
        global root3
        root3=Tk()
        root3.geometry('900x600')
        root3.title('--OUTPUT--')
        root3.iconbitmap(r'icons\py_icon.ico')

        state_=var.get()
        year_=var1.get()
        type_=var_.get()

        

        frame1=LabelFrame(root3,text='Selected values',
                        labelanchor=N,highlightbackground='#5F04B4',
                        highlightthickness=3,font=('ALGERIAN',14,'bold'))
        frame1.grid(row=0,column=0,padx=20,pady=20,ipadx=190,ipady=150)
        
        frame2=LabelFrame(root3,text='Present Values',
                        labelanchor=N,highlightbackground='#5F04B4',
                        highlightthickness=3,font=('ALGERIAN',14,'bold'))
        frame2.grid(row=1,column=0,padx=20,pady=20,ipadx=190,ipady=80)

        frame3=LabelFrame(root3,text='Predicted Values',
                        labelanchor=N,highlightbackground='#5F04B4',
                        highlightthickness=3,font=('ALGERIAN',14,'bold'))
        frame3.grid(row=0,column=1,rowspan=2,padx=40,pady=20,ipadx=200,ipady=250)

        #widgets on frame1:-
        lbl_1=Label(frame1,text='State:',
                        font=('Courier New',14,'bold')).place(relx=0.05,rely=0.1)

        lbl_2=Label(frame1,text='Year:',
                         font=('Courier New',14,'bold')).place(relx=0.05,rely=0.3)

        lbl_3=Label(frame1,text='Data:',
                        font=('Courier New',14,'bold')).place(relx=0.05,rely=0.5)

        lbl_4=Label(frame1,text=var.get(),bg='white',fg='green',
                        font=('Courier New',14,'bold')).place(relx=0.3,rely=0.1)

        lbl_5=Label(frame1,text=var1.get(),bg='white',fg='green',
                        font=('Courier New',14,'bold')).place(relx=0.3,rely=0.3)
        
        lbl_6=Label(frame1,text=var_.get(),bg='white',fg='green',
                        font=('Courier New',14,'bold')).place(relx=0.3,rely=0.5)

        button_1=Button(frame1,text='Change Values',bg='#BDBDBD',fg='black',bd=5,
                        font=('Courier New',15,'bold'),width=15,command=win_exit.close_root3).place(relx=0.2,rely=0.75)
        
        
        #widgets on frame 2

        lbl_7=Label(frame2,text='Present year:',
                        font=('Courier New',14,'bold')).place(relx=0.05,rely=0.2)

        lbl_8=Label(frame2,text=var_.get()+':',
                        font=('Courier New',14,'bold')).place(relx=0.05,rely=0.6)

        lbl_9=Label(frame2,text=present_year,bg='white',fg='green',
                        font=('Courier New',14,'bold')).place(relx=0.5,rely=0.2)

        lbl_10=Label(frame2,text=num_split(o[0]*1000),bg='white',fg='green',
                        font=('Courier New',14,'bold')).place(relx=0.65,rely=0.6)

        #widgets on frame 3

        lbl_11=Label(frame3,text=var_.get()+' predicted \nat the year '+str(var1.get())+' is :-',
                        font=('Courier New',14,'bold')).place(relx=0.1,rely=0.08)

        
        lbl_12=Label(frame3,text=num_split(int(predicted_population)),fg='green',bg='white',bd=7,
                        font=('Courier New',14,'bold')).place(relx=0.38,rely=0.2)

        lbl_13=Label(frame3,text='===================================',fg='black',
                        font=('Courier New',14,'bold')).place(relx=0,rely=0.3)

        lbl_14=Label(frame3,text='PIE-CHART',fg='#3104B4',
                        font=('ALGERIAN',18,'bold','underline')).place(relx=0.32,rely=0.36)

        my_canvas_1=Canvas(frame3,width=15,height=15,bg='#FF8000').place(relx=0.02,rely=0.9)

        my_canvas_2=Canvas(frame3,width=15,height=15,bg='green').place(relx=0.02,rely=0.95)

        lbl_15=Label(frame3,text='-> Male Population',fg='#FF8000',
                        font=('Courier New',10,'bold')).place(relx=0.04,rely=0.9)

        lbl_16=Label(frame3,text='-> Female Population',fg='green',
                        font=('Courier New',10,'bold')).place(relx=0.04,rely=0.95)

        lbl_17=Label(frame3,text='{Approx.}',fg='#3104B4',
                        font=('ALGERIAN',10,'bold','underline')).place(relx=0.75,rely=0.38)

        lbl_18=Label(frame3,text='Yr:'+str(var1.get()),fg='black',
                        font=('ALGERIAN',12,'bold','underline')).place(relx=0.05,rely=0.375)

        
        if z=='Total_Population':
                
                pie_angle=angle(int(predicted_population),int(predicted_male_population))
                #print(int(pred_male),int(pred_female))

        elif z=='Male_Population':
                
                pie_angle=angle(int(predicted_total_population),int(predicted_population))
                #print(int(pred_male),int(pred_female))


        else:
                
                pie_angle=angle(int(predicted_total_population),int(predicted_male_population))
                #print(int(pred_male),int(pred_female))

        deg='%'
        lbl_19=Label(frame3,text='Percent = '+str(int(pie_angle/360*100))+deg,fg='#FF8000',
                        font=('Courier New',10,'bold')).place(relx=0.5,rely=0.9)
        
        lbl_20=Label(frame3,text='Percent = '+str(int((360-pie_angle)/360 *100))+deg,fg='green',
                        font=('Courier New',10,'bold')).place(relx=0.5,rely=0.95)
        

        my_canvas_3=Canvas(frame3,width=250,height=180)
        my_canvas_3.place(relx=0.17,rely=0.47)

        #my_canvas_3.create_line(0,10,250,10,fill='red')
        my_canvas_3.create_rectangle(0,0,251,181,fill='#D8D8D8',width=0)

        my_canvas_3.create_arc(5,5,245,175,fill='#FF8000',outline='#FF8000',width=2,start=0,extent=pie_angle)
        my_canvas_3.create_arc(5,5,245,175,fill='green',outline='green',width=2,start=pie_angle,extent=360-pie_angle)
        #start=angle(0),extent=angle(percent_male))

        lbl_21=Label(root3,text='------xx--------THANK_YOU--------xx------',
                        font=('ALGERIAN',18,'bold'),fg='#0B0B61').place(relx=0.25,rely=0.92)
        conn.commit()
        cur.close()
        conn.close()

        root3.mainloop()

def lnr_regression(lst):

        
        import numpy as np
        from sklearn.linear_model import LinearRegression

        

        lst_yr=[]
        for i in range(2011,2037):
                lst_yr.append(i)


        x=np.array(lst_yr).reshape((-1, 1))

        y=np.array(lst)
        


        model = LinearRegression()

        model.fit(x, y)

        model = LinearRegression().fit(x, y)

        r_sq = model.score(x, y)

        intercept=model.intercept_
        slope=model.coef_

        global predicted_population

        return (slope*var1.get() + intercept)[0]

def num_split(x):   #To add commas to the numbers as in international standard system
        
        a=x//3
        h=str(x)
        n=h[::-1]
        l=[]
        i=0
        while i<a:
                if i+2>=len(n):
                        break
                else:
                        l.append(n[i]+n[i+1]+n[i+2])
                        i=i+3
        if len(n)%3==1:
                l.append(h[0])
        elif len(n)%3==2:
                l.append(h[1]+h[0])
        s=','.join(l)
        return s[::-1]
       
def angle(x,y): #x is total population and y is male population

        pie_angle=(y/x)*360

        return pie_angle

#=============================================================================



#Labels-8    
#==============================================================================
error=Label(root,text='Please select a valid input!!',
        fg='red',
        font=('ALERGIAN',12,'underline'))

lbl=Label(root,text='__________CHOOSE__________',
        fg='#0101DF',
        font=('ALGERIAN',20,'bold',)).place(relx=0.085,rely=0.01)

lb1=Label(root,text='State:',
        fg='black',
        font=('Courier New MT',16,'bold','underline')).place(relx=0.3,rely=0.3)

lbl2=Label(root,text='Year:',
        fg='black',
        font=('Courier New MT',16,'bold','underline')).place(relx=0.3,rely=0.4)

lbl3=Label(root,text='Data:',
        fg='black',
        font=('Courier New MT',16,'bold','underline')).place(relx=0.3,rely=0.5)

lbl4=Label(root,text='=============================',
        fg='#0101DF',
        font=('Courier New MT',18,'bold')).place(relx=0.085,rely=0.87)

lbl5=Label(root,text='Ver 1.0.0',
        fg='grey',
        font=('ALGERIAN',10)).place(relx=0.85,rely=0.93)


cpyright=Label(root,text='© '+present_year+' PACH Team - All Rights Reserved',
        fg='red',
        font=('Courier New',10,'bold')).place(relx=0.2,rely=0.93)


#combobox var,var1
#=================================
dp=ttk.Combobox(root,width=18,state='readonly',textvariable=var,values=Indian_states)
dp.place(relx=0.45,rely=0.31,height=25)

dp1=ttk.Combobox(root,width=7,state='readonly',textvariable=var1,values=yrs)
dp1.place(relx=0.45,rely=0.41,height=25)

dp2=ttk.Combobox(root,width=18,state='readonly',textvariable=var_,values=popu_options)
dp2.place(relx=0.45,rely=0.51,height=25)

dp.bind("<<ComboboxSelected>>",lambda e: root.focus())
dp1.bind("<<ComboboxSelected>>",lambda e: root.focus())
dp2.bind("<<ComboboxSelected>>",lambda e: root.focus())


#Buttons-2   help,database
#=======================================================

btn_ins=Button(root,text='README',
        bg='#BDBDBD',fg='black',
        font=('Courier New',13,'bold'),width=9,command=readme_).place(relx=0.05,rely=0.15)

btn_dbs=Button(root,text='Database',
        bg='#BDBDBD',fg='black',
        font=('Courier New',13,'bold'),width=9,command=dbs).place(relx=0.75,rely=0.15)


#Buttons-2  submit,clear
#=================================
btn_sub=Button(root,text='Submit',
        bg='#BDBDBD',fg='black',width=10,
        font=('Courier New MT',12,),bd=5,command=submit).place(relx=0.5,rely=0.7)

btn_clr=Button(root,text='Clear',
        bg='#BDBDBD',fg='black',width=10,
        font=('Courier New MT',12,),bd=5,command=clr).place(relx=0.3,rely=0.7)


#==================================================================================

conn.commit()
c.close()
conn.close()

root.mainloop()