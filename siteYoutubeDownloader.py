import streamlit as st
from pytube import YouTube

def start_download(yt_link, save_path):
    try:
        yt_object = YouTube(yt_link)
        st.write("Baixando:", yt_object.title)
        video = yt_object.streams.get_highest_resolution()
        video.download(output_path=save_path, filename="video")
        st.success("Download concluído!")
    except Exception as e:
        st.error(f"Erro: {str(e)}")

def main():
    st.markdown("<h1 style='color: red;'>YouTube Downloader</h1>", unsafe_allow_html=True)

    yt_link = st.text_input("Insira o link do vídeo do YouTube:"+" (Será baixado a mais alta qualidade)")
    save_path = st.text_input("Insira manualmente o caminho onde deseja salvar o vídeo:"+" - Ex: C:\TEMP")

    if st.button("Baixar"):
        progress_bar = st.progress(0)
        start_download(yt_link, save_path)
        with st.spinner('Baixando...'):
            for percent_complete in range(100):
                progress_bar.progress(percent_complete + 1)

if __name__ == "__main__":
    main()
