var vflashcards = new Vue({
    delimiters: ['[[', ']]'],
    el: '#vflashcards',
    data: {
        card_id: '',
        front_word: '',
        back_word: '',
        answer_text: '',
        flipped: false,
        card_ids: []
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

    var answertext = vflashcards.answer_text;
    var cardId = vflashcards.card_id;
    $.ajax({
        url : "answer/",
        type : "POST",
        data : { answer_text : answertext,
                card_id : cardId,
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()},
        success : function(data) {
            if (data.correct_answer == true){
                var element = document.getElementById("flashcard");
                vflashcards.flipped = true;
                $("#card-form").hide();
                $("#next-card-form").show();
                vflashcards.answer_text = '';
            }
        },
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); 
        }
    });
};

function get_next_card() {
    // Get next card in the array (sequence)
    var cardId = vflashcards.card_ids[0]
    var answertext = vflashcards.answer_text;

    $.ajax({
        url : "next_card/",
        type : "POST",
        data : {
                card_id : cardId,
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()},
        success : function(data) {
            if (data.next_card == false){
                document.location.href = '/flashcards'
            }
            else{
                // Flip card and hide elements to stop bleed
                $("#next-card-form").hide();
                vflashcards.flipped = false;

                // Update card values
                vflashcards.card_id = data.pk
                vflashcards.front_word = data.front_word
                vflashcards.back_word = data.back_word

                $("#card-form").show();

                // Remove shown card from sequence
                vflashcards.card_ids.splice(vflashcards.card_ids.indexOf(cardId), 1);
            }

        },
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });


};

$( document ).ready(function() {
    console.log(document)
    $.post("get_cards/",
    {
        set: "none",
        csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
    },
    function(data, status){
        if (data.card_ids != 'undefined'){
            vflashcards.card_ids = data.card_ids
            console.log(data)

            if (data.first_card != 'undefined'){
                var card = data.first_card

                // Set card values
                vflashcards.card_id = card.pk
                vflashcards.front_word = card.front_word
                vflashcards.back_word = card.back_word

                // Remove card from sequence
                vflashcards.card_ids.splice(vflashcards.card_ids.indexOf(card.pk), 1);
            }
        }
    });

});
