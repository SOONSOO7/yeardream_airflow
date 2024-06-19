import requests
# client_id, authorize_code 노출 주의, 실제 값은 임시로만 넣고 Git에 올라가지 않도록 유의

client_id = '5d894dfa54039f12a9290e13080f9307'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'p58gAe7GNiHoohEKwmGr6__1TBJr_MxoQlhszwozZ9om_WcwixvniwAAAAQKPXTaAAABkC3-VTLMISgqRbFCUQ'


token_url = 'https://kauth.kakao.com/oauth/token'
data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'code': authorize_code,
    }

response = requests.post(token_url, data=data)
tokens = response.json()
print(tokens)