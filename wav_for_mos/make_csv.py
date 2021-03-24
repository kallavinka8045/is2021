import glob
import os
import random

prefix = 'https://kallavinka8045.github.io/is2021/wav_for_mos/'
domain_list = ['ablation', 'seen', 'unseen', 'tts']

for domain in domain_list:
    category_list = os.listdir(domain)
    wav_name_list = os.listdir(os.path.join(domain, category_list[0]))
    random.shuffle(wav_name_list)
    with open('audio_url_{}.csv'.format(domain), 'w', encoding='utf-8') as f:
        for i in range(len(category_list)):
            if i != 0:
                f.write(',')
            f.write('audio_url{}'.format(i))
        f.write('\n')
        for wav_name in wav_name_list:
            random.shuffle(category_list)
            for i, category in enumerate(category_list):
                if i != 0:
                    f.write(',')
                f.write(os.path.join(prefix, domain, category, wav_name))
            f.write('\n')
