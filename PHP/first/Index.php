<?php
$array = [
	['address' => 'г. Минск, ул. Восточнаяя, д. 33', 'date_from' => '31-12-2002', 'date_to' => '31-12-2005'],
	['address' => 'г. Минск, ул. Восточнаяя, д. 34', 'date_from' => '31-12-2005', 'date_to' => '31-12-2006'],
	['address' => 'г. Минск, ул. Восточнаяя, д. 34', 'date_from' => '31-12-2006', 'date_to' => '31-12-2008'],
	['address' => 'г. Минск, ул. Тихая, д. 33', 'date_from' => '31-12-2000', 'date_to' => '31-12-2002'],
	['address' => 'г. Минск, ул. Ленина, д. 33', 'date_from' => '31-12-2008', 'date_to' => '31-12-2010'],
	['address' => 'г. Минск, ул. Ленина, д. 33', 'date_from' => '31-12-2010', 'date_to' => '31-12-2011'],
	['address' => 'г. Минск, ул. Тихая, д. 33', 'date_from' => '31-12-2012'],
	['address' => 'г. Минск, ул. Ленина, д. 33', 'date_from' => '31-12-2011', 'date_to' => '31-12-2012'],
];

function adress($array){
    foreach( $array as $val ){
        if($val == end($array)) {
            echo $val['date_from'], '/', date("d.m.Y"), ': ', $val ['address'], '<br />'; 
      }
      else {
          echo $val['date_from'], '/', $val ['date_to'], ': ', $val ['address'], '<br />'; 
      }
        
    }
}
adress($array);
?>
