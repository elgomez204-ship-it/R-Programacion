<?php
	
  $vegetales = [
  	"lechuga",
    "espinacas",
    "tomate",
    "zanahoria"
  ];
  
  foreach($vegetales as $vegetal){
  	echo $vegetal."<br>";
  }
  // Ventajas del foreach: Es mas limpio
  // Desventajas del foreach: En principio no está el índice
?>