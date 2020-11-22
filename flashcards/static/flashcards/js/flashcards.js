var vflashcards = new Vue({
    delimiters: ['[[', ']]'],
    el: '#vflashcards',
    data: {
        card_id: '',
        front_word: '',
        back_word: '',
        flipped: false

    },
    methods: {
        greet: function(name) {
            console.log('Hello from ' + name + '!')
        }
    }
});

$('#card-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    get_answer();
});

// $('#submit').on('click', function(event){
//     console.log("weeee")
// });

$('#next-card-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    get_next_card();
});


function get_answer() {
    console.log("get_answer is working!") // sanity check
    console.log($('#answer_text').val())


    var answertext = $('#answer_text').val();
    var cardId = $('#card_id').text();
    $.ajax({
        url : "answer/", // the endpoint
        type : "POST", // http method
        data : { answer_text : answertext,
                card_id : cardId,
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()}, // data sent with the post request

        // handle a successful response
        success : function(json) {
            // $('#post-text').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
            if (json.correct_answer == true){
                var element = document.getElementById("flashcard");
                // document.getElementById("flashcard").style.transform = "rotateY(180deg)";
                vflashcards.flipped = true;
                $("#card-form").hide();
                $("#next-card-form").show();
            }
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            // $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
            //     " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

function get_next_card() {
    console.log("get_next_card is working!") // sanity check
    var answertext = $('#answer_text').val();
    var cardId = $('#card_id').text();

    $.ajax({
        url : "next_card/", // the endpoint
        type : "POST", // http method
        data : {
                card_id : cardId,
                answer_text : answertext,
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()},

        // handle a successful response
        success : function(data) {
            // $('#post-text').val(''); // remove the value from the input
            console.log(data); // log the returned json to the console
            console.log("success"); // another sanity check
            // if (json.correct_answer == true){
            //     var element = document.getElementById("flashcard");
            //     document.getElementById("flashcard").style.transform = "rotateY(180deg)";
            // }
            // console.log(window.location.href)
            // window.location.href = '/'+ json.next_card_pk;
            // document.write(json)
            $("#next-card-form").hide();
            vflashcards.flipped = false;
            $('#card_id').text(data.pk)
            $('#front_word').text(data.front_word)
            $('#back_word').text(data.back_word)
            $("#card-form").show();

        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            // $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
            //     " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
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
