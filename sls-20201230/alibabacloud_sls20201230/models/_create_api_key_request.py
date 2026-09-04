# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateApiKeyRequest(DaraModel):
    def __init__(
        self,
        allowed_stores: List[str] = None,
        api_key_name: str = None,
        description: str = None,
    ):
        self.allowed_stores = allowed_stores
        self.api_key_name = api_key_name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_stores is not None:
            result['allowedStores'] = self.allowed_stores

        if self.api_key_name is not None:
            result['apiKeyName'] = self.api_key_name

        if self.description is not None:
            result['description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowedStores') is not None:
            self.allowed_stores = m.get('allowedStores')

        if m.get('apiKeyName') is not None:
            self.api_key_name = m.get('apiKeyName')

        if m.get('description') is not None:
            self.description = m.get('description')

        return self

