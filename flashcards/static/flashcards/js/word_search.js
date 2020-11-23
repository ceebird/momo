var vwordsearch = new Vue({
    delimiters: ['[[', ']]'],
    el: '#vwordsearch',
    data: {
        language_word: '',
        native_word: '',
        language: '',
        words: [ {} ],
        columns: [],
        message: ""
    }

});

$("#language_word").on("input", function(){
    if (vwordsearch.language_word != ''){
        vwordsearch.native_word = '';
        $("#native_word").prop("disabled", true );
    }
    else{$("#native_word").prop("disabled", false );}
});

$("#native_word").on("input", function(){
    if (vwordsearch.native_word != ''){
        vwordsearch.language_word = '';
        $("#language_word" ).prop( "disabled", true );
    }
    else{ $("#language_word" ).prop( "disabled", false );}
});

$('#search-form').on('submit', function(event){
    event.preventDefault();
    if (vwordsearch.columns.length != 0){ 
        vwordsearch.columns = [];
        vwordsearch.words = [];
    }

    var word;
    var filter;
    if (vwordsearch.language_word != ''){ 
        word = vwordsearch.language_word; 
        vwordsearch.columns.push('English', 'Spanish')
        filter = "en";
    }
    else if (vwordsearch.native_word != '')
    { 
        word = vwordsearch.native_word; 
        vwordsearch.columns.push('Spanish', 'English')
        filter = "es";
    }
    else{ return; }
    search_word(word, filter);
});

function search_word(word, filter) {
    $.post("search_word/",
    {
        csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
        word: word
    },
    function(data, status){
        if (data[data.length-1].message !== false){
            alert(data[data.length-1].message);
        }
        else{
            // Filter out any spanish entries that may have matched
            var es_words = data.filter(function (el) {
                return  typeof(el.meta) !== 'undefined' &&
                        el.meta.lang == filter
                });
            for (var i = 0; i < es_words.length; i++) {
                vwordsearch.words.push({  English: data[i].meta.stems, Spanish: data[i].shortdef })
                } 
        }
    });
};