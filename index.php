<?php 
ob_start();
$base = __DIR__;
//passthru("python /media/anwar/b972b4d0-d82b-405b-8e69-9c879f172d9f/pyzk-master/attendance.py 192.168.20.26");
passthru("python {$base}/attendance.py 192.168.20.26");
$output = ob_get_clean(); 
$abc = json_decode($output);
$i = 0;
$bcd = [];
foreach($abc as $a){
    $i++;
    $bcd[] = json_decode($a);
}
print_r($bcd);

?>