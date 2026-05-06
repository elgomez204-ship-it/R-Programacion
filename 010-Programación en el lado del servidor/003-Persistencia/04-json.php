<?php
  $usuario = [];
  $usuario['nombre'] = "Juan";
  $usuario['apellidos'] = "Patino";
  $usuario['email'] = "juan@empresa.com";
  
  $json = json_encode($usuario);
  echo $json;  
?>