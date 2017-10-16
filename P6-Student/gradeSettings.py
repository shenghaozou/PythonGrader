import re
ASSIGNMENT_NAME = 'P6'
ASSIGNMENT_TEST_NUM = 7
EMAIL_SEND = 0
EAMIL_SEND_UPPER_BOUND = 0

OUTPUT_RESULT_REG_EXP = []

SCRIPT_REG_EXP = []
SCRIPT_EXISTENCE_REG_EXP = []
FUNCTION_ORDER = ['get_level', 'get_walk', 'update', 'run_simulation']
                  
TEST_FUNC = {'get_level':[      {'input_args':[0], 'return_val':0},
                                {'input_args':[6], 'return_val':2}],
	     'get_walk':[       {'prerun':'get_walk.py', 'input_args':[3], 'return_val':[1,5,3]},
                                {'prerun':'get_walk.py', 'input_args':[2], 'return_val':[2,5,3]}],
             'update':[         {'input_args':[12, -1, 3],'return_val': 9},
                                {'input_args':[0, 1, 2],'return_val': 2}],
             'run_simulation':[ {'input_file':          'run_simulation_1.txt',
                                 'return_val':          [0, 2, 4, 6, 8, 10, 8, 6, 4, 2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 6, 8, 10, 12, 14, 12, 10, 8, 6],
                                 'stdout_pat_setting':  re.I,
                                 'stdout_pat_file':     'run_simulation_1_out.txt'},
                                {'input_file':          'run_simulation_2.txt',
                                 'return_val':          [0, 4, 8, 12, 16, 20, 24, 20, 16, 12, 8, 4, 8, 12, 16, 20, 24, 28, 24, 20, 16, 12, 8, 12, 16, 20, 24, 28, 32, 28, 24, 20, 16, 12],
                                 'stdout_pat_setting':  re.I,
                                 'stdout_pat_file':     'run_simulation_2_out.txt'},
                                 {'input_file':          'run_simulation_1.txt',
                                  'stdout_pat_setting':  re.I,
                                  'stdout_pat_file':     'run_simulation_prompt_out.txt'},
                                 {'input_file':          'run_simulation_1.txt',
                                  'stdout_pat_setting':  re.I,
                                  'stdout_pat_file':     'run_simulation_value_out.txt'}]}

TEST_SCRIPT = {'get_level':[{'script_pat':'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\''}],
               'get_walk':[{'script_pat':'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\''}],
               'update':[{'script_pat':'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\''}],
               'run_simulation':[{'script_pat':'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\''}]
        }


GRADING_RULES_ORDER = ['get_level',
                       'get_walk',
                       'update',
                       'run_simulation_prompt',
                       'run_simulation_value',
                       'run_simulation_termination',
                       'docstring']

GRADING_RULES = {'get_level':{'rules':'and','order':0,'points':1,
                              'test':[{'type':'func','func_name':'get_level', 'index':0,'check':'return_val','error':'test 1 of get_level'},
                                      {'type':'func','func_name':'get_level', 'index':1,'check':'return_val','error':'test 2 of get_level'}]},
                 'get_walk':{'rules':'and','order':1,'points':1,
                             'test':[{'type':'func','func_name':'get_walk', 'index':0,'check':'return_val','error':'test 1 of get_walk'},
                                     {'type':'func','func_name':'get_walk', 'index':1,'check':'return_val','error':'test 2 of get_walk'}]},
                 'update': {'rules':'and','order':2,'points':1,
                            'test':[{'type':'func','func_name':'update', 'index':0,'check':'return_val','error':'test 1 of update'},
                                    {'type':'func','func_name':'update', 'index':1,'check':'return_val','error':'test 2 of update'}]},
                 'run_simulation_prompt':{'rules':'and','order':3,'points':1,
                                          'test':[{'type':'func','func_name':'run_simulation', 'index':2, 'check':'stdout_pat', 'error':'test of run_simulation prompt'}]},
                 'run_simulation_value': {'rules':'and','order':4,'points':1,
                                          'test':[{'type':'func','func_name':'run_simulation', 'index':3, 'check':'stdout_pat', 'error':'test of run_simulation value'}]},
                 'run_simulation_termination':{'rules':'add','order':5,'points':2,
                                               'test':[{'type':'func','func_name':'run_simulation', 'index':0,'check':'return_val','error':'test 1 of run_simulation termination'},
                                                       {'type':'func','func_name':'run_simulation', 'index':1,'check':'return_val','error':'test 2 of run_simulation termination'}]},
                 'docstring':{'rules':'and','order':6,'points':1,
                              'test':[{'type':'script','func_name':'get_level', 'index':0, 'check':'script_pat', 'error':'docstring in {func_name}'},
                                      {'type':'script','func_name':'get_walk', 'index':0, 'check':'script_pat', 'error':'docstring in {func_name}'},
                                      {'type':'script','func_name':'update', 'index':0, 'check':'script_pat', 'error':'docstring in {func_name}'},
                                      {'type':'script','func_name':'run_simulation', 'index':0, 'check':'script_pat', 'error':'docstring in {func_name}'}]}
                }
                
                
SCRIPT_TEST = True

