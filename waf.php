<?php @include('/waf/waf.php');?>
<?php

if($_SERVER['REQUEST_METHOD']!="GET" or $_SERVER['REQUEST_METHOD']!="POST"){
    write_attack_log($_SEVER['REMOIT_ADDR'])
    
}
function write_attack_log($log){
    $log = date("Y/M/D H:i:s").$log
    $fileName = "log.txt";
    $file = fopen($fileName,'w') or die('Unable to open file');
    fwrite($file,$log);
    fclose($file);
    if strstr($log,'flag'){
        echo 'flag{776e723566d75e4e81c4c7d54612d52a}';
    } 
}
function filter_E_to_C($str){

}
?>