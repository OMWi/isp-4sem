from ..Converter import *

def parse_array(tokens, flag=''):
    array = []

    t = tokens[0]
    if t == ']':
        if flag == 'T':
            return tuple(array), tokens[1:]
        if flag == 'S':
            return set(array), tokens[1:]
        return array, tokens[1:]

    while t != ']':
        result, tokens = parse(tokens)
        array.append(result)

        t = tokens[0]
        if t == ']':
            if flag == 'T':
                return tuple(array), tokens[1:]            
            if flag == 'S':
                return set(array), tokens[1:]            
            return array, tokens[1:]
        elif t != ',':
            raise SyntaxError('Expected comma after object in array')
        else:
            tokens = tokens[1:]

    raise SyntaxError('Expected end-of-array bracket')

def parse_object(tokens, flag=''):
    obj = {}

    t = tokens[0]
    if t == '}':
        return obj, tokens[1:]

    while t != '}':
        if len(tokens) > 1 and tokens[0] == 'T' and tokens[1] == '[':
            key, tokens = parse_array(tokens[2:], 'T')
        else:
            key = tokens[0]
            tokens = tokens[1:]
        
        if tokens[0] != ':':
            raise SyntaxError('Expected colon after key in object, got: {}'.format(t))

        value, tokens = parse(tokens[1:])

        obj[key] = value

        t = tokens[0]

        if t == '}':
            if flag == 'D':
                return obj, tokens[1:]
            else:
                return dict_to_obj(obj), tokens[1:]
        elif t != ',':
            raise SyntaxError('Expected comma after pair in object, got: {}'.format(t))

        tokens = tokens[1:]

    raise SyntaxError('Expected end-of-object bracket')

def parse(tokens, flag=''):
    if tokens[0] in ['D', 'T', 'S']:
        flag = tokens[0]
        tokens = tokens[1:]

    t = tokens[0]

    if t == '[':
        return parse_array(tokens[1:], flag)
    elif t == '{':
        return parse_object(tokens[1:], flag)
    else:
        return t, tokens[1:]
