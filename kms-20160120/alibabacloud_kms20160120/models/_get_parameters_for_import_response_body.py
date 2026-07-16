# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetParametersForImportResponseBody(DaraModel):
    def __init__(
        self,
        import_token: str = None,
        key_id: str = None,
        public_key: str = None,
        request_id: str = None,
        token_expire_time: str = None,
    ):
        # The token that is used to import key material.
        # 
        # The token is valid for 24 hours. The value of this parameter is required when you call the [ImportKeyMaterial](https://help.aliyun.com/document_detail/68622.html) operation.
        self.import_token = import_token
        # The globally unique ID of the CMK.
        # 
        # The value of this parameter is required when you call the [ImportKeyMaterial](https://help.aliyun.com/document_detail/68622.html) operation.
        self.key_id = key_id
        # The public key that is used to encrypt key material.
        # 
        # The public key is Base64-encoded.
        self.public_key = public_key
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The time when the token expires.
        self.token_expire_time = token_expire_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.import_token is not None:
            result['ImportToken'] = self.import_token

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.public_key is not None:
            result['PublicKey'] = self.public_key

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.token_expire_time is not None:
            result['TokenExpireTime'] = self.token_expire_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportToken') is not None:
            self.import_token = m.get('ImportToken')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TokenExpireTime') is not None:
            self.token_expire_time = m.get('TokenExpireTime')

        return self

