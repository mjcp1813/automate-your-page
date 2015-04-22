def generate_concept_HTML(concept_title, concept_description):
	html_text_1='''
<div class="concept">
	<div class="concept_title">
		'''+concept_title
	html_text_2='''
	</div>
	<div class="concept-description">
		'''+concept_description
	html_text_3='''
	</div>
</div>'''
	full_html_text=html_text_1 + html_text_2 + html_text_3
	return full_html_text

def get_title(concept):
	start_location=concept.find('TITLE:')
	end_location=concept.find('DESCRIPTION:')
	title=concept[start_location+6:end_location-1]
	return title

def get_description(concept):
	start_location=concept.find('DESCRIPTION:')
	description=concept[start_location +12:]
	return description

def get_concept_by_number(text,concept_number):
	counter=0
	while counter<concept_number:
		counter=counter+1
		next_concept_start=text.find('TITLE:')
		next_concept_end=text.find ('TITLE:',next_concept_start+1)
		concept=text[next_concept_start:next_concept_end]
		text=text[next_concept_end:]
	return concept

TEST_TEXT="""

	TITLE:
	TITLE: World Wide Web
	DESCRIPTION:The World Wide Web or the Web consist of computers that
    use the Internet to communicate with one another.  The
    basics of the Web include a computer with a browser installed,
    the Internet, servers and HTTP. HTTP is the main protocol of the  web,
    the Internet can be consider the highway that connects the computers together.
    the servers are computer that are design to store an distribute information.     
           
    Files found on the World Wide Web can be any of the following types: 
    Plain Test, HTML, Videos, Images or Music.



	TITLE:Python
	DESCRIPTION:Python is a programming language that is characterized by its 
	readability and easy syntax structure. it is considered a high level 
	programing lanaguage.
	

	TITLE: Variables 
	DESCRIPTION:Variables utilize an assignment statement which
	allows the programmer to name an expression and refer to that name
	instead of having to input the expression each time it is needed.

	TITLE:STRINGS
	DESCRIPTION:A string is any character on a keyboard that can be 
	displayed on the screen. The character and can be alpha, numeric 
	or characters. Strings are declared by encasing them in either single, 
	double or triple quotation marks. A string may not have any characters 
	at all, an empty string."""

def generate_all_html(text):
	current_concept_number=1
	concept=get_concept_by_number(text,current_concept_number)
	all_html=''
	while concept!='':
		title=get_title(concept)
		description=get_description(concept)
		concept_html=generate_concept_HTML(title,description)
		all_html=all_html+concept_html
		current_concept_number=current_concept_number + 1
		concept=get_concept_by_number(text, current_concept_number)
	return all_html

print generate_all_html(TEST_TEXT)

	
