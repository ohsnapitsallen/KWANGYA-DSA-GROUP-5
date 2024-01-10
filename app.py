from flask import Flask, render_template, request
from TestData import *
import time

app = Flask(__name__)

def measure_time(search_function, data_set, target_element):
    start_time = time.time()
    result = search_function(data_set, target_element)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return result, elapsed_time

@app.route('/')
def show_index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/simple_profile')
def simple_profile():
    return render_template('simple_profile.html')

@app.route('/denie_profile')
def denie_profile():
    return render_template('denie_profile.html')

@app.route('/paige_profile')
def paige_profile():
    return render_template('paige_profile.html')


@app.route('/kaye_profile')
def kaye_profile():
    return render_template('kaye_profile.html')

@app.route('/ballena_profile')
def ballena_profile():
    return render_template('ballena_profile.html')

@app.route('/allen_profile')
def allen_profile():
    return render_template('allen_profile.html')

@app.route('/searchalgorithm')
def searchalgorithm():
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search():
    element_to_search = int(request.form['enter-here'])
    test_data_instance = testdata()

    # LinearSearch
    linearsearch_result, linearsearch_time = measure_time(test_data_instance.linear_search, test_data_instance.small_data_set, element_to_search)

    # BinarySearch
    binarysearch_result, binarysearch_time = measure_time(test_data_instance.binary_search, test_data_instance.small_data_set, element_to_search)

    # JumpSearch
    jumpsearch_result, jumpsearch_time = measure_time(test_data_instance.jump_search, test_data_instance.small_data_set, element_to_search)

    # ExponentialSearch
    exponentialsearch_result, exponentialsearch_time = measure_time(test_data_instance.exponential_search, test_data_instance.small_data_set, element_to_search)

    # InterpolationSearch
    interpolationsearch_result, interpolationsearch_time = measure_time(test_data_instance.interpolation_search, test_data_instance.small_data_set, element_to_search)

    # TernarySearch
    ternarysearch_result, ternarysearch_time = measure_time(test_data_instance.ternary_search, test_data_instance.small_data_set, element_to_search)

    return render_template('result.html', 
                           linearsearch_result=linearsearch_result, linearsearch_time=linearsearch_time,
                           binarysearch_result=binarysearch_result, binarysearch_time=binarysearch_time,
                           jumpsearch_result=jumpsearch_result, jumpsearch_time=jumpsearch_time,
                           exponentialsearch_result=exponentialsearch_result, exponentialsearch_time=exponentialsearch_time,
                           interpolationsearch_result=interpolationsearch_result, interpolationsearch_time=interpolationsearch_time,
                           ternarysearch_result=ternarysearch_result, ternarysearch_time=ternarysearch_time)

if __name__ == '__main__':
    app.run(debug=True)