const express      = require('express');
const cookieParser = require('cookie-parser');
const logger       = require('morgan');
const cors         = require('cors');
const createError  = require('http-errors');
const bodyParser   = require('body-parser');
const path         = require('path');

// using
const storeRouter = require('./routes/store');
const brandRouter = require('./routes/brand');
const orderRouter = require('./routes/order');
const menuRouter  = require('./routes/menu');

// not using
const indexRouter = require('./routes/index');
const usersRouter = require('./routes/users');

const app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(cors());
app.use(logger('dev'));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(cookieParser());
app.use('/static',express.static(path.join(__dirname, 'public')));

// using
app.use('/store', storeRouter);
app.use('/brand', brandRouter);
app.use('/menu', menuRouter);
app.use('/order', orderRouter);

// not using
app.use('/', indexRouter);
app.use('/users', usersRouter);

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
