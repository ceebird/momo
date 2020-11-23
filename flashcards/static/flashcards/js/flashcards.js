var vflashcards = new Vue({
    delimiters: ['[[', ']]'],
    el: '#vflashcards',
    data: {
        card_id: '',
        front_word: '',
        back_word: '',
        flipped: false

    },
});

$('#card-form').on('submit', function(event){
    event.preventDefault();
    get_answer();
});

$('#next-card-form').on('submit', function(event){
    event.preventDefault();
    get_next_card();
});


function get_answer() {

    var answertext = $('#answer_text').val();
    var cardId = $('#card_id').text();
    $.ajax({
        url : "answer/",
        type : "POST",
        data : { answer_text : answertext,
                card_id : cardId,
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()}, // data sent with the post request
        success : function(data) {
            if (data.correct_answer == true){
                var element = document.getElementById("flashcard");
                vflashcards.flipped = true;
                $("#card-form").hide();
                $("#next-card-form").show();
                $('#answer_text').val("");
            }
        },
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); 
        }
    });
};

function get_next_card() {
    console.log("get_next_card is working!") // sanity check
    var answertext = $('#answer_text').val();
    var cardId = $('#card_id').text();

    $.ajax({
        url : "next_card/",
        type : "POST",
        data : {
                card_id : cardId,
                answer_text : answertext,
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()},
        success : function(data) {
            console.log(data.next_card)
            if (data.next_card == false){
                document.location.href = '/flashcards'
            }
            else{
                $("#next-card-form").hide();
                vflashcards.flipped = false;
                $('#card_id').text(data.pk)
                $('#front_word').text(data.front_word)
                $('#back_word').text(data.back_word)
                $("#card-form").show();
            }

        },
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });


};

$( document ).ready(function() {
    console.log( "ready!" );
    $.post("first_card/",
    {
        set: "none",
        csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
    },
    function(data, status){
        $('#card_id').text(data.pk)
        $('#front_word').text(data.front_word)
        $('#back_word').text(data.back_word)
    });

});
