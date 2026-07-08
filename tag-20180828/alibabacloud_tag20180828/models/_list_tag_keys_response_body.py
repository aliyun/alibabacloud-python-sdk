# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tag20180828 import models as main_models
from darabonba.model import DaraModel

class ListTagKeysResponseBody(DaraModel):
    def __init__(
        self,
        keys: main_models.ListTagKeysResponseBodyKeys = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.keys = keys
        # Indicates whether the next query is required. The value of this parameter may be empty.
        # 
        # - If the value of this parameter is empty (`"NextToken": ""`), all results are returned, and the next query is not required.
        # 
        # - If the value of this parameter is not empty, the next query is required, and the value is the token used to start the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.keys:
            self.keys.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keys is not None:
            result['Keys'] = self.keys.to_map()

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keys') is not None:
            temp_model = main_models.ListTagKeysResponseBodyKeys()
            self.keys = temp_model.from_map(m.get('Keys'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListTagKeysResponseBodyKeys(DaraModel):
    def __init__(
        self,
        key: List[main_models.ListTagKeysResponseBodyKeysKey] = None,
    ):
        self.key = key

    def validate(self):
        if self.key:
            for v1 in self.key:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Key'] = []
        if self.key is not None:
            for k1 in self.key:
                result['Key'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key = []
        if m.get('Key') is not None:
            for k1 in m.get('Key'):
                temp_model = main_models.ListTagKeysResponseBodyKeysKey()
                self.key.append(temp_model.from_map(k1))

        return self

class ListTagKeysResponseBodyKeysKey(DaraModel):
    def __init__(
        self,
        category: str = None,
        description: str = None,
        key: str = None,
    ):
        self.category = category
        self.description = description
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.description is not None:
            result['Description'] = self.description

        if self.key is not None:
            result['Key'] = self.key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        return self

