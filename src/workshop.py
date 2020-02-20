def train_model(ModelClass, x_train, y_train, x_test):
    model = ModelClass()
    model.fit(x_train, y_train)
    score = round(model.score(x_train, y_train) * 100, 2)
    print(score)
    return score


def multiply_by10(dataframe):
    return dataframe * 10
