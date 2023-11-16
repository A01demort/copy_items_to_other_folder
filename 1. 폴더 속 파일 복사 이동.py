
import os
import shutil

# EX) out-0000001부터 out-0000154가 들어있는 폴더 경로
# EX) path to the folder containing out-0000001 through out-0000154
src_folder_prefix = r'C:\A01demort\out-'
dst_folder = r'C:\Magic'


# 폴더 속에 있는 파일만 복사하는 코드입니다.
# Code to copy only the files in a folder.

# Out-00000x 끝 숫자는 range의 숫자만 바꿔주면 됩니다.
#예를 들어 1부터 150까지면 1,150

# The ending number just needs to be changed in the range.
for i in range(1, 400):
    src_folder = f'{src_folder_prefix}{i:07d}'
    try:
        if os.path.exists(src_folder):
            for file_name in os.listdir(src_folder):
                full_file_name = os.path.join(src_folder, file_name)
                if os.path.isfile(full_file_name):
                    shutil.copy(full_file_name, os.path.join(dst_folder, os.path.basename(full_file_name)))
                else:
                    #No folder -> Pass
                    print(f'{src_folder} 폴더가 없음. Pass합니다.')


    except Exception as e:
        #Error occured
        print(f'{src_folder} 폴더에서 문제가 발생했습니다: {e}')
    
#Done    
print("작업 끝")


# Subscribe Youtube Channel
# https://www.youtube.com/@A01demort