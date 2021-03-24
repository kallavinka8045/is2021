import os
import numpy as np
import csv
import argparse
from collections import defaultdict

confidence_coeff = 1.96
round_num = 2

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_csv', type=str, required=True)
    args = parser.parse_args()

    f = open(args.input_csv, "r", encoding='utf-8')
    rdr = csv.reader(f)
    data_prev = [line for line in rdr]
    data_prev[0] = data_prev[0][:-2]

    data = []
    try:
        for i in range(1, len(data_prev)):
            d_dict = dict()
            for j in range(len(data_prev[0])):
                d_dict[data_prev[0][j]] = data_prev[i][j]
            if d_dict['AssignmentStatus'] != 'Rejected':
                data.append(d_dict)
    except:
        print(i, j)

    print(len(data))

    score_list = defaultdict(list)
    avg_list = defaultdict(float)
    con_list = defaultdict(float)

    for d in data:
        model = d['Input.audio_url'].split('/')[-3]
        score = float(d['Answer.audio-naturalness.label'][:2])
        score_list[model].append(score)

    model_name_list = ['wavenet', 'waveglow', 'wavernn', 'melgan_orig', 'melgan_ours', 'gt']
    for model in model_name_list:
        n_samples = len(score_list[model])
        avg_list[model] = np.average(score_list[model])
        con_list[model] = confidence_coeff*np.sqrt(np.var(score_list[model]))/np.sqrt(n_samples)

        print('{:12}{}+-{}'.format(model, round(avg_list[model], round_num), round(con_list[model], round_num)))

