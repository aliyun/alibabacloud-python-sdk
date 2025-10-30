# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class GetSupabaseProjectApiKeysResponseBody(DaraModel):
    def __init__(
        self,
        api_keys: List[main_models.GetSupabaseProjectApiKeysResponseBodyApiKeys] = None,
        request_id: str = None,
    ):
        self.api_keys = api_keys
        self.request_id = request_id

    def validate(self):
        if self.api_keys:
            for v1 in self.api_keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiKeys'] = []
        if self.api_keys is not None:
            for k1 in self.api_keys:
                result['ApiKeys'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_keys = []
        if m.get('ApiKeys') is not None:
            for k1 in m.get('ApiKeys'):
                temp_model = main_models.GetSupabaseProjectApiKeysResponseBodyApiKeys()
                self.api_keys.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetSupabaseProjectApiKeysResponseBodyApiKeys(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        name: str = None,
    ):
        self.api_key = api_key
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

