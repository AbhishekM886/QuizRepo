import argparse
import sys

def get_value_from_nested_object(obj, key):
    keys = key.split('/')
    value = obj

    try:
        for k in keys:
            value = value[k]
    except (KeyError, TypeError):
        return None

    return value

def main():
    parser = argparse.ArgumentParser(description='Retrieve value from nested object')
    parser.add_argument('object', help='Nested object in JSON format')
    parser.add_argument('key', help='Key to access the value in the object')

    args = parser.parse_args()
    object_arg = eval(args.object)
    key_arg = args.key

    result = get_value_from_nested_object(object_arg, key_arg)
    print(result)

if __name__ == '__main__':
    main()
