class Parent(object):

	def implicit(self):
		print "PARENT implicit()"

	def override(self):
		print "PARENT override()"

	def altered(self):
		print "PARENT altered()"

class Child(Parent):
	def override(self):
		print "CHILD override()"

	def altered(self):
		print "CHILD BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered"

class Other(object):
	def override(self):
		print "Other override()"

	def implicit(self):
		print "Other implicit()"

	def altered(self):
		print "Other altered()"

class Example(object):
	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()

	def override(self):
		print "Child override()"

	def altered(self):
		print "Child, before other altered()"
		self.other.altered()
		print "Child, after other altered()"


dad = Parent()
son = Child()

print "implicit"
print '-'*10

dad.implicit()
son.implicit()

print "override"
print '-'*10

dad.override()
son.override()

print "alter before or after"
print '-'*10

dad.altered()
son.altered()

print "composition"
print '-'*10

son = Example()
son.implicit()
son.override()
son.altered()