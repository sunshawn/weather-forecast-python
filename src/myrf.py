from sklearn.ensemble import RandomForestClassifier


class ShArtArgRandomForestClassifier(RandomForestClassifier):

    def my_artifi(self, trees, x, y, xtest, ytest, criterion='gini', max_features='sqrt'):
        rightl = []
        for i in range(1, trees):
            self.n_estimators = i
            self.criterion = criterion
            self.max_features = max_features
            self.fit(x, y)
            predict = self.predict(xtest)
            rights = (predict == ytest).mean()
            rightl.append(rights)
        return rightl.index(max(rightl)) + 1, max(rightl)
