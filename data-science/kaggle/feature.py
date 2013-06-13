import numpy as np

def extract(data, type):
	shift = (-1 if type == "test" else 0)
	
	name_idx = 2 + shift
	gender_idx = 3 + shift
	age_idx = 4 + shift
	sib_idx = 5 + shift
	par_idx = 6 + shift
	ticket_idx = 7 + shift
	fare_idx = 8 + shift
	carbin_idx = 9 + shift
	embark_idx = 10 + shift
	family_idx = 11 + shift
		
	# I need to convert all strings to integer classifiers:
    # Male = 1, female = 0:
	
	data[data[0::, gender_idx] == 'male', gender_idx] = 1
	data[data[0::, gender_idx] == 'female', gender_idx] = 0
    # embark c=0, s=1, q=2
    
	data[data[0::, embark_idx] == 'C', embark_idx] = 0
	data[data[0::, embark_idx] == 'S', embark_idx] = 1
	data[data[0::, embark_idx] == 'Q', embark_idx] = 2
    
    # I need to fill in the gaps of the data and make it complete.
    # So where there is no price, I will assume price on median of that class
    # Where there is no age I will give median of all ages
    
    # All the ages with no data make the median of the data
	data[data[0::, age_idx] == '', age_idx] = np.median(data[data[0::, age_idx]\
                                               != '', age_idx].astype(np.float))
	
    # All missing ebmbarks just make them embark from most common place
	data[data[0::, embark_idx] == '', embark_idx] = \
		np.round(np.mean(data[data[0::, embark_idx] != '', embark_idx].astype(np.float)))
		
	# All the missing prices assume median of their respectice class
	for i in xrange(np.size(data[0::, 0])):
		if data[i, fare_idx] == '':
			data[i, fare_idx] = np.median(data[(data[0::, fare_idx] != '') & \
                                                 (data[0::, 0] == data[i, 0])\
                , fare_idx].astype(np.float))
	
	# Make cabin count as a feature
	for row_idx, row in enumerate(data):
		carbin = row[carbin_idx]
		if not carbin:
			val = 0
		else:
			val = len(str.split(carbin, " "))
		data[row_idx][carbin_idx] = np.int(val)
		
	
	# Use family
	families = []
	for row_idx, row in enumerate(data):
		sib = int(row[sib_idx])
		par = int(row[par_idx])
		families.append([sib + par])
		
	data = np.append(data, families, 1)
    
	data = np.delete(data, [name_idx, sib_idx, par_idx, ticket_idx], 1)  # remove the name data, cabin and ticket3
	
	
	return data
