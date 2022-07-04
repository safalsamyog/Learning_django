class FourYearDigitConverter:
	regex='[0-9]{3}'

	def to_python(self,value):
		return int(value)
	def to_url(self,value):
		return f'{value:3d}'


#we can much value here