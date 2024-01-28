from pytube import YouTube

try:
    # Input the YouTube video link asked to user
    link = input("Enter the YouTube URL: ")
    
    yt = YouTube(link)
    
    print("Title:", yt.title)
    print("Views:", yt.views)

    # Retrieving highest resolution available
    yd = yt.streams.get_highest_resolution()
    
    # Download the video destination directory
    yd.download()
    
    #When we are done showing completed message
    print("Download complete.")
    
    # If any error let us know!
except Exception as e:
    print("An error occurred:", str(e))