var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'order' });
});

router.post('/', function(req, res, next) {
  console.log(req.body.name);  
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
