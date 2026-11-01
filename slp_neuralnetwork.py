import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=10):
        # self.weights[0] will be the bias, the rest are feature weights
        self.weights = np.zeros(input_size + 1)
        self.lr = learning_rate
        self.epochs = epochs

    def activation_function(self, x):
        return 1 if x >= 0 else 0

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        return self.activation_function(summation)

    def train(self, training_inputs, labels):
        for epoch in range(self.epochs):
            total_error = 0
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                error = label - prediction
                if error != 0:
                    total_error += abs(error)
                    self.weights[0] += self.lr * error
                    self.weights[1:] += self.lr * error * inputs
            if total_error == 0:
                break

if __name__ == "__main__":
    # Corrected input values for the AND gate
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])

    # Corrected target output values
    y = np.array([0, 0, 0, 1])

    perceptron = Perceptron(input_size=2, learning_rate=0.1, epochs=10)
    perceptron.train(X, y)

    print("Testing Final Predictions:")
    for test_input in X:
        print(f"Input: {test_input}->o/p:{perceptron.predict(test_input)}")
