var express = require('express');
var router = express.Router();

const mysql = require('mysql');
const connection = mysql.createConnection({
  host : 'localhost',
  port : '3306',
  user : 'localorder',
  password : '1234',
  database : 'order_db'
})
connection.connect();


/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'order' });
});

router.post('/orderInsert', function(req, res, next) {
  //console.log(req.body);
  var order_time = new Date(Date.now()).toString();
  var userInfo = {
    user_name: req.body.name,
    user_phone: req.body.phone,
    user_password: req.body.password,
    user_location: req.body.roomNumber
  }

  var storeInfo = {};
  // TODO Menu ID, Option ID seperate table.
  var cart = req.body.cart;
  for(const [key, value] of Object.entries(cart)) {
    var storeName = value.storeName;
    if (!(storeName in storeInfo)) {
      storeInfo[storeName] = {
        menu: [],
        options: [],
        order_price: 0
      }
    }
    storeInfo[storeName].menu.push(key),
    storeInfo[storeName].options.push([value.tempOption, value.denseOption])
    storeInfo[storeName].order_price += parseInt(value.price);
  }
  
  // TODO validation check

  // Insert
  for (const [store_name, store_info] of Object.entries(storeInfo)) {
    //console.log(store_name, store_info)
    //console.log(order_time, store_info.order_price.toString(), store_name, userInfo.user_name, userInfo.user_phone, userInfo.user_password, userInfo.user_location, JSON.stringify(store_info.menu), JSON.stringify(store_info.options));
    
    let inSql = 'insert into orders(order_time, order_price, store_name, user_name, user_phone, user_password, user_location, menu_name, menu_options, is_payed) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)';
    let inParam = [order_time, store_info.order_price.toString(), store_name, userInfo.user_name, userInfo.user_phone, userInfo.user_password, userInfo.user_location, JSON.stringify(store_info.menu), JSON.stringify(store_info.options), 0];
    connection.query(inSql, inParam,
      function(err, result, fields) {
        if(err) {
          //console.log(err);
          res.status(406).send({test: 'test'});
        }
        else {
          console.log(result);
          res.status(200).send({test: 'test'});
        }
      }
    );
  } 
});

router.post('/selectAllOrder', function(req, res, next) {
  console.log('Hello')
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
})

router.post('/checkOrder', function(req, res, next) {
  console.log('Hello');
  var name = req.body.name;
  var phone = req.body.phone;
  var password = req.body.password;

  let selectSql = 'select * from orders where user_name = ? and user_phone = ? and user_password = ?';
  let inParam = [name, phone, password];
  var ret;
  connection.query(selectSql, inParam, function (err, result, fields) {
    if (err) {
      console.log(err);
      res.status(406).send({ret: ret});
    }
    else {
      console.log(result);
      ret = result
      res.status(200).send({ret: ret});
    }
  })
})

router.post('/', function(req, res, next) {
  var timestamp = 'Mon Jan 09 01:26:44 GMT+09:00 2022';
  var username = 'thfdk0101';
  var coffeetype = '원두 1 (3500원)';
  var coffeedense = '100% (기본)';

  //console.log(req.body.name);
  //timestamp = req.body.timestamp;
  //username = req.body.name;
  //coffeetype = req.body.coffeetype;
  //coffeedense = req.body.coffeedense;

  try {
    const insertQuery = `
		  insert into orders(timestamp, username, coffeetype, coffeedense) values("${timestamp}", "${username}", "${coffeetype}", "${coffeedense}")
	  `;
	  db.run(insertQuery);
  } catch(error) {
    console.log(error)
  }


  const responseBody = {
    version: "2.0",
    template: {
      outputs: [
        {
          simpleText: {
            text: "d"
          }
        }
      ]
    }
  };
  res.status(200).send({responseBody}); 
});

module.exports = router;
