from flask import Flask, render_template, request
from TestData import *
from infixtopostfix import *
from hash import *
from MRTLRT import *
from Sorting import *
import time

app = Flask(__name__)
string_queue = []
hash_table = HashTable()

def measure_time(search_function, data_set, target_element):
    start_time = time.time()
    result = search_function(data_set, target_element)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return result, elapsed_time

@app.context_processor
def utility_processor():
    def enumerate(list_of_items):
        return zip(range(len(list_of_items)), list_of_items)
    return dict(enumerate=enumerate)

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

@app.route('/infixtopostfix')
def infix():
    return render_template('infix.html')

@app.route('/postfix', methods=['POST'])
def postfix():
    infix_expression = request.form['enter-here']
    postfix_steps = infix_to_postfix(infix_expression)
    return render_template('postfix.html', postfix_steps=postfix_steps)

@app.route('/queuedequeue')
def queuedequeue():
    return render_template('queuedequeue.html', queue=string_queue)

@app.route('/newqueue', methods=['POST'])
def newqueue():
    user_input = request.form['enter-here']

    if 'queue_button' in request.form:
        string_queue.append(user_input)
        dequeued_item = None
    elif 'dequeue_button' in request.form:
        if user_input in string_queue:
            string_queue.remove(user_input)
            dequeued_item = user_input
        else:
            dequeued_item = None

    return render_template('queuedequeue.html', queue=string_queue, dequeued_item=dequeued_item)

@app.route('/hashtable')
def input():
    return render_template('input.html')

@app.route('/hashtableoutput', methods=['POST'])
def output():
    hash_function = request.form['hash_function']
    num_commands = int(request.form['num_commands'])
    commands = request.form['commands'].splitlines()

    hash_table = HashTable()
    for command in commands:
        if command.startswith('del '):
            word = command[4:]
            hash_table.delete(word, getattr(hash_table, hash_function))
        else:
            hash_table.insert(command, getattr(hash_table, hash_function))

    return render_template('output.html', hash_table=hash_table)

@app.route('/graph')
def GraphInput():
    return render_template('graph.html', stations=stations)

@app.route('/graphresult', methods=['POST'])
def shortest_path():
    source_station = request.form['source']
    target_station = request.form['target']

    shortest_path_result = find_shortest_path(LRTMRT, source_station, target_station)

    return render_template('graph.html', stations=stations, source=source_station, target=target_station, shortest_path=shortest_path_result)

def parse_elements(elements_str):
    elements = elements_str.split('\n')
    parsed_elements = []
    for element in elements:
        element = element.strip()
        if element:
            try:
                parsed_element = int(element)
            except ValueError:
                parsed_element = element
            parsed_elements.append(parsed_element)
    return parsed_elements

@app.route('/sorting')
def Sorter():
    return render_template('sorting.html')

@app.route('/sort', methods=['POST'])
def sort():
    elements_str = request.form.get('elements')
    elements = parse_elements(elements_str)
    
    algorithm = request.form.get('algorithm')
    sorted_elements = []
    
    if algorithm == 'bubble':
        sorted_elements = bubble_sort(elements.copy())
    elif algorithm == 'quick':
        sorted_elements = quick_sort(elements.copy())
    elif algorithm == 'merge':
        sorted_elements = merge_sort(elements.copy())
    elif algorithm == 'selection':
        sorted_elements = selection_sort(elements.copy())
    elif algorithm == 'insertion':
        sorted_elements = insertion_sort(elements.copy())
    
    return render_template('sorting.html', elements=elements, sorted_elements=sorted_elements, selected_algorithm=algorithm)

if __name__ == '__main__':
    app.run(debug=True)