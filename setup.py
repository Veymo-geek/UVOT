from setuptools import setup, find_packages

setup(
    name='UVOT',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        "audio-separator==0.10.4",
        "lightning_fabric==2.1.3",
        "moviepy==1.0.3",
        "pysubs2==1.6.0",
        "pydub==0.25.1",
        "translatesubs==0.2.4",
        "torch==2.1.2",
        "ffmpeg-python==0.2.0",
        "faster-whisper==0.10.0",
        "gradio==3.45.1",
        "yt-dlp==2023.7.6"
    ],
)
