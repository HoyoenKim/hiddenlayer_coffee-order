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

router.post('/createBooth', function(req, res, next) {
	// TODO storeInfo 를 request body 에서 받아와야 함.
	// @Description: Create booth information.
	// @Related: admin
	// @Now: 하드코딩
	var boothInfo = req.body;

	let inSql = 'insert into booths ('
	+ 'booth_id, '
	+ 'booth_title, '
	+ 'booth_subtitle, '
	+ 'booth_description, '
	+ 'booth_address, '
	+ 'booth_location, '
	+ 'booth_images_nums, '
	+ 'booth_keyword_ids, '
	+ 'booth_menutable_ids, '
	+ 'booth_events_ids'
	+ ') values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)';
	
	let inParam = [
		boothInfo.booth_id,
		boothInfo.booth_title, 
		boothInfo.booth_subtitle,
		boothInfo.booth_description,
		boothInfo.booth_address,
		JSON.stringify(boothInfo.booth_location),
		boothInfo.booth_images_nums,
		JSON.stringify(boothInfo.booth_keyword_ids),
		JSON.stringify(boothInfo.booth_menutable_ids),
		JSON.stringify(boothInfo.booth_events_ids),
	];
	
	connection.query(inSql, inParam, function(err, result, fields) {
		if(err) {
			console.log(err);
			res.status(406).send('Already Exists booth!');
		}
		else {
			res.status(200).send('Success!');
		}
	})
});

router.get('/allBooths', function(req, res, next) {
  // @Description: Select all booth' information.
	
	let selectSql = 'select * from booths';
	
	connection.query(selectSql, function(err, result, fields) {
		if(err) {
			console.log(err);
			res.status(406).send({stores: []});
		}
		else {
			res.status(200).send({booths: result});
		}
	}) 
});

module.exports = router;