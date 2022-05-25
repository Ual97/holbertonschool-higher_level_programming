$(function () {
    $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, status) {
        if (status === 'success') {
            $('UL#list_movies').text(data.title);
        }
    });
});
