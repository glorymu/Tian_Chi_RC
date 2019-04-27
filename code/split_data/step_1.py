'''
@author: mumu
'''



raw_user_path = '../../data/raw/tianchi_fresh_comp_train_user.csv'
raw_item_path = '../../data/raw/tianchi_fresh_comp_train_item.csv'


path_df_part_1 = "../../data/split_raw/df_part_1.csv"
path_df_part_2 = "../../data/split_raw/df_part_2.csv"
path_df_part_3 = "../../data/split_raw/df_part_3.csv"

path_df_part_1_tar = "../../data/split_raw/df_part_1_tar.csv"
path_df_part_2_tar = "../../data/split_raw/df_part_2_tar.csv"

path_df_part_1_uic_label = "../../data/split_raw/df_part_1_uic_label.csv"
path_df_part_2_uic_label = "../../data/split_raw/df_part_2_uic_label.csv"
path_df_part_3_uic       = "../../data/split_raw/df_part_3_uic.csv"

import pandas as pd
import sys
import numpy as np
def split_1_2_3():
	batch = 0
	dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H')
	# for df  in  pd.read_csv(raw_user_path,parse_dates=['time']
	# 									,date_parser=dateparse,
	# 									chunksize=100000):
	df = pd.read_csv(raw_user_path,parse_dates=['time']
										,date_parser=dateparse)
	df.index = df.time
	# print(df.columns)
	# print(df[:2])
	# sys.exit()
	df_part_1     = df['2014-11-22':'2014-11-27']
	df_part_1_tar = df['2014-11-28']
	df_part_2     = df['2014-11-29':'2014-12-04']
	df_part_2_tar = df['2014-12-05']
	df_part_3     = df['2014-12-13':'2014-12-18']

	df_part_1.to_csv(path_df_part_1,  
					 columns=['time','user_id','item_id','behavior_type','item_category'],
					 index=None)        
	df_part_1_tar.to_csv(path_df_part_1_tar,
					 columns=['time','user_id','item_id','behavior_type','item_category'],
					  index=None)
	df_part_2.to_csv(path_df_part_2,  
					 columns=['time','user_id','item_id','behavior_type','item_category'],
					  index=None)  
	df_part_2_tar.to_csv(path_df_part_2_tar,
					 columns=['time','user_id','item_id','behavior_type','item_category'],
					  index=None)   
	df_part_3.to_csv(path_df_part_3,  
					 columns=['time','user_id','item_id','behavior_type','item_category'],
					  index=None)		
		# batch += 1
		# print('chunk %d done.' %batch) 
		# sys.exit()
	print('mumu split finished')

def mk_label():
	#为part1和part2两个部分构建标签
	df_part_1 = pd.read_csv(path_df_part_1)
	# print(df_part_1.time[0])
	# print(type(df_part_1.time[0]))
	# print(type(df_part_1.user_id[0]))
	# print(type(df_part_1.user_id[0]))
	# print(type(df_part_1.time[0]))
	# print(df_part_1.time[0])
	# sys.exit()
	# print(df_part_1[:5])
	df_part_1.drop_duplicates(['user_id','item_id'],inplace=True)
	new_part_1 = df_part_1[['user_id', 'item_id', 'item_category']]
	df_part_1_tar = pd.read_csv(path_df_part_1_tar)

	# print(df_part_1[:5])


	df_part_1_label_1 = df_part_1_tar[df_part_1_tar.behavior_type==1][['user_id', 'item_id', 'item_category']]
	# print(df_part_1_label_1[:5])
	df_part_1_label_1.drop_duplicates(['user_id', 'item_id', 'item_category'],inplace=True)
	df_part_1_label_1['label'] = 1
	# print(df_part_1_label_1[:5])

	df_part_1_label = pd.merge(new_part_1,df_part_1_label_1,
						on=['user_id', 'item_id', 'item_category'],
								how='left',).fillna(0).astype('int')
	print(df_part_1_label[:5])
	# print(df_part_1_label[7525:7526].astype(np.float32))
	# sys.exit()

	df_part_1_label.to_csv(path_df_part_1_uic_label,index=None)	



	df_part_2 = pd.read_csv(path_df_part_2)

	df_part_2.drop_duplicates(['user_id','item_id'],inplace=True)
	new_part_2 = df_part_2[['user_id', 'item_id', 'item_category']]
	df_part_2_tar = pd.read_csv(path_df_part_2_tar)

	df_part_2_label_1 = df_part_2_tar[df_part_2_tar.behavior_type==1][['user_id', 'item_id', 'item_category']]
	df_part_2_label_1.drop_duplicates(['user_id', 'item_id', 'item_category'],inplace=True)
	df_part_2_label_1['label'] = 1

	df_part_2_label = pd.merge(new_part_2,df_part_2_label_1,
						on=['user_id', 'item_id', 'item_category'],
								how='left',).fillna(0).astype('int')
	print(df_part_2_label[:5])

	df_part_2_label.to_csv(path_df_part_2_uic_label,index=None)



	df_part_3 = pd.read_csv(path_df_part_3)
	df_part_3.drop_duplicates(['user_id','item_id'],inplace=True)
	new_part_3 = df_part_3[['user_id', 'item_id', 'item_category']]
	new_part_3.to_csv(path_df_part_3_uic, index=None)


if __name__ == '__main__':
	# split_1_2_3()
	mk_label() 