<?php
    header("Content-Type:text/html; charset=utf-8");
    /* Temp->server */
    // ex: curl -d "sensor=1&Temp=28&Humid=75" http://192.168.185.86
    //curl -d "S=1&T=29&H=50&M=12&D=31" http://172.20.10.4/demo1.php

    $Temp=$_POST['T'];
    $Humid=$_POST['H'];
    $SensorID=$_POST['S'];

    echo 'Sensor:'.$SensorID."\n";
    echo 'Temperature:'.$Temp."\n";
    echo 'Humidity:' .$Humid."\n";

    $fp = fopen('/home/pi/www-data/temp_'.$SensorID.'.txt', 'w');
    fwrite($fp, $Temp);
    fclose($fp);
    $fp=fopen('/home/pi/www-data/humid_'.$SensorID.'.txt', 'w');
    fwrite($fp, $Humid);
    fclose($fp);

?>

