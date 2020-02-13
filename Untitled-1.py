b = '215'

html = open ("vivid.html", 'w')
html_body = """
	<html>
		<head><title>abel</title></head>
		<body>
			<center><h1>{b}</h1></center>
		</body>
	</html>
"""
html.write(html_body)
html.close()