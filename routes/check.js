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
  res.render('index', { title: 'order-check' });
});

router.post('/', function(req, res, next) {
  var searchkey = "thfdk0101";

  //console.log(req.body.action.params.username);
  //searchkey = req.body.action.params.username;

  const selectQuery = `
    SELECT timestamp, username, coffeetype, coffeedense
    from orders 
    where username = "${searchkey}"
    `;
  
  var searchret = "There is no order.";
  db.all(selectQuery, [], (err, rows) => {
    if (err) {
      console.log(err);
      console.log('Select error');
      const responseBody = {
        version: "2.0",
        template: {
          outputs: [
            {
              simpleText: {
                text: searchret
              }
            }
          ]
        }
      };
      res.status(200).send(responseBody); 
    }
    else {
      console.log(rows);
      if(rows.length != 0) {
        searchret = "";
      }
      for(var i = 0 ; i < rows.length ; i++) {
        searchret += rows[i].timestamp + " / ";
        searchret += rows[i].username + " / ";
        searchret += rows[i].coffeetype + " / ";
        searchret += rows[i].coffeedense + " / ";
        searchret += "\n\n";
      }

      const responseBody = {
        version: "2.0",
        template: {
          outputs: [
            {
              simpleText: {
                text: searchret
              }
            }
          ]
        }
      };
      res.status(200).send(responseBody); 
      }
  });

  
});

module.exports = router;
