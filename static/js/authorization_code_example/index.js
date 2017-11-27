$(function() {
  $('#oauth_btn').click(function() {
    window.open('https://yinfei.dev.mixpanel.org/oauthtest/authorization_code/authenticate') // the api on your backend which starts OAuth
  });

  $('#refresh_btn').click(function() {
    window.open('https://yinfei.dev.mixpanel.org/oauthtest/authorization_code/refresh_token') // the api on your backend which starts OAuth
  });
});
