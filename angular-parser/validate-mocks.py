import sys

def parse_dependency(line):
    parts = line.split(': ')

    if len(parts) != 2:
        return None

    serviceName = parts[1].replace(',', '').replace('\n', '')

    return serviceName


def parse_constructor(filename):
    all_dependencies = []
    try:
        with open(filename, 'r') as file:
            in_constructor = False
            for line in file:
                if not in_constructor and 'constructor(' in line:
                    in_constructor = True
                elif in_constructor and '):' in line:
                    break
                elif in_constructor:
                    dep = parse_dependency(line)
                    if dep:
                        all_dependencies.append(dep)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    
    return all_dependencies


def parse_describes(filename):
    '''
    Parse each describe into an array of lines until the first test

    returns a 2d list, a list for each describe
    '''
    all_describes = []
    try:
        with open(filename, 'r') as file:
            in_describe = False
            lines_in_describe = []
            for line in file:
                if not in_describe and 'describe(' in line:
                    in_describe = True
                elif in_describe and 'it(\'' in line:
                    in_describe = False
                    all_describes.append(lines_in_describe)
                    lines_in_describe = []
                elif in_describe:
                    lines_in_describe.append(line)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    
    return all_describes

def validate_providers(describe, dependencies):
    dep_dict = {}
    for dep in dependencies:
        dep_dict[dep] = False

    describe_as_string = str(describe)

    for dep in dependencies:
        provide_str = f'provide: {dep},'
        if provide_str in describe_as_string:
            dep_dict[dep] = True
    
    error_str = ''
    for dep in dep_dict.keys():
        if dep_dict[dep] == False:
            error_str += f'No provider for: {dep}\n'
    
    return error_str


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: validate-mocks.py <test_file_path>")
        sys.exit(1)

    ts_file = sys.argv[1]
    spec_file = ts_file.replace('.ts', '.spec.ts')

    

    dependencies = []
    describes = []
    dependencies = parse_constructor(ts_file)
    describes = parse_describes(spec_file)

    for i, describe in enumerate(describes, 1):
        error_str = validate_providers(describe, dependencies)

        if error_str != '':
            print(f'{spec_file}: Failure in Describe {i}:')
            print(error_str)








