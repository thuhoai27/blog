import os
import shutil
import sys

def remove_git_directory():
    """
    현재 디렉토리에서 .git 폴더를 찾아 삭제합니다.
    """
    current_dir = os.getcwd()
    git_dir = os.path.join(current_dir, '.git')
    
    try:
        if os.path.exists(git_dir):
            # .git 디렉토리가 있으면 삭제
            shutil.rmtree(git_dir)
            print(f"✅ Git 저장소가 성공적으로 제거되었습니다.")
            print(f"   제거된 경로: {git_dir}")
        else:
            print("❌ .git 디렉토리를 찾을 수 없습니다.")
            print("   이 디렉토리는 Git 저장소가 아닙니다.")
    except Exception as e:
        print(f"❌ 오류가 발생했습니다: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    # 사용자 확인
    response = input("⚠️ 정말로 Git 저장소를 제거하시겠습니까? (y/n): ")
    
    if response.lower() == 'y':
        remove_git_directory()
    else:
        print("작업이 취소되었습니다.") 