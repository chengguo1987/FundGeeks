# coding=utf-8

import argparse

# Define the main function
def main():

	parser = argparse.ArgumentParser(description='manual to this script')
	parser.add_argument('-i','--ini_value', type=float, default = 5000.00)
	parser.add_argument('-d','--increment', type=float, default = 500.00)
	parser.add_argument('-o','--option', type=str, default = '0')
	parser.add_argument('-t','--target_profit', type=float, default = 0.0)
	args = parser.parse_args()


	# initial investment
	#initial_value = float(input('Enter initial value: '))
	initial_value = args.ini_value

	# incremental investment everyday
	#delta = float(input('Enter delta: '))
	delta = args.increment

	# Load data from file, value started from present day
	input_file = open(get_input(), 'r')

	# Apply Stoploss/targetProfit or not
	#option = input('Default 0 | SL & TP 1: ')
	option = args.option

	# Set the target profit
	#tp = float(input('Enter tp: '))
	tp = args.target_profit

	# redemption rate
	rr = 0.005

	# List store original unit price
	num = list()

	# Present Day/Previous Day Ratio
	ratio = list()

	# load unit price value to list
	for line in input_file.readlines():
		num.append(float(line))
	
	# reverse unit price list
	num.reverse()

	# pair = dict()
	ratio.append(1.0)
	# pair[num[0]] = 1.0

	total_val = initial_value
	total_inv = initial_value
	total_yld = 0.0

	for day in range(1, len(num)):
		ratio.append(num[day]/num[day-1])
		# pair[num[day]] = ratio[day]

		total_val += delta
		total_inv += delta
		total_val *= ratio[day]
		x = num[day]/num[0]
	

		if option != '0': 
			if day > 7:
				
				if(x>1.05):
					#print(num[day], total_inv, total_val)
					total_inv -= under_weight(total_val, tp)
					total_val -= under_weight(total_val, tp)

				if(x<0.98):
					total_inv += over_weight(total_val)
					total_val -= under_weight(total_val)

	total_yld = total_val*(1.0-rr) - total_inv

	'''
	for p in pair:
		print(p, pair[p])
	'''

	print()
	print('Number of days: ', len(num))
	print('Total value: %.2f ' % total_val)
	print('Total investment: %.2f '% total_inv)
	print('Total yield: %.2f '% total_yld)

def over_weight(current_value):
	return current_value*0.25

def under_weight(current_value, tp):
	return current_value*tp

def get_input():
	file = input('Enter the source file name: ')
	return file

main()