DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'book',  # 데이터베이스 이름
        'USER': 'root',  # 유저 이름
        'PASSWORD': '##tkakrnl12',  # 패스워드
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'  # 아래와 같은 옵션을 줘야 각 모델의 table명을 동적으로 지정가능하다
        }
    }
}

SECRET_KEY = {
    'secret': '=ae)zm2$x8px8b*yg_nrx#_rz6nt*1d!^axcpa*n&@)8ldw-^=',
}

ALGORITHM = 'HS256'

