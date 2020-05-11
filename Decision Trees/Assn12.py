from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn import tree, ensemble
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


class Evaluation:

    def __init__(self):
        self.cancer = load_breast_cancer()
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.cancer.data, self.cancer.target, test_size=0.9)
        self.tree_score = 0
        self.bagging_score = {}
        self.boost_score = {}
        self.forest_score = {}

    def decision_tree(self):
        t1 = tree.DecisionTreeClassifier(
            criterion="gini").fit(self.X_train, self.y_train)
        tree_score = t1.score(self.X_test, self.y_test)
        print(tree_score)


    def bagging(self):
        for i in range(10):
            bagging = ensemble.BaggingClassifier(
                tree.DecisionTreeClassifier(), n_estimators=50*i + 1).fit(self.X_train, self.y_train)
            self.bagging_score[50*i +1] = bagging.score(self.X_test, self.y_test)
        print(self.bagging_score)
        


    def forest(self):
        max_list = []
        for i in range(1, 102):
            max_feat = random.randrange(1, 31)
            max_list.append(max_feat)
            
            forest = ensemble.RandomForestClassifier(
                n_estimators=20, max_features=max_feat).fit(self.X_train, self.y_train)
            self.forest_score[i] = forest.score(self.X_test, self.y_test)
            
        x_vals = np.array(list(self.forest_score.keys()))
        y_vals = np.array(max_list)
        z_vals = np.array(list(self.forest_score.values()))

        graph = plt.figure()
        axes = Axes3D(graph)
        surf = axes.plot_trisurf(x_vals, y_vals, z_vals, cmap=cm.gnuplot, linewidth=0.5)
        graph.colorbar(surf, shrink=0.5, aspect=5)
        plt.title('Forest Graph')
        plt.savefig('forest.png')
        plt.show()



    def boost(self):
        return 0


    def summary(self):
        return 0


if __name__ == '__main__':
    exp = Evaluation()
    exp.decision_tree()
    exp.bagging()
    exp.forest()
    exp.boost()
    exp.summary()