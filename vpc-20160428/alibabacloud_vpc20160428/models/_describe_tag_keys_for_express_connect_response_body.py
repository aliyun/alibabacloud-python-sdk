# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeTagKeysForExpressConnectResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_keys: main_models.DescribeTagKeysForExpressConnectResponseBodyTagKeys = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value is returned for **NextToken**, the value can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The tag keys.
        self.tag_keys = tag_keys

    def validate(self):
        if self.tag_keys:
            self.tag_keys.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TagKeys') is not None:
            temp_model = main_models.DescribeTagKeysForExpressConnectResponseBodyTagKeys()
            self.tag_keys = temp_model.from_map(m.get('TagKeys'))

        return self

class DescribeTagKeysForExpressConnectResponseBodyTagKeys(DaraModel):
    def __init__(
        self,
        tag_key: List[main_models.DescribeTagKeysForExpressConnectResponseBodyTagKeysTagKey] = None,
    ):
        self.tag_key = tag_key

    def validate(self):
        if self.tag_key:
            for v1 in self.tag_key:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TagKey'] = []
        if self.tag_key is not None:
            for k1 in self.tag_key:
                result['TagKey'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_key = []
        if m.get('TagKey') is not None:
            for k1 in m.get('TagKey'):
                temp_model = main_models.DescribeTagKeysForExpressConnectResponseBodyTagKeysTagKey()
                self.tag_key.append(temp_model.from_map(k1))

        return self

class DescribeTagKeysForExpressConnectResponseBodyTagKeysTagKey(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        type: str = None,
    ):
        # The key of the tag.
        self.tag_key = tag_key
        # The type of the resource. The value is set to **PHYSICALCONNECTION**, which indicates an Express Connect circuit.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

