import pandas as pd
a = pd.Series([1,2,3,5,5])
print(a.isin([2,3,10]))

# print(type(a.value_counts()))
# print(a.value_counts()[5])

# a = pd.read_csv('../data/raw/fresh_comp_offline/tianchi_fresh_comp_train_user.csv')
# print(a[:5])
# ps = pd.Series(list(range(5)))
# print(ps.sum)
# print(ps.sum())
# import datetime
# import pandas as pd
# import sys
# import numpy as np
# s = pd.Series(list(range(5)))
# print(s)


# new_s = pd.DataFrame(s,columns=['a'])
# print(new_s)
# new_s['time'] = new_s.index
# print(new_s)
# print(new_s.values)




# a = s.index
# b = s.values
# print(np.array(a))
# print(b)
# sys.exit()
# print(type(list(a)))
# print(type(b))

# data = []
# data.append(list(a))
# data.append(list(b))
# print(data)
# df = pd.DataFrame(data,columns=['a','b'])
# print(df)

import datetime
import numpy as np
from sklearn.utils import shuffle
# Date = '2014-11-18'
# a = datetime.datetime.strptime(Date, '%Y-%m-%d')
# # print(type(a))
# print(a)

# date_list = []
# for i in range(30):
#   delta = datetime.timedelta(days=i)
#   temp_date = a + delta
#   date_list.append(temp_date)
#   # date_list.append(temp_date.strftime('%Y-%m-%d'))

# # date_list = [datetime.datetime.strftime(x) for x in date_list]
# df  = pd.DataFrame(np.random.rand(30,2),index=date_list,columns=['a','b'])
# df = shuffle(df)
# print(df)
# print(df['2014-11-28':'2014-12-1'])

# print(date_list)


from pandas import Series,DataFrame
from numpy.random import randn
import numpy as np
import matplotlib.pyplot as plt
# df = DataFrame(abs(randn(10,5)),columns=['A','B','C','D','E'],index = np.arange(0,100,10))
# df.plot(kind='bar')
# df_dict1 = DataFrame({'time':['1','3','4','5','5'],'count':[44,178,29,88,88]})

# temp_df = df_dict1.groupby(['time','count']).cumcount()
# print(temp_df)
# for name,item in temp_df:
# 	print(name,item)
# print(temp_df)
# print(df_dict1)
# df_dict2 = DataFrame({'time':['1','1','3',],'count2':[44,45,178,]})
# print(pd.merge(df_dict1,df_dict2,on=['time'],how='left').fillna(0).astype('int'))
# df = DataFrame(df_dict)
# df.index = df.time
# print(df['1':'4'])

# print(df)
# df_1 = df_dict[df_dict.duplicated(subset=['time','count'],keep=False)]
# print(df_1)
# df_dict.plot.bar(x='time',y='count',label='day-count')

# plt.show()

# a = []
# for i in range(24):
# 	print('%02.d'%i)

# print('c'>'bs')
# print('%02d'%int('8'))
# print('2018-12-11 09'.split()[1])
# print('92'>'5')


# print(['2014-11-18''2014-11-28'])


# print('a':'g')


df_dict = {'user_id':[1,5,2,2,3,4,4,1],'item_id':[50,50,51,52,60,66,67,70],'behavior':[1,1,1,4,4,1,1,2.3]}
df = DataFrame(df_dict)
# df_groupby = df.groupby(['user_id','item_id'])
df_groupby = df.groupby(['user_id'])
# print(df_groupby.groups)
# for name,group in df_groupby:
# 	print(name)
# 	print(group)

print(df_groupby.cumcount())