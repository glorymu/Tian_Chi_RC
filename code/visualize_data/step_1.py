import pandas as pd
import sys
import datetime
import matplotlib.pyplot as plt
raw_user_path = '../../data/raw/tianchi_fresh_comp_train_user.csv'
raw_item_path = '../../data/raw/tianchi_fresh_comp_train_item.csv'
dest_path = '../../data/P_data/P.csv'
duplicated_path = '../../data/duplicated/dupli.csv'
def date_Series():
	Date = '2014-11-18'
	a = datetime.datetime.strptime(Date, '%Y-%m-%d')
	print(type(a))

	date_list = []
	for i in range(31):
		delta = datetime.timedelta(days=i)
		temp_date = a + delta
		date_list.append(temp_date.strftime('%Y-%m-%d'))
	length = len(date_list)
	value = [0]*length

	return pd.Series(dict(zip(date_list,value)))
def count_CTR():
	
	# step 1
	#计算转化率
	count_4 = 0
	count_all = 0
	i = 0
	for df in pd.read_csv(raw_user_path,chunksize=100000):
		temp_record = df.behavior_type.value_counts()
		count_4 += temp_record[4]
		count_all += temp_record.sum()
		i += 1
		print('{} chunk finish'.format(i))



	# CTR转化率指标为：1.0 %
	print('CTR转化率指标为：{}'.format(100*round(count_4/count_all,4)),'%')
	


def analyse_everyday():
	#step 2
	#计算D数据集上每一天的用户行为数量

	date_parser = lambda dates:pd.datetime.strptime(dates,'%Y-%m-%d %H')
	raw_ps = date_Series()
	i = 0
	for df in pd.read_csv(raw_user_path,chunksize=200000,):
										# date_parser=date_parser,
										# parse_dates=['time']):
		# print()
		temp_df = df.time.map(lambda x:x.split()[0])
		raw_ps += temp_df.value_counts()
		# print(raw_ps)
		# print(type(df.time[0]))
		# print(df.time[0].split()[0])
		# print(df.time[0])
		# sys.exit()
		i += 1
		# if i == 2:break
		print('{} chunk finish'.format(i))
	#打印每一天的用户行为
	print(raw_ps)

	#转为df
	df_dict = {'time':raw_ps.index,'count':raw_ps.values}
	new_df = pd.DataFrame(df_dict)

	new_df = new_df.set_index('time')
	new_df['count'].plot(kind='bar')
	plt.legend(loc='best')
	plt.grid(True)
	plt.show()


def process_data_P():
	item_df = pd.read_csv(raw_item_path)
	# for df in pd.read_csv(raw_user_path,chunksize=200000,):
	user_df = pd.read_csv(raw_user_path)
	new_df = user_df[user_df.item_id.isin(item_df.item_id)]
	new_df['date'] = new_df['time'].map(lambda x:x.split()[0])
	new_df['hour'] = new_df['time'].map(lambda x:'%02d'%int(x.split()[1]))
	new_df.to_csv(dest_path,index=None)


def analyse_everyday_on_P():

	date_parser = lambda dates:pd.datetime.strptime(dates,'%Y-%m-%d %H')
	raw_ps = date_Series()
	i = 0
	for df in pd.read_csv(dest_path,chunksize=200000,):
										# date_parser=date_parser,
										# parse_dates=['time']):
		# print()
		temp_df = df.time.map(lambda x:x.split()[0])
		raw_ps += temp_df.value_counts()
		# print(raw_ps)
		# print(type(df.time[0]))
		# print(df.time[0].split()[0])
		# print(df.time[0])
		# sys.exit()
		i += 1
		# if i == 2:break
		print('{} chunk finish'.format(i))
	#打印每一天的用户行为
	print(raw_ps)

	#转为df
	df_dict = {'time':raw_ps.index,'count':raw_ps.values}
	new_df = pd.DataFrame(df_dict)

	new_df = new_df.set_index('time')
	new_df['count'].plot(kind='bar')
	plt.legend(loc='best')
	plt.grid(True)
	plt.show()
# analyse_everyday()

def mk_hour():
	a = []
	for i in range(24):
		a.append('%02.d'%i)
	length = len(a)
	value = [0]*length	
	return pd.Series(dict(zip(a,value)))


def analyse_oneDay(date_a):
	df = pd.read_csv(dest_path)
	print(df.columns)
	print(df[:5])
	# df['hour'] = df.hour.map(lambda x:'%02d'%x)
	# print(df.hour[0])
	# print(type(df.hour[0]))
	# sys.exit()
	temp_df = df[df.date==date_a]
	# print(temp_df)
	ds = temp_df.hour.value_counts()
	# print(ds)
	# sys.exit()

	df_dict = {'hour':ds.index, 'count':ds.values}
	new_df = pd.DataFrame(df_dict)
	new_df = new_df.sort_values(by='hour')
	# print(new_df)
	# sys.exit()
	new_df = new_df.set_index('hour')
	new_df['count'].plot(kind='bar')
	plt.legend(loc='best')
	plt.grid(True)
	plt.show()	
	# new_df.plot.bar(x='hour',y='count',label=date_a)
	# plt.legend(loc='best')
	# plt.grid(True)
	# plt.show()
	# pass


def duplicated():
	df = pd.read_csv(raw_user_path)
	duplicated = df[df.duplicated(subset=['user_id','item_id'],keep=False)]
	duplicated.to_csv(duplicated_path,index=None)


if __name__ == '__main__':
	# process_data_P()
	duplicated()
	# analyse_oneDay('2014-12-18')



