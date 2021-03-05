import glob
import os
import random


for domain in os.listdir('.'):
    wav_list = glob.glob('{}/*/*.wav'.format(domain))
    random.shuffle(wav_list)
    prefix = 'https://kallavinka8045.github.io/is2021/wav_for_mos/'
    with open('audio_url_{}.csv'.format(domain), 'w', encoding='utf-8') as f:
        f.write('audio_url' + '\n')
        for wavname in wav_list:
            f.write(prefix + wavname + '\n')
