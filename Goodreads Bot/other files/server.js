/* server. js */

var express = require('express');
var app = express();
var bodyParser = require('body-parser');
const axios = require('axios')

app.use(bodyParser.json()); // for parsing application/json
app.use(bodyParser.urlencoded({
  extended: true
})); // for parsing application/x-www-form-urlencoded

//This is the route the API will call
app.post('/new-message', function(req, res) {
  const {message} = req.body

  /* Each message contains "text" and a "chat" object, which has an "id" 
  which is the chat id */

  if (!message || message.text.toLowerCase().indexOf('burgs') <0) {
    /* In case a message is not present, 
    or if our message does not have the word burgs in it, do nothing and 
    return an empty response*/
    return res.end()
  }

/* Querying for the book on GR 
var book = "Ender%27s+Game"
var gr_url = "https://www.goodreads.com/search.xml?key=mThN42bUl5LtbpR4ZAow&q="+book



var http = require('http');

var bookDetails = function getBookResults(callback) {

    return http.get({
        host: 'https://www.goodreads.com',
        path: '/search.xml?key=mThN42bUl5LtbpR4ZAow&q='+book
    }, function(response) {
        // Continuously update stream with data
        var body = '';
        response.on('data', function(d) {
            body += d;
        });
        response.on('end', function() {

            // Data reception is done, do whatever with it!
            var parsed = JSON.parse(body);
            console.log("I think we received the data!");
        });
    });

};

console.log("received bookDetails");

/* --- END ---*/

  /* If we've gotten this far, it means that we have received a message containing 
  the word "burgs".
  Respond by hitting the telegram bot API and responding to the approprite 
  chat_id with the word "Hello!!"
  Remember to use your own API toked instead of the one below  
  "https://api.telegram.org/bot<your_api_token>/sendMessage" */

  axios.post('https://api.telegram.org/bot398939207:AAEryDFxXtNflaP7ynBrOrslHDqDNVmXIvI/sendMessage', {
    chat_id: message.chat.id,
    text: 'Bababa!'
  })
    .then(response => {
      // We get here if the message was successfully posted
      console.log('Message posted')
      res.end('ok')
    })
    .catch(err => {
      // ...and here if it was not
      console.log('Error :', err)
      res.end('Error :' + err)
    })

});

// Finally, start our server
app.listen(process.env.PORT || 5000, function() {
  console.log('Telegram app listening on port 5000!');
});