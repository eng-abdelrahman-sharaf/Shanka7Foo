import numpy as np

class LinearRegression:
    def __init__(self,learning_rate=0.01,max_iter=1000 , early_stopping = 0.0001):
        self.learning_rate = learning_rate
        self.max_iter = max_iter
        self.early_stopping = early_stopping
        self.weights = None
        self.bias = None
    def fit(self,X,y):
        n_samples,n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        for i in range(self.max_iter):
            y_predicted = np.dot(X , self.weights) + self.bias
            self.ssr = np.sum((y_predicted-y)**2)
            dw = 2/n_samples * np.dot(X.T,(y_predicted-y))
            db = 2/n_samples * np.sum(y_predicted-y)
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
            if(all(abs(dw)< self.early_stopping) or abs(db) < self.early_stopping):
                print("i" , i , "dw", dw , "db", db)
                break
        print(self.ssr)
        
    def predict(self,X):
        return np.dot(X , self.weights)+self.bias

if __name__ == "__main__":
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 3, 4, 5, 5])

    # Create and train the model
    model = LinearRegression(learning_rate=0.01 , max_iter=100000 , early_stopping=0.001)
    model.fit(X, y)

    # Make predictions
    predictions = model.predict(X)
    print("Predictions:", predictions)
    print("Weights:",model.weights)
    print("Bias:",model.bias)