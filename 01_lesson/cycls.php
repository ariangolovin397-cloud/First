<form>
    <input type="text" name="username" />
    <button type="submit">Send</button>

<?php
$first = "Hi";
echo "<h1>".$first."</h1>";
// 1
$people = ["Maxim","Nikita","Markus"];
// $items  = ["Apple", "Banana", "Orange"]; 
// $len    = count($items);
$count  = count($people);

for ($i = 0; $i < $count; $i++) {
    echo "<h2 style=\"display:inline\">".$people[$i];
    if ($count - 1 > $i) {
        echo ", ";
    }
    echo "</h2>";
}
echo "<br><br>";

foreach ($people as $index => $value) {
    echo "Index: $index, Value: $value<br>";
}

echo "<br>";

$i = 0; 
while ($i < $count) {
    echo $people[$i] . "<br>";
    $i++;
}

echo "<br>";

array_walk($people, function ($value, $key) {
    echo "$key => $value<br>";
});

?>
</form>
