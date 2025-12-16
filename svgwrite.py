class Drawing:
	def __init__(s):
		s.elements = []
	def add(s,shape):
		s.elements.append(shape)
	def __str__(s):
		return (f'<svg width="100" height="100">'+'\n'
			+''.join(['  '+str(e)+'\n' for e in s.elements])+
			'</svg>')
class Rect:
	def __init__(s,x,y,w,h,fi,st):
		s.x, s.y, s.w, s.h, s.fill, s.stroke = x,y,w,h,fi,st
	def __str__(s):
		return (f'<rect x="{s.x}" y="{s.y}" '
			f'width="{s.w}" height="{s.h}" '
			f'fill="{s.fill}" stroke="{s.stroke}" />')
class Circle:
	def __init__(s,x,y,r,fi,st):
		s.x, s.y, s.r, s.fill, s.stroke = x,y,r,fi,st
	def __str__(s):
		return (f'<circle cx="{s.x}" cy="{s.y}" r="{s.r}" '
			f'fill="{s.fill}" stroke="{s.stroke}" />')

