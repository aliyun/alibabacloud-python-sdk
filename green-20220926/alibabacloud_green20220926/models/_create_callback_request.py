# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCallbackRequest(DaraModel):
    def __init__(
        self,
        crypt_type: str = None,
        name: str = None,
        region_id: str = None,
        scope: str = None,
        url: str = None,
    ):
        # Encryption algorithm.
        self.crypt_type = crypt_type
        # Plan name.
        self.name = name
        # Region ID.
        self.region_id = region_id
        # Review result.
        self.scope = scope
        # Callback URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.crypt_type is not None:
            result['CryptType'] = self.crypt_type

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CryptType') is not None:
            self.crypt_type = m.get('CryptType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

