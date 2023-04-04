var express = require('express');
var router = express.Router();

// TODO need to seperate.
// @Desciption DB Connection
const mysql = require('mysql');
const connection = mysql.createConnection({
  host : 'localhost',
  port : '3306',
  user : 'hoyeon',
  password : '12345678',
  database : 'order_db'
})
connection.connect();

// TODO need to use mvc pattern.
// @Description store Controllerz
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.post('/createEvent', function(req, res, next) {

})

module.exports = router;