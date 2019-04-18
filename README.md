# nx ny 좌표 검색 REST서버

# client.py
python3 client.py PORT_NUMBER (2|3) VALUE

2: VALUE(city level name), 3: VALUE(Address1)

 ex> python3 server.py 50001 2 강북구
 
     python3 server.py 50001 3 수유제3동

# server.py (port 50001)

python3 server.py

# test

$ python3 client.py 50001 3 수유제3동

{'result': 'ok', 'si': '서울특별시', 'gu': '강북구', 'nx': 61, 'ny': 128}

$ python3 client.py 50001 2 강북구

{'result': 'ok', 'si': '서울특별시', 'gu': '강북구', 'nx': 61, 'ny': 128}
