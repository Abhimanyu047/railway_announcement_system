import os
import pandas as pd
from pydub import AudioSegment # Pydub lets you do stuff to audio in a way that isn't stupid.
from gtts import gTTS #Google Text to Speech module


def textToSpeech(text,filename):
    '''
    Converts input text to .mp3 and saves to a given file
    '''
    # Read the documentation for Google Text to Speech module for python
    # to understand the below variables and parameters
    mytext = str(text)
    language = 'hi' #Hindi
    myobj = gTTS(text=mytext,lang=language,slow=False)
    myobj.save(filename)

def mergeAudios(audios):
    '''
    Returns pydubs Audio Segment by taking a list of audios and merging it
    '''
    combined = AudioSegment.empty()
    # Concatination begins
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    '''
    Breaks an audio into desired segments to create a general purpose audio track.
    '''
    # read the audio from the system
    audio = AudioSegment.from_mp3('railway.mp3')
    
    # Read pydub documentation to know how start, finish and audioProcessed variables got created
    # 1. generate the segment 'kripaya dhyan dijiye'
    start = 88000 #check the milisecond from where to start trimming the audio track
    finish = 90200 #check the milisecond upto which trim the audio track
    audioProcessed = audio[start:finish]
    audioProcessed.export('1_hindi.mp3',format='mp3') #save the mp3 file in the system

    # 2. generate the segment 'from city'

    # 3. generate the segment 'se chal kar'
    start = 91000 #check the milisecond from where to start trimming the audio track
    finish = 92200 #check the milisecond upto which trim the audio track
    audioProcessed = audio[start:finish]
    audioProcessed.export('3_hindi.mp3',format='mp3') #save the mp3 file in the system

    # 4. generate the segmnt 'via city'

    # 5. generate the segment 'ke raaste'
    start = 94000 #check the milisecond from where to start trimming the audio track
    finish = 95000 #check the milisecond upto which trim the audio track
    audioProcessed = audio[start:finish]
    audioProcessed.export('5_hindi.mp3',format='mp3') #save the mp3 file in the system

    # 6. generate the segment 'to city'
    
    # 7. generate the segment 'ko jaane wali gaadi sankhya'
    start = 96000 #check the milisecond from where to start trimming the audio track
    finish = 98900 #check the milisecond upto which trim the audio track
    audioProcessed = audio[start:finish]
    audioProcessed.export('7_hindi.mp3',format='mp3') #save the mp3 file in the system

    # 8. generate the segment 'train number and name'

    # 9. generate the segment 'kuch hi samay mein platform sankhya'
    start = 105500 #check the milisecond from where to start trimming the audio track
    finish = 108200 #check the milisecond upto which trim the audio track
    audioProcessed = audio[start:finish]
    audioProcessed.export('9_hindi.mp3',format='mp3') #save the mp3 file in the system

    # 10. generate the segment platform number
    
    # 11. generate the segment 'par aa rahi hai'
    start = 109000 #check the milisecond from where to start trimming the audio track
    finish = 112250 #check the milisecond upto which trim the audio track
    audioProcessed = audio[start:finish]
    audioProcessed.export('11_hindi.mp3',format='mp3') #save the mp3 file in the system

def generateAnnouncement(filename):
    '''
    This function manually generates speech for given text in the excel file and returns an aduio output
    '''
    df = pd.read_excel(filename)
    # Generating mp3 files for the rows in excel sheet
    for index, item in df.iterrows(): # get index and row from the df
        # Generate 'from city'
        textToSpeech(item['from'], '2_hindi.mp3')
        # Generate 'via-city'
        textToSpeech(item['via'], '4_hindi.mp3')
        # Generate 'to-city'
        textToSpeech(item['to'], '6_hindi.mp3')
        # Generate train no and name
        textToSpeech(item['train_no'] + " " + item['train_name'], '8_hindi.mp3')
        # Generate platform no.
        textToSpeech(item['platform'], '10_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1,12)]

        announcement = mergeAudios(audios) # Concatenate the audios
        announcement.export(f"announcement_{index + 1}.mp3",format="mp3")

if __name__ == '__main__':
    print("Generating Skeleton")
    generateSkeleton()
    print("Now generating Announcement...")
    generateAnnouncement('announce_hindi.xlsx')
