<?php

	class Perro{
  	function __construct($color,$edad){
    	$this->color = $color;
      $this->edad = $edad;
    }
  }
  
  $perro1 = new Perro("Negro",1);
  $perro2 = new Perro("Blanco",2);
  
  var_dump($perro1);

?>