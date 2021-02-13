<?php

require "../src/Sehir.php";

use TurkeyCities\Sehir;

$cities = new Sehir;

/* Büyük küçük harf duyarsızdır */

// İl ile il sorgusu
print_r($cities->il("istanbul"));

// İlçe ile il sorgusu
print_r($cities->ilce("esenyurt"));

// Plaka ile il sorgusu
print_r($cities->plaka("34"));

// Telefon kodu ile il sorgusu
print_r($cities->telefon("212"));

/* 
*stdClass Object
*(
*    [plaka] => 34
*    [il] => İstanbul
*    [telefon] => Array
*        (
*            [0] => 212
*            [1] => 216
*        )
*
*    [buyuksehir_den_beri] => 1984
*    [bolge] => Marmara
*    [ilceler] => Array
*        (
*            [0] => Adalar
*            [1] => Arnavutköy
*            [2] => Ataşehir
*            ...
*        )
*
*)
*/

// İllerin ilçelerine ait detaylı bilgiler
print_r($cities->ilceler_detay("istanbul"));

/* 
*stdClass Object
*(
*    [1] => stdClass Object
*        (
*            [Adalar] => stdClass Object
*                (
*                    [Burgazada] => stdClass Object
*                        (
*                            [posta_kodu] => 34975
*                            [mahalleler] => Array
*                                (
*                                    [0] => Burgazada Mah
*                                )
*
*                        )
*                )
*        )    
*   ....
*)   
*/