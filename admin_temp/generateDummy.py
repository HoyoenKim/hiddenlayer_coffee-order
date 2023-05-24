import requests
import os
from datetime import datetime

def createStore(baseUrl):
    url = baseUrl + 'store/createStore'

    storeInfoList = []
    storeInfoList.append({
                            "store_id": 0,
		                    "store_title": '재야의 커피',
		                    "store_type": '카페',
                            "store_subtitle": "사용자 맞춤 원두 추천 카페",
		                    "store_description": "잘 내린 핸드드립 한잔,\n잠을 포기하게 만드는 맛",
                            "store_address": "광주 북구 첨단과기로 123 창업진흥센터 B동 501호",
                            "store_location": ["35.23021", "126.83982"], # 위도, 경도                      
                            "store_images_nums": 4,
		                    "store_order_type": [1, 1, 1], # '테이블 주문 가능', '포장 가능', '배달 가능'
		                    "store_payment_type": [0, 1, "우리은행 류현석 1002-657-201417"], # '카드, 계좌이체'
		                    "store_open_time": [[10, 22], [10, 22], [10, 22], [10, 22], [10, 22], [10, 22], [10, 22], [10, 22]], # 월 - 일, 공휴일
		                    "store_official_information": ['류현석', '창업진흥센터 B동 401호', '010-2128-7164'], # 소유자, 장소, 담당자 연락처
		                    "store_keyword_ids": [0, 1, 2, 3, 4, 5, 6],
		                    "menu_table_ids": [0],
		                    "event_ids": [0, 1],
		                    "owner_ids": [0], # need to encription
                            "store_subscription_number": 0
                        })
    storeInfoList.append({
                            "store_id": 1,
		                    "store_title": '삼복당',
		                    "store_type": '음식점',
                            "store_subtitle": "닭칼국수 맛집",
		                    "store_description": "따끈한 국물로,\n겨울의 추위를 잊게 만드는 맛",
                            "store_address": "광주 광산구 첨단중앙로182번길 16 삼복당",
                            "store_location": [], # 위도, 경도                      
                            "store_images_nums": 0,
		                    "store_order_type": [0, 0, 0], # '테이블 주문 가능', '포장 가능', '배달 가능'
		                    "store_payment_type": [0, 0], # '카드, 계좌이체'
		                    "store_open_time": [], # 월 - 일, 공휴일
		                    "store_official_information": ['', '첨단중앙로182번길 16 삼복당', '062-972-4946'], # 소유자, 장소, 담당자 연락처
		                    "store_keyword_ids": [7],
		                    "menu_table_ids": [],
		                    "event_ids": [2],
		                    "owner_ids": [0], # need to encription
                            "store_subscription_number": 0
                        })
    storeInfoList.append({
                            "store_id": 2,
		                    "store_title": '소코아',
		                    "store_type": '음식점',
                            "store_subtitle": "돈까스 맛집",
		                    "store_description": "일식 볼모지에서 찾아낸,\n돈까스 카레 맛집",
                            "store_address": "광주 광산구 월계동 875-6 1층",
                            "store_location": [], # 위도, 경도                      
                            "store_images_nums": 0,
		                    "store_order_type": [0, 0, 0], # '테이블 주문 가능', '포장 가능', '배달 가능'
		                    "store_payment_type": [0, 0], # '카드, 계좌이체'
		                    "store_open_time": [], # 월 - 일, 공휴일
		                    "store_official_information": ['', '월계동 875-6 1층', '010-8622-4300'], # 소유자, 장소, 담당자 연락처
		                    "store_keyword_ids": [8],
		                    "menu_table_ids": [],
		                    "event_ids": [3],
		                    "owner_ids": [0], # need to encription
                            "store_subscription_number": 0
                        })
    #storeInfoList.append({
    #                        "store_id": 1,
		#                    "store_title": 'S305',
		#                    "store_subtitle": 'Home Cafe',
    #                        "store_images_nums": 3,
		#                    "store_description": '테스트 더미 데이터: 각종 모든 메뉴 테스트베드',
		#                    "store_order_type": [1, 1, 0], # '테이블 주문 가능', '포장 가능', '배달 가능'
		#                    "store_location": ["35.22959", "126.84775"], # 위도, 경도
		#                    "store_open_time": [[10, 22], [10, 22], [10, 22], [10, 22], [10, 22], [10, 22], [10, 22], [10, 22]], # 월 - 일, 공휴일
		#                    "store_official_information": ['김호연', '학사기숙사 B동 S305', '010-2128-7164'], # 소유자, 장소, 담당자 연락처
		#                    "story_ids": [12, 13, 14, 15, 16, 17, 18, 19],
		#                    "menu_table_ids": [3, 4, 5, 6, 7, 8],
		#                    "event_ids": [8, 9, 10, 11, 12],
		#                    "owner_ids": [1], # need to encription
    #                    })
    
    for storeInfo in storeInfoList:
        response = requests.post(url, json=storeInfo, verify=False)
        print(response)

def createVenue(baseUrl):
    url = baseUrl + 'venue/createVenue'

    venueInfoList = []
    venueInfoList.append({
                        "venue_id": 0,
                        "venue_title": "GIST 문행위 행사",
                        "venue_subtitle": "",
                        "venue_description": "GIST 문화행사위원회 축제 (2023.05.25)",
                        "venue_address": "광주 북구 첨단과기로123 제2학생회관",
                        "venue_location": [],
                        "venue_images_nums": 3,
                        "venue_keyword_ids": [],
                        "event_ids": [4, 5],
                        "owner_ids": [0],
                        "booth_ids": [0, 1, 2, 3, 4, 5, 6, 7] 
                    })
    
    for venueInfo in venueInfoList:
        response = requests.post(url, json=venueInfo, verify=False)
        print(response)

def createKeyword(baseUrl):
    url = baseUrl + 'keyword/createKeyword'

    keywordList = []
    keywordList.append({
                        "keyword_id": 0,
                        "keyword_title": "Speciality",
                        "keyword_description": "커피에 진심인 사람들이 모여 원두와 추출법에 대해 연구하여 만들어낸 최상의 조합으로 커피를 내려 드립니다.",
                        "origin_type": 0, # 0: 매장, 1: 행사장, 2 부스
                        "origin_id": 0
                    })
    keywordList.append({
                        "keyword_id": 1,
                        "keyword_title": "엘파라이소 리치 - 피치",
                        "keyword_description": "리치, 복숭아, 블루베리 향이 나는 콜롬비아산 원두로 내린 커피",
                        "origin_type": 0,
                        "origin_id": 0
                    })
    keywordList.append({
                        "keyword_id": 2,
                        "keyword_title": "시다모 문루게타 문타샤",
                        "keyword_description": "단맛, 패션후르츠 향이 나는 에티오피산 원두로 내린 커피",
                        "origin_type": 0,
                        "origin_id": 0
                    })
    keywordList.append({
                        "keyword_id": 3,
                        "keyword_title": "Location",
                        "keyword_description": "광주 북구 첨단과기로 123 창업진흥센터 B동 403호",
                        "origin_type": 0,
                        "origin_id": 0
                    })
    keywordList.append({
                        "keyword_id": 4,
                        "keyword_title": "Signature",
                        "keyword_description": "엘파라이소 리치-피치: 3900원\n시다모 문루게타 문타샤: 3900원\n * 메뉴 가격에 변동이 있을 수 있습니다.",
                        "origin_type": 0,
                        "origin_id": 0
                    })
    keywordList.append({
                        "keyword_id": 5,
                        "keyword_title": "Operations",
                        "keyword_description": "월 - 금 11:00 - 13:00",
                        "origin_type": 0,
                        "origin_id": 0
                    })
    keywordList.append({
                        "keyword_id": 6,
                        "keyword_title": "Calls",
                        "keyword_description": "010-2590-2746",
                        "origin_type": 0,
                        "origin_id": 0
                    })
    keywordList.append({
                        "keyword_id": 7,
                        "keyword_title": "Location",
                        "keyword_description": "광주 광산구 첨단중앙로182번길 16 삼복당",
                        "origin_type": 0,
                        "origin_id": 0
                    })
    keywordList.append({
                        "keyword_id": 8,
                        "keyword_title": "Location",
                        "keyword_description": "광주 광산구 월계동 875-6 1층",
                        "origin_type": 0,
                        "origin_id": 0
                    })
    
    
    for kewordInfo in keywordList:
        response = requests.post(url, json=kewordInfo, verify=False)
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
    #storyInfoList.append({
    #                        "story_id": 12,
    #                        "story_generate_time":  str(datetime.now()),
    #                        "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
    #                        "story_tag": [], 
    #                        "story_title": '테스트',
    #                        "story_subtitle": '테스트테스트',
    #                        "story_description": '테스트테스트테스트테스트',
    #                        "store_id": 1, # 'S305'
    #})
    #storyInfoList.append({
    #                        "story_id": 13,
    #                        "story_generate_time":  str(datetime.now()),
    #                        "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
    #                        "story_tag": [], 
    #                        "story_title": '테스트',
    #                        "story_subtitle": '테스트테스트',
    #                        "story_description": '테스트테스트테스트테스트',
    #                        "store_id": 1, # 'S305'
    #})
    #storyInfoList.append({
    #                        "story_id": 14,
    #                        "story_generate_time":  str(datetime.now()),
    #                        "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
    #                        "story_tag": [], 
    #                        "story_title": '테스트',
    #                        "story_subtitle": '테스트테스트',
    #                        "story_description": '테스트테스트테스트테스트',
    #                        "store_id": 1, # 'S305'
    #})
    #storyInfoList.append({
    #                        "story_id": 15,
    #                        "story_generate_time":  str(datetime.now()),
    #                        "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
    #                        "story_tag": [], 
    #                        "story_title": '테스트',
    #                        "story_subtitle": '테스트테스트',
    #                        "story_description": '테스트테스트테스트테스트',
    #                        "store_id": 1, # 'S305'
    #})
    #storyInfoList.append({
    #                        "story_id": 16,
    #                        "story_generate_time":  str(datetime.now()),
    #                        "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
    #                        "story_tag": [], 
    #                        "story_title": '테스트',
    #                        "story_subtitle": '테스트테스트',
    #                        "story_description": '테스트테스트테스트테스트',
    #                        "store_id": 1, # 'S305'
    #})
    #storyInfoList.append({
    #                        "story_id": 17,
    #                        "story_generate_time":  str(datetime.now()),
    #                        "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
    #                        "story_tag": [], 
    #                        "story_title": '테스트',
    #                        "story_subtitle": '테스트테스트',
    #                        "story_description": '테스트테스트테스트테스트',
    #                        "store_id": 1, # 'S305'
    #})
    #storyInfoList.append({
    #                        "story_id": 18,
    #                        "story_generate_time":  str(datetime.now()),
    #                        "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
    #                        "story_tag": [], 
    #                        "story_title": '테스트',
    #                        "story_subtitle": '테스트테스트',
    #                        "story_description": '테스트테스트테스트테스트',
    #                        "store_id": 1, # 'S305'
    #})
    #storyInfoList.append({
    #                        "story_id": 19,
    #                        "story_generate_time":  str(datetime.now()),
    #                        "story_type": 1, # 동영상: 0, 사진 개수: 1 ~ 5
    #                        "story_tag": [], 
    #                        "story_title": '테스트',
    #                        "story_subtitle": '테스트테스트',
    #                        "story_description": '테스트테스트테스트테스트',
    #                        "store_id": 1, # 'S305'
    #})

    for storyInfo in storyInfoList:
        response = requests.post(url, json=storyInfo)
        print(response)

def createMenuTable(baseUrl):
    url = baseUrl + 'menu/createMenuTable'
    menuTableInfoList = []
    menuTableInfoList.append({
                                "menu_table_id": 0,
                                "menu_table_title": '시그니처 커피',
                                "menu_table_subtitle": '이번주 커피',
                                "menu_ids": [0, 1],
                                "store_id": 0, # '재야의 커피'
    })
    #menuTableInfoList.append({
    #                            "menu_table_id": 1,
    #                            "menu_table_title": '블랜디드 원두',
    #                            "menu_table_subtitle": '',
    #                            "menu_ids": [0],
    #                            "store_id": 0, # '재야의 커피'
    #})
    #menuTableInfoList.append({
    #                            "menu_table_id": 2,
    #                            "menu_table_title": '고급 원두',
    #                            "menu_table_subtitle": '하루 10잔 한정 판매',
    #                            "menu_ids": [1],
    #                            "store_id": 0, # '재야의 커피'
    #})
    #menuTableInfoList.append({
    #                            "menu_table_id": 3,
    #                            "menu_table_title": '한식',
    #                            "menu_table_subtitle": '다양한 한식 메뉴',
    #                            "menu_ids": [2, 3, 4],
    #                            "store_id": 1, # 'S305'
    #})
    #menuTableInfoList.append({
    #                            "menu_table_id": 4,
    #                            "menu_table_title": '일식',
    #                            "menu_table_subtitle": '다양한 일식 메뉴',
    #                            "menu_ids": [5],
    #                            "store_id": 1, # 'S305'
    #})
    #menuTableInfoList.append({
    #                            "menu_table_id": 5,
    #                            "menu_table_title": '중식',
    #                            "menu_table_subtitle": '다양한 중식 메뉴',
    #                            "menu_ids": [6],
    #                            "store_id": 1, # 'S305'
    #})
    #menuTableInfoList.append({
    #                            "menu_table_id": 6,
    #                            "menu_table_title": '양식',
    #                            "menu_table_subtitle": '다양한 일식 메뉴',
    #                            "menu_ids": [7, 8],
    #                            "store_id": 1, # 'S305'
    #})
    #menuTableInfoList.append({
    #                            "menu_table_id": 7,
    #                            "menu_table_title": '음료',
    #                            "menu_table_subtitle": '다양한 음료 메뉴',
    #                            "menu_ids": [9, 10],
    #                            "store_id": 1, # 'S305'
    #})
    #menuTableInfoList.append({
    #                            "menu_table_id": 8,
    #                            "menu_table_title": '주류',
    #                            "menu_table_subtitle": '다양한 주류 메뉴',
    #                            "menu_ids": [11, 12],
    #                            "store_id": 1, # 'S305'
    #})
    for menuTableInfo in menuTableInfoList:
        response = requests.post(url, json=menuTableInfo)
        print(response)

def createMenu(baseUrl):
    url = baseUrl + 'menu/createMenu'
    menuInfoList = []
    menuInfoList.append({
        "menu_id": 0,
        "menu_title": '엘파라이소 리치-피치',
        "menu_subtitle": '콜롬비아, 리치, 복숭아, 블루베리 (300ml)',
        "menu_price": 3900,
        "menu_description": "콜롬비아산 원두, 리치, 복숭아, 블루베리, 메이플 시럽맛이 나는 연하고 부드러운 핸드드립 커피입니다.",
        "menu_price_options": {
                "type": 0, # 0 toggle, 1 checkbox
                "options": [
                    {
                      "label": "엘파라이소 리치-피치",
                      "value": 0,
                      "price": 3900,
                    }
                ]
        },
        "menu_additional_options": [
            {
                "type": 0, # 0 toggle, 1 checkbox
                "name": "온도",
                "options": [
                    {
                      "label": "ICE",
                      "value": 0, #index 와 같아야함!!
                      "price": 0,
                    }
                ]
            },
            {
                "type": 0, # 0 toggle, 1 checkbox
                "name": "커피 농도",
                "options": [
                    {
                      "label": "연하게",
                      "value": 0, #index 와 같아야함!!
                      "price": 0,
                    }
                ]
            }
        ],
        "store_id": 0, # 재야의 커피
        "menu_table_ids": [0],
    })
    menuInfoList.append({
        "menu_id": 1,
        "menu_title": '시다모 문루게타 문타샤',
        "menu_subtitle": '에티오피아, 단맛, 패션후르츠 (300ml)',
        "menu_price": 3900,
        "menu_description": "에티오피아 원두, 산뜻한 과일과 꿀이 섞여 부드럽고 진한 단맛이 길게 여운이 남는 연하고 부드러운 핸드드립 커피입니다.",
        "menu_price_options": {
                "type": 0, # 0 toggle, 1 checkbox
                "options": [
                    {
                      "label": "시다모 문루게타 문타샤",
                      "value": 0, #index 와 같아야함!!
                      "price": 3900,
                    }
                ]
        },
        "menu_additional_options": [
            {
                "type": 0, # 0 toggle, 1 checkbox
                "name": "온도",
                "options": [
                    {
                      "label": "HOT",
                      "value": 0, #index 와 같아야함!!
                      "price": 0,
                    }
                ]
            },
            {
                "type": 0, # 0 toggle, 1 checkbox
                "name": "커피 농도",
                "options": [
                    {
                      "label": "연하게",
                      "value": 0, #index 와 같아야함!!
                      "price": 0,
                    }
                ]
            }
        ],
        "store_id": 0, # 재야의 커피
        "menu_table_ids": [0],
    })
    #menuInfoList.append({
    #    "menu_id": 2,
    #    "menu_title": '김치찜',
    #    "menu_subtitle": '삼겹살 + 김치 + 공기밥',
    #    "menu_price": 15900,
    #    "menu_description": "1인(고기 150g, 공기밥 1), 2인(고기 320g, 공기밥 2), 3인(고기 500g, 공기밥 3)",
    #    "menu_price_options": {
    #            "type": 0, # 0 toggle, 1 checkbox
    #            "options": [
    #                {
    #                  "label": "1인",
    #                  "value": 0,
    #                  "price": 15900,
    #                },
    #                {
    #                  "label": "2인",
    #                  "value": 1,
    #                  "price": 24900,
    #                },
    #                {
    #                  "label": "3인",
    #                  "value": 2,
    #                  "price": 32900,
    #                }
    #            ]
    #    },
    #    "menu_additional_options": [
    #        {
    #            "type": 1, # 0 toggle, 1 checkbox
    #            "name": "사이드 메뉴",
    #            "options": [
    #                {
    #                  "label": "계란찜",
    #                  "value": 0,
    #                  "price": 4000,
    #                },
    #                {
    #                  "label": "계란말이",
    #                  "value": 1,
    #                  "price": 4000,
    #                },
    #                {
    #                  "label": "참치마요",
    #                  "value": 2,
    #                  "price": 4000,
    #                }
    #            ]
    #        },
    #        {
    #            "type": 1, # 0 toggle, 1 checkbox
    #            "name": "추가 선택",
    #            "options": [
    #                {
    #                  "label": "공기밥 1개",
    #                  "value": 0,
    #                  "price": 500,
    #                },
    #                {
    #                  "label": "공기밥 2개",
    #                  "value": 1,
    #                  "price": 1000,
    #                },
    #                {
    #                  "label": "공기밥 3개",
    #                  "value": 2,
    #                  "price": 1500,
    #                }
    #            ]
    #        }
    #    ],
    #    "store_id": 1, # S305
    #    "menu_table_ids": [3],
    #})
    #menuInfoList.append({
    #    "menu_id": 3,
    #    "menu_title": '곰탕',
    #    "menu_subtitle": '공기밥 + 쌈장 + 양파 + 청양고추 + 김치',
    #    "menu_price": 10000,
    #    "menu_description": "공기밥 + 쌈장 + 양파 + 청양고추 + 김치",
    #    "menu_price_options": {
    #            "type": 0, # 0 toggle, 1 checkbox
    #            "options": [
    #                {
    #                  "label": "1인",
    #                  "value": 0,
    #                  "price": 10000,
    #                },
    #            ]
    #    },
    #    "menu_additional_options": [],
    #    "store_id": 1, # S305
    #    "menu_table_ids": [3],
    #})
    #menuInfoList.append({
    #    "menu_id": 4,
    #    "menu_title": '부대찌개',
    #    "menu_subtitle": '공기밥 + 김치',
    #    "menu_price": 15900,
    #    "menu_description": "스팸 정품 사용합니다.",
    #    "menu_price_options": {
    #            "type": 0, # 0 toggle, 1 checkbox
    #            "options": [
    #                {
    #                  "label": "1~2인 + 공기밥1",
    #                  "value": 0,
    #                  "price": 15900,
    #                },
    #                {
    #                  "label": "2~3인 + 공기밥2",
    #                  "value": 1,
    #                  "price": 24900,
    #                },
    #                {
    #                  "label": "3~4인 + 공기밥3",
    #                  "value": 2,
    #                  "price": 32900,
    #                }
    #            ]
    #    },
    #    "menu_additional_options": [
    #        {
    #            "type": 0,
    #            "name": "맵기 선택",
    #            "options": [
    #                 {
    #                  "label": "0단계 (순한맛)",
    #                  "value": 0,
    #                  "price": 0,
    #                },
    #                {
    #                  "label": "1단계 (신라면)",
    #                  "value": 1,
    #                  "price": 0,
    #                },
    #                {
    #                  "label": "2단계 (불닭)",
    #                  "value": 2,
    #                  "price": 0,
    #                }
    #            ]
    #        },
    #        {
    #            "type": 1, # 0 toggle, 1 checkbox
    #            "name": "사이드 메뉴",
    #            "options": [
    #                {
    #                  "label": "계란찜",
    #                  "value": 0,
    #                  "price": 4000,
    #                },
    #                {
    #                  "label": "계란말이",
    #                  "value": 1,
    #                  "price": 4000,
    #                },
    #                {
    #                  "label": "참치마요",
    #                  "value": 2,
    #                  "price": 4000,
    #                }
    #            ]
    #        },
    #        {
    #            "type": 1, # 0 toggle, 1 checkbox
    #            "name": "추가 선택",
    #            "options": [
    #                {
    #                  "label": "공기밥 1개",
    #                  "value": 0,
    #                  "price": 500,
    #                },
    #                {
    #                  "label": "공기밥 2개",
    #                  "value": 1,
    #                  "price": 1000,
    #                },
    #                {
    #                  "label": "공기밥 3개",
    #                  "value": 2,
    #                  "price": 1500,
    #                }
    #            ]
    #        }
    #    ],
    #    "store_id": 1, # S305
    #    "menu_table_ids": [3],
    #})
    #menuInfoList.append({
    #    "menu_id": 5,
    #    "menu_title": '돈까스',
    #    "menu_subtitle": '수제 돈까스 도시락',
    #    "menu_price": 10900,
    #    "menu_description": "100% 국내산 냉장 등심, 손으로 만든 수제 돈까스, 최고급 소스",
    #    "menu_price_options": {
    #            "type": 0, # 0 toggle, 1 checkbox
    #            "options": [
    #                {
    #                  "label": "1인",
    #                  "value": 0,
    #                  "price": 10900,
    #                },
    #            ]
    #    },
    #    "menu_additional_options": [
    #        {
    #            "type": 1, # 0 toggle, 1 checkbox
    #            "name": "사이드 메뉴",
    #            "options": [
    #                {
    #                  "label": "소스",
    #                  "value": 0,
    #                  "price": 500,
    #                },
    #                {
    #                  "label": "계란말이",
    #                  "value": 1,
    #                  "price": 4000,
    #                },
    #                {
    #                  "label": "만두",
    #                  "value": 2,
    #                  "price": 4000,
    #                }
    #            ]
    #        },
    #    ],
    #    "store_id": 1, # S305
    #    "menu_table_ids": [4],
    #})
    #menuInfoList.append({
    #    "menu_id": 6,
    #    "menu_title": '짜장면',
    #    "menu_subtitle": '짜장면 + 양파 + 단무지',
    #    "menu_price": 8000,
    #    "menu_description": "양파즙으로 맛을 낸 고기가 많이 들어간 짜장면",
    #    "menu_price_options": {
    #            "type": 0, # 0 toggle, 1 checkbox
    #            "options": [
    #                {
    #                  "label": "1인",
    #                  "value": 0,
    #                  "price": 8000,
    #                },
    #            ]
    #    },
    #    "menu_additional_options": [
    #        {
    #            "type": 1, # 0 toggle, 1 checkbox
    #            "name": "추가",
    #            "options": [
    #                {
    #                  "label": "곱배기로 변경",
    #                  "value": 0,
    #                  "price": 1000,
    #                },
    #                {
    #                  "label": "군만두",
    #                  "value": 1,
    #                  "price": 4000,
    #                }
    #            ]
    #        },
    #    ],
    #    "store_id": 1, # S305
    #    "menu_table_ids": [5],
    #})
    #menuInfoList.append({
    #    "menu_id": 7,
    #    "menu_title": '햄버거 단품',
    #    "menu_subtitle": '햄버거',
    #    "menu_price": 8000,
    #    "menu_description": "소고기패티, 아메리칸치즈, 생양파, 피클, 토마토, 베이컨, 마요네즈",
    #    "menu_price_options": {
    #            "type": 0, # 0 toggle, 1 checkbox
    #            "options": [
    #                {
    #                  "label": "1개",
    #                  "value": 0,
    #                  "price": 10000,
    #                },
    #            ]
    #    },
    #    "menu_additional_options": [],
    #    "store_id": 1, # S305
    #    "menu_table_ids": [6],
    #})
    #menuInfoList.append({
    #    "menu_id": 8,
    #    "menu_title": '햄버거 세트',
    #    "menu_subtitle": '햄버거 + 감자튀김 + 음료',
    #    "menu_price": 8000,
    #    "menu_description": "소고기패티, 아메리칸치즈, 생양파, 피클, 토마토, 베이컨, 마요네즈",
    #    "menu_price_options": {
    #            "type": 0, # 0 toggle, 1 checkbox
    #            "options": [
    #                {
    #                  "label": "1개",
    #                  "value": 0,
    #                  "price": 10000,
    #                },
    #            ]
    #    },
    #    "menu_additional_options": [
    #        {
    #            "type": 0, # 0 toggle, 1 checkbox
    #            "name": "감자 튀김",
    #            "options": [
    #                {
    #                  "label": "기본",
    #                  "value": 0,
    #                  "price": 0,
    #                },
    #                {
    #                  "label": "치즈",
    #                  "value": 1,
    #                  "price": 1000,
    #                }
    #            ]
    #        },
    #        {
    #            "type": 1, # 0 toggle, 1 checkbox
    #            "name": "음료",
    #            "options": [
    #                {
    #                  "label": "콜라",
    #                  "value": 0,
    #                  "price": 0,
    #                },
    #                {
    #                  "label": "제로콜라",
    #                  "value": 1,
    #                  "price": 0,
    #                }
    #            ]
    #        },
    #        { 
    #            "type": 1, # 0 toggle, 1 checkbox
    #            "name": "추가",
    #            "options": [
    #                {
    #                  "label": "곱배기로 변경",
    #                  "value": 0,
    #                  "price": 1000,
    #                },
    #                {
    #                  "label": "군만두",
    #                  "value": 2,
    #                  "price": 4000,
    #                }
    #            ]
    #        }
    #        
    #    ],
    #    "store_id": 1, # S305
    #    "menu_table_ids": [6],
    #})
    #menuInfoList.append({
    #    "menu_id": 9,
    #    "menu_title": '콜라',
    #    "menu_subtitle": '콜라',
    #    "menu_price": 1500,
    #    "menu_description": "콜라",
    #    "menu_price_options": {
    #            "type": 0, # 0 toggle, 1 checkbox
    #            "options": [
    #                {
    #                  "label": "1개",
    #                  "value": 0,
    #                  "price": 1500,
    #                },
    #            ]
    #    },
    #    "menu_additional_options": [],
    #    "store_id": 1, # S305
    #    "menu_table_ids": [7],
    #})
    #menuInfoList.append({
    #    "menu_id": 10,
    #    "menu_title": '사이다',
    #    "menu_subtitle": '사이다',
    #    "menu_price": 1500,
    #    "menu_description": "사이다",
    #    "menu_price_options": {
    #            "type": 0, # 0 toggle, 1 checkbox
    #            "options": [
    #                {
    #                  "label": "1개",
    #                  "value": 0,
    #                  "price": 1500,
    #                },
    #            ]
    #    },
    #    "menu_additional_options": [],
    #    "store_id": 1, # S305
    #    "menu_table_ids": [7],
    #})
    #menuInfoList.append({
    #    "menu_id": 11,
    #    "menu_title": '맥주',
    #    "menu_subtitle": '맥주',
    #    "menu_price": 4000,
    #    "menu_description": "맥주",
    #    "menu_price_options": {
    #            "type": 0, # 0 toggle, 1 checkbox
    #            "options": [
    #                {
    #                  "label": "1개",
    #                  "value": 0,
    #                  "price": 4000,
    #                },
    #            ]
    #    },
    #    "menu_additional_options": [],
    #    "store_id": 1, # S305
    #    "menu_table_ids": [8],
    #})
    #menuInfoList.append({
    #    "menu_id": 12,
    #    "menu_title": '소주',
    #    "menu_subtitle": '소주',
    #    "menu_price": 4000,
    #    "menu_description": "소주",
    #    "menu_price_options": {
    #            "type": 0, # 0 toggle, 1 checkbox
    #            "options": [
    #                {
    #                  "label": "1개",
    #                  "value": 0,
    #                  "price": 4000,
    #                },
    #            ]
    #    },
    #    "menu_additional_options": [],
    #    "store_id": 1, # S305
    #    "menu_table_ids": [8],
    #})
    for menuInfo in menuInfoList:
        response = requests.post(url, json=menuInfo)
        print(response)

def createEvent(baseUrl):
    url = baseUrl + 'event/createEvent'
    eventInfoList = []
    eventInfoList.append({
        "event_id":  0,
        "event_title": '신메뉴 출시: 엘파라이소 리치 - 피치',
        "event_subtitle": '리치, 블루베리, 복숭아',
        "event_description": '엘파라이소 리치 - 피치 판매 시작합니다.',
        "event_duedate": str(datetime(2023, 4, 30)),
        "event_images_nums": 1,
        "origin_type": 0, # 0: 매장, 1: 행사장, 2 부스
        "origin_id": 0, # 재야의 커피
        "event_subscription_number": 0,
    })
    eventInfoList.append({
        "event_id":  1,
        "event_title": '신메뉴 출시: 시다모 문루게타 문타샤',
        "event_subtitle": '단맛, 패션후르츠',
        "event_description": '시다모 문루게타 문타샤 판매 시작합니다.',
        "event_duedate": str(datetime(2023, 4, 30)),
        "event_images_nums": 1,
        "origin_type": 0, # 0: 매장, 1: 행사장, 2 부스
        "origin_id": 0, # 재야의 커피
        "event_subscription_number": 0,
    })
    eventInfoList.append({
        "event_id":  2,
        "event_title": '증정: 인스타 스토리 이벤트',
        "event_subtitle": '인스타 스토리 게시',
        "event_description": '정인분 주문하고/인스타 스토리 게시할 시 탄산음료 500mL 1개를 제공합니다.',
        "event_duedate": str(datetime(2023, 12, 31)),
        "event_images_nums": 1,
        "origin_type": 0, # 0: 매장, 1: 행사장, 2 부스
        "origin_id": 1,
        "event_subscription_number": 0,
    })
    eventInfoList.append({
        "event_id":  3,
        "event_title": '증정: GIST 방문 주문 이벤트',
        "event_subtitle": '탄산음료 증정',
        "event_description": '테이블 당 콜라 또는 사이다를 서비스로 제공합니다.',
        "event_duedate": str(datetime(2023, 12, 31)),
        "event_images_nums": 1,
        "origin_type": 0, # 0: 매장, 1: 행사장, 2 부스
        "origin_id": 2,
        "event_subscription_number": 0,
    })
    for eventInfo in eventInfoList:
        response = requests.post(url, json=eventInfo, verify=False)
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
    baseUrl = 'https://localhost:3000/'
    #baseUrl = 'http://18.118.221.107:3001/'
    #createStore(baseUrl)
    #createVenue(baseUrl)
    #createKeyword(baseUrl)
    #createStory(baseUrl)
    #createMenuTable(baseUrl)
    #createMenu(baseUrl)
    createEvent(baseUrl)
    #rename()
    