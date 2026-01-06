# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class DescribeHotBigKeysResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeHotBigKeysResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The list of hot keys and large keys.
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
            temp_model = main_models.DescribeHotBigKeysResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeHotBigKeysResponseBodyData(DaraModel):
    def __init__(
        self,
        big_key_msg: str = None,
        big_keys: main_models.DescribeHotBigKeysResponseBodyDataBigKeys = None,
        high_traffic_key_msg: str = None,
        high_traffic_keys: main_models.DescribeHotBigKeysResponseBodyDataHighTrafficKeys = None,
        hot_key_msg: str = None,
        hot_keys: main_models.DescribeHotBigKeysResponseBodyDataHotKeys = None,
        large_key_msg: str = None,
        large_keys: main_models.DescribeHotBigKeysResponseBodyDataLargeKeys = None,
    ):
        # The reason why the large key failed to be queried.
        self.big_key_msg = big_key_msg
        # The list of large keys.
        self.big_keys = big_keys
        self.high_traffic_key_msg = high_traffic_key_msg
        self.high_traffic_keys = high_traffic_keys
        # The reason why the hot key failed to be queried.
        self.hot_key_msg = hot_key_msg
        # The list of hot keys.
        self.hot_keys = hot_keys
        self.large_key_msg = large_key_msg
        self.large_keys = large_keys

    def validate(self):
        if self.big_keys:
            self.big_keys.validate()
        if self.high_traffic_keys:
            self.high_traffic_keys.validate()
        if self.hot_keys:
            self.hot_keys.validate()
        if self.large_keys:
            self.large_keys.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.big_key_msg is not None:
            result['BigKeyMsg'] = self.big_key_msg

        if self.big_keys is not None:
            result['BigKeys'] = self.big_keys.to_map()

        if self.high_traffic_key_msg is not None:
            result['HighTrafficKeyMsg'] = self.high_traffic_key_msg

        if self.high_traffic_keys is not None:
            result['HighTrafficKeys'] = self.high_traffic_keys.to_map()

        if self.hot_key_msg is not None:
            result['HotKeyMsg'] = self.hot_key_msg

        if self.hot_keys is not None:
            result['HotKeys'] = self.hot_keys.to_map()

        if self.large_key_msg is not None:
            result['LargeKeyMsg'] = self.large_key_msg

        if self.large_keys is not None:
            result['LargeKeys'] = self.large_keys.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BigKeyMsg') is not None:
            self.big_key_msg = m.get('BigKeyMsg')

        if m.get('BigKeys') is not None:
            temp_model = main_models.DescribeHotBigKeysResponseBodyDataBigKeys()
            self.big_keys = temp_model.from_map(m.get('BigKeys'))

        if m.get('HighTrafficKeyMsg') is not None:
            self.high_traffic_key_msg = m.get('HighTrafficKeyMsg')

        if m.get('HighTrafficKeys') is not None:
            temp_model = main_models.DescribeHotBigKeysResponseBodyDataHighTrafficKeys()
            self.high_traffic_keys = temp_model.from_map(m.get('HighTrafficKeys'))

        if m.get('HotKeyMsg') is not None:
            self.hot_key_msg = m.get('HotKeyMsg')

        if m.get('HotKeys') is not None:
            temp_model = main_models.DescribeHotBigKeysResponseBodyDataHotKeys()
            self.hot_keys = temp_model.from_map(m.get('HotKeys'))

        if m.get('LargeKeyMsg') is not None:
            self.large_key_msg = m.get('LargeKeyMsg')

        if m.get('LargeKeys') is not None:
            temp_model = main_models.DescribeHotBigKeysResponseBodyDataLargeKeys()
            self.large_keys = temp_model.from_map(m.get('LargeKeys'))

        return self

class DescribeHotBigKeysResponseBodyDataLargeKeys(DaraModel):
    def __init__(
        self,
        large_key: List[main_models.DescribeHotBigKeysResponseBodyDataLargeKeysLargeKey] = None,
    ):
        self.large_key = large_key

    def validate(self):
        if self.large_key:
            for v1 in self.large_key:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LargeKey'] = []
        if self.large_key is not None:
            for k1 in self.large_key:
                result['LargeKey'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.large_key = []
        if m.get('LargeKey') is not None:
            for k1 in m.get('LargeKey'):
                temp_model = main_models.DescribeHotBigKeysResponseBodyDataLargeKeysLargeKey()
                self.large_key.append(temp_model.from_map(k1))

        return self

class DescribeHotBigKeysResponseBodyDataLargeKeysLargeKey(DaraModel):
    def __init__(
        self,
        data_size: str = None,
        db: str = None,
        key: str = None,
        key_type: str = None,
        node_id: str = None,
    ):
        self.data_size = data_size
        self.db = db
        self.key = key
        self.key_type = key_type
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.db is not None:
            result['Db'] = self.db

        if self.key is not None:
            result['Key'] = self.key

        if self.key_type is not None:
            result['KeyType'] = self.key_type

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('Db') is not None:
            self.db = m.get('Db')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self

class DescribeHotBigKeysResponseBodyDataHotKeys(DaraModel):
    def __init__(
        self,
        hot_key: List[main_models.DescribeHotBigKeysResponseBodyDataHotKeysHotKey] = None,
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
                temp_model = main_models.DescribeHotBigKeysResponseBodyDataHotKeysHotKey()
                self.hot_key.append(temp_model.from_map(k1))

        return self

class DescribeHotBigKeysResponseBodyDataHotKeysHotKey(DaraModel):
    def __init__(
        self,
        db: int = None,
        hot: str = None,
        key: str = None,
        key_type: str = None,
        lfu: int = None,
        node_id: str = None,
        size: int = None,
    ):
        # The database in which the key is stored.
        self.db = db
        # The frequency at which the key is accessed, which indicates the queries per second (QPS) of the key.
        self.hot = hot
        # The key.
        self.key = key
        # The type of the key.
        self.key_type = key_type
        # The statistical value that is calculated based on the least frequently used (LFU) caching algorithm.
        self.lfu = lfu
        # The ID of the data shard on the ApsaraDB for Redis instance.
        self.node_id = node_id
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

        if self.hot is not None:
            result['Hot'] = self.hot

        if self.key is not None:
            result['Key'] = self.key

        if self.key_type is not None:
            result['KeyType'] = self.key_type

        if self.lfu is not None:
            result['Lfu'] = self.lfu

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Db') is not None:
            self.db = m.get('Db')

        if m.get('Hot') is not None:
            self.hot = m.get('Hot')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')

        if m.get('Lfu') is not None:
            self.lfu = m.get('Lfu')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

class DescribeHotBigKeysResponseBodyDataHighTrafficKeys(DaraModel):
    def __init__(
        self,
        high_traffic_key: List[main_models.DescribeHotBigKeysResponseBodyDataHighTrafficKeysHighTrafficKey] = None,
    ):
        self.high_traffic_key = high_traffic_key

    def validate(self):
        if self.high_traffic_key:
            for v1 in self.high_traffic_key:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HighTrafficKey'] = []
        if self.high_traffic_key is not None:
            for k1 in self.high_traffic_key:
                result['HighTrafficKey'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.high_traffic_key = []
        if m.get('HighTrafficKey') is not None:
            for k1 in m.get('HighTrafficKey'):
                temp_model = main_models.DescribeHotBigKeysResponseBodyDataHighTrafficKeysHighTrafficKey()
                self.high_traffic_key.append(temp_model.from_map(k1))

        return self

class DescribeHotBigKeysResponseBodyDataHighTrafficKeysHighTrafficKey(DaraModel):
    def __init__(
        self,
        db: int = None,
        hot: str = None,
        key: str = None,
        key_type: str = None,
        node_id: str = None,
        size: int = None,
        in_bytes: int = None,
        out_bytes: int = None,
    ):
        self.db = db
        self.hot = hot
        self.key = key
        self.key_type = key_type
        self.node_id = node_id
        self.size = size
        self.in_bytes = in_bytes
        self.out_bytes = out_bytes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db is not None:
            result['Db'] = self.db

        if self.hot is not None:
            result['Hot'] = self.hot

        if self.key is not None:
            result['Key'] = self.key

        if self.key_type is not None:
            result['KeyType'] = self.key_type

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.size is not None:
            result['Size'] = self.size

        if self.in_bytes is not None:
            result['inBytes'] = self.in_bytes

        if self.out_bytes is not None:
            result['outBytes'] = self.out_bytes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Db') is not None:
            self.db = m.get('Db')

        if m.get('Hot') is not None:
            self.hot = m.get('Hot')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('inBytes') is not None:
            self.in_bytes = m.get('inBytes')

        if m.get('outBytes') is not None:
            self.out_bytes = m.get('outBytes')

        return self

class DescribeHotBigKeysResponseBodyDataBigKeys(DaraModel):
    def __init__(
        self,
        big_key: List[main_models.DescribeHotBigKeysResponseBodyDataBigKeysBigKey] = None,
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
                temp_model = main_models.DescribeHotBigKeysResponseBodyDataBigKeysBigKey()
                self.big_key.append(temp_model.from_map(k1))

        return self

class DescribeHotBigKeysResponseBodyDataBigKeysBigKey(DaraModel):
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

