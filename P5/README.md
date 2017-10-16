#Introduction
This is my auto-grading scripts for Python course CS301 in University of Wisconsin-Madison. It can generate report for graders. Submissions are downloaded from Canvas. Filename will be studentName\_sid\_filename.py.

When grading, you should:
1. Put them into one folder. I suggest you name it as 'submissions'. You can enter 'python GraderP5.py' in terminal. It will automatically run grading scripts for submissions.

2. Or put them in one folder with other name, for example 'submissions2'. You can run the auto-grading script by 'python GraderP5.py submission2'

3. If you need to test one submission, move it to 'test' folder. Run 'python GraderP5.py hw.py' if the file name is 'hw.py'. If you only test one file, program will not require the format of filename. 


Folders:
1. submissions - student's submissions
2. temp - students didn't guard their 'main' function with if __name__ == '__main__' so I have to use code to delete all extra parts besides functions. If you meet any problems when grading, plz take a look at temp folder. I am not sure whether I made some mistakes in my code. Just search for their own submission id.
3. tester - all the input files.

Tests:
we have 6 grading parts this week. All the test file can be found in tester folder. All the right answer will be found in HTML files, follwed by students' error.

1. calculate_food
I will check:
    1. input_calc_food_1.txt as stdin. args: 'S' & True
    2. input_calc_food_2.txt as stdin. args: 'S' & False
    3. input_calc_food_3.txt as stdin. args: 'F' & True

2. calculate_other
I will check:
    1. input_calc_other_1.txt as stdin

3. calculate_total_invalid(will give invalid input)
I will check:
    1. input_calc_total_invalid.txt, for the output, I will try to find 'invalid' in student's output.

4. calculate_total
I will check:
    1. input_calc_total_1.txt
    2. input_calc_total_2.txt
    3. input_calc_total_3.txt

5. prompt_correct
I will check:
1. input_calc_food_1.txt for calculate_food, only focus on output format.
2. input calc_other_1.txt for calculate_other, only focus on output

6. output_correct
1. input_calc_main_1.txt, only focus on extra thing after the right output.

