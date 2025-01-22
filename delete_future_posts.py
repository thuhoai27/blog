import os
from datetime import datetime
import re

def delete_future_posts():
    # 현재 날짜 가져오기
    today = datetime.now().date()
    
    # _posts 디렉토리 내의 모든 파일 검사
    posts_dir = '_posts'
    deleted_count = 0
    
    for filename in os.listdir(posts_dir):
        if filename.endswith('.markdown') or filename.endswith('.md'):
            # 파일명에서 날짜 추출 (YYYY-MM-DD 형식)
            date_match = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
            if date_match:
                post_date = datetime.strptime(date_match.group(1), '%Y-%m-%d').date()
                
                # 파일 날짜가 현재 날짜보다 미래인 경우 삭제
                if post_date > today:
                    file_path = os.path.join(posts_dir, filename)
                    os.remove(file_path)
                    deleted_count += 1
                    print(f'삭제됨: {filename}')
    
    print(f'\n총 {deleted_count}개의 미래 날짜 포스트가 삭제되었습니다.')

if __name__ == "__main__":
    delete_future_posts() 