import pandas as pd
import seaborn as sns
import difflib
from sklearn import tree
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score

data = pd.read_csv("dt.csv")


class tree:
    def __init__(self, data):
        self.data = data


    def split_data(data):
        X = data[['Вредоносность', 'Регистрация в реестре', 'Используется арендованное помещение', 'Категория объекта', 'Колличество жалоб на предприятие']]
        y = data[['Маскируют свою деятельность']]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, train_size=0.75)

        return [X_train, X_test, y_train, y_test]


    def get_results(X_train, X_test, y_train, y_test):

        max_depth_values = range(1, 40)
        scores_data = pd.DataFrame()

        for max_depth in max_depth_values:
            clf = tree.DecisionTreeClassifier(criterion="entropy", max_depth=max_depth)
            clf.fit(X_train, y_train)
            train_score = clf.score(X_train, y_train)
            test_score = clf.score(X_test, y_test)

            temp_score_data = pd.DataFrame({
                "max_depth": [max_depth],
                "train_score": [train_score],
                "test_score": [test_score]
            })

            scores_data = scores_data.append(temp_score_data)

                
        scores_data_long = pd.melt(scores_data, id_vars = ['max_depth'], value_vars = ['train_score','test_score'], var_name = 'set_type', value_name = 'score')
        return scores_data_long


    def get_best(X_train, y_train):
        parameters = {'max_depth': range(3, 400)}
        clf = GridSearchCV(tree.DecisionTreeClassifier(), parameters, n_jobs = 4)
        clf.fit(X_train, y_train)
        tree_model = clf.best_estimator_
        return clf.best_score_, clf.best_params_ 


    def paint(x, y, hue, data):
        sns.lineplot(x=x, y=y, hue=hue, data=data)






# sns.lineplot(x='max_depth', y='score', hue='set_type', data=scores_data_long)


# scores_data_long.plot(x='max_depth', y='score')

# tree.plot_tree(clf);