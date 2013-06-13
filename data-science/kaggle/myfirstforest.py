
import numpy as np
import csv as csv
import feature
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm

def main():
    csv_file_object = csv.reader(open('csv/train.csv', 'rb'))  # Load in the training csv file
    header = csv_file_object.next()  # Skip the fist line as it is a header
    train_data = []  # Creat a variable called 'train_data'
    for row in csv_file_object:  # Skip through each row in the csv file
        train_data.append(row)  # adding each row to the data variable
    train_data = np.array(train_data)  # Then convert from a list to an array
    
    train_data = feature.extract(train_data, "train")
    
    
    # I need to do the same with the test data now so that the columns are in the same
    # as the training data
    
    test_file_object = csv.reader(open('csv/test.csv', 'rb'))  # Load in the test csv file
    header = test_file_object.next()  # Skip the fist line as it is a header
    test_data = []  # Creat a variable called 'test_data'
    for row in test_file_object:  # Skip through each row in the csv file
        test_data.append(row)  # adding each row to the data variable
    test_data = np.array(test_data)  # Then convert from a list to an array
    
    test_data = feature.extract(test_data, "test")
    
    # The data is now ready to go. So lets train then test!
    
    print 'Training'
    
    cv_data = np.array([row[1:] for row in train_data])
    cv_target = np.array([row[0] for row in train_data])
    
    forest = RandomForestClassifier(n_estimators=100)
    scores = cross_validation.cross_val_score(forest, cv_data, cv_target, cv=5)    
    print "Cross Validation for random forest, scores: " + str(np.mean(scores))
    
    '''
    C_list = [0.1, 0.3, 1, 3, 10, 30, 100, 300, 1000]
    for c in C_list:
        svm_clf = svm.SVC(C=c)
        scores = cross_validation.cross_val_score(svm_clf, cv_data, cv_target, cv=5)
        print "Cross Validation for SVM, scores with C = %f : %f" % (c, np.mean(scores))
    '''     
    
    
    forest = forest.fit(cv_data, cv_target)
    
    print 'Predicting'
    for row in test_data:
        print row
    output = forest.predict(test_data)
    
    open_file_object = csv.writer(open("csv/submission.csv", "wb"))
    test_file_object = csv.reader(open('csv/test.csv', 'rb'))  # Load in the csv file

    
    test_file_object.next()
    i = 0
    for row in test_file_object:
        row.insert(0, output[i].astype(np.uint8))
        open_file_object.writerow(row)
        i += 1
    
    print "Done"
    
if __name__ == "__main__":
    main()
 
