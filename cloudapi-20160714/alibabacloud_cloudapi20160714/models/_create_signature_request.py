# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSignatureRequest(DaraModel):
    def __init__(
        self,
        security_token: str = None,
        signature_key: str = None,
        signature_name: str = None,
        signature_secret: str = None,
    ):
        # The security token included in the WebSocket request header. The system uses this token to authenticate the request.
        self.security_token = security_token
        # The Key value of the key. The value must be 6 to 20 characters in length and can contain letters, digits, and underscores (_). It must start with a letter.
        # 
        # This parameter is required.
        self.signature_key = signature_key
        # The displayed name of the key. The name must be 4 to 50 characters in length and can contain letters, digits, and underscores (_). It must start with a letter.
        # 
        # This parameter is required.
        self.signature_name = signature_name
        # The Secret value of the key. The value must be 6 to 30 characters in length and can contain letters, digits, and special characters. Special characters include underscores (_), at signs (@), number signs (#), exclamation points (!), and asterisks (\\*). The value must start with a letter.
        # 
        # This parameter is required.
        self.signature_secret = signature_secret

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.signature_key is not None:
            result['SignatureKey'] = self.signature_key

        if self.signature_name is not None:
            result['SignatureName'] = self.signature_name

        if self.signature_secret is not None:
            result['SignatureSecret'] = self.signature_secret

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SignatureKey') is not None:
            self.signature_key = m.get('SignatureKey')

        if m.get('SignatureName') is not None:
            self.signature_name = m.get('SignatureName')

        if m.get('SignatureSecret') is not None:
            self.signature_secret = m.get('SignatureSecret')

        return self

