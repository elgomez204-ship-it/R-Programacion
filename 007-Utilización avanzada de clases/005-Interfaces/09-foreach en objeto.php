<?php
	
  $Usuario = [
  	"nombre" => "Juan",
    "apellidos" => "Patino",
    "email" => "juan@empresa.com"
  ];
  
  foreach($Usuario as $clave=>$valor){
  	echo $clave.": ".$valor."<br>";
  }
 

?>