<?php
if (!empty($_POST)) {
    /*Проверяем поле name если что то есть тогда приветсвие если поле пустое ошибка*/
    if (!empty($_POST['name'])) {
        print_r('Приветствую'.$_POST['name']);
    }
    else {
        $errors[] = 'Поле name пустое';
    }

    /*Проверяем правильность ввода телефона в данном случае РБ*/
    if (preg_match('/(\+375|80)(29|25|44|33)(\d{3})(\d{2})(\d{2})/', $_POST['phone'])) {
        echo 'Телефон введен правильно'; }
        else{
            $errors[] = 'Не правильный номер телефона';
        }




    /*Проверяем правильность ввода email в данном случае РБ*/
    if (preg_match ('/[\.a-z0-9_\-]+[@][a-z0-9_\-]+([.][a-z0-9_\-]+)+[a-z]{1,4}/i', $_POST['email'])){
        echo 'Email введен правильно';}
        else{
            $errors[] = 'email введен не правильно';
        }



    /*Если массив с ошибками не пустой проходимся и выводим*/
    if (!empty($errors)) {
        foreach ($errors as $err) {
            echo "<strong>$err</strong><br>";
        }
    }

}



