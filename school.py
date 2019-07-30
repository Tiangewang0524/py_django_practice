"""
√构造一个父类学校成员，
√子类老师、学生，
√其他还有班级类，小组类什么的你们自己规划，


√实例化一个学生学校成员就自动增加1人，

√缴费情况，学校账余额，


√有上课这个行为，输出谁在上课，随机百分之多少的人理解了
"""


import random


class SchoolMember:
    number = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        SchoolMember.number += 1
        print("学校新加入一个成员:%s" % self.name, end=' ')
        print("现在学校有成员%d人" % SchoolMember.number)


class Teacher(SchoolMember):
    tea_num = 0
    tea_list = []

    def __init__(self, name, age, course, salary):
        SchoolMember.__init__(self, name, age)
        self.course = course
        self.salary = salary
        Teacher.tea_num += 1
        print("该成员是一名老师。", end=' ')
        print("现在有老师%d人" % Teacher.tea_num)
        print('\n')
        Teacher.tea_list.append(self)

    def __str__(self):
        return "{}老师教{} 课程".format(self.name, self.course)


class Student(SchoolMember):
    money = 0
    stu_num = 0
    stu_list = []
    dict_class = dict()

    def __init__(self, name, age, marks, enrolled_class, judge_jiaofei):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        self.enrolled_class = enrolled_class
        self.judge_jiaofei = judge_jiaofei
        Student.stu_num += 1
        print("该成员是一名学生。", end=' ')
        print("现在有学生%d人" % Student.stu_num)
        print('\n')
        Student.stu_list.append(self)

    def have_class(self):
        if self.enrolled_class in Student.dict_class.keys():
            Student.dict_class[self.enrolled_class][0] += 1
            Student.dict_class[self.enrolled_class].append(self.name)
        else:
            Student.dict_class[self.enrolled_class] = []
            # print(Student.dict_class[self.enrolled_class])
            Student.dict_class[self.enrolled_class].append(0)
            Student.dict_class[self.enrolled_class][0] += 1
            Student.dict_class[self.enrolled_class].append(self.name)

    # 假设学费5000元/人
    def jiaofei(self):
        if self.judge_jiaofei == '是':
            print("学生{}已成功缴学费5000元！".format(self.name))
            return 1
        elif self.judge_jiaofei == '否':
            print("学生{}没有缴费！".format(self.name))
            return 0


class Class:
    def __init__(self, class_name):
        self.class_name = class_name

    def num_in_class(self):
        stu_num = Student.dict_class[self.class_name][0]
        return stu_num

    def __str__(self):
        x = random.randint(0, int(Student.dict_class[self.class_name][0]))
        y = x / Student.dict_class[self.class_name][0]
        z = str(y * 100) + '%'
        return "{}课上课人数{}人，学生的理解率为{}".format(self.class_name, self.num_in_class(), z)


class School:
    judge = 0
    salary = 0
    income = 0

    # 账户余额
    def __init__(self, stu_list, tea_list):
        for each_student in stu_list:
            if each_student.jiaofei():
                self.judge += 1
        self.income = self.judge * 5000
        for each_teacher in tea_list:
            self.salary += int(each_teacher.salary)

    def __str__(self):
        return "学校账户余额为:{}".format(self.income - self.salary)


if __name__ == '__main__':
    stu_1 = Student('Tom', 21, 80, 'python', '是')
    stu_2 = Student('Jerry', 19, 86, 'java', '否')
    stu_3 = Student('Michael', 20, 73, 'sql', '是')
    stu_4 = Student('Jordan', 21, 78, 'python', '否')
    stu_5 = Student('Russell', 22, 53, 'python', '是')
    stu_6 = Student('Mike', 23, 58, 'java', '是')
    stu_7 = Student('Spike', 26, 62, 'python', '是')
    stu_8 = Student('Bob', 18, 70, 'java', '否')
    stu_9 = Student('Danny', 17, 89, 'java', '是')
    stu_10 = Student('Jenny', 20, 92, 'sql', '否')
    stu_11 = Student('Angela', 24, 74, 'sql', '是')
    stu_12 = Student('Jack', 25, 66, 'sql', '是')
    stu_13 = Student('Rose', 22, 68, 'python', '是')
    for each in Student.stu_list:
        each.have_class()
    tea_1 = Teacher('James', 48, 'java', '8000')
    tea_2 = Teacher('Kevin', 56, 'sql', '12000')
    tea_3 = Teacher('Tony', 33, 'python', '11000')
    print(tea_1, tea_2, tea_3)
    school_1 = School(Student.stu_list, Teacher.tea_list)
    print(school_1)
    # print(Student.dict_class)
    class_1 = Class('python')
    class_2 = Class('java')
    class_3 = Class('sql')
    print(class_1)
    print(class_2)
    print(class_3)
