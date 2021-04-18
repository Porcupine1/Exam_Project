window.onload = load;

function load() {
    document.getElementById("pop_sound").play();
}

function showSoftbookForm() {
    $('#softbook_form').css('visibility', 'visible');
}

function hideSoftbookForm() {
    $('#softbook_form').css('visibility', 'hidden');
}

setTimeout(function () {
    if ($('#msg').length > 0) {
        $('#msg').remove()
    }
}, 10000)

function searchBooks() {

    let filter, tables, textValue, tr;
    filter = $('#filter').val().toUpperCase();
    tables = $('table')

    for (let i = 0; i < tables.length; i++) {
        tr = tables[i].getElementsByTagName('tr')
        for (let j = 0; j < tr.length; j++) {
            let td = tr[j].getElementsByTagName('td')[1];

            if (td) {
                textValue = td.textContent || td.innerHTML;

                if (textValue.toUpperCase().startsWith(filter)) {
                    tr[j].style.display = "";
                } else {
                    tr[j].style.display = "none";
                }
            }
        }
    }
}