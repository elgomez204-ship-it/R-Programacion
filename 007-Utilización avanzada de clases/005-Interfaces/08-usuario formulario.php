<?php
	
  $campos_usuario = [
  	"nombre",
    "apellidos",
    "email",
    "telefono",
    "direccion",
    "poblacion"
  ];
  
  foreach($campos_cliente as $campo){
  	echo '<input type="text" placeholder="'.$campo.'"><br>';
  }

?>