import matplotlib.pyplot as plt
import pyaudio
import wave

def transforming_to_tones(area):

    # SIGNAL NORMALISATION
    # min and max area found empirically
    max_area=300000
    min_area=32000
    tone_range = max_area - min_area
    areatone = (area - min_area ) / tone_range

    if areatone > 0.2 and areatone < 0.4:
        areatone = 440
        note="A4"
    elif areatone >=0.4 and areatone < 0.6:
        areatone = 523
        note="C5"
    elif areatone >= 0.6 and areatone < 0.7:
        areatone = 587
        note="D5"
    elif areatone >= 0.7 and areatone < 0.8:
        areatone = 659
        note="C5"
    elif areatone >= 0.8 and areatone < 0.9:
        areatone = 698
        note="F5"
    elif areatone >= 0.9 and areatone < 1:
        areatone = 784
        note="G5"
    elif areatone >= 1:
        areatone = 880
        note="A5"
    else:
        note="Rest"
        areatone=0
    return note, areatone

def plotting_notes(notes):
    interval=[]
    for e in range(len(notes)):
        interval.append(e)
    plt.plot(interval, notes, "s")
    labels=set(notes)
    plt.ylabel('Notes')
    plt.xlabel('Frame number')
    return plt.show()

def recording_all():
    # This code belongs to:
    # https://gist.github.com/mabdrabo/8678538        
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 2
    WAVE_OUTPUT_FILENAME = "./output/song_and_environment.wav"
    
    audio = pyaudio.PyAudio()
    
    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    print ("Recording...")
    frames = []
    
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print ("Finished recording")
    
    
    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
