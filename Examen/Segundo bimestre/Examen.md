
Nuestro proyecto grupal es en base a la idea de una tienda de cosas retro, llamada Retroplay, para poder generar el catalogo de productos y reservarlos, en este examen nos enfocaremos en php y las conexones hacia la base de datos y el como muchas acciones de la página se procesan.

El sistema se articula en varios componentes claves

`conexion.php:` Este archivo se encarga de la conexion a la base de datos y se reutiliza en varios archivos para asegurar la conexion.

`procesar.php:` Este se encarga de procesar las acciones que se realizan en la pagina, recibir y procesar los datos enviados desde el front-end.

`inicio.php:` Este archivo se encarga de mostrar las imagenes, titulo y precio de los productos (Consolas o videojuegos) y permite agregar.

`carrito.php:` Este archivo se encarga de mostrar los productos agregados al carrito, eliminar productos del carrito y reservarlos

`reservas.php:` Este archivo se encarga de mostrar las reservas realizadas por el usuario, mostrando los productos reservados, la fecha de la reserva y el estado de la reserva.

`mi_cuenta.php:` Este archivo se encarga de mostrar la informacion del usuario y permite modificar la informacion del usuario tal como contraseña y permite hacer logout.

El codigo a continuacion esta comentado para su mejor entendimiento.

### 1. Conexion.php
```php
<?php
$conexion = mysqli_connect("localhost", "retroplay", "Retroplay123$", "retroplay");
if (!$conexion) {
    die("Error de conexión: " . mysqli_connect_error());
}
?>
```
Este apartado
### 2. Procesar.php
```php
<?php
// CONEXIÓN A LA BASE DE DATOS
// Incluimos el archivo que contiene la configuración para conectarse a la base de datos (host, usuario, contraseña, nombre BD).
include '../Conexion_BD/conexion.php';

// VERIFICACIÓN DE DATOS RECIBIDOS
// Comprobamos si el formulario nos ha enviado un campo llamado 'accion' (hidden input) para saber qué hacer.
if (isset($_POST['accion'])) {

    // Guardamos la acción en una variable para usarla más fácilmente.
    $accion = $_POST['accion'];

    // PROCESO DE REGISTRO
    // Si la acción es 'registro', entramos en este bloque.
    if ($accion == 'registro') {

        // Recogemos los datos enviados desde el formulario de registro.
        $nickname = $_POST['nickname'];
        $contrasena = password_hash($_POST['contrasena'], PASSWORD_DEFAULT);
        $correo = $_POST['correo'];
        $telefono = $_POST['telefono'];

        // Usar prepared statement para insertar de forma segura.
        $stmt = $conexion->prepare("INSERT INTO usuarios (nickname, correo, telefono, contrasena) VALUES (?, ?, ?, ?)");
        if ($stmt) {
            $stmt->bind_param("ssss", $nickname, $correo, $telefono, $contrasena);
            if ($stmt->execute()) {
                // Registro exitoso — redirigir al login.
                header('Location: ../../front/login/login.html');
                exit;
            } else {
                echo "Error al registrar: " . htmlspecialchars($stmt->error);
            }
            $stmt->close();
        } else {
            echo "Error al preparar la consulta: " . htmlspecialchars($conexion->error);
        }

        // PROCESO DE LOGIN
        // Si la acción es 'login', entramos en este otro bloque.
    } elseif ($accion == 'login') {

        // Recogemos los datos del formulario de login.
        $nickname = $_POST['nickname'];
        $contrasena = $_POST['contrasena'];

        // Buscar usuario por nickname y comprobar contraseña con password_verify().
        $stmt = $conexion->prepare("SELECT id, nickname, contrasena FROM usuarios WHERE nickname = ?");
        if ($stmt) {
            $stmt->bind_param("s", $nickname);
            $stmt->execute();
            $res = $stmt->get_result();
            if ($res && $res->num_rows > 0) {
                $row = $res->fetch_assoc();
                if (password_verify($contrasena, $row['contrasena'])) {
                    session_start();
                    $_SESSION['user_id'] = $row['id'];
                    $_SESSION['nickname'] = $row['nickname'];
                    $_SESSION['flash'] = "¡Bienvenido, " . $row['nickname'] . "!";
                    header('Location: ../../front/inicio/inicio.php');
                    exit;
                } else {
                    echo "<script>alert('Usuario o contraseña incorrectos.'); window.history.back();</script>";
                }
            } else {
                echo "<script>alert('Usuario o contraseña incorrectos.'); window.history.back();</script>";
            }
            $stmt->close();
        } else {
            echo "Error en el servidor. Inténtalo más tarde.";
        }
    }

    // NUEVA ACCIÓN: CREAR RESERVA (ENVÍO DESDE EL FRONTEND)
    elseif ($accion == 'create_reserva') {
        // Devolver JSON
        header('Content-Type: application/json');

        session_start();
        if (!isset($_SESSION['user_id'])) {
            echo json_encode(['success' => false, 'error' => 'No autenticado']);
            exit;
        }

        $usuario_id = intval($_SESSION['user_id']);
        $reservas_json = isset($_POST['reservas']) ? $_POST['reservas'] : '[]';
        $items = json_decode($reservas_json, true);

        if (!is_array($items) || count($items) === 0) {
            echo json_encode(['success' => false, 'error' => 'Sin artículos para reservar']);
            exit;
        }

        // Transacción para insertar reserva y sus líneas
        mysqli_begin_transaction($conexion);
        try {
            $fecha = date('Y-m-d H:i:s');

            $stmt = $conexion->prepare("INSERT INTO reservas (fecha, usuario_id) VALUES (?, ?)");
            if (!$stmt) throw new Exception($conexion->error);
            $stmt->bind_param("si", $fecha, $usuario_id);
            if (!$stmt->execute()) throw new Exception($stmt->error);
            $reserva_id = $conexion->insert_id;
            $stmt->close();

            $stmt2 = $conexion->prepare("INSERT INTO lineareservas (reservas_id, producto_id) VALUES (?, ?)");
            if (!$stmt2) throw new Exception($conexion->error);

            foreach ($items as $it) {
                $pid = isset($it['id']) ? intval($it['id']) : 0;
                if ($pid <= 0) continue;
                $stmt2->bind_param("ii", $reserva_id, $pid);
                if (!$stmt2->execute()) throw new Exception($stmt2->error);
            }
            $stmt2->close();

            mysqli_commit($conexion);

            // Limpiar carrito si existe en la sesión
            session_start();
            if (isset($_SESSION['cart'])) {
                $_SESSION['cart'] = [];
            }

            echo json_encode(['success' => true, 'reserva_id' => $reserva_id]);
            exit;
        } catch (Exception $e) {
            mysqli_rollback($conexion);
            echo json_encode(['success' => false, 'error' => $e->getMessage()]);
            exit;
        }
    }

    // ACCIÓN: ACTUALIZAR CARRITO EN LA SESIÓN
    elseif ($accion == 'update_cart') {
        header('Content-Type: application/json');
        session_start();
        $cart_json = isset($_POST['cart']) ? $_POST['cart'] : '[]';
        $cart = json_decode($cart_json, true);
        if (!is_array($cart)) {
            echo json_encode(['success' => false, 'error' => 'Formato de carrito no válido']);
            exit;
        }
        $_SESSION['cart'] = $cart;
        echo json_encode(['success' => true]);
        exit;
    }

} else {
    // CASO DE ERROR: PARAMETROS FALTANTES
    // Si alguien intenta entrar a este archivo directamente sin enviar datos POST.
    echo "Faltan parámetros.";
}
?>
```
### 3. Inicio.php
```php
<?php
session_start();
// Incluir el archivo de conexión a la base de datos.
include '../../back/Conexion_BD/conexion.php';

// Capturar mensaje flash (si existe) y eliminarlo de la sesión.
$flash = '';
if (isset($_SESSION['flash'])) {
  $flash = $_SESSION['flash'];
  unset($_SESSION['flash']);
}

// VERIFICACIÓN DE CONEXIÓN
// Verificamos si la variable $conexion existe y es válida.
if (!isset($conexion) || !$conexion) {
  echo '<h2 style="color:red">Error: no se pudo conectar a la base de datos.</h2>';
  // Si el modo debug está activo, mostramos el error específico de MySQL.
  if (isset($_GET['debug'])) {
    echo '<pre style="color:red">' . htmlspecialchars(mysqli_connect_error()) . '</pre>';
  }
  echo '</body></html>';
  // Detenemos la ejecución si no hay base de datos.
  exit;
}
?>

--------------------------------------
<?php

      // SECCIÓN DE CONSOLAS

      // Consulta SQL para seleccionar consolas.
      $sql_c = "SELECT * FROM producto WHERE LOWER(categoria) = 'consola'";

      // Ejecutar consulta.
      $res_c = mysqli_query($conexion, $sql_c);

      // Comprobar errores.
      if (!$res_c) {
        if (isset($_GET['debug'])) {
          echo "<p style='color:red'>Error consulta consolas: " . htmlspecialchars(mysqli_error($conexion)) . "</p>";
        }
      } else {
        // Comprobar si está vacío.
        if (mysqli_num_rows($res_c) === 0 && isset($_GET['debug'])) {
          echo "<p style='color:orange'>Aviso: no se encontraron consolas.</p>";
        }

        // Recorrer los resultados.
        while ($p = mysqli_fetch_assoc($res_c)) {
          // Lógica de imagen (similar a videojuegos pero buscando en carpeta consolas).
          $filename = isset($p['imagen']) && trim($p['imagen']) !== '' ? basename($p['imagen']) : '';

          if ($filename !== '') {
            $img_path = "css/img/consolas/{$filename}";
            // Verificación de existencia del archivo.
            if (!file_exists(__DIR__ . '/' . $img_path)) {
              if (isset($_GET['debug'])) {
                echo "<p style='color:orange'>Aviso: imagen no encontrada: " . htmlspecialchars($img_path) . "</p>";
              }
              $img_path = 'css/img/nintendogs.jpg'; // Imagen fallback (puede que quieras cambiarla a una genérica de consola)
            }
          } else {
            $img_path = 'css/img/nintendogs.jpg';
          }

          // Renderizar HTML.
          echo "<article>";
          echo "<img src=\"{$img_path}\" alt=\"" . htmlspecialchars($p['titulo']) . "\">";
          echo "<h3>" . htmlspecialchars($p['titulo']) . "</h3>";
          echo "<h4>Disponibilidad</h4>";
          echo "<p>" . htmlspecialchars($p['precio']) . " por semana</p>";
          // Botón 'Añadir al carrito'.
          echo '<a href="#" class="add-to-cart" data-id="' . htmlspecialchars($p['id'], ENT_QUOTES) . '" data-title="' . htmlspecialchars($p['titulo'], ENT_QUOTES) . '" data-price="' . htmlspecialchars($p['precio'], ENT_QUOTES) . '" data-img="' . htmlspecialchars($img_path, ENT_QUOTES) . '">Añadir al carrito</a>';
          echo "</article>";
        }
      }
      ?>
```
### 4. Carrito.php
```php
<?php
session_start();
// Cargamos el carrito de la sesión (si existe)
$server_cart = isset($_SESSION['cart']) ? $_SESSION['cart'] : [];
?>
```
### 5. reservas.php
```php
<?php
session_start();
include '../../back/Conexion_BD/conexion.php';

if (!isset($_SESSION['user_id'])) {
  header('Location: ../login/login.html');
  exit;
}

$uid = intval($_SESSION['user_id']);
$sql = "SELECT id, fecha FROM reservas WHERE usuario_id = $uid ORDER BY fecha DESC";
$res = mysqli_query($conexion, $sql);
?>

<?php
      if (!mysqli_num_rows($res)) {
        echo '<p>No tienes reservas registradas en el servidor.</p>';
      } else {
        while ($r = mysqli_fetch_assoc($res)) {
          echo '<section class="reserva">';
          echo '<h3>Reserva #' . htmlspecialchars($r['id']) . ' — ' . htmlspecialchars($r['fecha']) . '</h3>';
          echo '<div class="items">';

          $rid = intval($r['id']);
          $sql2 = "SELECT p.id, p.titulo, p.precio, p.imagen, p.categoria FROM lineareservas lr JOIN producto p ON lr.producto_id = p.id WHERE lr.reservas_id = $rid";
          $res2 = mysqli_query($conexion, $sql2);

          while ($p = mysqli_fetch_assoc($res2)) {
            $filename = isset($p['imagen']) && trim($p['imagen']) !== '' ? basename($p['imagen']) : '';
            $categoria = isset($p['categoria']) ? strtolower(trim($p['categoria'])) : 'videojuego';
            
            if ($filename !== '') {
              $folder = ($categoria === 'consola') ? 'consolas' : 'videojuegos';
              $img = 'css/img/' . $folder . '/' . htmlspecialchars($filename);
            } else {
              $folder = ($categoria === 'consola') ? 'consolas' : 'videojuegos';
              $img = 'css/img/' . $folder . '/nintendogs.jpg';
            }
            
            echo '<article><img src="' . $img . '" alt="' . htmlspecialchars($p['titulo']) . '"><h4>' . htmlspecialchars($p['titulo']) . '</h4><p>' . htmlspecialchars($p['precio']) . '</p></article>';
          }

          echo '</div></section>';
        }
      }
      ?>
```
### 6. Mi cuenta.php
```php
<?php
// Iniciar el manejo de sesiones. Esto es necesario para acceder a las variables $_SESSION.
session_start();

// Verificar si el usuario NO ha iniciado sesión comprobando si 'user_id' no existe.
if (!isset($_SESSION['user_id'])) {
  // Si no hay sesión activa, redirigir al usuario al formulario de login.
  header('Location: ../login/login.html');
  // Detener la ejecución del script para evitar que se cargue el resto de la página.
  exit;
}

// Incluir el archivo de conexión a la base de datos.
include '../../back/Conexion_BD/conexion.php';

// Obtener id del usuario desde la sesión (como entero)
$id = isset($_SESSION['user_id']) ? intval($_SESSION['user_id']) : 0;

// Consulta simple (estilo alumno)
$sql = "SELECT nickname, correo, telefono FROM usuarios WHERE id = $id";
$res = mysqli_query($conexion, $sql);
if ($res && mysqli_num_rows($res) > 0) {
  $user = mysqli_fetch_assoc($res);
} else {
  $user = ['nickname' => '', 'correo' => '', 'telefono' => ''];
}
?>
```

En conclusión, el desarrollo de **Retroplay** nos ha servido para unir todas las piezas del rompecabezas del desarrollo web. Hemos pasado de ver archivos sueltos a construir un sistema dinamico donde lo que ve el usuario (frontend) se comunica realmente con la lógica del servidor (PHP) y los datos (MySQL).

Lo más importante de este proceso ha sido entender el "detrás de escena": cómo verificamos quién es el usuario para que sus datos estén seguros, cómo gestionamos sus reservas y cómo organizamos el código para que todo tenga sentido. Aunque es un proyecto de clase, refleja fielmente los retos de crear una tienda online real, donde la seguridad y la funcionalidad deben ir siempre de la mano.