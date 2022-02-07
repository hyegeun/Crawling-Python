# [Python] Crawling

- 사용 환경: Windows 10 / Chrome / python 3.8 / Prompt에서 실행 

- crawling 하고 싶은 data가 많은 경우 csv파일에 정리하여 한번에 crawling 할 수 있도록 설계

- crawling 중간에 멈춤 현상 Timeout으로 해결

------

#### **1. csv파일 형식**

- Folder_name : crawling한 이미지를 저장하는 폴더 
- Search : 구글에 검색할 단어 
- example: cat, dog, bird를 각각 crawling 하고싶은 경우 아래와 같이 csv파일 작성

| Folder_name | Search |
| ----------- | ------ |
| Cat         | cat    |
| Dog         | dog    |
| Bird        | bird   |

------

#### **2. Crawling Driver**

[Chrome Driver Download](https://chromedriver.chromium.org/downloads)

-> crawling.py Line 32

```python
options = webdriver.ChromeOptions()
```

사용자 Chrome 버전에 맞는 파일 다운로드 후 경로 설정

------

#### 3. Start Crawling

```python
python main.py --input [csv file] --name [result folder]
```

- --input : crawling할 csv파일 path
- --name : crawling 결과를 저장할 폴더

------

#### 4. Etc.

crawling.py Line 30

```python
limit_time = 10
```

- crawling 중 멈춤을 방지하기 위한 Timeout
- 한 이미지에 10초가 지나면 이미지를 다운받고 있던 Thread 종료시킨 후 다음 이미지로 넘어감

------

#### 5. Reference

- Thread : [Link Click](https://web.archive.org/web/20130503082442/http://mail.python.org/pipermail/python-list/2004-May/281943.html)