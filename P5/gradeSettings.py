ASSIGNMENT_NAME = 'P5'
ASSIGNMENT_TEST_NUM = 8

OUTPUT_RESULT_REG_EXP = []

SCRIPT_REG_EXP = []
SCRIPT_EXISTENCE_REG_EXP = []
FUNCTION_ORDER = ['most_repeated_letters', 'has_equal_letters', 'is_palindrome', 'is_trick_round', 'total_points']
                  
TEST_FUNC = {'most_repeated_letters':[  {'input_args':['a'], 'return_val':1},
                                        {'input_args':['aabbcc'],'return_val':2},
                                        {'input_args':['azaca'],'return_val':3},
                                        {'input_args':['tttzzkzbza'],'return_val':4},
                                        {'input_args':['qwhertyuiopasdfghjklzoxcvbnom'],'return_val':3}],
	     'has_equal_letters':[      {'input_args':['khaleesi'],'return_val':True},
                                        {'input_args':['brood'],'return_val':False},
                                        {'input_args':['aeiou'],'return_val':False},
                                        {'input_args':['bdfzh'],'return_val':False},
                                        {'input_args':['abcduo'],'return_val':True},
                                        {'input_args':['zaxecivobu'],'return_val':True}],
             'is_palindrome':[          {'input_args':['a'],'return_val':True},
                                        {'input_args':['level'],'return_val':True},
                                        {'input_args':['palindrome'],'return_val':False},
                                        {'input_args':['beliilec'],'return_val':False},
                                        {'input_args':['levvel'],'return_val':True},
                                        {'input_args':['op'],'return_val':False}],
             'is_trick_round':[         {'input_args':['angry','imbue'],'return_val':True},
                                        {'input_args':['ayewrngry','imywerewrwerdewdescbue'],'return_val':True},
                                        {'input_args':['hotcat','mouse'],'return_val':False},
                                        {'input_args':['y','y'],'return_val':False},
                                        {'input_args':['youtube','findyo'],'return_val':False},
                                        {'input_args':['itshard','toyfind'],'return_val':True}],
             'total_points':[           {'input_args':['dog'],'return_val':3},
                                        {'input_args':['auffer'],'return_val':24},
                                        {'input_args':['evlevelve'],'return_val':15},
                                        {'input_args':['glgjssa'],'return_val':14},
                                        {'input_args':['oliveisbutifulufitubsievilo'],'return_val':45},
                                        {'input_args':['qyhfbzzbfhyq'],'return_val':120}]
        }

TEST_SCRIPT = {'total_points':[{'script_pat':'most_repeated_letters\('},
                               {'script_pat':'has_equal_letters\('},
                               {'script_pat':'is_palindrome\('},
                               {'script_pat_count':'for '},
                               {'script_pat':'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\''}],
               'most_repeated_letters':[{'script_pat_count':'for '},
                                        {'script_pat':'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\''}],
               'has_equal_letters':[{'script_pat_count':'for '},
                                    {'script_pat':'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\''}],
               'is_palindrome':[{'script_pat_count':'for '},
                                {'script_pat':'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\''}],
               'is_trick_round':[{'script_pat_count':'for '},
                                 {'script_pat':'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\''}]
        }


GRADING_RULES_ORDER = ['most_repeated_letters',
                        'has_equal_letters',
                        'is_palindrome',
                        'total_points_use_3_func',
                        'total_points',
                        'is_trick_round',
                        'docstring',
                        'atleast_2_for']

GRADING_RULES = {'most_repeated_letters':{'rules':'and','order':0,'points':1,
                                          'test':[{'type':'func','func_name':'most_repeated_letters', 'index':0,'check':'return_val','error':'test 1 of most_repeated_letters'},
                                                  {'type':'func','func_name':'most_repeated_letters', 'index':1,'check':'return_val','error':'test 2 of most_repeated_letters'},
                                                  {'type':'func','func_name':'most_repeated_letters', 'index':2,'check':'return_val','error':'test 3 of most_repeated_letters'},
                                                  {'type':'func','func_name':'most_repeated_letters', 'index':3,'check':'return_val','error':'test 4 of most_repeated_letters'}]},
                 'has_equal_letters':{'rules':'and','order':1,'points':1,
                                      'test':[{'type':'func','func_name':'has_equal_letters', 'index':0,'check':'return_val','error':'test 1 of has_equal_letters'},
                                              {'type':'func','func_name':'has_equal_letters', 'index':1,'check':'return_val','error':'test 2 of has_equal_letters'},
                                              {'type':'func','func_name':'has_equal_letters', 'index':2,'check':'return_val','error':'test 3 of has_equal_letters'},
                                              {'type':'func','func_name':'has_equal_letters', 'index':3,'check':'return_val','error':'test 4 of has_equal_letters'},
                                              {'type':'func','func_name':'has_equal_letters', 'index':4,'check':'return_val','error':'test 5 of has_equal_letters'}]},
                 'is_palindrome': {'rules':'and','order':2,'points':1,
                                      'test':[{'type':'func','func_name':'is_palindrome', 'index':0,'check':'return_val','error':'test 1 of is_palindrome'},
                                              {'type':'func','func_name':'is_palindrome', 'index':1,'check':'return_val','error':'test 2 of is_palindrome'},
                                              {'type':'func','func_name':'is_palindrome', 'index':2,'check':'return_val','error':'test 3 of is_palindrome'},
                                              {'type':'func','func_name':'is_palindrome', 'index':3,'check':'return_val','error':'test 4 of is_palindrome'},
                                              {'type':'func','func_name':'is_palindrome', 'index':4,'check':'return_val','error':'test 5 of is_palindrome'}]},
                 'total_points_use_3_func':{'rules':'and','order':3,'points':1,
                                           'test':[{'type':'script','func_name':'total_points', 'index':0, 'check':'script_pat', 'error':'most_repeated_letters in total_points'},
                                                   {'type':'script','func_name':'total_points', 'index':1, 'check':'script_pat', 'error':'has_equal_letters in total_points'},
                                                   {'type':'script','func_name':'total_points', 'index':2, 'check':'script_pat', 'error':'is_palindrome in total_points'}]},
                 'total_points': {'rules':'groupadd','order':4,'points':3,
                                  'groups':[(1,[{'type':'func','func_name':'total_points', 'index':0,'check':'return_val','error':'test 1-1 of total_points'},
                                               {'type':'func','func_name':'total_points', 'index':1,'check':'return_val','error':'test 1-2 of total_points'}]),
                                           (1,[{'type':'func','func_name':'total_points', 'index':2,'check':'return_val','error':'test 2-1 of total_points'},
                                               {'type':'func','func_name':'total_points', 'index':3,'check':'return_val','error':'test 2-2 of total_points'}]),
                                           (1,[{'type':'func','func_name':'total_points', 'index':4,'check':'return_val','error':'test 3-1 of total_points'},
                                               {'type':'func','func_name':'total_points', 'index':5,'check':'return_val','error':'test 3-2 of total_points'}])]},
                 'is_trick_round':{'rules':'and','order':5,'points':1,
                                      'test':[{'type':'func','func_name':'is_trick_round', 'index':0,'check':'return_val','error':'test 1 of is_trick_round'},
                                              {'type':'func','func_name':'is_trick_round', 'index':1,'check':'return_val','error':'test 2 of is_trick_round'},
                                              {'type':'func','func_name':'is_trick_round', 'index':2,'check':'return_val','error':'test 3 of is_trick_round'},
                                              {'type':'func','func_name':'is_trick_round', 'index':3,'check':'return_val','error':'test 4 of is_trick_round'},
                                              {'type':'func','func_name':'is_trick_round', 'index':4,'check':'return_val','error':'test 5 of is_trick_round'}]},
                 'docstring':{'rules':'and','order':6,'points':1,
                              'test':[{'type':'script','func_name':'total_points', 'index':4, 'check':'script_pat', 'error':'docstring in total_points'},
                                      {'type':'script','func_name':'most_repeated_letters', 'index':1, 'check':'script_pat', 'error':'docstring in most_repeated_letters'},
                                      {'type':'script','func_name':'has_equal_letters', 'index':1, 'check':'script_pat', 'error':'docstring in has_equal_letters'},
                                      {'type':'script','func_name':'is_palindrome', 'index':1, 'check':'script_pat', 'error':'docstring in is_palindrome'},
                                      {'type':'script','func_name':'is_trick_round', 'index':1, 'check':'script_pat', 'error':'docstring in is_trick_round'}]},
                 'atleast_2_for':{'rules':'sum','order':7,'lowerBound':2,'points':1,
                                  'test':[{'type':'script','func_name':'total_points', 'index':3, 'check':'script_pat_count', 'error':'for in total_points'},
                                          {'type':'script','func_name':'most_repeated_letters', 'index':0, 'check':'script_pat_count', 'error':'for in most_repeated_letters'},
                                          {'type':'script','func_name':'has_equal_letters', 'index':0, 'check':'script_pat_count', 'error':'for in has_equal_letters'},
                                          {'type':'script','func_name':'is_palindrome', 'index':0, 'check':'script_pat_count', 'error':'for in is_palindrome'},
                                          {'type':'script','func_name':'is_trick_round', 'index':0, 'check':'script_pat_count', 'error':'for in is_trick_round'}]}
                }
                
                
SCRIPT_TEST = True

