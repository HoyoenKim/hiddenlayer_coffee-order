var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.post('/createMenuTable', function(req, res, next) {
  // TODO menuTableInfo 를 request body 에서 받아와야 함.
  // TODO 1개의 Object 씩 insert 하도록 변경
	// @Description: Create menu table's information.
	// @Related: admin
	// @Now: 하드코딩

  var menuTableInfo = [
    {
      menu_table_id: 0,
      menu_table_title: '사장님 추천',
      menu_table_subtitle: '이번주 커피',
      menu_ids: [0, 1],
      store_id: 0, // '재야의 커피'
    },
    {
      menu_table_id: 1,
      menu_table_title: '블랜디드 원두',
      menu_table_subtitle: '',
      menu_ids: [0],
      store_id: 0, // '재야의 커피'
    },
    {
      menu_table_id: 2,
      menu_table_title: '고급 원두',
      menu_table_subtitle: '1일 10잔 한정판매',
      menu_ids: [1],
      store_id: 0, // '재야의 커피'
    }
  ]
  next();

}, function(req, res, next) {
  res.status(200).send('Success!');
});

router.post('/createMenu', function(req, res, next) {
  // TODO menuInfo 를 request body 에서 받아와야 함.
  // TODO 1개의 Object 씩 insert 하도록 변경
  // TODO creatMenuTable 로 합치기
	// @Description: Create menu's information.
	// @Related: admin
	// @Now: 하드코딩
  
  var menuInfo = [
    {
      menu_id: 0,
      menu_title: '밸런스 블랜딩',
      menu_price: 3500,
      menu_description: "국내 정상급 바리스타가 만든 최고급 품종의 게이샤 원두 그리고 게이샤 원두와 최적의 조화를 이루는 헤리움 품종의 원두를 섞어 내린 고급 블랜디드 커피입니다.",
      menu_options: [0, 1],
      menu_table_ids: [0, 1],
      menu_options: [
        [
          "가격",
          {
            label: "3500원",
            value: "defalut",
          }
        ],
        [
          "HOT / ICE",
          {
            label: "Hot",
            value: "hot",
          },
          {
            label: "Ice",
            value: "ice",
          },
        ],
        [
          "커피 농도",
          {
            label: "진하게",
            value: "high",
          },
          {
            label: "연하게",
            value: "low",
          },
        ]
      ],
    },
    {
      menu_id: 1,
      menu_title: '싱글 오리진',
      menu_price: 4000,
      menu_description: "국내 정상급 로스터가 최고급 생두를 선점하고 로스팅하여 만든 원두 입니다. 단 한 종류의 원두만을 최고급 원두를 골라내 원두의 맛을 극한까지 끌어내기 위한 노력을 기울였습니다.",
      menu_options: [0, 1],
      menu_table_ids: [0, 1],
      menu_options: [
        [
          "가격",
          {
            label: "3500원",
            value: "defalut",
          }
        ],
        [
          "HOT / ICE",
          {
            label: "Hot",
            value: "hot",
          },
          {
            label: "Ice",
            value: "ice",
          },
        ],
        [
          "커피 농도",
          {
            label: "진하게",
            value: "high",
          },
          {
            label: "연하게",
            value: "low",
          },
        ]
      ],
    }
  ]

  next();
}, function(req, res, next) {
  res.status(200).send('Success!');
});

router.get('/readMenuTable/:menu_table_id', function(req, res, next) {
  // @Description: Select specific menu table's information and all menu's information in that menu table. 
	// @Related: MenuPage.vue
});

router.get('/readMenu/:menu_table_id', function(req, res, next) {
  // TODO readMenuTable 와 합쳐야함.
  // @Description: Select specific menu table's information and all menu's information in that menu table. 
	// @Related: MenuPage.vue
});

router.put('/updateMenuTable', function(req, res, next) {
  // TODO admin 페이지 구현 필요.
	// @Description: Update specific menu table's information.
	// @Related: admin
	// @Now: 미구현
  
  res.status(200).send({test: 'test'});
});

router.put('/updateMenu', function(req, res, next) {
  // TODO admin 페이지 구현 필요.
	// @Description: Update specific menu's information.
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
});

router.delete('/deleteMenu', function(req, res, next) {
  // TODO admin 페이지 구현 필요.
  // TODO deleteMenuTable 로 합치기
	// @Description: Delete specific menu's information.
	// @Related: admin
	// @Now: 테스트 데이터 삭제
	// @Issue: DB delete 및 이미지까지 같이 지워야 함.
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
