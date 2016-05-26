"use strict";

// This function gets cookie with a given name
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
 
/*
The functions below will create a header with csrftoken
*/
 
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}
 
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

// Funkcja jest wywoływana podczas kliknięcia na przycisk "Edytuj"
function onclick_edit(id) {
    $.ajax({
        url : "/edit/",
        type : "POST",
        data : { obw_id : id },

        // Zapytanie powiodło się
        success : function(json) {
            $('#edytuj_'+id).toggleClass("invisible", true);
            $('#zapisz_'+id).toggleClass("invisible", false);
            $('#anuluj_'+id).toggleClass("invisible", false);
            var td = '#td_'+id;
            $(td+'_głosy').html("");
            $(td+'_karty').html("");
            $(td+'_licznik').html("");
            $('<input type="number" name="głosy" id="form_glosy_'+id+'" value="'+json.ile_glosow+'"/>').appendTo(td+'_głosy');
            $('<input type="number" name="karty" id="form_karty_'+id+'" value="'+json.ile_kart+'"/>').appendTo(td+'_karty');
            $('<input type="hidden" name="licznik" id="form_licznik_'+id+'" value="'+json.licznik+'"/>').appendTo(td+'_licznik');
        },

        // Zapytanie nie powiodło się
        error : function(xhr,errmsg,err) {
            alert('Wystąpił błąd.')
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });

}

// Funkcja jest wywoływana podczas kliknięcia na przycisk "Anuluj"
function onclick_cancel(id) {
    $.ajax({
        url : "/edit/",
        type : "POST",
        data : { obw_id : id },

        // Zapytanie powiodło się
        success : function(json) {
            $('#edytuj_'+id).toggleClass("invisible", false);
            $('#zapisz_'+id).toggleClass("invisible", true);
            $('#anuluj_'+id).toggleClass("invisible", true);
            var td = '#td_'+id;
            $(td+'_głosy').html("");
            $(td+'_karty').html("");
            $(td+'_licznik').html("");
            $('#error_div').toggleClass("invisible", true);
            $('#tr_'+id).toggleClass("red", false);
            $('<span>'+json.ile_glosow+'</span>').appendTo(td+'_głosy');
            $('<span>'+json.ile_kart+'</span>').appendTo(td+'_karty');
        },

        // Zaoytanie nie powiodło się
        error : function(xhr,errmsg,err) {
            alert('Wystąpił błąd.')
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });
}

// Funkcja zapobiega domyślnemu zachowaniu podczas wysyłania formularza
$('#post-form').live('submit', function(event){
    event.preventDefault();
});

// Funkcja jest wywoływana podczas kliknięcia na przycisk "Zapisz"
function onclick_accept(id) {
    var td = '#td_'+id;
    var licznik = $('#form_licznik_'+id).val();
    var ile_glosow = $('#form_glosy_'+id).val();
    var ile_kart = $('#form_karty_'+id).val();

    // Sprawdzanie poprawności danych wpisanych do pól formularza
    if ($.isNumeric(ile_glosow) && $.isNumeric(ile_kart) && ile_glosow >= 0 && ile_kart >= 0 && Math.round(ile_kart) == ile_kart && Math.round(ile_glosow) == ile_glosow) {
        $.ajax({
            url : "/accept/",
            type : "POST",
            data : { obw_id : id, obw_licznik : licznik, karty : ile_kart, glosy : ile_glosow },

            // Zapytanie powiodło się
            success : function(json) {
                var changed = json.changed;
                if (!changed) {
                    $('#tr_'+id).toggleClass("red", true);
                    $('#error_div').toggleClass("invisible", false);
                    $('#error_div').html("");
                    $('<span>Uwaga! Dane zostały zmienione od ostatniego odczytu.<br>Liczba uprawnionych do głosowania: '+json.ile_glosow+'<br>Liczba wydanych kart do głosowania: '+json.ile_kart+'</span>').appendTo('#error_div');
                    $('#form_licznik_'+id).val(json.licznik);
                }
                else {
                    $('#error_div').toggleClass("invisible", true);
                    $('#edytuj_'+id).toggleClass("invisible", false);
                    $('#zapisz_'+id).toggleClass("invisible", true);
                    $('#anuluj_'+id).toggleClass("invisible", true);
                    $(td+'_głosy').html("");
                    $(td+'_karty').html("");
                    $(td+'_licznik').html("");
                    $('#tr_'+id).toggleClass("red", false);
                    $('<span>'+json.ile_glosow+'</span>').appendTo(td+'_głosy');
                    $('<span>'+json.ile_kart+'</span>').appendTo(td+'_karty');
                }
            },

            // Zapytanie nie powiodło się
            error : function(xhr,errmsg,err) {
                alert('Wystąpił błąd.');
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    }
    else {
        alert('Wprowadź poprawne dane. Muszą być to liczby całkowite większe od zera.');
    }
}