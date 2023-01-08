var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');
var orderRouter = require('./routes/order');
var checkRouter = require('./routes/check');
var app = express();

const sqlite3 = require('sqlite3').verbose();
let db = new sqlite3.Database('./db/order.db', sqlite3.OPEN_READWRITE, (err) => {
  if (err) {
      console.error(err.message);
  } else {
      console.log('Connected to the orders database.');
  }
});

const createQuery = `
    CREATE TABLE IF NOT EXISTS orders(
        timestamp VARCHAR(100) PRIMARY KEY,
        username VARCHAR(100),
        coffeetype VARCHAR(100),
        coffeedense VARCHAR(100)
    )
`;

db.each(createQuery);

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/users', usersRouter);
app.use('/order', orderRouter);
app.use('/check', checkRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
