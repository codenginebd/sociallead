__author__ = 'Codengine'

app_key = '75zsaemfpnjp6v'
app_secret = 'S4u1DCShnHk4se4f'

scope_params = 'r_network'
state = 'STATE'
redirect_uri = 'http://codenginebd.appspot.com'

login_email = 'codenginebd@gmail.com'
login_password = 'lapsso065lapsso065'

authorization_url = 'https://www.linkedin.com/uas/oauth2/authorization?response_type=code&client_id=%s&scope=%s&state=%s&redirect_uri=%s' % (app_key,scope_params,state,redirect_uri)
access_token_url = 'https://www.linkedin.com/uas/oauth2/accessToken?grant_type=authorization_code&code=__CODE__&redirect_uri=%s&client_id=%s&client_secret=%s' % (redirect_uri,app_key,app_secret)
people_search_url = 'https://api.linkedin.com/v1/people-search?company-name=__COMPANY_NAME__&oauth2_access_token=__OAUTH2_ACCESS_TOKEN_URL__'

