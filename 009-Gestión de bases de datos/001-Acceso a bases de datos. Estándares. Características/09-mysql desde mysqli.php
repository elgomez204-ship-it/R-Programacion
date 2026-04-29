<?php

$conn = mysqli_connect(
    "localhost",
    "corporacion2026",
    "Corporacion2026$",
    "corporacion2026"
);

if (!$conn) {
    die("Error de conexión: " . mysqli_connect_error());
}

mysqli_set_charset($conn, "utf8mb4");

$result = mysqli_query($conn, "SELECT * FROM usuarios");

while ($row = mysqli_fetch_assoc($result)) {
    print_r($row);
}

mysqli_close($conn);