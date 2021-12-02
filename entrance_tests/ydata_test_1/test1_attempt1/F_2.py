import pandas as pd

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

    df = pd.read_csv(r"C:\Users\sfrie\Ydata_practice\Test_1\titanic.csv", index_col='PassengerId')
        #Index column becomes passengerid, currently, default is the automated index in excel, which does not align with PassenID
    with open(r"C:\Users\sfrie\Ydata_practice\Test_1\input.txt", 'r') as f:
        next(f)

        for line in f:
            passenger_a, passenger_b = (df.loc[int(x)] for x in line.split())
            print(similarity(passenger_a, passenger_b))

if __name__ == '__main__':
    main()