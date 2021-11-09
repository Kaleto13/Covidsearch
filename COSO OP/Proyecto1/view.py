from django import http
from django.http import HttpResponse
from django.http.response import HttpResponseBadRequest

def saludo(request):

  respuesta = """
<html>
<head>
<style>
body {
  background-color: grey;
}
h1 {
  color: white;
  text-align: center;
}
  
p {
  font-family: comicsans;
  font-size: 20px;
}
</style>
</head>
<body>

<h1>TITULO GENIAL B)</h1>
<p>Si porfavor.</p>
<ul>
<li><a href="default.asp">Home</a></li>
<li><a href="news.asp">News</a></li>
<li><a href="contact.asp">Contact</a></li>
<li><a href="about.asp">About</a></li>
</ul>

</body>
</html>"""

  return HttpResponse(respuesta)
  
def default(request):
  respuesta = """
<html>
<head>
<style>
body {
  background-color: red;
  font-family: verdana, helvetica;
  font-weight: bold;
}
#nav{
   width: 155px;
}
.titulonav{
  border-right-width: 1px;
  border-right-style: solid;
  border-right-color: #d7d7d7;
  border-bottom-width: 1px;
  border-bottom-style: solid;
  border-bottom-color: #d7d7d7;
  padding-top: 5px;
  padding-right: 0pt;
  padding-bottom: 5px;
  padding-left: 4px;
  font-size: 8pt;
  font-weight: bold;
  background-color: #e8e8e8;
}
.cuerporec{
  border-width: 1px;
  border-style: solid;
  border-color: #d7d7d7;
  margin-top: 4px;
  margin-right: 0pt;
  margin-bottom: 10px;
  margin-left: 0pt;
}
.cuerporec ul{
  margin-top: 5px;
  margin-right: 10px;
  margin-bottom: 20px;
  margin-left: 0px;
  padding-top: 0pt;
  padding-right: 0pt;
  padding-bottom: 0pt;
  padding-left: 1px;
  list-style-type: none;
  list-style-image: none;
  list-style-position: outside;
}
.cuerporec li{
  padding-left: 12px;
  font-size: 8pt;
  padding-bottom: 2px;
  margin-top: 1px;
  margin-right: 0pt;
  margin-bottom: 1px;
  margin-left: 0pt;
  background: transparent url("cuadrado-amarillo.gif") 0 2px no-repeat;
}
.cuerporec a{
  text-decoration: none;
}
h1 {
  color: white;
  text-align: center;
}

p {
  font-family: comicsans;
  font-size: 40px;
}
</style>
</head>
<body>

<h1>TITULO GENIAL B)</h1>
<p>Si porfavor.</p>

</body>
</html>"""
  return HttpResponse(respuesta)
