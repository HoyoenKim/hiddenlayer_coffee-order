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
// @Description store Controllerz
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.post('/createEvent', function(req, res, next) {
	var eventInfo = req.body;

	let inSql = 'insert into events('
	+ 'event_id, '
	+ 'event_title, '
	+ 'event_subtitle, '
	+ 'event_description, '
	+ 'event_duedate, '
	+ 'event_images_nums, '
	+ 'origin_type, '
	+ 'origin_id, '
	+ 'event_subscription_number'
	+ ') values(?, ?, ?, ?, ?, ?, ?, ?, ?)';

	let inParam = [
		eventInfo.event_id,
		eventInfo.event_title,
		eventInfo.event_subtitle,
		eventInfo.event_description,
		eventInfo.event_duedate,
		eventInfo.event_images_nums,
		eventInfo.origin_type,
		eventInfo.origin_id,
		eventInfo.event_subscription_number
	];

	connection.query(inSql, inParam, function(err, result, fields) {
		if(err) {
			console.log(err);
			res.status(406).send('Already Exists Event!')
		}
		else {
			res.status(200).send('Sucess!');
		}
	})
});

router.get('/allEvents', function(req, res, next) {
	// TODO admin 페이지 구현 필요.
	// @Description: Read all events' information.
	// @Related: EventPage.vue

	let selectSql = 'select * from events';

	connection.query(selectSql, function(err, result, fields) {
		if(err) {
			console.log(err);
			res.status(406).send({events: []});
		}
		else {
			res.status(200).send({events: result});
		}
	})
});

router.get('/readEvent/:event_id', function(req, res, next) {
	// TODO admin 페이지 구현 필요.
	// @Description: Read specific event's information.
	// @Related: EventPage.vue

	res.status(200).send({test: 'test'});
});

router.put('/updateEvent', function(req, res, next) {
	// TODO admin 페이지 구현 필요.
	// @Description: Update specific event's information.
	// @Related: admin

	res.status(200).send({test: 'test'});
});

router.delete('deleteEvent', function(req, res, next) {
	// TODO admin 페이지 구현 필요.
	// @Description: Delete specific event's information.
	// @Related: admin
	// @Now: 테스트 데이터 삭제
	// @Issue: DB delete 및 이미지까지 같이 지워야 함.

	res.status(200).send({test: 'test'});
});

router.post('/uploadImage', function(req, res, next) {
	// TODO admin 페이지 구현 필요.
	// @Description: Upload store's images.
	// @Related: admin
	// @Now: 미구현

	res.status(200).send({test: 'test'});
})

router.put('/updateImage', function(req, res, next) {
	// TODO admin 페이지 구현 필요.
	// @Description: Update specific number of store's image.
	// @Related: admin
	// @Now: 미구현

	res.status(200).send({test: 'test'});
})
module.exports = router;