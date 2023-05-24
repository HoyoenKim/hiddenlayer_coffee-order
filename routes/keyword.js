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
  database : 'order_db2'
})
connection.connect();

// TODO need to use mvc pattern.
// @Description store Controller
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

router.post('/createKeyword', function(req, res, next) {
	// TODO storeInfo 를 request body 에서 받아와야 함.
	// @Description: Create keyword information.
	// @Related: admin
	// @Now: 하드코딩
	var keywordInfo = req.body;

	let inSql = 'insert into keywords('
	+ 'keyword_id, '
	+ 'keyword_title, '
	+ 'keyword_description, '
	+ 'origin_type, '
	+ 'origin_id'
	+ ') values(?, ?, ?, ?, ?)';
	
	let inParam = [
		keywordInfo.keyword_id,
		keywordInfo.keyword_title, 
		keywordInfo.keyword_description,
		keywordInfo.origin_type,
		keywordInfo.origin_id,
	];
	
	connection.query(inSql, inParam, function(err, result, fields) {
		if(err) {
			console.log(err);
			res.status(406).send('Already Exists Keyword!');
		}
		else {
			res.status(200).send('Success!');
		}
	})
});

router.get('/allKeywords', function(req, res, next) {
  // @Description: Select all keyword' information.
	
	let selectSql = 'select * from keywords';
	
	connection.query(selectSql, function(err, result, fields) {
		if(err) {
			console.log(err);
			res.status(406).send({stores: []});
		}
		else {
			res.status(200).send({keywords: result});
		}
	}) 
});

module.exports = router;