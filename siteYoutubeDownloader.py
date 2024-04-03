import streamlit as st
from pytube import YouTube
import os
import shutil

def start_download(yt_link, save_path):
    try:
        yt_object = YouTube(yt_link)
        st.write("Baixando:", yt_object.title)
        video = yt_object.streams.get_highest_resolution()
        filename = video.default_filename
        video.download(output_path=save_path)
        original_path = os.path.join(save_path, filename)
        new_path = os.path.join(save_path, yt_object.title + '.' + filename.split('.')[-1])
        shutil.move(original_path, new_path)
        st.success("Download concluído!")
    except Exception as e:
        st.error(f"Erro: {str(e)}")

def main():
    st.markdown("<h1 style='color: red;'>YouTube Downloader</h1>", unsafe_allow_html=True)

    yt_link = st.text_input("Insira o link do vídeo do YouTube:"+" (Será baixado na mais alta qualidade)")
    save_path = st.text_input("Insira manualmente o caminho onde deseja salvar o vídeo:"+" - Ex: C:\TEMP")

    if st.button("Baixar"):
        progress_bar = st.progress(0)
        start_download(yt_link, save_path)
        with st.spinner('Baixando...'):
            for percent_complete in range(100):
                progress_bar.progress(percent_complete + 1)

if __name__ == "__main__":
    main()
