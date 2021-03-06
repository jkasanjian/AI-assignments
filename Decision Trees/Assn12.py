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
        tree_one = tree.DecisionTreeClassifier(criterion="gini").fit(self.X_train, self.y_train)
        self.tree_score = tree_one.score(self.X_test, self.y_test)
        #print(tree_score)


    def bagging(self):
        for i in range(40):
            bagging = ensemble.BaggingClassifier(tree.DecisionTreeClassifier(), n_estimators=i+1).fit(self.X_train, self.y_train)
            self.bagging_score[i] = bagging.score(self.X_test, self.y_test)
        #print(self.bagging_score)
        k = list(self.bagging_score.keys())
        v = list(self.bagging_score.values())
        plt.plot(k, v)
        plt.axis([0,39,0,1])
        plt.title("Bagging Graph")
        plt.savefig("Bagging.png")
        plt.show()



    def forest(self):
        max_list = []
        for i in range(1, 102):
            max_feat = random.randrange(1, 31)
            max_list.append(max_feat)

            forest = ensemble.RandomForestClassifier(n_estimators=20, max_features=max_feat).fit(self.X_train, self.y_train)
            self.forest_score[i] = forest.score(self.X_test, self.y_test)

        x_vals = np.array(list(self.forest_score.keys()))
        y_vals = np.array(max_list)
        z_vals = np.array(list(self.forest_score.values()))

        graph = plt.figure()
        axes = Axes3D(graph)
        surf = axes.plot_trisurf(x_vals, y_vals, z_vals, cmap=cm.gnuplot, linewidth=0.5)
        graph.colorbar(surf, shrink=0.5, aspect=5)
        plt.title('Forest Graph')
        plt.savefig('Forest.png')
        plt.show()



    def boost(self):
        i = 1
        while (i < 21):
            boost = ensemble.AdaBoostClassifier(tree.DecisionTreeClassifier(),n_estimators=i).fit(self.X_train, self.y_train)
            self.boost_score[i] = boost.score(self.X_test, self.y_test)
            i += 1
        #print(self.boost_score)
        x = list(self.boost_score.keys())
        y = list(self.boost_score.values())
        plt.plot(x, y)
        plt.axis([0,20,0,1])
        plt.title('Boost Graph')
        plt.savefig("Boost.png")
        plt.show()


    def summary(self):
        return 0


if __name__ == '__main__':
    exp = Evaluation()
    exp.decision_tree()
    exp.bagging()
    exp.forest()
    exp.boost()
    # exp.summary()
