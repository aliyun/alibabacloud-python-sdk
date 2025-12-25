# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PutKvRequest(DaraModel):
    def __init__(
        self,
        base_64: bool = None,
        expiration: int = None,
        expiration_ttl: int = None,
        key: str = None,
        namespace: str = None,
        value: str = None,
    ):
        # Specifies whether the content of the key is Base64-encoded. Set this parameter to true if you want to store the key content in binary format. When this parameter is set to true, the Value parameter must be Base64-encoded.
        self.base_64 = base_64
        # The time when the key-value pair expires, which cannot be earlier than the current time. The value is a timestamp in seconds. If you specify both Expiration and ExpirationTtl, only ExpirationTtl takes effect.
        self.expiration = expiration
        # The relative expiration time. Unit: seconds. If you specify both Expiration and ExpirationTtl, only ExpirationTtl takes effect.
        self.expiration_ttl = expiration_ttl
        # The key name. The name can be up to 512 characters in length and cannot contain spaces or backslashes (\\\\).
        # 
        # This parameter is required.
        self.key = key
        # The name of the namespace that you specify when you call the [CreateKvNamespace](https://help.aliyun.com/document_detail/2850317.html) operation.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The content of the key, which can be up to 2 MB (2 × 1000 × 1000). If the content is larger than 2 MB, call [PutKvWithHighCapacity](https://help.aliyun.com/document_detail/2850486.html).
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_64 is not None:
            result['Base64'] = self.base_64

        if self.expiration is not None:
            result['Expiration'] = self.expiration

        if self.expiration_ttl is not None:
            result['ExpirationTtl'] = self.expiration_ttl

        if self.key is not None:
            result['Key'] = self.key

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Base64') is not None:
            self.base_64 = m.get('Base64')

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

        if m.get('ExpirationTtl') is not None:
            self.expiration_ttl = m.get('ExpirationTtl')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

