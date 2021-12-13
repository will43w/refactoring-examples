import numpy as np

class DataAnalyzer:
    def __init__(self, data1, data2, weights, results):
        self.data1 = data1
        self.data2 = data2
        self.weights = weights
        self.results = results
    
    def get_number_of_critial_values(self):
        number_of_critial_values = np.count_nonzero(self.results > 5)
        if number_of_critial_values == 1:
            print("criticality: 1 result above 5")
        else:
            print(f"criticality: {number_of_critial_values} results above 5")

    def get_d_index(self):
        print(f"d-index: {np.average(self.results)}")

class DataAnalyzerBuilder:
    def __init__(self, path_data1, path_data2, path_weights):
        self.dataAnalyzer = DataAnalyzer(None, None, None, None)

        self.path_data1 = path_data1
        self.path_data2 = path_data2
        self.path_weights = path_weights

    def load_data(self):
        self.dataAnalyzer.data1 = np.loadtxt(self.path_data1, delimiter = ',')
        self.dataAnalyzer.data2 = np.loadtxt(self.path_data2, delimiter = ',')
        self.dataAnalyzer.weights = np.loadtxt(self.path_weights, delimiter = ',')

    def get_results(self):
        self.dataAnalyzer.results = np.abs(self.data1 - self.data2) @ self.weights # Dimensions are assumed to be compatible

    def validate(self):
        assert(self.dataAnalyzer.data1 is not None)
        assert(self.dataAnalyzer.data2 is not None)
        assert(self.dataAnalyzer.weights is not None)
        assert(self.dataAnalyzer.results is not None)

    def finish(self):
        self.validate()
        return self.dataAnalyzer

if __name__ == "__main__":
    dataAnalyzerBuilder = DataAnalyzerBuilder('data1.csv', 'data2.csv', 'weights.csv')
    dataAnalyzerBuilder.load_data()
    dataAnalyzerBuilder.get_results()
    dataAnalyzer = dataAnalyzerBuilder.finish()
    dataAnalyzer.get_number_of_critial_values()
