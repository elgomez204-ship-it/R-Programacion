persona = {
	"nombre":"Juan",
  "apellidos":"Patino",
  "correo":"juan@empresa.com",
  "edad":22,
  "telefonos":[
  	{	
      "tipo":"fijo",
    	"número":62123455
    },
    {	
      "tipo":"movil",
    	"número":65456546
    }
  ]
}

print(persona)
print(persona["telefonos"][0]["número"])