# СДЕЛАТЬ: приведите код в порядок: оформите согласно рекомендациям и примерам горизонтальные и вертикальные отступы, правильно расположите строки документации

from pathlib import Path
# разделил параметры по такому принципу, потому что все остальные являются числами.
def parse_sound_file(file_extension: str,
                                        *,
                                        audio_format: str | int,
                                        channels: str | int,
                                        frequency:str | int,
                                        depth: str | int) -> str:
                                        
    """Проверяет корректность переданных аргументов звукового файла и печатает результат проверки. """                                    
    frequency_range = (8000, 11025, 16000, 22050, 32000, 44100, 48000, 88200, 96000, 176400, 192000, 352800, 384000)
    depth_range = (8, 16, 24, 32)
    result = ' '       
    song_object = Path(file_extension)
      
    if song_object.suffix[1:] == 'wav':
        result += f"{file_extension = } верно\n"
    else:
        result += f"{file_extension = } неверно\n"
        
    if 0 < int(audio_format) < 9999:
         result += f"{audio_format = } верно\n" 
    else:
        result += f"{audio_format = } неверно\n"
        
    if 1 < int(channels) < 10:
        result += f"{channels = } верно\n" 
    else:
        result += f"{channels = } неверно\n"
        
    if int(frequency) in frequency_range:
        result += f"{frequency = } верно\n" 
    else:
        result += f"{frequency = } неверно\n"
        
    if int(depth) in depth_range:
        result += f"{depth = } верно\n" 
    else:
        result += f"{depth = } неверно\n"
        
    return result
        
    
    
 # stdin:
print(parse_sound_file(
    "./file.wav",
    audio_format='25',
    channels=5,
    frequency='44100',
    depth=16
))      
# stdout:
# file_extension = './file.wav' верно
# audio_format = '25' верно
# channels = 5 верно
# frequency = '44100' верно
# depth = 16 верно


# stdin:
print(parse_sound_file(
    "./file.wov",
    audio_format='-25',
    channels=12,
    frequency='441100',
    depth=17
))   
# stdout:
 # file_extension = './file.wov' неверно
# audio_format = '-25' неверно
# channels = 12 неверно
# frequency = '441100' неверно
# depth = 17 неверно

 
 
    
