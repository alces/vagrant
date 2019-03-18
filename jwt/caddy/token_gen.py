#!/usr/bin/env python

# Generate token for JWT
# required pyjwt to be installed by pip

import jwt
import time

jwt_days = 365
jwt_secret = 'verysecret'
jwt_payload = {
    'iss': 'griddynamics.net',
    'user': 'admin'
}

jwt_payload.update({'exp': int(time.time()) + jwt_days * 24 * 3600})
print jwt.encode(jwt_payload, jwt_secret, algorithm = 'HS256')

