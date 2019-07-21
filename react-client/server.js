
const io = require('socket.io')();

io.on('connection', (client) => {
    var gaze = io.of('/gaze').on('connection', function (socket) {
        socket.on('gaze', function (gdata) {
            gaze.emit('gaze', gdata.toString());
        });
    });
});

const port = 8000;
io.listen(port);
console.log('listening on port ', port);