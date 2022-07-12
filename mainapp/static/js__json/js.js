$(document).ready(function () {
            $('#example').DataTable({
                "language":{
                    url:"static/js__json/ru.json"
                },
                "order": [[3, 'desc']],
                "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "Все"]]
        });
    });

