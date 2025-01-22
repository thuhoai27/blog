import random
from datetime import datetime, timedelta
import os

# 주제 카테고리 정의
categories = {
    'technology': ['AI', '블록체인', '클라우드', '사이버보안', 'IoT', '모바일', '프로그래밍'],
    'lifestyle': ['여행', '요리', '운동', '독서', '취미', '인테리어', '패션'],
    'food': ['한식', '양식', '중식', '일식', '베이킹', '디저트', '음료'],
    'health': ['운동', '영양', '멘탈케어', '수면', '요가', '명상', '다이어트']
}

# 제목 템플릿
title_templates = {
    'technology': [
        "{tech}의 최신 트렌드 분석",
        "{tech} 초보자 가이드",
        "{tech}로 시작하는 디지털 혁신",
        "미래를 바꿀 {tech} 기술",
        "알아두면 좋은 {tech} 핵심 개념"
    ],
    'lifestyle': [
        "{activity} 시작하기 완벽 가이드",
        "{activity} 전문가의 조언",
        "일상을 바꾸는 {activity} 팁",
        "{activity} 초보자도 할 수 있어요",
        "나만의 {activity} 스타일 찾기"
    ],
    'food': [
        "맛있는 {cuisine} 레시피",
        "{cuisine} 요리 비법 공개",
        "초간단 {cuisine} 만들기",
        "{cuisine} 마스터하기",
        "집에서 만드는 {cuisine}"
    ],
    'health': [
        "{topic} 시작하기",
        "건강한 {topic} 가이드",
        "{topic} 전문가 조언",
        "일상 속 {topic} 실천법",
        "효과적인 {topic} 방법"
    ]
}

def generate_post_content(category, topic):
    """포스트 내용 생성"""
    content = f"""---
layout: post
title: "{generate_title(category, topic)}"
date: {generate_date()}
categories: {category} {topic.lower()}
---

# {topic}에 대해 알아보기

## 소개
{topic}은(는) 현대 생활에서 매우 중요한 부분을 차지하고 있습니다.

## 주요 특징
- 특징 1
- 특징 2
- 특징 3

## 실천 방법
1. 첫 번째 방법
2. 두 번째 방법
3. 세 번째 방법

## 마무리
{topic}에 대해 알아보았습니다. 이를 통해 더 나은 삶을 살 수 있기를 바랍니다.
"""
    return content

def generate_title(category, topic):
    """제목 생성"""
    template = random.choice(title_templates[category])
    return template.format(tech=topic, activity=topic, cuisine=topic, topic=topic)

def generate_date():
    """날짜 생성 (2024-2025년 사이)"""
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2025, 12, 31)
    days_between = (end_date - start_date).days
    random_days = random.randint(0, days_between)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime("%Y-%m-%d %H:%M:%S +0900")

def main():
    """메인 함수"""
    # _posts 디렉토리 생성
    if not os.path.exists('_posts'):
        os.makedirs('_posts')

    # 1만개의 포스트 생성
    for i in range(10000):
        # 랜덤 카테고리와 주제 선택
        category = random.choice(list(categories.keys()))
        topic = random.choice(categories[category])
        
        # 날짜 생성
        date = datetime.strptime(generate_date(), "%Y-%m-%d %H:%M:%S +0900")
        
        # 파일명 생성
        filename = f"_posts/{date.strftime('%Y-%m-%d')}-{topic.lower().replace(' ', '-')}-{i+1}.markdown"
        
        # 포스트 내용 생성 및 저장
        content = generate_post_content(category, topic)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # 진행상황 출력
        if (i + 1) % 100 == 0:
            print(f"{i + 1}개의 포스트 생성 완료")

if __name__ == "__main__":
    main()
    print("모든 포스트 생성이 완료되었습니다!") 