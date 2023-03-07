var express = require('express');
var router = express.Router();

// TODO need to seperate.
// @Desciption DB Connection
const mysql = require('mysql');
const connection = mysql.createConnection({
  host : 'localhost',
  port : '3306',
  user : 'localorder',
  password : '1234',
  database : 'order_db'
})
connection.connect();

// TODO need to use mvc pattern.
// @Description store Controller
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

router.get('/allStores', function(req, res, next) {
  // @Description: Select all stores' information.
	// @Related: StorePage.vue
	
	let selectSql = 'select * from stores';
	
	connection.query(selectSql, function(err, result, fields) {
		if(err) {
			console.log(err);
			res.status(406).send({stores: []});
		}
		else {
			res.status(200).send({stores: result});
		}
	}) 
});

router.post('/createStore', function(req, res, next) {
	// TODO storeInfo 를 request body 에서 받아와야 함.
	// @Description: Create store information.
	// @Related: admin
	// @Now: 하드코딩

	var storeInfo = {
		store_id: 0,
		store_title: '재야의 커피',
		store_subtitle: 'Cafe',
		store_description: '사용자 맞춤 원두 추천 카페',
		store_order_type: [1, 1, 1], // '테이블 주문 가능', '포장 가능', '배달 가능'
		store_location: ["35.23021", "126.839829"], // 위도, 경도
		store_open_time: [[10, 22], [10, 22], [10, 22], [10, 22], [10, 22], [10, 22], [10, 22], [10, 22]], // 월 - 일, 공휴일
		store_official_information: ['류현석', '창업진흥센터 B동 401호', '010-2128-7164'], // 소유자, 장소, 담당자 연락처
		branding_ids: [0, 1],
		menu_ids: [0, 1, 2],
		owner_ids: [0], // need to encription
	}

	let inSql = 'insert into stores('
	+ 'store_id, '
	+ 'store_title, '
	+ 'store_subtitle, '
	+ 'store_description, '
	+ 'store_order_type, '
	+ 'store_location, '
	+ 'store_open_time, '
	+ 'store_official_information, '
	+ 'brand_ids, '
	+ 'menu_ids, '
	+ 'owner_ids'
	+ ') values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)';
	
	let inParam = [
		storeInfo.store_id,
		storeInfo.store_title, 
		storeInfo.store_subtitle, 
		storeInfo.store_description, 
		JSON.stringify(storeInfo.store_order_type), 
		JSON.stringify(storeInfo.store_location),
		JSON.stringify(storeInfo.store_open_time),
		JSON.stringify(storeInfo.store_official_information),
		JSON.stringify(storeInfo.branding_ids),
		JSON.stringify(storeInfo.menu_ids),
		JSON.stringify(storeInfo.owner_ids),
	];
	
	connection.query(inSql, inParam, function(err, result, fields) {
		if(err) {
			console.log(err);
			res.status(406).send('Already Exists Store!');
		}
		else {
			res.status(200).send('Success!');
		}
	})

});

router.get('/readStore/:store_id', function(req, res, next) {
	// TODO 프론트 동작 방식과 깊게 연관되어 있어서 아직 구현 안함.
	// @Description: Select specific store's information.
	// @Related: BrandPage.vue, MenuPage.vue
	// @Now: vue pinia caching, using quasar localstorage

	res.status(200).send({test: 'test'});
});

router.put('/updateStore', function(req, res, next) {
	// TODO admin 페이지 구현 필요.
	// @Description: Update specific store's information.
	// @Related: admin
	// @Now: 미구현

	res.status(200).send({test: 'test'});
});

router.delete('/deleteStore', function(req, res, next) {
	// TODO admin 페이지 구현 필요.
	// @Description: Delete specific store's information.
	// @Related: admin
	// @Now: 테스트 데이터 삭제
	// @Issue: DB delete 및 이미지까지 같이 지워야 함.
	var store_title = '재야의 커피';

	let deleteSql = 'delete from stores where store_title = ?';
	let deleteParam = [store_title];

	connection.query(deleteSql, deleteParam, function(err, result, fields) {
		if(err) {
			console.log(err);
			res.status(406).send('There is no Store!');
		}
		else {
			res.status(200).send('Success!');
		}
	});
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
