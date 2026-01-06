# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class DescribeHotKeysResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeHotKeysResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The details of the hot keys.
        self.data = data
        # The returned message.
        # 
        # >  If the request was successful, Successful is returned. If the request failed, an error message such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeHotKeysResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeHotKeysResponseBodyData(DaraModel):
    def __init__(
        self,
        hot_key: List[main_models.DescribeHotKeysResponseBodyDataHotKey] = None,
    ):
        self.hot_key = hot_key

    def validate(self):
        if self.hot_key:
            for v1 in self.hot_key:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HotKey'] = []
        if self.hot_key is not None:
            for k1 in self.hot_key:
                result['HotKey'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hot_key = []
        if m.get('HotKey') is not None:
            for k1 in m.get('HotKey'):
                temp_model = main_models.DescribeHotKeysResponseBodyDataHotKey()
                self.hot_key.append(temp_model.from_map(k1))

        return self

class DescribeHotKeysResponseBodyDataHotKey(DaraModel):
    def __init__(
        self,
        category: str = None,
        db: int = None,
        hot: str = None,
        in_bytes: int = None,
        key: str = None,
        key_type: str = None,
        node_id: str = None,
        out_bytes: int = None,
        size: int = None,
    ):
        self.category = category
        # The database in which the key is stored.
        self.db = db
        # The frequency at which the key is accessed, which indicates the queries per second (QPS) of the key.
        self.hot = hot
        self.in_bytes = in_bytes
        # The name of the key.
        self.key = key
        # The type of the key.
        self.key_type = key_type
        self.node_id = node_id
        self.out_bytes = out_bytes
        # The number of elements in the key.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.db is not None:
            result['Db'] = self.db

        if self.hot is not None:
            result['Hot'] = self.hot

        if self.in_bytes is not None:
            result['InBytes'] = self.in_bytes

        if self.key is not None:
            result['Key'] = self.key

        if self.key_type is not None:
            result['KeyType'] = self.key_type

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.out_bytes is not None:
            result['OutBytes'] = self.out_bytes

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Db') is not None:
            self.db = m.get('Db')

        if m.get('Hot') is not None:
            self.hot = m.get('Hot')

        if m.get('InBytes') is not None:
            self.in_bytes = m.get('InBytes')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OutBytes') is not None:
            self.out_bytes = m.get('OutBytes')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

