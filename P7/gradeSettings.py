import re
ASSIGNMENT_NAME = 'P7'
ASSIGNMENT_TEST_NUM = 6
EMAIL_SEND = 0
EAMIL_SEND_UPPER_BOUND = 0


OUTPUT_RESULT_REG_EXP = []

SCRIPT_REG_EXP = []
SCRIPT_EXISTENCE_REG_EXP = []
FUNCTION_ORDER = ['main']
TEST_FUNC = {'main':[           {'input_file':          'P7_menu_input.txt',
                                 'stdout_pat_setting':  re.I,
                                 'stdout_pat_del_space':True,
                                 'stdout_pat_file':     'P7_menu.txt'},
                                {'input_file':          'P7_quit_input.txt',
                                 'stdout_pat_setting':  re.I,
                                 'stdout_pat_del_space':True,
                                 'stdout_pat_file':     'P7_quit.txt'},
                                {'input_file':          'P7_add_input.txt',
                                 'stdout_pat_setting':  re.I,
                                 'stdout_pat_del_space':True,
                                 'stdout_pat_file':     'P7_add.txt'},
                                {'input_file':          'P7_display_input.txt',
                                 'stdout_pat_setting':  re.I,
                                 'stdout_pat_del_space':True,
                                 'stdout_pat_file':     'P7_display.txt'},
                                {'input_file':          'P7_cancel_input.txt',
                                 'stdout_pat_setting':  re.I,
                                 'stdout_pat_del_space':True,
                                 'stdout_pat_file':     'P7_cancel.txt'},
                                {'input_file':          'P7_error_input_1.txt',
                                 'stdout_pat_setting':  re.I,
                                 'stdout_pat_del_space':True,
                                 'stdout_pat_file':     'P7_error_1.txt'},
                                {'input_file':          'P7_error_input_2.txt',
                                 'stdout_pat_setting':  re.I,
                                 'stdout_pat_del_space':True,
                                 'stdout_pat_file':     'P7_error_2.txt'},
                                {'input_file':          'P7_error_input_3.txt',
                                 'stdout_pat_setting':  re.I,
                                 'stdout_pat_del_space':True,
                                 'stdout_pat_file':     'P7_error_3.txt'},
                                {'input_file':          'P7_cancel_n_input.txt',
                                 'stdout_pat_setting':  re.I,
                                 'stdout_pat_del_space':True,
                                 'stdout_pat_file':     'P7_cancel_n.txt'}]}

TEST_SCRIPT = {'main':[{'script_pat':'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\''}],
               'all_function':[{'script_pat':'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\''},
                               {'script_pat':'\W#\s*?\w'}]}


GRADING_RULES_ORDER = ['greeting_menu_quit_opt',
                       'add_opt',
                       'display_opt',
                       'cancel_opt',
                       'error_handling',
                       'commenting']

GRADING_RULES = {'greeting_menu_quit_opt':      {'rules':'and','order':0,'points':1,
                                                 'test':[{'type':'func','func_name':'main', 'index':0,'check':'stdout_pat','error':'test of greeting & menu'},
                                                         {'type':'func','func_name':'main', 'index':1,'check':'stdout_pat','error':'test of quit'}]
                                                },
                 'add_opt':                     {'rules':'and','order':1,'points':1,
                                                 'test':[{'type':'func','func_name':'main', 'index':2,'check':'stdout_pat','error':'test of add'}]
                                                },
                 'display_opt':                 {'rules':'and','order':2,'points':1,
                                                 'test':[{'type':'func','func_name':'main', 'index':3,'check':'stdout_pat','error':'test of display'}]
                                                },
                 'cancel_opt':                  {'rules':'select','order':3,'points':2,
                                                 'test':[{'type':'func','func_name':'main', 'index':4,'check':'stdout_pat', 'points':2, 'error':'test of cancel & event successfully deleted'},
                                                         {'type':'func','func_name':'main', 'index':8,'check':'stdout_pat', 'points':1, 'error':'cancel cannot delete the event but not crashed'}]
                                                },
                 'error_handling':              {'rules':'and','order':4,'points':1,
                                                 'test':[{'type':'func','func_name':'main', 'index':5,'check':'stdout_pat','error':'test 1 of error handling'},
                                                         {'type':'func','func_name':'main', 'index':6,'check':'stdout_pat','error':'test 2 of error handling'},
                                                         {'type':'func','func_name':'main', 'index':7,'check':'stdout_pat','error':'test 3 of error handling'}]
                                                },
                 'commenting':                  {'rules':'and','order':5,'points':1,
                                                 'test':[{'type':'all','subtype':'script','func_name':'all_function', 'index':0,'check':'script_pat','error':'docstring of {func_name}'},
                                                         {'type':'all','subtype':'script','func_name':'all_function', 'index':1,'check':'script_pat','error':'comments of {func_name}'}]
                                                }
                }
                
                
SCRIPT_TEST = True

