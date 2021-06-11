from ..Converter import *

def parse_array(tokens, flag='', level=0):
    array = []

    main_flag = flag

    t = tokens[0]
    if t == ']':
        if flag == 'T':
            return tuple(array), tokens[1:], level
        if flag == 'S':
            return set(array), tokens[1:], level
        return array, tokens[1:], level

    while t != ']':
        result, tokens, level = parse(tokens, flag=flag, level=level)
        
        array.append(result)

        flag = main_flag

        t = tokens[0]
        if t == ']':
            if flag == 'T':
                return tuple(array), tokens[1:], level          
            if flag == 'S':
                return set(array), tokens[1:], level           
            return array, tokens[1:], level
        elif t != ',':
            raise SyntaxError('Expected comma after object in array')
        else:
            tokens = tokens[1:]

    raise SyntaxError('Expected end-of-array bracket')

def parse_object(tokens, flag='', level=0):
    obj = {}

    main_flag = flag

    current_level = level

    while len(tokens) > 2 and current_level == level:
        prev_tokens = tokens
        if len(tokens) > 1 and tokens[0] in ['D', 'T', 'S', 'L', 'O']:
            flag = tokens[0]
            tokens = tokens[1:]
        else:
            flag = main_flag

        if len(tokens) > 0 and tokens[0] == '[' and flag != 'T':
            current_level = 0
            tokens = tokens[1:]
            while tokens[0] != ']':
                if tokens[0] == '.':
                    tokens = tokens[1:]
                    continue
                if tokens[0] == 'T':
                    current_key, tokens, current_level = parse(tokens, flag=flag, level=current_level)
                else:
                    current_key = tokens[0]
                    tokens = tokens[1:]

                current_level += 1
                last_key = current_key

            if current_level <= level:
                tokens = prev_tokens
                return obj, tokens, level - 1

            tokens = tokens[1:]
            key = last_key

            value, tokens, current_level = parse(tokens, flag=flag, level=current_level)

            obj[key] = value
        else:
            if flag == 'T' and tokens[0] == '[':
                key, tokens, current_level = parse_array(tokens[1:], level=level)
                key = tuple(key)
            else:
                key = tokens[0]

                tokens = tokens[1:]

            if tokens[0] == '=':
                tokens = tokens[1:]
            else:
                return key, tokens, current_level
            
            value, tokens, current_level = parse(tokens, flag=flag, level=level)

            obj[key] = value
        
        if (len(tokens) > 0 and (tokens[0] == ',' or tokens[0] == ']')
            or len(tokens) == 0):
            return obj, tokens, 0 if current_level <= 0 else current_level - 1

    return obj, tokens, 0 if current_level <= 0 else current_level - 1

def parse(tokens, flag='', level=0):
    main_flag = flag
    prev_tokens = tokens

    if ((len(tokens) > 1 and tokens[0] in ['D', 'T', 'S', 'L', 'O'] and tokens[1] != '=') or
        len(tokens) == 1 and tokens[0] in ['D', 'T', 'S', 'L', 'O']):
        flag = tokens[0]
        tokens = tokens[1:]

    if (len(tokens) == 0 or (len(tokens) > 0 and (tokens[0] == ']' or
                                                tokens[0] == ','))):
        return {}, tokens, level

    t = tokens[0]

    if t == '[' and (flag == 'L' or flag == 'S' or flag == 'T'):
        result, tokens, _ = parse_array(tokens[1:], flag, level)

        if len(tokens) > 0 and tokens[0] == '=':
            tokens = prev_tokens
            flag = main_flag

            result = parse_object(tokens, flag, level)
            if flag == 'D':
                    return result
            else:
                return dict_to_obj(result[0]), result[1], result[2]
        else:
            return result, tokens, level

        return parse_array(tokens[1:], flag, level)
    elif (t == '[' or (len(tokens) > 1 and tokens[1] == '=') or 
                t == 'D' or t == 'O' or t == 'T'):
        result = parse_object(tokens, flag, level)
        if flag == 'D':
                return result
        else:
            return dict_to_obj(result[0]), result[1], result[2]
    else:
        return t, tokens[1:], level
