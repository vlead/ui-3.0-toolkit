from bs4 import BeautifulSoup
def writefile(fname,s):
	f=open(fname, 'w+')
	f.write(template)
	f.seek(0)
	content = f.read()
	k=content.index('<div class="col-md-10 lab-list-col-10">')
	t= content.index('<!--edit -->')
	f.seek(t+13)
	s=s+f.read()
	f.seek(t+13)
	f.write(s)
f=open("template.html",'r')
template=f.read()
f=open("content.html",'r')
srchtml=f.read()
f.close()
soup = BeautifulSoup(srchtml, 'html.parser')
sectionno=soup.find_all('section')
d=['introduction','experiments','target_audience','courses_aligned','prerequisites','feedback']
print len(sectionno)
sectionNumber=1
while sectionNumber<=len(sectionno):
	tag=""
	att = ''+'lab-article-section-'+str(sectionNumber)+'-heading'
	tagger = soup.findAll('div', attrs={'id':att,'class':'heading'})
	tag=str(tagger[0])
	att = ''+'lab-article-section-'+str(sectionNumber)+'-content'
	tagger = soup.findAll('div', attrs={'id':att,'class':'content'})
	tag+=str(tagger[0])
	print tag
	writefile(d[sectionNumber-1]+'.html',tag)
	sectionNumber=sectionNumber+1
	
	
