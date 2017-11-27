$(function() {
  var YOUR_CLIENT_ID = 'wwR7NaPxpyPtbfvN85V3xNAM7EF7MLl0qVPZ5WN3';
  var YOUR_REDIRECT_URI = 'https://yinfei.dev.mixpanel.org/oauthtest/implicit/';

  var state = parseInt(Math.random() * 100)

  $('#oauth_btn').click(function() {
    var url = 'https://mixpanel.com/oauth/authorize/?client_id=' + encodeURIComponent(YOUR_CLIENT_ID) + '&redirect_uri=' + encodeURIComponent(YOUR_REDIRECT_URI) + '&response_type=token&approval_prompt=auto&state=' + state;
    window.location = url;
  });

  $('#stream_btn').click(function() {
    $.ajax({
      url: 'https://mixpanel.com/api/2.0/stream?event=%24custom_event%3A394936&type=average&selected_from_date=2017-06-01&to_date=2017-09-14&from_date=2017-04-13&unit=month',
      headers: {
        'Authorization': 'Bearer ' + window.location.hash.split('&')[0].substr(14)
      },
      success: function(data) {
        $('#result').text(data);
      },
      error: function(error) {
        $('#result').text(error);
      },
    })
  });
});
