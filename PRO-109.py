import statistics
import math
import pandas as pd

read = pd.read_csv('StudentsPerformance.csv')

math_score = read['math score'].to_list()
reading_score  = read['reading score'].to_list()
writing_score = read['writing score'].to_list()

mean1 = statistics.mean(math_score)
mean2 = statistics.mean(reading_score)
mean3 = statistics.mean(writing_score)

median1 = statistics.median(math_score)
median2 = statistics.median(reading_score)
median3 = statistics.median(writing_score)

mode1 = statistics.mode(math_score)
mode2 = statistics.mode(reading_score)
mode3 = statistics.mode(writing_score)

st_dev_1 = statistics.stdev(math_score)
st_dev_2 = statistics.stdev(reading_score)
st_dev_3 = statistics.stdev(writing_score)

math_first_st_dev_start,math_first_st_dev_end = mean1 - st_dev_1 , mean1 + st_dev_1
math_second_st_dev_start,math_second_st_dev_end = mean1 - (2*st_dev_1), mean1 + (2*st_dev_1)
math_third_st_dev_start,math_third_st_dev_end = mean1 - (3*st_dev_1) , mean1 + (3*st_dev_1)

math_data_in_first_st_dev = [result for result in math_score if result > math_first_st_dev_start and result < math_first_st_dev_end]
math_data_in_second_st_dev = [result2 for result2 in math_score if result2 > math_second_st_dev_start and result2 < math_second_st_dev_end]
math_data_in_third_st_dev = [result3 for result3 in math_score if result3 > math_third_st_dev_start and result3 < math_third_st_dev_end]

math_percentage1 = len(math_data_in_first_st_dev) * 100 / len(math_score)
math_percentage2 = len(math_data_in_second_st_dev) * 100 / len(math_score)
math_percentage3 = len(math_data_in_third_st_dev) * 100 / len(math_score)


reading_first_st_dev_start,reading_first_st_dev_end = mean2 - st_dev_2 , mean2 + st_dev_2
reading_second_st_dev_start,reaidng_second_st_dev_end = mean2 - (2*st_dev_2), mean2 + (2*st_dev_2)
reading_third_st_dev_start,reading_third_st_dev_end = mean2 - (3*st_dev_2) , mean2 + (3*st_dev_2)

reading_data_in_first_st_dev = [result for result in reading_score if result > reading_first_st_dev_start and result < reading_first_st_dev_end]
reading_data_in_second_st_dev = [result2 for result2 in reading_score if result2 > reading_second_st_dev_start and result2 < reaidng_second_st_dev_end]
reading_data_in_third_st_dev = [result3 for result3 in reading_score if result3 > reading_third_st_dev_start and result3 < reading_third_st_dev_end]

reading_percentage1 = len(reading_data_in_first_st_dev) * 100 / len(reading_score)
reading_percentage2 = len(reading_data_in_second_st_dev) * 100 / len(reading_score)
reading_percentage3 = len(reading_data_in_third_st_dev) * 100 / len(reading_score)


writing_first_st_dev_start,writing_first_st_dev_end = mean3 - st_dev_3 , mean3 + st_dev_3
writing_second_st_dev_start,writing_second_st_dev_end = mean3 - (2*st_dev_3), mean3 + (2*st_dev_3)
writing_third_st_dev_start,writing_third_st_dev_end = mean3 - (3*st_dev_3) , mean3 + (3*st_dev_3)

writing_data_in_first_st_dev = [result for result in writing_score if result > writing_first_st_dev_start and result < writing_first_st_dev_end]
writing_data_in_second_st_dev = [result2 for result2 in writing_score if result2 > writing_second_st_dev_start and result2 < writing_second_st_dev_end]
writing_data_in_third_st_dev = [result3 for result3 in writing_score if result3 > writing_third_st_dev_start and result3 < writing_third_st_dev_end]

writing_percentage1 = len(writing_data_in_first_st_dev) * 100 / len(writing_score)
writing_percentage2 = len(writing_data_in_second_st_dev) * 100 / len(writing_score)
writing_percentage3 = len(writing_data_in_third_st_dev) * 100 / len(writing_score)


print('Mean , median , mode of Math marks respectively are :- {},{},{}'.format(mean1 , median1 , mode1))
print('Mean , median , mode of Reading marks respectively are :- {},{},{}'.format(mean2 , median2 , mode2))
print('Mean , median , mode of Writing marks respectively are :- {},{},{}'.format(mean3 , median3 , mode3))

print('')
print('{}% Is the percentage of the data of math marks in the first standard deviation'.format(math_percentage1))
print('{}% Is the percentage of the data of math marks in the second standard deviation'.format(math_percentage2))
print('{}% Is the percentage of the data of math marks in the third standard deviation'.format(math_percentage3))
print('')

print('')
print('{}% Is the percentage of the data of reading marks in the first standard deviation'.format(reading_percentage1))
print('{}% Is the percentage of the data of reading marks in the second standard deviation'.format(reading_percentage2))
print('{}% Is the percentage of the data of reading marks in the third standard deviation'.format(reading_percentage3))
print('')

print('')
print('{}% Is the percentage of the data of writing marks in the first standard deviation'.format(writing_percentage1))
print('{}% Is the percentage of the data of writing marks in the second standard deviation'.format(writing_percentage2))
print('{}% Is the percentage of the data of writing marks in the third standard deviation'.format(writing_percentage3))
print('')