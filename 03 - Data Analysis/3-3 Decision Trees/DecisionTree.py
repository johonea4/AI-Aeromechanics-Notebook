import numpy as np
from collections import Counter
import time


class DecisionNode:
    def __init__(self, leftNode, rightNode, decision_function, class_label=None):
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.decision_function = decision_function
        self.class_label = class_label

    def decide(self, feature):
        """Get a child node based on the decision function.

        Args:
            feature (list(int)): vector for feature.

        Return:
            Class label if a leaf node, otherwise a child node.
        """

        if self.class_label is not None:
            return self.class_label

        elif self.decision_function(feature):
            return self.leftNode.decide(feature)

        else:
            return self.rightNode.decide(feature)

class DecisionTree:
    def __init__(self, depthLimit = float('inf')):
        self.depthLimit = depthLimit
        self.root = None

    def gini_impurity(self, class_vector):
        nvals = len(class_vector)
        n0 = 0
        n1 = 0

        if nvals <= 0: 
            return 0
        for c in class_vector:
            if(c==0):
                n0+=1
            elif(c==1):
                n1+=1

        impurity = 1 - (pow((n0/nvals),2) + pow((n1/nvals),2))

        return impurity


    def gini_gain(self, previous_classes, current_classes):
        nvals = len(previous_classes)
        if nvals <= 0:
            return 0
        impurity = self.gini_impurity(previous_classes)
        summation = 0

        for c in current_classes:
            summation += (len(c)/nvals) * self.gini_impurity(c)

        gain = impurity - summation

        return gain

    def testAllSame(self,classes):
        test = classes[0]
        for c in classes:
            if c != test:
                return None
        return DecisionNode(None,None,None,test)

    def testDepth(self,depth,numAttr,classes):
        #if depth > self.depth_limit or depth >= numAttr:
        if depth > self.depthLimit:
            nt = classes.count(1)
            nf = classes.count(0)
            if nt>nf:
                return DecisionNode(None,None,None,1)
            elif nf>nt:
                return DecisionNode(None,None,None,0)
            else:
                return DecisionNode(None,None,None,classes[0])
        return None

    def getThresh(self,arr):
        return np.average(arr)

    def getGains(self,features,classes,numAttr):
        gains = list()
        splitlist = list()

        for i in range(numAttr):
            attr = features[:,i]
            if attr[0]==None or np.isnan(attr[0]):
                splitlist.append([list(),list()])
                gains.append(-1)
                continue
            thresh = self.getThresh(attr)
            pList = list()
            nList = list()
            for j in range(len(attr)):
                if(attr[j]>=thresh):
                    pList.append(classes[j])
                else:
                    nList.append(classes[j])
            splitlist.append([pList,nList])
            gains.append(self.gini_gain(classes,splitlist[i]))
        alpha_max = max(gains)
        alpha_index = gains.index(alpha_max)

        results = dict()
        results['gains'] = gains
        results['split_classes'] = splitlist[alpha_index]
        results['alpha_max'] = alpha_max
        results['alpha_index'] = alpha_index
        results['thresh'] = self.getThresh(features[:,alpha_index])
        return results

    def BuildTree(self,features,classes):
        self.root = self.__BuildTree__(features,classes)

    def __BuildTree__(self, features, classes, depth=0):
        #First Check if all classes are the same
        test = self.testAllSame(classes)
        if test != None:
            return test

        #Next Check if depth > depthLimit and return the most frequent class
        numfeatures = np.size(features,0)
        numattributes = np.size(features,1)

        test = self.testDepth(depth,numattributes,classes)
        if test != None:
            return test
        
        #Get all the GiniGains for the features
        results = self.getGains(features,classes,numattributes)
        alpha_index = results['alpha_index']
        thresh = results['thresh']
        posFeatures = list()
        negFeatures = list()
        for i,f in enumerate(features):
            if f[alpha_index]>=thresh:
                posFeatures.append(list(f))
                # posFeatures[len(posFeatures)-1][alpha_index] = None
            else:
                negFeatures.append(list(f))
                # negFeatures[len(negFeatures)-1][alpha_index] = None
        if len(results['split_classes'][0])<=0:
            return self.testDepth(self.depthLimit+1,numattributes,results['split_classes'][1])
        elif len(results['split_classes'][1])<=0:
            return self.testDepth(self.depthLimit+1,numattributes,results['split_classes'][0])

        node = DecisionNode(None,None,lambda feat: feat[alpha_index]>=thresh)
        node.leftNode = self.__BuildTree__(np.array(posFeatures),results['split_classes'][0],depth+1)
        node.rightNode = self.__BuildTree__(np.array(negFeatures),results['split_classes'][1],depth+1)

        return node

    def classify(self, features):
        class_labels = []

        for feature in features:
            class_labels.append(self.root.decide(feature))

        return class_labels
