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
    data_prev = [line[27:] for line in rdr]
    data_prev[0] = data_prev[0][:-2]
    print(data_prev[0])
    print(data_prev[1])
    print(len(data_prev[0]))
    print(len(data_prev[1]))

    N = len(data_prev[0])//6
    model_list = [dat.split('/')[-2] for dat in data_prev[1][:N]]

    data = []
    for i in range(1, len(data_prev)):
        model_seq = [dat.split('/')[-2] for dat in data_prev[i][:N]]
        for j in range(N, len(data_prev[i])):
            if data_prev[i][j] == 'true':
                score = int(data_prev[0][j].split('.')[-1])
                model = model_seq[int(data_prev[0][j].split('.')[-2][-1])]
                data.append([model, score])

    score_list = defaultdict(list)
    avg_list = defaultdict(float)
    con_list = defaultdict(float)

    for model, score in data:
        score_list[model].append(score)

    for model in model_list:
        n_samples = len(score_list[model])
        avg_list[model] = np.average(score_list[model])
        con_list[model] = confidence_coeff*np.sqrt(np.var(score_list[model]))/np.sqrt(n_samples)

        print('{:12}{}+-{}'.format(model, round(avg_list[model], round_num), round(con_list[model], round_num)))
