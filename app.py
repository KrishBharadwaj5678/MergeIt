import streamlit as st
from moviepy.editor import *

st.set_page_config(
    page_title="Merge It - Merge Videos Online",
    page_icon="icon.png",
    menu_items={
        "About":"MergeIt makes it a breeze to combine multiple video into one seamless video. Upload and merge your videos online, then download your polished masterpiece with just a click!"
    }   
)

st.write("<h2 style='color:#F58229;'> Merge Videos and Download Instantly.</h2>",unsafe_allow_html=True)

file=st.file_uploader("Upload Your Videos",type="mp4",accept_multiple_files=True)
btn=st.button("Merge")

files=[]

if btn:
    with st.spinner("We’re working on your video…"):
        for i in range(0,len(file)):
            with open(f"video_{i}.mp4","wb") as video:
                video.write(file[i].read())
            vid=VideoFileClip(f"video_{i}.mp4")
            files.append(vid)

        out=concatenate_videoclips(files)
        out.write_videofile("merge.mp4")
    
    st.video("merge.mp4")

    with open("merge.mp4","rb") as output:
        st.download_button("Download",output.read(),"mergeit.mp4")
