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

router.post('/createVenue', function(req, res, next) {
	// TODO storeInfo 를 request body 에서 받아와야 함.
	// @Description: Create venue information.
	// @Related: admin
	// @Now: 하드코딩
	var venueInfo = req.body;

	let inSql = 'insert into venues('
	+ 'venue_id, '
	+ 'venue_title, '
	+ 'venue_subtitle, '
	+ 'venue_description, '
	+ 'venue_address, '
	+ 'venue_location, '
	+ 'venue_images_nums, '
	+ 'venue_keyword_ids, '
	+ 'event_ids, '
	+ 'owner_ids, '
	+ 'booth_ids'
	+ ') values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)';
	
	let inParam = [
		venueInfo.venue_id,
		venueInfo.venue_title, 
		venueInfo.venue_subtitle,
		venueInfo.venue_description,
		venueInfo.venue_address,
		JSON.stringify(venueInfo.venue_location),
		venueInfo.venue_images_nums,
		JSON.stringify(venueInfo.venue_keyword_ids),
		JSON.stringify(venueInfo.event_ids),
		JSON.stringify(venueInfo.owner_ids),
		JSON.stringify(venueInfo.booth_ids),
	];
	
	connection.query(inSql, inParam, function(err, result, fields) {
		if(err) {
			console.log(err);
			res.status(406).send('Already Exists Venue!');
		}
		else {
			res.status(200).send('Success!');
		}
	})
});

router.get('/allVenues', function(req, res, next) {
  // @Description: Select all venues' information.
	
	let selectSql = 'select * from venues';
	
	connection.query(selectSql, function(err, result, fields) {
		if(err) {
			console.log(err);
			res.status(406).send({stores: []});
		}
		else {
			res.status(200).send({venues: result});
		}
	}) 
});

module.exports = router;