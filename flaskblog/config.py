import os




class Config():
    # SECRET_KEY  = os.environ.get('SECRET_KEY')
    SECRET_KEY='0e381ea573250fa9bcc51a7a364878de'
    # SQLALCHEMY_DATABASE_URI  = 'sqlite:///site.db'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Omni3255??!!@localhost/ourdb'
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:dYkbaCUBPgwYGdlvxVakhDdtzXWjVBLN@autorack.proxy.rlwy.net:37912/railway"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://omniblogs:Extra111??!!@omniblogs.mysql.pythonanywhere-services.com/omniblogs$omniblogs"


    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS  = True
    # MAIL_USERNAME = os.environ.get('EMAIL_USER')
    # MAIL_PASSWORD  = os.environ.get('EMAIL_PASS')
    MAIL_PASSWORD= 'xvdkbixwoalcfdoo'
    MAIL_USERNAME='noreply325nr@gmail.com'
