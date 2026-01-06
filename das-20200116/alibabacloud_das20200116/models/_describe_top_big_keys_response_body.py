# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class DescribeTopBigKeysResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeTopBigKeysResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The detailed information about the large keys.
        # 
        # > This parameter is left empty If no large keys exist within the specified time range.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
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
            temp_model = main_models.DescribeTopBigKeysResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeTopBigKeysResponseBodyData(DaraModel):
    def __init__(
        self,
        big_key: List[main_models.DescribeTopBigKeysResponseBodyDataBigKey] = None,
    ):
        self.big_key = big_key

    def validate(self):
        if self.big_key:
            for v1 in self.big_key:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BigKey'] = []
        if self.big_key is not None:
            for k1 in self.big_key:
                result['BigKey'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.big_key = []
        if m.get('BigKey') is not None:
            for k1 in m.get('BigKey'):
                temp_model = main_models.DescribeTopBigKeysResponseBodyDataBigKey()
                self.big_key.append(temp_model.from_map(k1))

        return self

class DescribeTopBigKeysResponseBodyDataBigKey(DaraModel):
    def __init__(
        self,
        db: int = None,
        key: str = None,
        key_type: str = None,
        node_id: str = None,
        size: int = None,
    ):
        # The database in which the key is stored.
        self.db = db
        # The key.
        self.key = key
        # The type of the key.
        self.key_type = key_type
        # The ID of the data shard on the ApsaraDB for Redis instance.
        self.node_id = node_id
        # The number of elements in the key.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db is not None:
            result['Db'] = self.db

        if self.key is not None:
            result['Key'] = self.key

        if self.key_type is not None:
            result['KeyType'] = self.key_type

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Db') is not None:
            self.db = m.get('Db')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

