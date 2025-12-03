<form>
    <input type="text" name="username" />
    <button type="submit">Send</button>

<?php
$first = "Hi";
echo "<h1>".$first."</h1>";

$people = ["Maxim","Nikita","Markus"];
$items  = ["Apple", "Banana", "Orange"]; 
$len    = count($items);
$count  = count($people);

for ($i = 0; $i < $count; $i++) {
    echo "<h2 style=\"display:inline\">".$people[$i]."</h2>";
    if ($count - 1 > $i) {
        echo ", ";
    }
}
echo "<br><br>";

foreach ($items as $index => $value) {
    echo "Index: $index, Value: $value<br>";
}

echo "<br>";

$i = 0; 
while ($i < $len) {
    echo $items[$i] . "<br>";
    $i++;
}

echo "<br>";

array_walk($items, function ($value, $key) {
    echo "$key => $value<br>";
});

?>
</form>
