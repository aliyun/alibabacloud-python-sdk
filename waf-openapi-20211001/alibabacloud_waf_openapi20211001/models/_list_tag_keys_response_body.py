# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class ListTagKeysResponseBody(DaraModel):
    def __init__(
        self,
        keys: List[main_models.ListTagKeysResponseBodyKeys] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The keys and types of the tags.
        self.keys = keys
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.keys:
            for v1 in self.keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Keys'] = []
        if self.keys is not None:
            for k1 in self.keys:
                result['Keys'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.keys = []
        if m.get('Keys') is not None:
            for k1 in m.get('Keys'):
                temp_model = main_models.ListTagKeysResponseBodyKeys()
                self.keys.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListTagKeysResponseBodyKeys(DaraModel):
    def __init__(
        self,
        category: str = None,
        key: str = None,
    ):
        # The type of the tag. Valid values:
        # 
        # *   custom
        # *   system
        self.category = category
        # The key of the tag.
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

        if self.key is not None:
            result['Key'] = self.key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        return self

