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
// @Description store Controller
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.post('/createMenuTable', function(req, res, next) {
  // TODO menuTableInfo 를 request body 에서 받아와야 함.
  // TODO 1개의 Object 씩 insert 하도록 변경
	// @Description: Create menu table's information.
	// @Related: admin
	// @Now: 하드코딩

  var menuTableInfo = req.body;
  
  let inSql = 'insert into menuTables('
  + 'menu_table_id, '
  + 'menu_table_title, '
  + 'menu_table_subtitle, '
  + 'menu_ids, '
  + 'store_id'
  + ') values(?, ?, ?, ?, ?)';

  let inParam = [
    menuTableInfo.menu_table_id,
    menuTableInfo.menu_table_title,
    menuTableInfo.menu_table_subtitle,
    JSON.stringify(menuTableInfo.menu_ids),
    menuTableInfo.store_id
  ]

  connection.query(inSql, inParam, function(err, result, fields) {
    if(err) {
      console.log(err);
      res.status(406).send('Already Exists MenuTable!');
    }
    else {
      res.status(200).send('Success!');
    }
  })
});

router.get('/allMenuTables', function(req, res, next) {
  // @Description: Select all menu table's information and all menu's information in that menu table. 
	// @Related: MenuPage.vue

  let selectSql = 'select * from menuTables';

  connection.query(selectSql, function(err, result, fields) {
    if(err) {
      console.log(err);
      res.status(406).send('Ther is no Menu Table');
    }
    else {
      res.status(200).send({menuTables: result});
    }
  })
})

router.get('/readMenuTable/:menu_table_id', function(req, res, next) {
  // @Description: Select specific menu table's information and all menu's information in that menu table. 
	// @Related: MenuPage.vue

  var menu_table_id = req.params.menu_table_id;
  
  let selectSql = 'select * from menuTables where menu_table_id = ?';
  let selectParams = [menu_table_id];

  connection.query(selectSql, selectParams, function(err, result, fields) {
    if(err) {
      console.log(err);
      res.status(406).send('Ther is no Menu Table');
    }
    else {
      res.status(200).send({menuTable: result});
    }
  })
});

router.put('/updateMenuTable', function(req, res, next) {
  // TODO admin 페이지 구현 필요.
	// @Description: Update specific menu table's information.
	// @Related: admin
	// @Now: 미구현
  
  res.status(200).send({test: 'test'});
});

router.delete('/deleteMenuTable', function(req, res, next) {
  // TODO admin 페이지 구현 필요.
	// @Description: Delete specific menu table's information.
	// @Related: admin
	// @Now: 테스트 데이터 삭제
	// @Issue: DB delete 및 이미지까지 같이 지워야 함.
  
  //var store_id = 0;
  //
  //let deleteSql = 'delete from menuTables where store_id = ?';
  //let deleteParam = [store_id];
  //
  //connection.query(deleteSql, deleteParam, function(err, result, fields) {
	//	if(err) {
	//		console.log(err);
	//		res.status(406).send('There is no Menu Table!');
	//	}
  //  else {
  //    res.status(200).send('Success!');
  //  }
	//});
  res.status(200).send({test: 'test'});
});

router.post('/createMenu', function(req, res, next) {
  // TODO menuInfo 를 request body 에서 받아와야 함.
  // TODO 1개의 Object 씩 insert 하도록 변경
  // TODO creatMenuTable 로 합치기
	// @Description: Create menu's information.
	// @Related: admin
	// @Now: 하드코딩, 여러개를 한번에 집어 넣기 때문에 오류 처리가 잘못 되어서 한번 넣은 이후에는 에러 발생.
  
  var menuInfo = req.body;

  let inSql = 'insert into menus('
  + 'menu_id, '
  + 'menu_title, '
  + 'menu_subtitle, '
  + 'menu_price, '
  + 'menu_description, '
  + 'menu_price_options, '
  + 'menu_additional_options, '
  + 'store_id, '
  + 'menu_table_ids'
  + ') values(?, ?, ?, ?, ?, ?, ?, ?, ?)';

  let inParam = [
    menuInfo.menu_id,
    menuInfo.menu_title,
    menuInfo.menu_subtitle,
    menuInfo.menu_price,
    menuInfo.menu_description,
    JSON.stringify(menuInfo.menu_price_options),
    JSON.stringify(menuInfo.menu_additional_options),
    menuInfo.store_id,
    JSON.stringify(menuInfo.menu_table_ids)
  ]

  connection.query(inSql, inParam, function(err, result, fields) {
    if(err) {
      console.log(err);
      res.status(406).send('Already Exists Menu!');
    }
    else {
      res.status(200).send('Success!');
    }
  })
});

router.get('/allMenus', function(req, res, next) {
  // @Description: Select all stores' information.
	// @Related: StorePage.vue, MainLayout.vue
	
	let selectSql = 'select * from menus';
	
	connection.query(selectSql, function(err, result, fields) {
		if(err) {
			console.log(err);
			res.status(406).send({menus: []});
		}
		else {
			res.status(200).send({menus: result});
		}
	}) 
});

router.get('/readMenu/:menu_id', function(req, res, next) {
  // TODO readMenuTable 와 합쳐야함.
  // @Description: Select specific menu table's information and all menu's information in that menu table. 
	// @Related: MenuPage.vue

  var menu_id = req.params.menu_id;
  
  let selectSql = 'select * from menus where menu_id = ?';
  let selectParams = [menu_id];

  connection.query(selectSql, selectParams, function(err, result, fields) {
    if(err) {
      console.log(err);
      res.status(406).send('Ther is no Menu');
    }
    else {
      res.status(200).send({menu: result});
    }
  })
});


router.put('/updateMenu', function(req, res, next) {
  // TODO admin 페이지 구현 필요.
	// @Description: Update specific menu's information.
	// @Related: admin
	// @Now: 미구현
  
  res.status(200).send({test: 'test'});
});

router.delete('/deleteMenu', function(req, res, next) {
  // TODO admin 페이지 구현 필요.
  // TODO deleteMenuTable 로 합치기
	// @Description: Delete specific menu's information.
	// @Related: admin
	// @Now: 테스트 데이터 삭제
	// @Issue: DB delete 및 이미지까지 같이 지워야 함.
  var store_id = 0;

  let deleteSql = 'delete from menus where store_id = ?';
  let deleteParam = [store_id];

  connection.query(deleteSql, deleteParam, function(err, result, fields) {
		if(err) {
			console.log(err);
			res.status(406).send('There is no Menu!');
		}
    else {
      res.status(200).send('Success!');
    }
	});
});

router.post('/uploadImage', function(req, res, next) {
	// TODO admin 페이지 구현 필요.
	// @Description: Upload menu's images.
	// @Related: admin
	// @Now: 미구현

	res.status(200).send({test: 'test'});
})

router.put('/updateImage', function(req, res, next) {
	// TODO admin 페이지 구현 필요.
	// @Description: Update specific menu's image.
	// @Related: admin
	// @Now: 미구현

	res.status(200).send({test: 'test'});
})

module.exports = router;
