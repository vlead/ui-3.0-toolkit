def writefile(fname,s): # to write to a file
	f=open(fname, 'w+')
	f.write(template)
	f.seek(0)
	content = f.read()
	t= content.index('<!--edit -->')
	f.seek(t+13)
	s=s+f.read()
	f.seek(t+13)
	f.write(s)

def readfile(fname): # to read the file
	with open(fname, 'r') as f:
	    content = f.read()
	    k=content.index('<div id="experiment-article-section-1-heading" class="heading">')
	    t= content.index('</section>')
	    f.seek(k)
	    s= f.read(t-k)
	return s
	
#Readthe basic template file for the lab
f=open("template.html",'r')
template=f.read()

#Change experiments file
s=""
s=readfile('index.php?section=List%20of%20experiments') 
writefile('experiments.html',s)

#Change introduction file
s=""
s=readfile('index.php?section=Introduction') 
writefile('introduction.html',s)
#Change feedback file
s=""
s=readfile('index.php?section=Feedback')
writefile('feedback.html', s)
#Change prerequisite file
s=""
s=readfile('index.php?section=Prerequisite%20S%2FW')
writefile('prerequisites.html', s)

#Change course_aligned file
s=""
s=readfile('index.php?section=Courses%20Aligned')
writefile('courses_aligned.html', s)
#Change targetaudience file
s=""
s=readfile('index.php?section=Target%20Audience') 
writefile('target_audience.html', s)

