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
  res.render('index', { title: 'order' });
});

router.post('/createOrder', function(req, res, next) {
  // TODO using user table
  // TODO 송금 여부 자동화
  // @Description: Create order
  // @Related: CartPage.vue, BrandLayout.vue
  var order_time = new Date(Date.now()).toString();

  var userInfo = {
    user_name: req.body.name,
    user_phone: req.body.phone,
    user_password: req.body.password,
    user_location: req.body.roomNumber
  }

  var cart = req.body.cart;
  var storeInfo = {}
  for (const [menuId, menu] of Object.entries(cart)) {
    var storeTitle = menu.store_title;
    var menuOptions = menu.menu_option_select.menu_option_values;
    menuOptions.push(menu.menu_option_select.number)
    var menuPrice = menu.menu_option_select.menu_price;
    var menuNumber = menu.menu_option_select.number;

    if (!(storeTitle in storeInfo)) {
      storeInfo[storeTitle] = {
        menu_ids: [menuId],
        menu_options: [menuOptions],
        order_price: menuPrice * menuNumber
      }
    }
    else {
      storeInfo[storeTitle].menu_ids.push(menuId);
      storeInfo[storeTitle].menu_options.push(menuOptions);
      storeInfo[storeTitle].order_price += menuPrice * menuNumber;
    }
  }

  var is_payed = 0;
  
  for (const [store_title, orderInfo] of Object.entries(storeInfo)) {
    let inSql = 'insert into orders('
    + 'order_time, '
    + 'order_price, '
    + 'user_name, '
    + 'user_phone, '
    + 'user_password, '
    + 'user_location, '
    + 'menu_ids, '
    + 'menu_options, '
    + 'is_payed'
    + ') values(?, ?, ?, ?, ?, ?, ?, ?, ?)';

    let inParam = [
      order_time,
      orderInfo.order_price,
      userInfo.user_name,
      userInfo.user_phone,
      userInfo.user_password,
      userInfo.user_location,
      JSON.stringify(orderInfo.menu_ids),
      JSON.stringify(orderInfo.menu_options),
      is_payed
    ];

    connection.query(inSql, inParam,
      function(err, result, fields) {
        if(err) {
          console.log(err);
          //res.status(406).send({test: 'test'});
        }
      }
    );
  }
  next();
}, function(req, res, next) {
  res.status(200).send('Success!');
})

router.get('/selectAllOrders', function(req, res, next) {
  // @Description: Select all orders
  // @Related: admin
  let selectSql = 'select * from orders';
  connection.query(selectSql, function(err, result, fields) {
    if(err) {
      //console.log(err);
      res.status(406).send({test: 'test'});
    }
    else {
      console.log(result);
      res.status(200).send({test: 'test'});
    }
  });

  res.status(200).send({test: 'test'});
})

router.get('/selectOrder/:name/:phone/:password', function(req, res, next) {
  // TODO Need to check timestamp!
  // @Description: Select all orders
  // @Related: admin

  var name = req.params.name;
  var phone = req.params.phone;
  var password = req.params.password;

  let selectSql = 'select * from orders where user_name = ? and user_phone = ? and user_password = ?';
  let inParam = [name, phone, password];
  connection.query(selectSql, inParam, function (err, result, fields) {
    if (err) {
      console.log(err);
      res.status(406).send('There is no Order!');
    }
    else {
      // TODO Need to check timestamp!
      result.sort(function(a, b) {
        return Date.parse(b.order_time) - Date.parse(a.order_time);
      })
      res.status(200).send({orders: result});
    }
  })
})

router.delete('/deleteOrder/:order_id', function(req, res, next) {
  // @Description: Delete certain order
  // @Related: OrderCheck.vue

  var order_id = req.params.order_id;

  let deleteSql = 'delete from orders where order_id = ?';
  let deleteParam = [order_id];

  connection.query(deleteSql, deleteParam, function(err, result, fields) {
		if(err) {
			console.log(err);
			res.status(406).send('There is no Order!');
		}
    else {
      res.status(200).send('Success!');
    }
	});
})

//const sqlite3 = require('sqlite3').verbose();
//let db = new sqlite3.Database('./db/order.db', sqlite3.OPEN_READWRITE, (err) => {
//  if (err) {
//      console.error(err.message);
//  } else {
//      console.log('Connected to the orders database.');
//  }
//});

router.post('/kakaoChatBotOrder', function(req, res, next) {
  // @Description: Kakao Chatbot Order BE
  // @Related: Kakao Chatbot
  // @Now: Not used

  //var timestamp = req.body.timestamp;
  //var username = req.body.name;
  //var coffeetype = req.body.coffeetype;
  //var coffeedense = req.body.coffeedense;

  //timestamp = 'Mon Jan 09 01:26:44 GMT+09:00 2022';
  //username = 'thfdk0101';
  //coffeetype = '원두 1 (3500원)';
  //coffeedense = '100% (기본)';

  //const insertQuery = `
	//  insert into orders(timestamp, username, coffeetype, coffeedense) values("${timestamp}", "${username}", "${coffeetype}", "${coffeedense}")
	//`;
	//  
  //try {
  //  db.run(insertQuery);
  //} catch(error) {
  //  console.log(error)
  //}

  //const responseBody = {
  //  version: "2.0",
  //  template: {
  //    outputs: [
  //      {
  //        simpleText: {
  //          text: "d"
  //        }
  //      }
  //    ]
  //  }
  //};
  //res.status(200).send({responseBody});
  res.status(200).send({test: 'test'});
});

router.post('/kakaoChatBotOrderCheck', function(req, res, next) {
  // @Description: Kakao Chatbot Order BE
  // @Related: Kakao Chatbot
  // @Now: Not used

  //var searchkey = req.body.action.params.username;
  // searchkey = "thfdk0101";

  //const selectQuery = `
  //  SELECT timestamp, username, coffeetype, coffeedense
  //  from orders 
  //  where username = "${searchkey}"
  //  `;
  //
  //var searchret = "There is no order.";
  //db.all(selectQuery, [], (err, rows) => {
  //  if (err) {
  //    console.log(err);
  //    console.log('Select error');
  //    const responseBody = {
  //      version: "2.0",
  //      template: {
  //        outputs: [
  //          {
  //            simpleText: {
  //              text: searchret
  //            }
  //          }
  //        ]
  //      }
  //    };
  //    res.status(200).send(responseBody); 
  //  }
  //  else {
  //    console.log(rows);
  //    if(rows.length != 0) {
  //      searchret = "";
  //    }
  //    for(var i = 0 ; i < rows.length ; i++) {
  //      searchret += rows[i].timestamp + " / ";
  //      searchret += rows[i].username + " / ";
  //      searchret += rows[i].coffeetype + " / ";
  //      searchret += rows[i].coffeedense + " / ";
  //      searchret += "\n\n";
  //    }
  //    const responseBody = {
  //      version: "2.0",
  //      template: {
  //        outputs: [
  //          {
  //            simpleText: {
  //              text: searchret
  //            }
  //          }
  //        ]
  //      }
  //    };
  //    res.status(200).send(responseBody); 
  //    
  //  }
  //});
  res.status(200).send({test: 'test'});
});
module.exports = router;
