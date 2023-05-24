const express      = require('express');
const cookieParser = require('cookie-parser');
const cookieSession = require("cookie-session");
const logger       = require('morgan');
const cors         = require('cors');
const createError  = require('http-errors');
const bodyParser   = require('body-parser');
const path         = require('path');

const swaggerUi = require('swagger-ui-express');
const swaggerJsdoc = require("swagger-jsdoc");
const options = {
  definition: {
    openapi: "3.0.0",
    info: {
      title: "LocalOrder Express API with Swagger",
      version: "0.0.1",
      description:
        "This is a simple CRUD API application made with Express and documented with Swagger",
      contact: {
        name: "HiddenLayer",
        email: "cabinkhy@gm.gist.ac.kr",
      },
    },
    servers: [
      {
        url: "http://18.118.221.107:3001",
      },
    ],
  },
  apis: [
    "./routes/store.js",
    "./routes/brand.js",
    "./routes/menu.js",
    "./routes/event.js",
    "./routes/order.js",
  ],
};

const specs = swaggerJsdoc(options);
const https = require('https');
const fs = require('fs');

// using
const storeRouter = require('./routes/store');
const brandRouter = require('./routes/brand');
const orderRouter = require('./routes/order');
const menuRouter  = require('./routes/menu');
const eventRouter = require('./routes/event');
const usersRouter = require('./routes/users');
const venueRouter = require('./routes/venue');
const keywordRouter = require('./routes/keyword');

// not using
const indexRouter = require('./routes/index');

// database
const db = require("./models");
const Role = db.role;

db.sequelize.sync();
//force: true will drop the table if it already exists
//db.sequelize.sync({force: true}).then(() => {
//  console.log('Drop and Resync Database with { force: true }');
//  initial();
//});


const app = express();
app.set('views', path.join(__dirname, 'views')),
app.set('view engine', 'jade'),

// view engine setup
app.use(cors()),
app.use(logger('dev')),
app.use(bodyParser.urlencoded({ extended: true })),
app.use(bodyParser.json()),
app.use(cookieParser()),
app.use(
  cookieSession({
    name: "bezkoder-session",
    secret: "COOKIE_SECRET", // should use as secret environment variable
    httpOnly: true,
    sameSite: 'strict'
  })
),
app.use('/static',express.static(path.join(__dirname, 'public'))),
// routes
require("./routes/auth.routes")(app),
require("./routes/user.routes")(app),

https.createServer(
  {
    key: fs.readFileSync(__dirname + '/keys/key.pem', 'utf-8'),
    cert: fs.readFileSync(__dirname + '/keys/cert.pem', 'utf-8'),
  },
  app.use('/', indexRouter),
  app.use('/store', storeRouter),
  app.use('/brand', brandRouter),
  app.use('/menu', menuRouter),
  app.use('/event', eventRouter),
  app.use('/order', orderRouter),
  app.use('/users', usersRouter),
  app.use('/venue', venueRouter),
  app.use('/keyword', keywordRouter),

  app.use("/api-docs",
    swaggerUi.serve,
    swaggerUi.setup(specs)
  ),

  // catch 404 and forward to error handler
  app.use(function(req, res, next) {
    next(createError(404));
  }),

  // error handler
  app.use(function(err, req, res, next) {
    // set locals, only providing error in development
    res.locals.message = err.message;
    res.locals.error = req.app.get('env') === 'development' ? err : {};

    // render the error page
    res.status(err.status || 500);
    res.render('error');
  })
).listen(3000);

function initial() {
  Role.create({
    id: 1,
    name: "user",
  });

  Role.create({
    id: 2,
    name: "moderator",
  });

  Role.create({
    id: 3,
    name: "admin",
  });
}

module.exports = app;
