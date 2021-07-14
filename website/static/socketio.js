document.addEventListener('DOMContentLoaded', () => {
  var socket = io();

  socket.on('disconnect', () => {
    socket.emit('exit_chat')
  });

  socket.on('refresh_page', () => {
    location.reload();
  });
  
  socket.on('send_message', data => {
    socket.emit('receive_message', data);
  });

  socket.on('receive_message', data => {
    $('#display-messages').append('<li class="list-group-item">' + data + '</li>');
  });

  document.querySelector('#send_message').onclick = () => {
    data = document.querySelector('#user_message').value.trim()
    
    if(data.length) {
      socket.emit('send_message', data);
      socket.emit('store_message', data);
    }

    $('#user_message').val('');
  }
})