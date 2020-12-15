import os
import codecs
import re

import numpy as np
# import seaborn as sns

league_round = 2

pat = re.compile("\|\s+(.*?)@([a-zA-Z0-9\-_]+)\s+\|\s+(\d+)\s+\|\s+(\d+)\s+\|\s+(\d+)\s+\|\s+(\d+)\s+\|\s+(\d+)\s+\|\s+(\d+)\s+\|")
fpath = "../leaderboard_round-0%d.md"%(league_round)

list_github_id = []
list_score = []

with codecs.open(fpath, "r", encoding="utf-8") as fin:
    for line in fin:
        #print(line)
        mat = pat.search(line)
        if mat:
            github_id = mat.group(2)
            
            if github_id in ["dwgoon", "bigoriginlee"]:
                continue
            
            rank = int(mat.group(3))
            games = int(mat.group(4))
            wins = int(mat.group(5))
            draws = int(mat.group(6))
            losses = int(mat.group(7))
            score = int(mat.group(8))
            assert(games == (wins + draws + losses))
            
            list_github_id.append(github_id)
            list_score.append(int(score))
        # end of if
    # end of for
    

arr_score = np.array(list_score)

# plt.plot(arr_zscore)
#ax = sns.distplot(arr_score, bins=20)
#ax = sns.histplot(arr_score, bins=10)


# GOAL: MAX=100, MEAN=80
max_score = arr_score.max()
mean_score = arr_score.mean()
a = 20/(max_score - mean_score)
b = 100 - a*max_score

arr_final_score = a*arr_score + b

fpath_out = "../finalscore-round-0%d.md"%(league_round)
with open(fpath_out, "w", encoding="utf-8") as fout:
    fout.write("Final Score (Round #%d)\n"%(league_round))
    fout.write("======================\n\n")
    fout.write("| 참가자 | 점수 |\n")
    fout.write("|:---:|:---:|\n")
    fstr_score = "| %s | %.2f |\n"
    for i, github_id in enumerate(list_github_id):    
        fout.write(fstr_score%(github_id, arr_final_score[i]))