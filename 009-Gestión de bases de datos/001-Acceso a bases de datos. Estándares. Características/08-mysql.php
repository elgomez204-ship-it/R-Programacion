<?php
// sudo apt install php php-mysql
// sudo systemctl restart apache2
$host = "localhost";
$db   = "corporacion2026";
$user = "corporacion2026";
$pass = "Corporacion2026$";
$charset = "utf8mb4";

$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
    $pdo = new PDO($dsn, $user, $pass, $options);

    $stmt = $pdo->query("SELECT * FROM usuarios");
    while ($row = $stmt->fetch()) {
        print_r($row);
    }

} catch (PDOException $e) {
    die("Error de conexión: " . $e->getMessage());
}