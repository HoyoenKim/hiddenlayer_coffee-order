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

  var brandInfo = [
    {
      brand_id: 0,
      brand_title: '사장님의 식부심',
      brand_subtitle: '',
      story_ids: [0, 1, 2],
      store_id: 0, // '재야의 커피'
    },
    {
      brand_id: 1,
      brand_title: '가게 스토리',
      brand_subtitle: '',
      story_ids: [3, 4, 5],
      store_id: 0, // '재야의 커피'
    }
  ]

  let inSql = 'insert into brands('
  + 'brand_id, '
  + 'brand_title, '
  + 'brand_subtitle, '
  + 'story_ids, '
  + 'store_id'
  + ') values(?, ?, ?, ?, ?)';

  for(const brand_info of brandInfo) {
    let inParam = [
      brand_info.brand_id,
      brand_info.brand_title,
      brand_info.brand_subtitle,
      JSON.stringify(brand_info.story_ids),
      brand_info.store_id
    ]

    connection.query(inSql, inParam, function(err, result, fields) {
      if(err) {
        //console.log(err);
        //res.status(406).send('Already Exists Brand!');
      }
    })
  }
  next();

}, function(req, res, next) {
  res.status(200).send('Success!');
})

router.post('/createStory', function(req, res, next) {
  // TODO storeInfo 를 request body 에서 받아와야 함.
  // TODO 1개의 Object 씩 insert 하도록 변경
  // TODO createBrand 로 합치기
	// @Description: Create story's information.
	// @Related: admin
	// @Now: 하드코딩

  var storyInfo = [
    {
      story_id: 0,
      story_generate_time: new Date(Date.now()).toString(),
      story_type: 0, // 사진
      story_tag: [0, 0, 0, 0], 
      story_title: '',
      story_subtitle: '',
      story_description: '',
      store_id: 0, // '재야의 커피'
      brand_id: 0,
    },
    {
      story_id: 1,
      story_generate_time: new Date(Date.now()).toString(),
      story_type: 0, // 사진
      story_tag: [0, 0, 0, 0],
      story_title: '',
      story_subtitle: '',
      story_description: '',
      store_id: 0, // '재야의 커피'
      brand_id: 0,
    },
    {
      story_id: 2,
      story_generate_time: new Date(Date.now()).toString(),
      story_type: 0, // 사진
      story_tag: [0, 0, 0, 0],
      story_title: '',
      story_subtitle: '',
      story_description: '',
      store_id: 0, // '재야의 커피'
      brand_id: 0,
    },
    {
      story_id: 3,
      story_generate_time: new Date(Date.now()).toString(),
      story_type: 1, // 사진 + 글
      story_tag: [1, 0, 0, 0], // 큐레이션, 할인, 프로모션, 신메뉴
      story_title: '원두 큐레이션',
      story_subtitle: '사용자 맞춤 원두 큐레이션',
      story_description: '주문 내역을 바탕으로 원두를 추천해 드립니다.',
      store_id: 0, // '재야의 커피'
      brand_id: 1,
    },
    {
      story_id: 4,
      story_generate_time: new Date(Date.now()).toString(),
      story_type: 1, // 사진 + 글
      story_tag: [0, 1, 1, 0], // 큐레이션, 할인, 프로모션, 신메뉴
      story_title: '밸런스 블랜딩 할인',
      story_subtitle: '오픈 이벤트: 커피 할인',
      story_description: '밸런스 블랜딩 4000원 -> 3500원 할인합니다.',
      store_id: 0, // '재야의 커피'
      brand_id: 1,
    },
    {
      story_id: 5,
      story_generate_time: new Date(Date.now()).toString(),
      story_type: 1, // 사진 + 글
      story_tag: [0, 0, 0, 1], // 큐레이션, 할인, 프로모션, 신메뉴
      story_title: '싱글 오리진 출시',
      story_subtitle: '신메뉴 출시: 싱글 오리진',
      story_description: '신메뉴 싱글 오리진이 출시되었습니다.',
      store_id: 0, // '재야의 커피'
      brand_id: 1,
    },
  ]
  
  let inSql = 'insert into stories('
  + 'story_id, '
  + 'story_generate_time, '
  + 'story_type, '
  + 'story_tag, '
  + 'story_title, '
  + 'story_subtitle, '
  + 'story_description, '
  + 'store_id, '
  + 'brand_id'
  + ') values(?, ?, ?, ?, ?, ?, ?, ?, ?)';

  for(const story_info of storyInfo) {
    let inParam = [
      story_info.story_id,
      story_info.story_generate_time,
      story_info.story_type,
      JSON.stringify(story_info.story_tag),
      story_info.story_title,
      story_info.story_subtitle,
      story_info.story_description,
      story_info.store_id,
      story_info.brand_id
    ]

    connection.query(inSql, inParam, function(err, result, fields) {
      if(err) {
        console.log(err);
        res.status(406).send('Already Exists Story!');
      }
    })
  }
  next();

}, function(req, res, next) {
  res.status(200).send('Success!');
})

router.get('/readBrand/:brand_id', function(req, res, next) {
  // @Description: Select specific brand's information and all story's information in that brand. 
	// @Related: BrandPage.vue

  var brand_id = req.params.brand_id;

  let selectSql = 'select * from brands where brand_id = ?';
  let selectParams = [brand_id];
  
  connection.query(selectSql, selectParams, function(err, result, fields) {
    if(err) {
      console.log(err);
      res.status(406).send('There is no Brand!');
    }
    else {
      res.status(200).send({brand: result});
    }
  });
});

router.get('/readAllStory/:brand_id', function(req, res, next) {
  // TODO readBrand 와 합쳐야함.
  // @Description: Select specific brand's information and all story's information in that brand. 
	// @Related: BrandPage.vue

  var brand_id = req.params.brand_id;

  let selectSql = 'select * from stories where brand_id = ?';
  let selectParams = [brand_id];
  
  connection.query(selectSql, selectParams, function(err, result, fields) {
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
  // TODO readBrand 와 합쳐야함.
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

router.put('/updateBrand', function(req, res, next) {
  // TODO admin 페이지 구현 필요.
	// @Description: Update specific brand's information.
	// @Related: admin
	// @Now: 미구현

	res.status(200).send({test: 'test'});
});

router.put('/updateStory', function(req, res, next) {
  // TODO admin 페이지 구현 필요.
	// @Description: Update specific story's information.
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
  
  var store_id = 0;

  let deleteSql = 'delete from brands where store_id = ?';
  let deleteParam = [store_id];

  connection.query(deleteSql, deleteParam, function(err, result, fields) {
		if(err) {
			console.log(err);
			res.status(406).send('There is no Brand!');
		}
    else {
      res.status(200).send('Success!');
    }
	});
})

router.delete('/deleteStory', function(req, res, next) {
  // TODO admin 페이지 구현 필요.
  // TODO deleteBrand 로 합치기
	// @Description: Delete specific story's information.
	// @Related: admin
	// @Now: 미구현
	// @Issue: DB delete 및 이미지까지 같이 지워야 함.
  var store_id = 0;

  let deleteSql = 'delete from stories where store_id = ?';
  let deleteParam = [store_id];

  connection.query(deleteSql, deleteParam, function(err, result, fields) {
		if(err) {
			console.log(err);
			res.status(406).send('There is no Story!');
		}
    else {
      res.status(200).send('Success!');
    }
	});
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
