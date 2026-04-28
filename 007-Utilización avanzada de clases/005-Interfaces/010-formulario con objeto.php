<?php
	
  $usuario = [
  	"nombre" => "Juan",
    "apellidos" => "Patino",
    "email" => "juan@empresa.com"
  ];
  
  foreach($usuario as $clave=>$valor){
  	echo "<label>".$clave."</label>";
    echo "<input type='text' value='".$valor."'>";
  }
 
?>