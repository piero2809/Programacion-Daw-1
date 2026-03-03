<?php

$cliente = [
    "nombre" => "Piero",
    "apellidos" => "Funes Larios",
    "email" => "piero@jocarsa.com"
];

foreach ($cliente as $clave => $valor) {
    echo "<legend>" . $clave . "</legend>";
    echo "<input type='text' value='" . $valor . "'>";
}


?>