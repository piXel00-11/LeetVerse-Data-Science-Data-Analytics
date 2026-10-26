# LIST QUESTIONS

#Q1: chunk_list(): splits a list into smaller sub lists of a given size

def chunk_list():
    a=input("Enter the list (with spaces between elements):")
    lst=a.split()
    b=[]
    c=int(input("Enter the chunk size:"))
    for i in range (0, len(lst), c):
        chunk=lst[i:i+c]
        b.append(chunk)
    print("Original List:", lst)
    print("Divided List:", b)



#Q2: flatten_list(): Takes a list of nested lists and flattens it completely.

def flatten_list(nested_lst):
    flat = []
    for item in nested_lst:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat



#Q3: Find all continuous sublists within a list of integers where the sum of elements equals a target value k. Return their starting and ending indices as a list of tuples.

def find_sublists(lst, k):
    result = []
    n = len(lst)
    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += lst[end]
            if current_sum == k:
                result.append((start, end))   
    return result


# TUPLE QUESTIONS

#Q1: You receive a list of tuples representing sales records: (product_name, quantity, price_per_unit). Write a function to calculate the total revenue per unique product and return it as a sorted list of tuples (product_name, total_revenue) in descending order of revenue.

def aggregate_sales(records):
    revenue_map = {}
    for record in records:
        product = record[0]
        qty = record[1]
        price = record[2]
        
        revenue = qty * price
        if product in revenue_map:
            revenue_map[product] += revenue
        else:
            revenue_map[product] = revenue
    sales_list = list(revenue_map.items())
    for i in range(len(sales_list)):
        for j in range(0, len(sales_list) - i - 1):
            if sales_list[j][1] < sales_list[j + 1][1]:
                # Swap elements
                sales_list[j], sales_list[j + 1] = sales_list[j + 1], sales_list[j]
                
    return sales_list

#Q2: Write a function that takes a matrix represented as a tuple of tuples and returns its mathematical transpose, also as a tuple of tuples. Do not use external libraries like NumPy.


def transpose_matrix(matrix):
    if not matrix:
        return ()
        
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    transposed = []
    for col in range(num_cols):
        new_row = []
        for row in range(num_rows):
            new_row.append(matrix[row][col])
        transposed.append(tuple(new_row))
        
    return tuple(transposed)


# DICTIONARY QUESTIONS

#Q1: Write a function deep_merge(d1, d2) that merges two dictionaries. If a key exists in both and the values are dictionaries, merge them recursively. If the values are not dictionaries, the value from d2 should overwrite d1.


def deep_merge(d1, d2):
    result = d1.copy()    
    for key in d2:
        value = d2[key]
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
            
    return result


#Q3: Write a function to invert a dictionary. Since multiple keys might have the same value, group the original keys into a set under their new inverted key.


def invert_and_group(d):
    inverted = {}    
    for key in d:
        val = d[key]
        if val not in inverted:
            inverted[val] = set()
        inverted[val].add(key)
        
    return inverted


