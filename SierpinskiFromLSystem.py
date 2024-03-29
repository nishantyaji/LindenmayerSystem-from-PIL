import sys
sys.path.insert(0,'.')
from LindenMayerSystem import LindenMayerSystem

if __name__ == '__main__':
    rules_dict={'F':'G-F-G', 'G':'F+G+F'}
    start_string='F'    
    measures_dict = {'length':5, 'angle':60}
    fn_dict = {'F':lambda turtle1: turtle1.forward(measures_dict['length']), 
            'G':lambda turtle1: turtle1.forward(measures_dict['length']), 
            'B':lambda turtle1: turtle1.backward(measures_dict['length']),
            '+':lambda turtle1: turtle1.left(measures_dict['angle']),
            '-':lambda turtle1: turtle1.right(measures_dict['angle']),}

    filename = __file__.split('.')[0] + '.bmp'
    ls = LindenMayerSystem(start_string=start_string, rules_dict=rules_dict, iterations=6, fn_dict=fn_dict, filename=filename)
    ls.display()
    

