import moviepy.editor

cvt_video=moviepy.editor.VideoFileClip("The Most Inspiring Speech_ 4 True Rules To Success _ A. P. J. Abdul Kalam.mp4")
ext_audio=cvt_video.audio
ext_audio.write_audiofile("audio_Extracted.mp3")