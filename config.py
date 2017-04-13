import os
basedir = os.path.abspath(os.path.dirname(__file__))

# BASIC APP CONFIG
WTF_CSRF_ENABLED = os.getenv('CSRF_ENABLED', 'yes') == 'yes'
SECRET_KEY = os.getenv('SECRET_KEY', 'secret')
BIND_ADDRESS = os.getenv('BIND_ADDRESS', '0.0.0.0')
PORT = os.getenv('PORT', 9393)
LOGIN_TITLE = os.getenv('LOGIN_TITLE', 'PDNS')

# TIMEOUT - for large zones
TIMEOUT = os.getenv('TIMEOUT', 10)

# LOG CONFIG
LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
LOG_FILE = ''

# Upload
UPLOAD_DIR = os.path.join(basedir, 'upload')

# DATABASE CONFIG
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('DATABASE_TRACK_MODIFICATIONS', 'yes') == 'yes'

# LDAP CONFIG
LDAP_TYPE = os.getenv('LDAP_TYPE', 'ldap')
LDAP_URI = os.getenv('LDAP_URI', 'ldaps://your-ldap-server:636')
LDAP_USERNAME = os.getenv('LDAP_USERNAME', 'cn=dnsuser,ou=users,ou=services,dc=duykhanh,dc=me')
LDAP_PASSWORD = os.getenv('LDAP_PASSWORD', 'dnsuser')
LDAP_SEARCH_BASE = os.getenv('LDAP_SEARCH_BASE', 'ou=System Admins,ou=People,dc=duykhanh,dc=me')
# Additional options only if LDAP_TYPE=ldap
LDAP_USERNAMEFIELD = os.getenv('LDAP_USERNAMEFIELD', 'uid')
LDAP_FILTER = os.getenv('LDAP_FILTER', '(objectClass=inetorgperson)')

## AD CONFIG
LDAP_TYPE = os.getenv('LDAP_TYPE', 'ad')
LDAP_URI = os.getenv('LDAP_URI', 'ldaps://your-ad-server:636')
LDAP_USERNAME = os.getenv('LDAP_USERNAME', 'cn=dnsuser,ou=Users,dc=domain,dc=local')
LDAP_PASSWORD = os.getenv('LDAP_PASSWORD', 'dnsuser')
LDAP_SEARCH_BASE = os.getenv('LDAP_SEARCH_BASE', 'dc=domain,dc=local')
# You may prefer 'userPrincipalName' instead
LDAP_USERNAMEFIELD = os.getenv('LDAP_USERNAMEFIELD', 'sAMAccountName')
# AD Group that you would like to have accesss to web app
LDAP_FILTER = os.getenv('LDAP_FILTER', 'memberof=cn=DNS_users,ou=Groups,dc=domain,dc=local')

# Github Oauth
GITHUB_OAUTH_ENABLE = os.getenv('GITHUB_OAUTH_ENABLE', 'no') == 'yes'
GITHUB_OAUTH_KEY = os.getenv('GITHUB_OAUTH_KEY')
GITHUB_OAUTH_SECRET = os.getenv('GITHUB_OAUTH_SECRET')
GITHUB_OAUTH_SCOPE = os.getenv('GITHUB_OAUTH_SCOPE', 'email')
GITHUB_OAUTH_URL = os.getenv('GITHUB_OAUTH_URL', 'https://github.com/api/v3/')
GITHUB_OAUTH_TOKEN = os.getenv('GITHUB_OAUTH_TOKEN', 'https://github.com/oauth/token')
GITHUB_OAUTH_AUTHORIZE = os.getenv('GITHUB_OAUTH_AUTHORIZE', 'https://github.com/oauth/authorize')

#Default Auth
BASIC_ENABLED = os.getenv('BASIC_ENABLED', 'yes') == 'yes'
SIGNUP_ENABLED = os.getenv('SIGNUP_ENABLED', 'yes') == 'yes'

# POWERDNS CONFIG
PDNS_STATS_URL = os.getenv('PDNS_STATS_URL')
PDNS_API_KEY = os.getenv('PDNS_API_KEY', '')
PDNS_VERSION = os.getenv('PDNS_VERSION', '4.0.1')

# RECORDS ALLOWED TO EDIT
RECORDS_ALLOW_EDIT = os.getenv('RECORDS_ALLOW_EDIT', 'A,AAAA,CNAME,PTR,MX,TXT,NS').split(',')

# EXPERIMENTAL FEATURES
PRETTY_IPV6_PTR = False
