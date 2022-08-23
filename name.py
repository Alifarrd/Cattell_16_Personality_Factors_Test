import random
my=['alifarrd','marzie ramezani']
list1=['hamed','meysam','reza','javad','arezo','pegah',
'Ahura', 'Ashkan', 'Armin', 'Afshin', 'Aria']
st="Bahman. Bijan. Babak. Bahram. Bardia. Dana. Dariush. Derafsh. Ervin. Ebrahim. Ehsan. Farhad. Farbod. Farrokh. Farshid. Farzad. Garshasp. Ghazi. Gilgamesh. Giv. Goshtasb. Hashem. Homayun. Hormuzd. Hooman. Ibrahim. Iman. Izad. Iraj"
list2=st.split('. ')
list1.extend(list2)
list1.extend(my)
Char=random.choice(list1)
print(list1)