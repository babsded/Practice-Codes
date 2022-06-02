departments = ['chemical','physics','mechanical','electrical']
enum_dept = enumerate(departments, start=1)

for number, dept in enum_dept:
    print('The departments available arranged serially are: ',number,dept)
   
print(list(enumerate(departments, start=3)))
      
