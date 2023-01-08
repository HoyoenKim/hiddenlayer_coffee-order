var express = require('express');
var router = express.Router();
const sqlite3 = require('sqlite3').verbose();
let db = new sqlite3.Database('./db/order.db', sqlite3.OPEN_READWRITE, (err) => {
  if (err) {
      console.error(err.message);
  } else {
      console.log('Connected to the orders database.');
  }
});

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'order' });
});

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
    console.log(errror)
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
