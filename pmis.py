"""
你现在需要创建一个Python程序来实现工人信息的保存。这个系统可以查询，添加，修改，删除工人的信息。这个系统需要满足以下要求：
1.使用Python + MongoDB来完成；
2.工人信息包括：id, name, age, sex, salary；
3.可以使用一条命令显示所有工人的信息；
4.可以使用多个条件来过滤显示特定的工人信息；
5.可以增加工人的信息；ok
6.可以修改工人的信息；ok
7.可以删除工人的信息；ok
8.id 不能重复；增加信息前，先查重
最后呈现的结果是一个可以运行的Python程序。
"""

from mongoengine import *

connect('jikexueyuan')


class People(Document):
    pid = StringField(required=True)
    name = StringField(required=True)
    age = IntField(required=True)
    sex = StringField(required=True)
    salary = IntField()

    @staticmethod
    def queryAll():
        namelist = People.objects()
        for x in namelist:
            print('员工编号：%s, 员工姓名：%s, 员工年龄：%d， 员工性别：%s, 员工工资：%d' %(x.pid,x.name,x.age,x.sex,x.salary))

    @staticmethod
    def queryUnderCondition(query_select_input):
        if query_select_input == 'a':#by pid
            pid_condition = input('￥输入查询的员工编号：')
            peoplelist = People.objects(pid=pid_condition)
            for x in peoplelist:
                print('员工编号：%s, 员工姓名：%s, 员工年龄：%d， 员工性别：%s, 员工工资：%d' % (x.pid, x.name, x.age, x.sex, x.salary))
        elif query_select_input == 'b':#by name
            name_condition = input('￥输入查询的员工姓名：')
            peoplelist = People.objects(name=name_condition)
            for x in peoplelist:
                print('员工编号：%s, 员工姓名：%s, 员工年龄：%d， 员工性别：%s, 员工工资：%d' % (x.pid, x.name, x.age, x.sex, x.salary))
        elif query_select_input == 'c':#by age
            age_condition = int(input('￥输入查询的员工年龄：'))
            equation_condition = input('￥输入过滤方式，> or < or =：')
            if equation_condition == '>':
                peoplelist = People.objects(age__gt=age_condition)
                for x in peoplelist:
                    print('员工编号：%s, 员工姓名：%s, 员工年龄：%d， 员工性别：%s, 员工工资：%d' % (x.pid, x.name, x.age, x.sex, x.salary))
            elif equation_condition == '=':
                peoplelist = People.objects(age=age_condition)
                for x in peoplelist:
                    print('员工编号：%s, 员工姓名：%s, 员工年龄：%d， 员工性别：%s, 员工工资：%d' % (x.pid, x.name, x.age, x.sex, x.salary))
            else:
                peoplelist = People.objects(age__lt=age_condition)
                for x in peoplelist:
                    print('员工编号：%s, 员工姓名：%s, 员工年龄：%d， 员工性别：%s, 员工工资：%d' % (x.pid, x.name, x.age, x.sex, x.salary))
        elif query_select_input == 'd':#by sex
            sex_condition = input('￥输入查询的员工性别：')
            peoplelist = People.objects(sex=sex_condition)
            for x in peoplelist:
                print('员工编号：%s, 员工姓名：%s, 员工年龄：%d， 员工性别：%s, 员工工资：%d' % (x.pid, x.name, x.age, x.sex, x.salary))
        elif query_select_input == 'e':#by salary
            salary_condition = input('￥输入查询的员工工资：')
            peoplelist = People.objects(salary=salary_condition)
            equation_condition = input('￥输入过滤方式，> or < or =：')
            if equation_condition == '>':
                peoplelist = People.objects(salary__gt=salary_condition)
                for x in peoplelist:
                    print('员工编号：%s, 员工姓名：%s, 员工年龄：%d， 员工性别：%s, 员工工资：%d' % (x.pid, x.name, x.age, x.sex, x.salary))
            elif equation_condition == '=':
                peoplelist = People.objects(salary=salary_condition)
                for x in peoplelist:
                    print('员工编号：%s, 员工姓名：%s, 员工年龄：%d， 员工性别：%s, 员工工资：%d' % (x.pid, x.name, x.age, x.sex, x.salary))
            else:
                peoplelist = People.objects(salary__lt=salary_condition)
                for x in peoplelist:
                    print('员工编号：%s, 员工姓名：%s, 员工年龄：%d， 员工性别：%s, 员工工资：%d' % (x.pid, x.name, x.age, x.sex, x.salary))
        elif query_select_input == 'f':#by Synthesis
            age_condition = input('￥输入查询的员工年龄：')
            age_equation_condition = input('￥输入年龄过滤方式，> or < or =：')
            sex_condition = input('￥输入查询的员工性别：')
            salary_condition = input('￥输入查询的员工工资：')
            salary_equation_condition = input('￥输入工资过滤方式，> or < or =：')
            if age_equation_condition == '>' and salary_equation_condition == '>':
                peoplelist = People.objects(age__gt=age_condition, salary__gt=salary_condition, sex=sex_condition)
                for x in peoplelist:
                    print('员工编号：%s, 员工姓名：%s, 员工年龄：%d， 员工性别：%s, 员工工资：%d' % (x.pid, x.name, x.age, x.sex, x.salary))
            elif age_equation_condition == '>' and salary_equation_condition == '<':
                peoplelist = People.objects(age__gt=age_condition, salary__lt=salary_condition, sex=sex_condition)
                for x in peoplelist:
                    print('员工编号：%s, 员工姓名：%s, 员工年龄：%d， 员工性别：%s, 员工工资：%d' % (x.pid, x.name, x.age, x.sex, x.salary))
            elif age_equation_condition == '>' and salary_equation_condition == '=':
                peoplelist = People.objects(age__gt=age_condition, salary=salary_condition, sex=sex_condition)
                for x in peoplelist:
                    print('员工编号：%s, 员工姓名：%s, 员工年龄：%d， 员工性别：%s, 员工工资：%d' % (x.pid, x.name, x.age, x.sex, x.salary))
            elif age_equation_condition == '<' and salary_equation_condition == '>':
                peoplelist = People.objects(age__lt=age_condition, salary__gt=salary_condition, sex=sex_condition)
                for x in peoplelist:
                    print('员工编号：%s, 员工姓名：%s, 员工年龄：%d， 员工性别：%s, 员工工资：%d' % (x.pid, x.name, x.age, x.sex, x.salary))
            elif age_equation_condition == '<' and salary_equation_condition == '<':
                peoplelist = People.objects(age__lt=age_condition, salary__lt=salary_condition, sex=sex_condition)
                for x in peoplelist:
                    print('员工编号：%s, 员工姓名：%s, 员工年龄：%d， 员工性别：%s, 员工工资：%d' % (x.pid, x.name, x.age, x.sex, x.salary))
            elif age_equation_condition == '<' and salary_equation_condition == '=':
                peoplelist = People.objects(age__lt=age_condition, salary=salary_condition, sex=sex_condition)
                for x in peoplelist:
                    print('员工编号：%s, 员工姓名：%s, 员工年龄：%d， 员工性别：%s, 员工工资：%d' % (x.pid, x.name, x.age, x.sex, x.salary))
            elif age_equation_condition == '=' and salary_equation_condition == '>':
                peoplelist = People.objects(age=age_condition, salary__gt=salary_condition, sex=sex_condition)
                for x in peoplelist:
                    print('员工编号：%s, 员工姓名：%s, 员工年龄：%d， 员工性别：%s, 员工工资：%d' % (x.pid, x.name, x.age, x.sex, x.salary))
            elif age_equation_condition == '=' and salary_equation_condition == '<':
                peoplelist = People.objects(age=age_condition, salary__lt=salary_condition, sex=sex_condition)
                for x in peoplelist:
                    print('员工编号：%s, 员工姓名：%s, 员工年龄：%d， 员工性别：%s, 员工工资：%d' % (x.pid, x.name, x.age, x.sex, x.salary))
            elif age_equation_condition == '=' and salary_equation_condition == '=':
                peoplelist = People.objects(age=age_condition, salary=salary_condition, sex=sex_condition)
                for x in peoplelist:
                    print('员工编号：%s, 员工姓名：%s, 员工年龄：%d， 员工性别：%s, 员工工资：%d' % (x.pid, x.name, x.age, x.sex, x.salary))
            else:
                print('@queryUnderCondition age_equation_condition & salary_equation_condition input error')
        else:
            print('@queryUnderCondition query_select input error')

    def addPeople(self, pid_input, name_input, age_input, sex_input, salary_input):
        self.pid = pid_input
        self.name = name_input
        self.age = age_input
        self.sex = sex_input
        self.salary = salary_input
        self.save()
        print("Personnel information within id is %s has been entered", id)

    @staticmethod
    def delPeople(pid_input):
        People.objects(pid=pid_input).delete()
        # self.objects.delete()
        print("Personnel information within id is %s has been deleted", id)

    @staticmethod
    def updatePeople(pid_input, name_input, age_input, sex_input, salary_input):
        pid_find = People.objects(pid=pid_input)
        # print('pid_find is ', pid_find)
        for x in pid_find:
            pid_update_is_need = input('！是否需要修改员工编号pid？y or n:')
            if pid_update_is_need == 'y':
                new_pid = input('请输入新的员工编号pid，注意pid为5为十进制数字，唯一且不可重复！:')
                if someone.isRepeat(pidI) != 0:
                    print('员工编号pid重复！请从新录入')
                    continue
                else:
                    if new_pid != '' and len(new_pid) == 5:
                        x.update(pid=new_pid)
            else:
                x.update(name=name_input)
                x.update(age=age_input)
                x.update(sex=sex_input)
                x.update(salary=salary_input)

    @staticmethod
    def isRepeat(pid_input):
        pid_find = People.objects(pid=pid_input)
        # print('pid_find is ', pid_find)
        # for x in pid_find:
        # print('pid_find name is ', x.name)
        if len(pid_find) == 0:
            print("ok! this id which can be use is vacancy")
            return 0  # 返回0,说明id可用，查无此人。


withdraw = 'n'
while withdraw == 'n':
    print('=-=-=-人员信息管理系统V1.0=-=-=-')
    print('3.一条命令显示所有工人的信息')
    print('4.使用多个条件来过滤显示特定的工人信息')
    print('5.增加工人的信息')
    print('6.修改工人的信息')
    print('7.删除工人的信息')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print(' ')
    someone = People()

    selection = int(input('@请用数字选择你的操作: '))

    # someone.addPeople(pidI, nameI, ageI, sexI, salaryI)
    # someone.delPeople(pidI)

    if selection == 3:  # 一条命令显示所有工人的信息
        print('@显示所有工人信息')
        someone.queryAll()
    elif selection == 4:  # 使用多个条件来过滤显示特定的工人信息
        print('@条件过滤显示特定的工人信息')
        print('#a.根据编号查询')
        print('#b.根据姓名查询')
        print('#c.根据年龄查询')
        print('#d.根据性别查询')
        print('#e.根据工资查询')
        print('#f.综合查询')
        query_select = input('#请用字符选择你的操作: ')
        someone.queryUnderCondition(query_select)
    elif selection == 5:  # 增加工人的信息
        print('@增加工人信息')
        pidI = input("type pid:")
        if someone.isRepeat(pidI) != 0:
            print('员工编号pid重复！请从新录入')
            continue
        else:
            nameI = input("type name:")
            ageI = input("type age:")
            sexI = input("type sex:")
            salaryI = input("type salary:")
            someone.addPeople(pidI, nameI, ageI, sexI, salaryI)
    elif selection == 6:  # 修改工人的信息
        print('@修改工人信息')
        pidI = input("type pid:")
        if someone.isRepeat(pidI) == 0:
            print('查无此人，无法执行修改操作！请从新录入')
            continue
        else:
            nameI = input("type name:")
            ageI = input("type age:")
            sexI = input("type sex:")
            salaryI = input("type salary:")
            someone.updatePeople(pidI, nameI, ageI, sexI, salaryI)
    elif selection == 7:  # 删除工人的信息
        print('@删除工人信息')
        pidI = input("type pid:")
        if someone.isRepeat(pidI) == 0:
            print('查无此人，无法执行删除操作！请从新录入')
            continue
        else:
            someone.delPeople(pidI)
    #elif (selection < 3) or (selection > 7):
    else:
        print('@输入有误！')

    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('y.退出程序')
    print('n.继续操作')
    print(' ')
    withdraw = input('@退出程序？y or n: ')

"""
pidI = '00000001'
nameI = 'jay chow'
ageI = 39
sexI = 'male'
salaryI = 42158523
"""
# pidI = input("type pid:")
# nameI = input("type name:")
# ageI = input("type age:")
# sexI = input("type sex:")
# salaryI = input("type salary:")

# someone = People()
# someone.addPeople(pidI, nameI, ageI, sexI, salaryI)
# someone.delPeople(pidI)
