import pandas as pd

#I am reciving the right maxes for the firs and last input. When I input 891 however, I am reciving an output of 570, with a max of .98.
#The test says the right output is 383. However, when I hard code 383 into passenger b, i am reciving .968, which is less than .98

def similarity(passenger_a, passenger_b):

    result = 0  
    if passenger_a.Pclass == passenger_b.Pclass:  
        result += 1  
    if passenger_a.Sex == passenger_b.Sex:  
        result += 3  
    if passenger_a.SibSp == passenger_b.SibSp:  
        result += 1  
    if passenger_a.Parch == passenger_b.Parch:  
        result += 1  
    result += max(0, 2 - abs(passenger_a.Age - passenger_b.Age) / 10.0)  
    result += max(0, 2 - abs(passenger_a.Fare - passenger_b.Fare) / 5.0)  
    return result / 10.0


def main():

    df = pd.read_csv(r"C:\Users\sfrie\Ydata_practice\Test_1\f_titanic.csv", index_col='PassengerId')
        #Index column becomes passengerid, currently, default is the automated index in excel, which does not align with PassenID
    with open(r"C:\Users\sfrie\Ydata_practice\Test_1\f3_input.txt", 'r') as f:
        next(f)

        for line in f:
            dict = {}
            print('a: ', line)
            max_list = [] 
            passenger_a = df.loc[int(line)]

            for passenger_test in df.index:
                
                passenger_b = df.loc[passenger_test]
                number = similarity(passenger_a, passenger_b)
                if number != 1:
                    dict[number] = [line, passenger_test]
                    #max_list.append(number)

            #print(max(max_list))
            max_key = max(dict.keys())
            print(dict[max_key][1])

if __name__ == '__main__':
    main()