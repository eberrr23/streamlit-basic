import streamlit as st
import pandas as pd
import time  as ts #for progresss bar
import datetime
from datetime import time#to set timer for progress bar
from matplotlib import pyplot as plt
import numpy as np
import pygwalker as pyg
import streamlit.components.v1 as components#for pygwalker
import cv2



st.set_page_config(
    layout='wide'
)

#to hide streamlit hamburger...ie the top right stuff
st.markdown('''
<style>
.css-zq5wmm.ezrtsby0{
    visibility: hidden;
}
</style>
''', unsafe_allow_html=True)

st.markdown('''
<style>
.css-cio0dv.ea3mdgi1{
    visibility: hidden;
}

</style>
''', unsafe_allow_html=True)

#creating a dataframe
t1=pd.DataFrame({"column 1":[1,2,3,4,5,6,7],"column 2": [11,12,13,14,15,16,17]})


st.title("hi i am streamlit web app")
st.subheader("Hi , I am your subheader")
st.header("I am Header")
st.text("this is a text ")
st.markdown("**Hello** *world!* ")
#more markdowns can be found on google for different styles

st.markdown("[Google](https://www.google.com)")

st.markdown("---")
st.caption("Hi i am caption")

st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
#kateex.org for more matrice stuffff



json={"a":"1,2,3","b":"4,5,6"}
st.json(json)
#for json data


code='''
print("hello world")
x=123
b=x + 66
'''

st.code(code,language='python')
# to add grabbable code


#for implementation of all above things
st.write("## H2")
#check official streamlit docu for more stuff with write


st.metric(label="wind speed",value="120ms⁻¹", delta="1.4ms⁻¹")#to get power...use ⁻¹ and hit tab
# for tables
st.table(t1)
#for dataframes
st.dataframe(t1)

#adding pictures
st.image("Sebastian-Vettel-PA4.jpg",caption="this is my image",width=600)

#embedding audio

st.audio("Kavinsky - Nightcall (Drive Original Movie Soundtrack) (Official Audio) (320 kbps).mp3")

#video
st.video("Lost in Time - Sebastian Vettel _  Inspirational & Sad F1 Edit - Scuderia Ferrari.mp4")

def change():
    print(st.session_state.checker)
st.checkbox("checkbox",value=True, on_change=change, key="checker")#value to auto check the box


#for the below.....assign state to above widget
#if state:
    #st.write("hello")
#else:
    #st.write("bye")

radio_btn=st.radio("where do you belong from???",key="btn_1", options=("us","uk","canada"))



def btn_click():
    print("button clicker")
btn=st.button("click now!!!",on_click=btn_click)

select=st.selectbox("what is your favourite car?", options=("audi r8","corvette c8", "ford gt"))
#print(select)

multi_select=st.multiselect("what are your favourite car brands",options=("audi","bmw","mercedes","Ferrari","ford","Porsche","dodge"))
st.write(multi_select)

image=st.file_uploader("Please upload an image",type=["png","jpg"],accept_multiple_files=True)

#to display the image uploaded 
#if image is not None: 
    #st.image(image)

val=st.slider("this is a slider",min_value=50,max_value=70,value=70)
#print(val)


txt=st.text_area(label="add your comments",max_chars=60)
txt1=st.text_input(label="tell em",max_chars=30)
txt2=st.date_input(label="enter your date of birth")



st.markdown("---")

st.header("Timer app with progress bar")

def converter(value):
    print(value)
    m,s,ms=value.split(":")
    t_in_s=int(m)*60+int(s)+int(ms)/1000
    return t_in_s

#timer
txt3=st.time_input("set your time",value=time(0,0,0))#(0,0,0) forhours mins seconds
if str(txt3)=="00:00:00":
    st.write("please set timer") 
else:
    sec=converter(str(txt3))
    bar=st.progress(0)
    percentage=sec/100
    progress_status=st.empty()
    for i in range(100):
        bar.progress(i+1)#i+1 because i starts from 0
        progress_status.write(str(i)+"%")
        ts.sleep(percentage)#the amount of time in seconds to stay at one point





#FORMS

st.markdown("<h1 style='text-align: center;'>User Registration</h1>",unsafe_allow_html=True)
form=st.form("Form 1")
form.text_input(label="First Name")#we use form. so that the text input is created inside the form

form._form_submit_button("Submit")

#2nd method of form creation

with st.form("form2",clear_on_submit=True):
    col1,col2=st.columns(2)
    f_name=col1.text_input("First name")
    s_name=col2.text_input("second name")
    st.text_input("Enter your email")
    st.text_input("Enter password")
    st.text_input("confirm password")
    
    day,month,year=st.columns(3)
    day.text_input("enter day")
    month.text_input("month")
    year.text_input("year")

    state=st.form_submit_button("Submit")
    if state:
        if f_name == "" and s_name == "":
            st.warning("please fill the above fields")
        else:
            st.success("submitted successfully")






#SIDEBAR AND GRAPHS


opt=st.sidebar.radio("select any graph",options=("line","bar","horizontal bar"))


x=np.linspace(0,10,100)
bar_x=np.array([1,2,3,4,5])

if opt=="line":
    
    fig=plt.figure()
    #plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.plot(x,np.sin(x))
    plt.plot(x,np.cos(x),"--")
    st.write(fig)
    st.markdown("<h1 style='text-align : center'>LINE GRAPH</h1>",unsafe_allow_html=True)

elif opt=="bar":
    fig=plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.bar(bar_x,bar_x*10)
    st.write(fig)

    st.markdown("<h1 style='text-align : center'>bar graph</h1>",unsafe_allow_html=True)

elif opt=="horizontal bar":
    fig=plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.barh(bar_x*10,bar_x*10)
    st.write(fig)

    st.markdown("<h1 style='text-align : center'>horizontal bar graph</h1>",unsafe_allow_html=True)

st.markdown("DATA VISUALIZER")


files=st.file_uploader("upload multiple files", type=["xlsx"],accept_multiple_files=True)
files_names=list()



def date_converter(date_col):
    result=list()
    values=date_col.values
    for value in values:
        result.append(str(value.split("T")[0]))
    return result


figure=plt.figure()
if files:
    for file in files:
        files_names.append(file.name)
    selected_files=st.multiselect("select files",options=files_names)
    if selected_files:
        option=st.radio("select entity",options=["Country","Date","Age","Gender","none"])
        if option !="none":
            for file in files:
                if file.name in selected_files:
                    data=pd.read_excel(file)
                    item=list(data[option])
                    dates=date_converter(data["Date"])
                    print(dates)
                    index=np.arange(len(dates))#to assign a number to dates
                    plt.xticks(index, dates)#to replace those numbers with actual dates
                    plt.gcf().autofmt_xdate() #to solve the dates being all cramped up in the plot
                    plt.plot(index,item,label=file.name,marker='o')
                    plt.xlabel("DATES")
                    plt.ylabel(option)
                    plt.title(option+" chart")
                    plt.grid(True)
                    plt.legend()
                    print(data[option].values)
            st.write(figure)



df= pd.read_csv('kaggle_income.csv', encoding='latin-1')

walker=pyg.walk(df,return_html=True)

components.html(walker, height=1000,width=1000, scrolling=True)




option2=st.radio("select entity",options=["take photo","none"])


# Initialize the webcam
webcam = cv2.VideoCapture(0)  # Use index 0 for the default camera (you can change it if needed)

# Check if the webcam opened successfully
if not webcam.isOpened():
    print("Error: Could not open webcam.")
    exit(1)

while True:
    try:
        # Read a frame from the webcam
        check, frame = webcam.read()
        
        # Check if the frame was read successfully
        if not check:
            print("Error: Could not read frame from the webcam.")
            break

        # Display the frame
        cv2.imshow("Capturing", frame)

        # Check for key presses
        key = cv2.waitKey(1)

        if key == ord('s'):
            # Save the current frame as 'saved_img.jpg'
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            print("Image saved!")

            # Read the saved image in grayscale mode
            img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
            
            # Display the grayscale image
            cv2.imshow("Captured Image", img_new)
            
            # Wait for a moment and then close the window
            cv2.waitKey(2000)
            cv2.destroyWindow("Captured Image")

            print("Processing image...")

            # Read the saved image in color mode
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_COLOR)
            
            # Convert the image to grayscale
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            
            # Resize the image to 28x28 pixels
            img_resized = cv2.resize(gray, (28, 28))
            
            # Save the resized image as 'saved_img-final.jpg'
            cv2.imwrite(filename='saved_img-final.jpg', img=img_resized)
            
            print("Image saved!")
            break

        elif key == ord('q'):
            print("Turning off camera.")
            break

    except KeyboardInterrupt:
        print("Turning off camera.")
        break

# Release the webcam and close all OpenCV windows
webcam.release()
cv2.destroyAllWindows()
