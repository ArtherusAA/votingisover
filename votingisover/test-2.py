import matplotlib.pyplot as plt
import numpy as np

import sqlite3 as lite
import sys

con = lite.connect('./db.sqlite3')

with con:
    cur = con.cursor()

    cur.execute("SELECT * FROM voting_variant") # tabel of variant
    rows_in_variant = cur.fetchall()

    cur.execute("SELECT * FROM voting_vote") # tabel of variant
    rows_in_vote = cur.fetchall()
    ans = [0] * len(rows_in_variant)

    #for row in rows_in_variant:
    for row_vote in rows_in_vote:
        ans[int(row_vote[3]) - 1] += 1

    #for i in range(0, len(rows_in_variant)):
    i = 0
    print(len(rows_in_variant))
    while(i < len(rows_in_variant)):
        x = []
        y = []
        for j in range(len(rows_in_variant)):
            if (rows_in_variant[i][2] == rows_in_variant[j][2]):
                x.append(rows_in_variant[j][1])
                y.append(ans[j])

        fig = plt.figure()
        plt.bar(x, y)
        plt.title('Соотношение голосования')
        plt.grid(True)   # линии вспомогательной сетки
        plt.savefig('./media/id' + str(rows_in_variant[i][2]) + '.png')
        #plt.show()
        plt.close(fig)
        
        i = i + len(x)
        print(i)

        # print(rows_in_variant[i][1], ' ', ans[i])
        # print(rows_in_variant[i + 1][1], ' ', ans[i + 1])
        # print('')
        # x = [rows_in_variant[i][1], rows_in_variant[i + 1][1]]
        # y = [ans[i], ans[i + 1]]
