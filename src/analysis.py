from src.myrf import ShArtArgRandomForestClassifier
from src.spider import scratch_weather
from src.exmatch import scratch_info, turn_info, make_dataframe
from sklearn.model_selection import train_test_split


def experiments():
    htmlstr = scratch_weather()
    weather, temp, wind = scratch_info(htmlstr)
    weather = turn_info(weather)
    temp = turn_info(temp)
    wind = turn_info(wind)
    df = make_dataframe(weather, temp, wind)
    data = df.iloc[:, 1:]
    target = df.iloc[:, 0]
    x_train2, x_test2, y_train2, y_test2 = train_test_split(data, target, test_size=0.3, random_state=6)
    myforest = ShArtArgRandomForestClassifier()
    num, accu = myforest.my_artifi(trees=150, x=x_train2, xtest=x_test2, y=y_train2, ytest=y_test2, criterion='entropy')
    print(num, accu)


experiments()


def forecast(df):
    pass
