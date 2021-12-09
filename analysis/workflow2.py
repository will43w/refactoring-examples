from workflow1 import *

if __name__ == "__main__":
    dataAnalyzerBuilder = DataAnalyzerBuilder('samples1.csv', 'samples2.csv', 'weights.csv')
    dataAnalyzerBuilder.load_data()
    dataAnalyzerBuilder.get_results()
    dataAnalyzer = dataAnalyzerBuilder.finish()
    dataAnalyzer.get_d_index()
