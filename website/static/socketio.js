document.addEventListener('DOMContentLoaded', () => {
  var socket = io();

  socket.on('message', data => {
    $('#display-messages').append('<ol>' + data + '</ol>')
  });

  document.querySelector('#send_message').onclick = () => {
    socket.send(document.querySelector('#user_message').value);
    $('#user_message').val('');
  }
})