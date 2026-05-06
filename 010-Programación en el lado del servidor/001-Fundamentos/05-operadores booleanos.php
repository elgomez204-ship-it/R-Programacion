<?php
  echo 5 == 5 && 3 == 3 && 2 == 2; // Verdadero
  echo 5 == 5 && 3 == 3 && 2 == 1; // Falso
  
  echo 5 == 5 || 3 == 3 || 2 == 2; // Verdadero
  echo 5 == 5 || 3 == 3 || 2 == 1; // Verdadero
  echo 5 == 5 || 3 == 2 || 2 == 1; // Verdadero
  echo 5 == 3 || 3 == 2 || 2 == 1; // Falso
?>