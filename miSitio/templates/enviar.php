<?php
//Llamando a los campos

    $name=$_POST['name'];
    $email=$_POST['email'];
    $subject=$_POST['subject'];
    $message=$_POST['message'];

//Datos para el correo

$destinatario="gustavo.soader.cx@gmail.com";
$asunto="Contacto de Nuestra Pagina Web";


$mensaje = "De: $name \n";
$mensaje .= "Correo: $email \n";
$mensaje .= "Tema: $subject \n";
$mensaje .= "Mensaje: $message \n";

//Enviar mensaje
mail($destinatario, $asunto, $mensaje);

?>