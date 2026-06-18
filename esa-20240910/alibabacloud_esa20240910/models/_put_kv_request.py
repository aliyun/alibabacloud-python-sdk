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
        # Indicates whether the Value parameter uses Base64 encoding. Set this to true when storing a binary value. If this parameter is true, Value must be a valid Base64-encoded string.
        self.base_64 = base_64
        # The expiration time for the key-value pair, as a Unix timestamp in seconds. This value cannot be earlier than the current time. If you specify both Expiration and ExpirationTtl, ExpirationTtl takes precedence.
        self.expiration = expiration
        # The time-to-live (TTL) for the key-value pair, in seconds. If you specify both Expiration and ExpirationTtl, ExpirationTtl takes precedence.
        self.expiration_ttl = expiration_ttl
        # The key can be up to 512 bytes long and cannot contain spaces or forward slashes (/).
        # 
        # This parameter is required.
        self.key = key
        # The name of the namespace. You specify this name when you call the [CreateKvNamespace](https://help.aliyun.com/document_detail/2850317.html) operation.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The value to associate with the key. The maximum size is 2 MB (2,000,000 bytes). For values that exceed this limit, use the [PutKvWithHighCapacity](https://help.aliyun.com/document_detail/2850486.html) operation.
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

