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

router.post('/createBrand', function(req, res, next) {
  // TODO storeInfo 를 request body 에서 받아와야 함.
  // TODO 1개의 Object 씩 insert 하도록 변경
	// @Description: Create brand's information.
	// @Related: admin
	// @Now: 하드코딩
  // brand 삭제, only story

  //var brandInfo = [
  //  {
  //    brand_id: 0,
  //    brand_title: '사장님의 식부심',
  //    brand_subtitle: '',
  //    story_ids: [0, 1, 2],
  //    store_id: 0, // '재야의 커피'
  //  },
  //  {
  //    brand_id: 1,
  //    brand_title: '가게 스토리',
  //    brand_subtitle: '',
  //    story_ids: [3, 4, 5],
  //    store_id: 0, // '재야의 커피'
  //  }
  //]
  //
  //let inSql = 'insert into brands('
  //+ 'brand_id, '
  //+ 'brand_title, '
  //+ 'brand_subtitle, '
  //+ 'story_ids, '
  //+ 'store_id'
  //+ ') values(?, ?, ?, ?, ?)';
  //
  //for(const brand_info of brandInfo) {
  //  let inParam = [
  //    brand_info.brand_id,
  //    brand_info.brand_title,
  //    brand_info.brand_subtitle,
  //    JSON.stringify(brand_info.story_ids),
  //    brand_info.store_id
  //  ]
  //
  //  connection.query(inSql, inParam, function(err, result, fields) {
  //    if(err) {
  //      //console.log(err);
  //      //res.status(406).send('Already Exists Brand!');
  //    }
  //  })
  //}
  next();

}, function(req, res, next) {
  res.status(200).send('Success!');
})

router.get('/readBrand/:brand_id', function(req, res, next) {
  // @Description: Select specific brand's information and all story's information in that brand. 
	// @Related: BrandPage.vue
  // brand 삭제, only story

  //var brand_id = req.params.brand_id;
  //
  //let selectSql = 'select * from brands where brand_id = ?';
  //let selectParams = [brand_id];
  //
  //connection.query(selectSql, selectParams, function(err, result, fields) {
  //  if(err) {
  //    console.log(err);
  //    res.status(406).send('There is no Brand!');
  //  }
  //  else {
  //    res.status(200).send({brand: result});
  //  }
  //});
  res.status(200).send('Success!');
});

router.put('/updateBrand', function(req, res, next) {
  // TODO admin 페이지 구현 필요.
	// @Description: Update specific brand's information.
	// @Related: admin
	// @Now: 미구현

	res.status(200).send({test: 'test'});
});

router.delete('/deleteBrand', function(req, res, next) {
  // TODO admin 페이지 구현 필요.
	// @Description: Delete specific brand's information.
	// @Related: admin
	// @Now: 테스트 데이터 삭제
	// @Issue: DB delete 및 이미지까지 같이 지워야 함.
  // brand 삭제, only story

  //var store_id = 0;
  //
  //let deleteSql = 'delete from brands where store_id = ?';
  //let deleteParam = [store_id];
  //
  //connection.query(deleteSql, deleteParam, function(err, result, fields) {
	//	if(err) {
	//		console.log(err);
	//		res.status(406).send('There is no Brand!');
	//	}
  //  else {
  //    res.status(200).send('Success!');
  //  }
	//});
})

router.post('/createStory', function(req, res, next) {
  var storyInfo = req.body;
  
  let inSql = 'insert into stories('
  + 'story_id, '
  + 'story_generate_time, '
  + 'story_type, '
  + 'story_tag, '
  + 'story_title, '
  + 'story_subtitle, '
  + 'story_description, '
  + 'store_id'
  + ') values(?, ?, ?, ?, ?, ?, ?, ?)';


  let inParam = [
    storyInfo.story_id,
    storyInfo.story_generate_time,
    storyInfo.story_type,
    JSON.stringify(storyInfo.story_tag),
    storyInfo.story_title,
    storyInfo.story_subtitle,
    storyInfo.story_description,
    storyInfo.store_id,
  ]

  connection.query(inSql, inParam, function(err, result, fields) {
    if(err) {
      console.log(err);
      res.status(406).send('Already Exists Story!');
    }
    else {
      res.status(200).send('Success!');
    }
  })
})

router.get('/allStories', function(req, res, next) {
  // @Description: Select specific brand's information and all story's information in that brand. 
	// @Related: BrandPage.vue

  let selectSql = 'select * from stories';
  connection.query(selectSql, function(err, result, fields) {
    if(err) {
      console.log(err);
      res.status(406).send('There is no Story!');
    }
    else {
      res.status(200).send({stories: result});
    }
  }) 
})

router.get('/readStory/:story_id', function(req, res, next) {
  // @Description: Select specific brand's information and all story's information in that brand. 
	// @Related: BrandPage.vue

  var story_id = req.params.story_id;

  let selectSql = 'select * from stories where story_id = ?';
  let selectParams = [story_id];

  connection.query(selectSql, selectParams, function(err, result, fields) {
    if(err) {
      console.log(err);
      res.status(406).send('There is no Story!');
    }
    else {
      res.status(200).send({story: result});
    }
  })
});


router.put('/updateStory', function(req, res, next) {
  // TODO admin 페이지 구현 필요.
	// @Description: Update specific story's information.
	// @Related: admin
	// @Now: 미구현
  
  res.status(200).send({test: 'test'});
});



router.delete('/deleteStory', function(req, res, next) {
  // TODO admin 페이지 구현 필요.
  // TODO deleteBrand 로 합치기
	// @Description: Delete specific story's information.
	// @Related: admin
	// @Now: 미구현
	// @Issue: DB delete 및 이미지까지 같이 지워야 함.
  //var store_id = 0;
  //
  //let deleteSql = 'delete from stories where store_id = ?';
  //let deleteParam = [store_id];
  //
  //connection.query(deleteSql, deleteParam, function(err, result, fields) {
	//	if(err) {
	//		console.log(err);
	//		res.status(406).send('There is no Story!');
	//	}
  //  else {
  //    res.status(200).send('Success!');
  //  }
	//});
  res.status(200).send({test: 'test'});
})

router.post('/uploadImage', function(req, res, next) {
	// TODO admin 페이지 구현 필요.
	// @Description: Upload story's images.
	// @Related: admin
	// @Now: 미구현

	res.status(200).send({test: 'test'});
})

router.put('/updateImage', function(req, res, next) {
	// TODO admin 페이지 구현 필요.
	// @Description: Update specific story's image.
	// @Related: admin
	// @Now: 미구현

	res.status(200).send({test: 'test'});
})

module.exports = router;
