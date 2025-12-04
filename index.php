<!DOCTYPE html>
<html>
<body>
    <a href="#map">Map</a>
<form method="POST">

    <input type="text" name="num1" placeholder="Number 1">
    <br><br>

    <input type="text" name="num2" placeholder="Number 2">
    <br><br>

    <select name="action">
        <option value="add">+</option>
        <option value="sub">-</option>
        <option value="mul">*</option>
        <option value="div">/</option>
    </select>

    <br><br>

    <button type="submit">Calculate</button>

</form>

<hr>

<?php

if ($_SERVER["REQUEST_METHOD"] === "POST") {

    $num1 = $_POST["num1"];
    $num2 = $_POST["num2"];
    $action = $_POST["action"];
    $error = null;
    $result = null;


    if (!is_numeric($num1) || !is_numeric($num2)) {
        $error = "Both inputs must be numbers!";
    }

    if ($action === "div" && $num2 == 0) {
        $error = "Division by zero is not allowed!";
    }

    if (!$error) {
        switch ($action) {
            case "add":
                $result = $num1 + $num2;
                break;
            case "sub":
                $result = $num1 - $num2;
                break;
            case "mul":
                $result = $num1 * $num2;
                break;
            case "div":
                $result = $num1 / $num2;
                break;
        }

        echo "<h3>Result: $result</h3>";
    } else {
        echo "<h3 style='color:red;'>$error</h3>";
    }
}

?>

</body>
</html>
