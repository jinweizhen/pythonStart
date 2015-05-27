class Student(object):
	"""docstring for Student"""
	def __init__(self, name,score):
		 
		self.name = name
		self.score=score
	def get_score():
		return self.name
	def print_score(self):
		print '%s: %s' % (self.name,self.score)

peter=Student('Peter',88)
peter.print_score()

print 'name:',peter.name,"score:",peter.score,"Before:|"

def set_age(self,age):
	self.age=age

from types import MethodType

Student.set_age=MethodType(set_age,None,Student)#给实例绑定一个方法
 