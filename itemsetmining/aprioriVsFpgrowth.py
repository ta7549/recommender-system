import time

import matplotlib.pyplot as plt
import seaborn as sns
from initDataAnalysis import new_df
from mlxtend.frequent_patterns import apriori, fpgrowth

min_sup = [0.01, 0.02, 0.03, 0.04, 0.05]
apriori_time = []
for x in min_sup:
    apriori_time_b = time.time()
    apriori(new_df, min_support=x, use_colnames=True)
    apriori_time_a = time.time()
    apriori_time.append((apriori_time_a - apriori_time_b) * 1000)

min_sup = [0.01, 0.02, 0.03, 0.04, 0.05]
fpgrowth_time = []
for x in min_sup:
    fpgrowth_time_b = time.time()
    fpgrowth(new_df, min_support=x, use_colnames=True)
    fpgrowth_time_a = time.time()
    fpgrowth_time.append((fpgrowth_time_a - fpgrowth_time_b) * 1000)

plt.figure(figsize=(12,8))
sns.lineplot(x=min_sup, y=apriori_time, label="apriori")
sns.lineplot(x=min_sup, y=fpgrowth_time, label="fpgrowth")
plt.title("Execution time comparison between Apriori and FP Growth")
plt.xlabel("Min. Support")
plt.ylabel("Time (in sec)")
plt.savefig("../fig/aprioriVsFpgrowth.png")

min_sup = [0.01,0.013,0.015, 0.02,0.023,0.025,0.03]
           #0.033, 0.035]
apriori_time = []
for x in min_sup:
    apriori_time_b = time.time()
    apriori(new_df, min_support=x, use_colnames=True)
    apriori_time_a = time.time()
    apriori_time.append((apriori_time_a - apriori_time_b) * 1000)

min_sup = [0.01,0.013,0.015, 0.02,0.023,0.025 ,0.03]
#, 0.033, 0.035]
fpgrowth_time = []
for x in min_sup:
    fpgrowth_time_b = time.time()
    fpgrowth(new_df, min_support=x, use_colnames=True)
    fpgrowth_time_a = time.time()
    fpgrowth_time.append((fpgrowth_time_a - fpgrowth_time_b) * 1000)

plt.figure(figsize=(12,8))
sns.lineplot(x=min_sup, y=apriori_time, label="apriori")
sns.lineplot(x=min_sup, y=fpgrowth_time, label="fpgrowth")
plt.title("Execution time comparison between Apriori and FP Growth")
plt.xlabel("Min. Support")
plt.ylabel("Time (in sec)")
plt.savefig("../fig/aprioriVsFpgrowthGranular.png")