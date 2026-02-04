# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PutDcdnKvRequest(DaraModel):
    def __init__(
        self,
        expiration: int = None,
        expiration_ttl: int = None,
        key: str = None,
        namespace: str = None,
        value: str = None,
    ):
        # The time when the key expires.Example: "1690081381".
        self.expiration = expiration
        # The time when the key expires.Example: "3600".
        self.expiration_ttl = expiration_ttl
        # The key. The key can be up to 512 characters in length, and cannot contain spaces.
        # 
        # This parameter is required.
        self.key = key
        # The name of the namespace.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The value of the key. The maximum size is 2 MB (2 x 1000 x 1000 bytes).
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

