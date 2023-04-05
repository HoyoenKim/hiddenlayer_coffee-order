import requests
import os
from datetime import datetime

def createStore(baseUrl):
    url = baseUrl + 'store/createStore'
    
    storeInfoList = []
    storeInfoList.append({
                            "store_id": 0,
		                    "store_title": '재야의 커피',
		                    "store_subtitle": 'Cafe',
		                    "store_description": '사용자 맞춤 원두 추천 카페',
                            "store_images_nums": 6,
		                    "store_order_type": [1, 1, 1], # '테이블 주문 가능', '포장 가능', '배달 가능'
		                    "store_location": ["35.23021", "126.83982"], # 위도, 경도
		                    "store_open_time": [[10, 22], [10, 22], [10, 22], [10, 22], [10, 22], [10, 22], [10, 22], [10, 22]], # 월 - 일, 공휴일
		                    "store_official_information": ['류현석', '창업진흥센터 B동 401호', '010-2128-7164'], # 소유자, 장소, 담당자 연락처
		                    "story_ids": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
		                    "menu_table_ids": [0, 1, 2],
		                    "event_ids": [0, 1, 2, 3, 4, 5, 6, 7],
		                    "owner_ids": [0], # need to encription
                        })
    storeInfoList.append({
                            "store_id": 1,
		                    "store_title": 'S305',
		                    "store_subtitle": 'Home Cafe',
                            "store_images_nums": 3,
		                    "store_description": '테스트 더미 데이터: 각종 모든 메뉴 테스트베드',
		                    "store_order_type": [1, 1, 0], # '테이블 주문 가능', '포장 가능', '배달 가능'
		                    "store_location": ["35.22959", "126.84775"], # 위도, 경도
		                    "store_open_time": [[10, 22], [10, 22], [10, 22], [10, 22], [10, 22], [10, 22], [10, 22], [10, 22]], # 월 - 일, 공휴일
		                    "store_official_information": ['김호연', '학사기숙사 B동 S305', '010-2128-7164'], # 소유자, 장소, 담당자 연락처
		                    "story_ids": [12, 13, 14, 15, 16, 17, 18, 19],
		                    "menu_table_ids": [3, 4, 5, 6, 7, 8],
		                    "event_ids": [8, 9, 10, 11, 12],
		                    "owner_ids": [1], # need to encription
                        })
    
    for storeInfo in storeInfoList:
        response = requests.post(url, json=storeInfo)
        print(response)

def createStory(baseUrl):
    url = baseUrl + 'brand/createStory'

    storyInfoList = []
    storyInfoList.append({
                            "story_id": 0,
                            "story_generate_time":  str(datetime.now()),
                            "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
                            "story_tag": [], 
                            "story_title": '재야의 커피 영업 시작',
                            "story_subtitle": '2022.04.01',
                            "story_description": '재야의 커피 영업을 시작했습니다.',
                            "store_id": 0, # '재야의 커피'
    })
    storyInfoList.append({
                            "story_id": 1,
                            "story_generate_time":  str(datetime.now()),
                            "story_type": 3, # 동영상: 0, 사진 개수: 1 ~ 5
                            "story_tag": ["신메뉴 출시"], 
                            "story_title": '싱글 오리진 출시',
                            "story_subtitle": '신메뉴 출시: 싱글 오리진',
                            "story_description": '신메뉴 싱글 오리진이 출시되었습니다.',
                            "store_id": 0, # '재야의 커피'
    })
    storyInfoList.append({
                            "story_id": 2,
                            "story_generate_time":  str(datetime.now()),
                            "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
                            "story_tag": ["할인", "프로모션"], 
                            "story_title": '밸런스 블랜딩 할인',
                            "story_subtitle": '오픈 이벤트: 커피 할인',
                            "story_description": '밸런스 블랜딩 4000원 -> 3500원 할인합니다.',
                            "store_id": 0, # '재야의 커피'
    })
    storyInfoList.append({
                            "story_id": 3,
                            "story_generate_time":  str(datetime.now()),
                            "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
                            "story_tag": ["큐레이션"], 
                            "story_title": '원두 큐레이션',
                            "story_subtitle": '사용자 맞춤 원두 큐레이션',
                            "story_description": '주문 내역을 바탕으로 원두를 추천해 드립니다.',
                            "store_id": 0, # '재야의 커피'
    })
    storyInfoList.append({
                            "story_id": 4,
                            "story_generate_time":  str(datetime.now()),
                            "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
                            "story_tag": [], 
                            "story_title": '재야의 커피 영업 시작',
                            "story_subtitle": '2022.04.01',
                            "story_description": '재야의 커피 영업을 시작했습니다.',
                            "store_id": 0, # '재야의 커피'
    })
    storyInfoList.append({
                            "story_id": 5,
                            "story_generate_time":  str(datetime.now()),
                            "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
                            "story_tag": [], 
                            "story_title": '재야의 커피 영업 시작',
                            "story_subtitle": '2022.04.01',
                            "story_description": '재야의 커피 영업을 시작했습니다.',
                            "store_id": 0, # '재야의 커피'
    })
    storyInfoList.append({
                            "story_id": 6,
                            "story_generate_time":  str(datetime.now()),
                            "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
                            "story_tag": [], 
                            "story_title": '테스트',
                            "story_subtitle": '테스트테스트',
                            "story_description": '테스트테스트테스트테스트',
                            "store_id": 0, # '재야의 커피'
    })
    storyInfoList.append({
                            "story_id": 7,
                            "story_generate_time":  str(datetime.now()),
                            "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
                            "story_tag": [], 
                            "story_title": '테스트',
                            "story_subtitle": '테스트테스트',
                            "story_description": '테스트테스트테스트테스트',
                            "store_id": 0, # '재야의 커피'
    })
    storyInfoList.append({
                            "story_id": 8,
                            "story_generate_time":  str(datetime.now()),
                            "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
                            "story_tag": [], 
                            "story_title": '테스트',
                            "story_subtitle": '테스트테스트',
                            "story_description": '테스트테스트테스트테스트',
                            "store_id": 0, # '재야의 커피'
    })
    storyInfoList.append({
                            "story_id": 9,
                            "story_generate_time":  str(datetime.now()),
                            "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
                            "story_tag": [], 
                            "story_title": '테스트',
                            "story_subtitle": '테스트테스트',
                            "story_description": '테스트테스트테스트테스트',
                            "store_id": 0, # '재야의 커피'
    })
    storyInfoList.append({
                            "story_id": 10,
                            "story_generate_time":  str(datetime.now()),
                            "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
                            "story_tag": [], 
                            "story_title": '테스트',
                            "story_subtitle": '테스트테스트',
                            "story_description": '테스트테스트테스트테스트',
                            "store_id": 0, # '재야의 커피'
    })
    storyInfoList.append({
                            "story_id": 11,
                            "story_generate_time":  str(datetime.now()),
                            "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
                            "story_tag": [], 
                            "story_title": '테스트',
                            "story_subtitle": '테스트테스트',
                            "story_description": '테스트테스트테스트테스트',
                            "store_id": 0, # '재야의 커피'
    })
    storyInfoList.append({
                            "story_id": 12,
                            "story_generate_time":  str(datetime.now()),
                            "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
                            "story_tag": [], 
                            "story_title": '테스트',
                            "story_subtitle": '테스트테스트',
                            "story_description": '테스트테스트테스트테스트',
                            "store_id": 1, # 'S305'
    })
    storyInfoList.append({
                            "story_id": 13,
                            "story_generate_time":  str(datetime.now()),
                            "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
                            "story_tag": [], 
                            "story_title": '테스트',
                            "story_subtitle": '테스트테스트',
                            "story_description": '테스트테스트테스트테스트',
                            "store_id": 1, # 'S305'
    })
    storyInfoList.append({
                            "story_id": 14,
                            "story_generate_time":  str(datetime.now()),
                            "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
                            "story_tag": [], 
                            "story_title": '테스트',
                            "story_subtitle": '테스트테스트',
                            "story_description": '테스트테스트테스트테스트',
                            "store_id": 1, # 'S305'
    })
    storyInfoList.append({
                            "story_id": 15,
                            "story_generate_time":  str(datetime.now()),
                            "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
                            "story_tag": [], 
                            "story_title": '테스트',
                            "story_subtitle": '테스트테스트',
                            "story_description": '테스트테스트테스트테스트',
                            "store_id": 1, # 'S305'
    })
    storyInfoList.append({
                            "story_id": 16,
                            "story_generate_time":  str(datetime.now()),
                            "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
                            "story_tag": [], 
                            "story_title": '테스트',
                            "story_subtitle": '테스트테스트',
                            "story_description": '테스트테스트테스트테스트',
                            "store_id": 1, # 'S305'
    })
    storyInfoList.append({
                            "story_id": 17,
                            "story_generate_time":  str(datetime.now()),
                            "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
                            "story_tag": [], 
                            "story_title": '테스트',
                            "story_subtitle": '테스트테스트',
                            "story_description": '테스트테스트테스트테스트',
                            "store_id": 1, # 'S305'
    })
    storyInfoList.append({
                            "story_id": 18,
                            "story_generate_time":  str(datetime.now()),
                            "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
                            "story_tag": [], 
                            "story_title": '테스트',
                            "story_subtitle": '테스트테스트',
                            "story_description": '테스트테스트테스트테스트',
                            "store_id": 1, # 'S305'
    })
    storyInfoList.append({
                            "story_id": 19,
                            "story_generate_time":  str(datetime.now()),
                            "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
                            "story_tag": [], 
                            "story_title": '테스트',
                            "story_subtitle": '테스트테스트',
                            "story_description": '테스트테스트테스트테스트',
                            "store_id": 1, # 'S305'
    })

    for storyInfo in storyInfoList:
        response = requests.post(url, json=storyInfo)
        print(response)

def createMenuTable(baseUrl):
    url = baseUrl + 'menu/createMenuTable'
    menuTableInfoList = []
    menuTableInfoList.append({
                                "menu_table_id": 0,
                                "menu_table_title": '사장님 추천',
                                "menu_table_subtitle": '이번주 커피',
                                "menu_ids": [0, 1],
                                "store_id": 0, # '재야의 커피'
    })
    menuTableInfoList.append({
                                "menu_table_id": 1,
                                "menu_table_title": '블랜디드 원두',
                                "menu_table_subtitle": '',
                                "menu_ids": [0],
                                "store_id": 0, # '재야의 커피'
    })
    menuTableInfoList.append({
                                "menu_table_id": 2,
                                "menu_table_title": '고급 원두',
                                "menu_table_subtitle": '하루 10잔 한정 판매',
                                "menu_ids": [1],
                                "store_id": 0, # '재야의 커피'
    })
    menuTableInfoList.append({
                                "menu_table_id": 3,
                                "menu_table_title": '한식',
                                "menu_table_subtitle": '다양한 한식 메뉴',
                                "menu_ids": [2, 3, 4],
                                "store_id": 1, # 'S305'
    })
    menuTableInfoList.append({
                                "menu_table_id": 4,
                                "menu_table_title": '일식',
                                "menu_table_subtitle": '다양한 일식 메뉴',
                                "menu_ids": [5],
                                "store_id": 1, # 'S305'
    })
    menuTableInfoList.append({
                                "menu_table_id": 5,
                                "menu_table_title": '중식',
                                "menu_table_subtitle": '다양한 중식 메뉴',
                                "menu_ids": [6],
                                "store_id": 1, # 'S305'
    })
    menuTableInfoList.append({
                                "menu_table_id": 6,
                                "menu_table_title": '양식',
                                "menu_table_subtitle": '다양한 일식 메뉴',
                                "menu_ids": [7, 8],
                                "store_id": 1, # 'S305'
    })
    menuTableInfoList.append({
                                "menu_table_id": 7,
                                "menu_table_title": '음료',
                                "menu_table_subtitle": '다양한 음료 메뉴',
                                "menu_ids": [9, 10],
                                "store_id": 1, # 'S305'
    })
    menuTableInfoList.append({
                                "menu_table_id": 8,
                                "menu_table_title": '주류',
                                "menu_table_subtitle": '다양한 주류 메뉴',
                                "menu_ids": [11, 12],
                                "store_id": 1, # 'S305'
    })
    for menuTableInfo in menuTableInfoList:
        response = requests.post(url, json=menuTableInfo)
        print(response)

def createMenu(baseUrl):
    url = baseUrl + 'menu/createMenu'
    menuInfoList = []
    menuInfoList.append({
        "menu_id": 0,
        "menu_title": '밸런스 블랜딩',
        "menu_subtitle": '게이샤 원두 + 헤리움 원두',
        "menu_price": 3500,
        "menu_description": "국내 정상급 바리스타가 만든 게이샤 원두, 이와 최적의 조화를 이루는 헤리움 원두를 섞은 고급 블랜디드 커피입니다.",
        "menu_price_options": {
                "type": 0, # 0 toggle, 1 checkbox
                "options": [
                    {
                      "label": "밸런스 블랜딩",
                      "value": 0,
                      "price": 3500,
                    }
                ]
        },
        "menu_additional_options": [
            {
                "type": 0, # 0 toggle, 1 checkbox
                "name": "HOT / ICE",
                "options": [
                    {
                      "label": "HOT",
                      "value": 0,
                      "price": 0,
                    },
                    {
                      "label": "ICE",
                      "value": 1,
                      "price": 0,
                    }
                ]
            },
            {
                "type": 0, # 0 toggle, 1 checkbox
                "name": "커피 농도",
                "options": [
                    {
                      "label": "진하게",
                      "value": 0,
                      "price": 0,
                    },
                    {
                      "label": "연하게",
                      "value": 1,
                      "price": 0,
                    }
                ]
            }
        ],
        "store_id": 0, # 재야의 커피
        "menu_table_ids": [0, 1],
    })
    menuInfoList.append({
        "menu_id": 1,
        "menu_title": '싱글 오리진',
        "menu_subtitle": '최고급 생두',
        "menu_price": 4000,
        "menu_description": "국내 정상급 로스터가 최고급 생두로 로스팅하였습니다. 한 종류의 최고급 원두로 맛을 극한까지 끌어냈습니다.",
        "menu_price_options": {
                "type": 0, # 0 toggle, 1 checkbox
                "options": [
                    {
                      "label": "싱글 오리진",
                      "value": 0,
                      "price": 4000,
                    }
                ]
        },
        "menu_additional_options": [
            {
                "type": 0, # 0 toggle, 1 checkbox
                "name": "HOT / ICE",
                "options": [
                    {
                      "label": "HOT",
                      "value": 0,
                      "price": 0,
                    },
                    {
                      "label": "ICE",
                      "value": 1,
                      "price": 0,
                    }
                ]
            },
            {
                "type": 0, # 0 toggle, 1 checkbox
                "name": "커피 농도",
                "options": [
                    {
                      "label": "진하게",
                      "value": 0,
                      "price": 0,
                    },
                    {
                      "label": "연하게",
                      "value": 1,
                      "price": 0,
                    }
                ]
            }
        ],
        "store_id": 0, # 재야의 커피
        "menu_table_ids": [0, 2],
    })
    menuInfoList.append({
        "menu_id": 2,
        "menu_title": '김치찜',
        "menu_subtitle": '삼겹살 + 김치 + 공기밥',
        "menu_price": 15900,
        "menu_description": "1인(고기 150g, 공기밥 1), 2인(고기 320g, 공기밥 2), 3인(고기 500g, 공기밥 3)",
        "menu_price_options": {
                "type": 0, # 0 toggle, 1 checkbox
                "options": [
                    {
                      "label": "1인",
                      "value": 0,
                      "price": 15900,
                    },
                    {
                      "label": "2인",
                      "value": 1,
                      "price": 24900,
                    },
                    {
                      "label": "3인",
                      "value": 2,
                      "price": 32900,
                    }
                ]
        },
        "menu_additional_options": [
            {
                "type": 1, # 0 toggle, 1 checkbox
                "name": "사이드 메뉴",
                "options": [
                    {
                      "label": "계란찜",
                      "value": 0,
                      "price": 4000,
                    },
                    {
                      "label": "계란말이",
                      "value": 1,
                      "price": 4000,
                    },
                    {
                      "label": "참치마요",
                      "value": 2,
                      "price": 4000,
                    }
                ]
            },
            {
                "type": 1, # 0 toggle, 1 checkbox
                "name": "추가 선택",
                "options": [
                    {
                      "label": "공기밥 1개",
                      "value": 0,
                      "price": 500,
                    },
                    {
                      "label": "공기밥 2개",
                      "value": 1,
                      "price": 1000,
                    },
                    {
                      "label": "공기밥 3개",
                      "value": 2,
                      "price": 1500,
                    }
                ]
            }
        ],
        "store_id": 1, # S305
        "menu_table_ids": [3],
    })
    menuInfoList.append({
        "menu_id": 3,
        "menu_title": '곰탕',
        "menu_subtitle": '공기밥 + 쌈장 + 양파 + 청양고추 + 김치',
        "menu_price": 10000,
        "menu_description": "공기밥 + 쌈장 + 양파 + 청양고추 + 김치",
        "menu_price_options": {
                "type": 0, # 0 toggle, 1 checkbox
                "options": [
                    {
                      "label": "1인",
                      "value": 0,
                      "price": 10000,
                    },
                ]
        },
        "menu_additional_options": [],
        "store_id": 1, # S305
        "menu_table_ids": [3],
    })
    menuInfoList.append({
        "menu_id": 4,
        "menu_title": '부대찌개',
        "menu_subtitle": '공기밥 + 김치',
        "menu_price": 15900,
        "menu_description": "스팸 정품 사용합니다.",
        "menu_price_options": {
                "type": 0, # 0 toggle, 1 checkbox
                "options": [
                    {
                      "label": "1~2인 + 공기밥1",
                      "value": 0,
                      "price": 15900,
                    },
                    {
                      "label": "2~3인 + 공기밥2",
                      "value": 1,
                      "price": 24900,
                    },
                    {
                      "label": "3~4인 + 공기밥3",
                      "value": 2,
                      "price": 32900,
                    }
                ]
        },
        "menu_additional_options": [
            {
                "type": 0,
                "name": "맵기 선택",
                "options": [
                     {
                      "label": "0단계 (순한맛)",
                      "value": 0,
                      "price": 0,
                    },
                    {
                      "label": "1단계 (신라면)",
                      "value": 1,
                      "price": 0,
                    },
                    {
                      "label": "2단계 (불닭)",
                      "value": 2,
                      "price": 0,
                    }
                ]
            },
            {
                "type": 1, # 0 toggle, 1 checkbox
                "name": "사이드 메뉴",
                "options": [
                    {
                      "label": "계란찜",
                      "value": 0,
                      "price": 4000,
                    },
                    {
                      "label": "계란말이",
                      "value": 1,
                      "price": 4000,
                    },
                    {
                      "label": "참치마요",
                      "value": 2,
                      "price": 4000,
                    }
                ]
            },
            {
                "type": 1, # 0 toggle, 1 checkbox
                "name": "추가 선택",
                "options": [
                    {
                      "label": "공기밥 1개",
                      "value": 0,
                      "price": 500,
                    },
                    {
                      "label": "공기밥 2개",
                      "value": 1,
                      "price": 1000,
                    },
                    {
                      "label": "공기밥 3개",
                      "value": 2,
                      "price": 1500,
                    }
                ]
            }
        ],
        "store_id": 1, # S305
        "menu_table_ids": [3],
    })
    menuInfoList.append({
        "menu_id": 5,
        "menu_title": '돈까스',
        "menu_subtitle": '수제 돈까스 도시락',
        "menu_price": 10900,
        "menu_description": "100% 국내산 냉장 등심, 손으로 만든 수제 돈까스, 최고급 소스",
        "menu_price_options": {
                "type": 0, # 0 toggle, 1 checkbox
                "options": [
                    {
                      "label": "1인",
                      "value": 0,
                      "price": 10900,
                    },
                ]
        },
        "menu_additional_options": [
            {
                "type": 1, # 0 toggle, 1 checkbox
                "name": "사이드 메뉴",
                "options": [
                    {
                      "label": "소스",
                      "value": 0,
                      "price": 500,
                    },
                    {
                      "label": "계란말이",
                      "value": 1,
                      "price": 4000,
                    },
                    {
                      "label": "만두",
                      "value": 2,
                      "price": 4000,
                    }
                ]
            },
        ],
        "store_id": 1, # S305
        "menu_table_ids": [4],
    })
    menuInfoList.append({
        "menu_id": 6,
        "menu_title": '짜장면',
        "menu_subtitle": '짜장면 + 양파 + 단무지',
        "menu_price": 8000,
        "menu_description": "양파즙으로 맛을 낸 고기가 많이 들어간 짜장면",
        "menu_price_options": {
                "type": 0, # 0 toggle, 1 checkbox
                "options": [
                    {
                      "label": "1인",
                      "value": 0,
                      "price": 8000,
                    },
                ]
        },
        "menu_additional_options": [
            {
                "type": 1, # 0 toggle, 1 checkbox
                "name": "추가",
                "options": [
                    {
                      "label": "곱배기로 변경",
                      "value": 0,
                      "price": 1000,
                    },
                    {
                      "label": "군만두",
                      "value": 1,
                      "price": 4000,
                    }
                ]
            },
        ],
        "store_id": 1, # S305
        "menu_table_ids": [5],
    })
    menuInfoList.append({
        "menu_id": 7,
        "menu_title": '햄버거 단품',
        "menu_subtitle": '햄버거',
        "menu_price": 8000,
        "menu_description": "소고기패티, 아메리칸치즈, 생양파, 피클, 토마토, 베이컨, 마요네즈",
        "menu_price_options": {
                "type": 0, # 0 toggle, 1 checkbox
                "options": [
                    {
                      "label": "1개",
                      "value": 0,
                      "price": 10000,
                    },
                ]
        },
        "menu_additional_options": [],
        "store_id": 1, # S305
        "menu_table_ids": [6],
    })
    menuInfoList.append({
        "menu_id": 8,
        "menu_title": '햄버거 세트',
        "menu_subtitle": '햄버거 + 감자튀김 + 음료',
        "menu_price": 8000,
        "menu_description": "소고기패티, 아메리칸치즈, 생양파, 피클, 토마토, 베이컨, 마요네즈",
        "menu_price_options": {
                "type": 0, # 0 toggle, 1 checkbox
                "options": [
                    {
                      "label": "1개",
                      "value": 0,
                      "price": 10000,
                    },
                ]
        },
        "menu_additional_options": [
            {
                "type": 0, # 0 toggle, 1 checkbox
                "name": "감자 튀김",
                "options": [
                    {
                      "label": "기본",
                      "value": 0,
                      "price": 0,
                    },
                    {
                      "label": "치즈",
                      "value": 1,
                      "price": 1000,
                    }
                ]
            },
            {
                "type": 1, # 0 toggle, 1 checkbox
                "name": "음료",
                "options": [
                    {
                      "label": "콜라",
                      "value": 0,
                      "price": 0,
                    },
                    {
                      "label": "제로콜라",
                      "value": 1,
                      "price": 0,
                    }
                ]
            },
            { 
                "type": 1, # 0 toggle, 1 checkbox
                "name": "추가",
                "options": [
                    {
                      "label": "곱배기로 변경",
                      "value": 0,
                      "price": 1000,
                    },
                    {
                      "label": "군만두",
                      "value": 2,
                      "price": 4000,
                    }
                ]
            }
            
        ],
        "store_id": 1, # S305
        "menu_table_ids": [6],
    })
    menuInfoList.append({
        "menu_id": 9,
        "menu_title": '콜라',
        "menu_subtitle": '콜라',
        "menu_price": 1500,
        "menu_description": "콜라",
        "menu_price_options": {
                "type": 0, # 0 toggle, 1 checkbox
                "options": [
                    {
                      "label": "1개",
                      "value": 0,
                      "price": 1500,
                    },
                ]
        },
        "menu_additional_options": [],
        "store_id": 1, # S305
        "menu_table_ids": [7],
    })
    menuInfoList.append({
        "menu_id": 10,
        "menu_title": '사이다',
        "menu_subtitle": '사이다',
        "menu_price": 1500,
        "menu_description": "사이다",
        "menu_price_options": {
                "type": 0, # 0 toggle, 1 checkbox
                "options": [
                    {
                      "label": "1개",
                      "value": 0,
                      "price": 1500,
                    },
                ]
        },
        "menu_additional_options": [],
        "store_id": 1, # S305
        "menu_table_ids": [7],
    })
    menuInfoList.append({
        "menu_id": 11,
        "menu_title": '맥주',
        "menu_subtitle": '맥주',
        "menu_price": 4000,
        "menu_description": "맥주",
        "menu_price_options": {
                "type": 0, # 0 toggle, 1 checkbox
                "options": [
                    {
                      "label": "1개",
                      "value": 0,
                      "price": 4000,
                    },
                ]
        },
        "menu_additional_options": [],
        "store_id": 1, # S305
        "menu_table_ids": [8],
    })
    menuInfoList.append({
        "menu_id": 12,
        "menu_title": '소주',
        "menu_subtitle": '소주',
        "menu_price": 4000,
        "menu_description": "소주",
        "menu_price_options": {
                "type": 0, # 0 toggle, 1 checkbox
                "options": [
                    {
                      "label": "1개",
                      "value": 0,
                      "price": 4000,
                    },
                ]
        },
        "menu_additional_options": [],
        "store_id": 1, # S305
        "menu_table_ids": [8],
    })
    for menuInfo in menuInfoList:
        response = requests.post(url, json=menuInfo)
        print(response)

def createEvent(baseUrl):
    url = baseUrl + 'event/createEvent'
    eventInfoList = []
    eventInfoList.append({
        "event_id":  0,
        "event_title": '재야의 커피 판매 시작',
        "event_subtitle": '판매 시작',
        "event_description": '재야의 커피 판매 시작합니다.',
        "event_duedate": str(datetime(2023, 1, 1)),
        "store_id": 0, # 재야의 커피
    })
    eventInfoList.append({
        "event_id":  1,
        "event_title": '신메뉴 출시: 블랜디드 원두',
        "event_subtitle": '블랜디드 원두 출시',
        "event_description": '블랜디드 원두 판매 시작합니다.',
        "event_duedate": str(datetime(2023, 1, 1)),
        "store_id": 0, # 재야의 커피
    })
    eventInfoList.append({
        "event_id":  2,
        "event_title": '신메뉴 출시: 싱글 오리진',
        "event_subtitle": '싱글 오리진 출시',
        "event_description": '싱글 오리진 판매 시작합니다.',
        "event_duedate": str(datetime(2023, 2, 1)),
        "store_id": 0, # 재야의 커피
    })
    eventInfoList.append({
        "event_id":  3,
        "event_title": 'test',
        "event_subtitle": 'testtest',
        "event_description": 'testtesttest',
        "event_duedate": str(datetime(2023, 3, 1)),
        "store_id": 0, # 재야의 커피
    })
    eventInfoList.append({
        "event_id":  4,
        "event_title": 'test',
        "event_subtitle": 'testtest',
        "event_description": 'testtesttest',
        "event_duedate": str(datetime(2023, 3, 15)),
        "store_id": 0, # 재야의 커피
    })
    eventInfoList.append({
        "event_id":  5,
        "event_title": 'test',
        "event_subtitle": 'testtest',
        "event_description": 'testtesttest',
        "event_duedate": str(datetime(2023, 3, 30)),
        "store_id": 0, # 재야의 커피
    })
    eventInfoList.append({
        "event_id":  6,
        "event_title": '세상에서 가장 싼 커피',
        "event_subtitle": '커피 할인 이벤트',
        "event_description": '선착순 100분에게 할인 혜택을 제공합니다.',
        "event_duedate": str(datetime(2023, 4, 30)),
        "store_id": 0, # 재야의 커피
    })
    eventInfoList.append({
        "event_id":  7,
        "event_title": '세상에서 가장 싼 와인',
        "event_subtitle": '와인 할인 이벤트',
        "event_description": '선착순 100분에게 할인 혜택을 제공합니다.',
        "event_duedate": str(datetime(2023, 4, 30)),
        "store_id": 0, # 재야의 커피
    })
    eventInfoList.append({
        "event_id":  8,
        "event_title": 'test',
        "event_subtitle": 'testtest',
        "event_description": 'testtestest',
        "event_duedate": str(datetime(2023, 1, 15)),
        "store_id": 1, # S305
    })
    eventInfoList.append({
        "event_id":  9,
        "event_title": 'test',
        "event_subtitle": 'testtest',
        "event_description": 'testtestest',
        "event_duedate": str(datetime(2023, 2, 15)),
        "store_id": 1, # S305
    })
    eventInfoList.append({
        "event_id":  10,
        "event_title": 'test',
        "event_subtitle": 'testtest',
        "event_description": 'testtestest',
        "event_duedate": str(datetime(2023, 3, 15)),
        "store_id": 1, # S305
    })
    eventInfoList.append({
        "event_id":  11,
        "event_title": 'test',
        "event_subtitle": 'testtest',
        "event_description": 'testtestest',
        "event_duedate": str(datetime(2023, 4, 15)),
        "store_id": 1, # S305
    })
    eventInfoList.append({
        "event_id":  12,
        "event_title": 'test',
        "event_subtitle": 'testtest',
        "event_description": 'testtestest',
        "event_duedate": str(datetime(2023, 5, 15)),
        "store_id": 1, # S305
    })
    for eventInfo in eventInfoList:
        response = requests.post(url, json=eventInfo)
        print(response)

def rename():
    p = '../public/images/story'
    for pn in os.listdir(p):
        if pn[0] == '.':
            continue
        i = 0
        temp = os.listdir(os.path.join(p, pn))
        temp.sort()
        for pnn in temp:
            if pnn[0] == '.':
                continue
            print(pnn)
            os.rename(os.path.join(p, pn, pnn), os.path.join(p, pn, str(i)  + '.jpg'))
            i += 1

if __name__ == "__main__":
    baseUrl = 'http://localhost:3000/'
    #createStore(baseUrl)
    #createStory(baseUrl)
    #createMenuTable(baseUrl)
    #createMenu(baseUrl)
    createEvent(baseUrl)
    #rename()
    