# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class DescribeCacheAnalysisJobResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeCacheAnalysisJobResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The details of the cache analysis task.
        self.data = data
        # The message that is returned for the request.
        # 
        # >  If the request is successful, **Successful** is returned. If the request fails, an error message that contains information such as an error code is returned.
        self.message = message
        # The ID of the request.
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
            temp_model = main_models.DescribeCacheAnalysisJobResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeCacheAnalysisJobResponseBodyData(DaraModel):
    def __init__(
        self,
        big_keys: main_models.DescribeCacheAnalysisJobResponseBodyDataBigKeys = None,
        big_keys_of_num: main_models.DescribeCacheAnalysisJobResponseBodyDataBigKeysOfNum = None,
        expiry_keys_level_count: main_models.DescribeCacheAnalysisJobResponseBodyDataExpiryKeysLevelCount = None,
        instance_id: str = None,
        job_id: str = None,
        key_prefixes: main_models.DescribeCacheAnalysisJobResponseBodyDataKeyPrefixes = None,
        message: str = None,
        node_id: str = None,
        task_state: str = None,
        unex_big_keys_of_bytes: main_models.DescribeCacheAnalysisJobResponseBodyDataUnexBigKeysOfBytes = None,
        unex_big_keys_of_num: main_models.DescribeCacheAnalysisJobResponseBodyDataUnexBigKeysOfNum = None,
    ):
        # The details of the large keys. The returned large keys are sorted in descending order based on the number of bytes occupied by the keys.
        self.big_keys = big_keys
        # The details of the large keys. The returned large keys are sorted in descending order based on the number of keys.
        self.big_keys_of_num = big_keys_of_num
        # The statistics of the keys that have expired.
        self.expiry_keys_level_count = expiry_keys_level_count
        # The instance ID.
        self.instance_id = instance_id
        # The ID of the cache analysis task.
        self.job_id = job_id
        # The prefixes of the keys.
        self.key_prefixes = key_prefixes
        # The message that is returned for the request.
        # 
        # >  If the request is successful, **Successful** is returned. If the request fails, an error message that contains information such as an error code is returned.
        self.message = message
        # The ID of the data node on the instance.
        self.node_id = node_id
        # The state of the cache analysis task. Valid values:
        # 
        # *   **BACKUP**: The data is being backed up.
        # *   **ANALYZING**: The data is being analyzed.
        # *   **FINISHED**: The data is analyzed.
        # *   **FAILED**: An error occurred.
        self.task_state = task_state
        # The details of permanent keys. The returned keys are sorted in descending order based on the number of bytes occupied by the keys.
        self.unex_big_keys_of_bytes = unex_big_keys_of_bytes
        # The details of permanent keys. The returned keys are sorted in descending order based on the number of keys.
        self.unex_big_keys_of_num = unex_big_keys_of_num

    def validate(self):
        if self.big_keys:
            self.big_keys.validate()
        if self.big_keys_of_num:
            self.big_keys_of_num.validate()
        if self.expiry_keys_level_count:
            self.expiry_keys_level_count.validate()
        if self.key_prefixes:
            self.key_prefixes.validate()
        if self.unex_big_keys_of_bytes:
            self.unex_big_keys_of_bytes.validate()
        if self.unex_big_keys_of_num:
            self.unex_big_keys_of_num.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.big_keys is not None:
            result['BigKeys'] = self.big_keys.to_map()

        if self.big_keys_of_num is not None:
            result['BigKeysOfNum'] = self.big_keys_of_num.to_map()

        if self.expiry_keys_level_count is not None:
            result['ExpiryKeysLevelCount'] = self.expiry_keys_level_count.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.key_prefixes is not None:
            result['KeyPrefixes'] = self.key_prefixes.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.task_state is not None:
            result['TaskState'] = self.task_state

        if self.unex_big_keys_of_bytes is not None:
            result['UnexBigKeysOfBytes'] = self.unex_big_keys_of_bytes.to_map()

        if self.unex_big_keys_of_num is not None:
            result['UnexBigKeysOfNum'] = self.unex_big_keys_of_num.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BigKeys') is not None:
            temp_model = main_models.DescribeCacheAnalysisJobResponseBodyDataBigKeys()
            self.big_keys = temp_model.from_map(m.get('BigKeys'))

        if m.get('BigKeysOfNum') is not None:
            temp_model = main_models.DescribeCacheAnalysisJobResponseBodyDataBigKeysOfNum()
            self.big_keys_of_num = temp_model.from_map(m.get('BigKeysOfNum'))

        if m.get('ExpiryKeysLevelCount') is not None:
            temp_model = main_models.DescribeCacheAnalysisJobResponseBodyDataExpiryKeysLevelCount()
            self.expiry_keys_level_count = temp_model.from_map(m.get('ExpiryKeysLevelCount'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('KeyPrefixes') is not None:
            temp_model = main_models.DescribeCacheAnalysisJobResponseBodyDataKeyPrefixes()
            self.key_prefixes = temp_model.from_map(m.get('KeyPrefixes'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')

        if m.get('UnexBigKeysOfBytes') is not None:
            temp_model = main_models.DescribeCacheAnalysisJobResponseBodyDataUnexBigKeysOfBytes()
            self.unex_big_keys_of_bytes = temp_model.from_map(m.get('UnexBigKeysOfBytes'))

        if m.get('UnexBigKeysOfNum') is not None:
            temp_model = main_models.DescribeCacheAnalysisJobResponseBodyDataUnexBigKeysOfNum()
            self.unex_big_keys_of_num = temp_model.from_map(m.get('UnexBigKeysOfNum'))

        return self

class DescribeCacheAnalysisJobResponseBodyDataUnexBigKeysOfNum(DaraModel):
    def __init__(
        self,
        key_info: List[main_models.DescribeCacheAnalysisJobResponseBodyDataUnexBigKeysOfNumKeyInfo] = None,
    ):
        self.key_info = key_info

    def validate(self):
        if self.key_info:
            for v1 in self.key_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KeyInfo'] = []
        if self.key_info is not None:
            for k1 in self.key_info:
                result['KeyInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key_info = []
        if m.get('KeyInfo') is not None:
            for k1 in m.get('KeyInfo'):
                temp_model = main_models.DescribeCacheAnalysisJobResponseBodyDataUnexBigKeysOfNumKeyInfo()
                self.key_info.append(temp_model.from_map(k1))

        return self

class DescribeCacheAnalysisJobResponseBodyDataUnexBigKeysOfNumKeyInfo(DaraModel):
    def __init__(
        self,
        bytes: int = None,
        count: int = None,
        db: int = None,
        encoding: str = None,
        expiration_time_millis: int = None,
        key: str = None,
        node_id: str = None,
        type: str = None,
    ):
        # The number of bytes that are occupied by the key.
        self.bytes = bytes
        # The number of elements in the key.
        self.count = count
        # The database name.
        self.db = db
        # The data type of the key.
        self.encoding = encoding
        # The time when the key expires. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. A value of 0 indicates that the key never expires.
        self.expiration_time_millis = expiration_time_millis
        # The key name.
        self.key = key
        # The ID of the data node on the instance.
        self.node_id = node_id
        # The data type of the instance.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bytes is not None:
            result['Bytes'] = self.bytes

        if self.count is not None:
            result['Count'] = self.count

        if self.db is not None:
            result['Db'] = self.db

        if self.encoding is not None:
            result['Encoding'] = self.encoding

        if self.expiration_time_millis is not None:
            result['ExpirationTimeMillis'] = self.expiration_time_millis

        if self.key is not None:
            result['Key'] = self.key

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Db') is not None:
            self.db = m.get('Db')

        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')

        if m.get('ExpirationTimeMillis') is not None:
            self.expiration_time_millis = m.get('ExpirationTimeMillis')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeCacheAnalysisJobResponseBodyDataUnexBigKeysOfBytes(DaraModel):
    def __init__(
        self,
        key_info: List[main_models.DescribeCacheAnalysisJobResponseBodyDataUnexBigKeysOfBytesKeyInfo] = None,
    ):
        self.key_info = key_info

    def validate(self):
        if self.key_info:
            for v1 in self.key_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KeyInfo'] = []
        if self.key_info is not None:
            for k1 in self.key_info:
                result['KeyInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key_info = []
        if m.get('KeyInfo') is not None:
            for k1 in m.get('KeyInfo'):
                temp_model = main_models.DescribeCacheAnalysisJobResponseBodyDataUnexBigKeysOfBytesKeyInfo()
                self.key_info.append(temp_model.from_map(k1))

        return self

class DescribeCacheAnalysisJobResponseBodyDataUnexBigKeysOfBytesKeyInfo(DaraModel):
    def __init__(
        self,
        bytes: int = None,
        count: int = None,
        db: int = None,
        encoding: str = None,
        expiration_time_millis: int = None,
        key: str = None,
        node_id: str = None,
        type: str = None,
    ):
        # The number of bytes that are occupied by the key.
        self.bytes = bytes
        # The number of elements in the key.
        self.count = count
        # The database name.
        self.db = db
        # The data type of the key.
        self.encoding = encoding
        # The time when the key expires. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. A value of 0 indicates that the key never expires.
        self.expiration_time_millis = expiration_time_millis
        # The key name.
        self.key = key
        # The ID of the data node on the instance.
        self.node_id = node_id
        # The data type of the instance.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bytes is not None:
            result['Bytes'] = self.bytes

        if self.count is not None:
            result['Count'] = self.count

        if self.db is not None:
            result['Db'] = self.db

        if self.encoding is not None:
            result['Encoding'] = self.encoding

        if self.expiration_time_millis is not None:
            result['ExpirationTimeMillis'] = self.expiration_time_millis

        if self.key is not None:
            result['Key'] = self.key

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Db') is not None:
            self.db = m.get('Db')

        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')

        if m.get('ExpirationTimeMillis') is not None:
            self.expiration_time_millis = m.get('ExpirationTimeMillis')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeCacheAnalysisJobResponseBodyDataKeyPrefixes(DaraModel):
    def __init__(
        self,
        prefix: List[main_models.DescribeCacheAnalysisJobResponseBodyDataKeyPrefixesPrefix] = None,
    ):
        self.prefix = prefix

    def validate(self):
        if self.prefix:
            for v1 in self.prefix:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Prefix'] = []
        if self.prefix is not None:
            for k1 in self.prefix:
                result['Prefix'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.prefix = []
        if m.get('Prefix') is not None:
            for k1 in m.get('Prefix'):
                temp_model = main_models.DescribeCacheAnalysisJobResponseBodyDataKeyPrefixesPrefix()
                self.prefix.append(temp_model.from_map(k1))

        return self

class DescribeCacheAnalysisJobResponseBodyDataKeyPrefixesPrefix(DaraModel):
    def __init__(
        self,
        bytes: int = None,
        count: int = None,
        key_num: int = None,
        prefix: str = None,
        type: str = None,
    ):
        # The number of bytes that are occupied by the key.
        self.bytes = bytes
        # The number of elements in the key.
        self.count = count
        # The number of keys that contain the prefix.
        self.key_num = key_num
        # The prefix of the key.
        self.prefix = prefix
        # The data type of the instance.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bytes is not None:
            result['Bytes'] = self.bytes

        if self.count is not None:
            result['Count'] = self.count

        if self.key_num is not None:
            result['KeyNum'] = self.key_num

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('KeyNum') is not None:
            self.key_num = m.get('KeyNum')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeCacheAnalysisJobResponseBodyDataExpiryKeysLevelCount(DaraModel):
    def __init__(
        self,
        expiry_level: List[main_models.DescribeCacheAnalysisJobResponseBodyDataExpiryKeysLevelCountExpiryLevel] = None,
    ):
        self.expiry_level = expiry_level

    def validate(self):
        if self.expiry_level:
            for v1 in self.expiry_level:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ExpiryLevel'] = []
        if self.expiry_level is not None:
            for k1 in self.expiry_level:
                result['ExpiryLevel'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.expiry_level = []
        if m.get('ExpiryLevel') is not None:
            for k1 in m.get('ExpiryLevel'):
                temp_model = main_models.DescribeCacheAnalysisJobResponseBodyDataExpiryKeysLevelCountExpiryLevel()
                self.expiry_level.append(temp_model.from_map(k1))

        return self

class DescribeCacheAnalysisJobResponseBodyDataExpiryKeysLevelCountExpiryLevel(DaraModel):
    def __init__(
        self,
        analysis_ts: int = None,
        level: int = None,
        total_bytes: int = None,
        total_keys: int = None,
    ):
        # The time when the cache analysis task was complete. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.analysis_ts = analysis_ts
        # The expiration level. Valid values:
        # 
        # *   **0**: The key never expires.
        # *   **1**: The key has expired.
        # *   **2**: The key has expired for 0 to 1 hour.
        # *   **3**: The key has expired for 1 to 3 hours.
        # *   **4**: The key has expired for 3 to 12 hours.
        # *   **5**: The key has expired for 12 to 24 hours.
        # *   **6**: The key has expired for one to two days.
        # *   **7**: The key has expired for three to seven days.
        # *   **8**: The key has expired for more than seven days.
        self.level = level
        # The number of bytes occupied by the keys that have expired.
        self.total_bytes = total_bytes
        # The total number of the keys that have expired.
        self.total_keys = total_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_ts is not None:
            result['AnalysisTs'] = self.analysis_ts

        if self.level is not None:
            result['Level'] = self.level

        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes

        if self.total_keys is not None:
            result['TotalKeys'] = self.total_keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalysisTs') is not None:
            self.analysis_ts = m.get('AnalysisTs')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')

        if m.get('TotalKeys') is not None:
            self.total_keys = m.get('TotalKeys')

        return self

class DescribeCacheAnalysisJobResponseBodyDataBigKeysOfNum(DaraModel):
    def __init__(
        self,
        key_info: List[main_models.DescribeCacheAnalysisJobResponseBodyDataBigKeysOfNumKeyInfo] = None,
    ):
        self.key_info = key_info

    def validate(self):
        if self.key_info:
            for v1 in self.key_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KeyInfo'] = []
        if self.key_info is not None:
            for k1 in self.key_info:
                result['KeyInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key_info = []
        if m.get('KeyInfo') is not None:
            for k1 in m.get('KeyInfo'):
                temp_model = main_models.DescribeCacheAnalysisJobResponseBodyDataBigKeysOfNumKeyInfo()
                self.key_info.append(temp_model.from_map(k1))

        return self

class DescribeCacheAnalysisJobResponseBodyDataBigKeysOfNumKeyInfo(DaraModel):
    def __init__(
        self,
        bytes: int = None,
        count: int = None,
        db: int = None,
        encoding: str = None,
        expiration_time_millis: int = None,
        key: str = None,
        node_id: str = None,
        type: str = None,
    ):
        # The number of bytes that are occupied by the key.
        self.bytes = bytes
        # The number of elements in the key.
        self.count = count
        # The database name.
        self.db = db
        # The data type of the key.
        self.encoding = encoding
        # The time when the key expires. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. A value of 0 indicates that the key never expires.
        self.expiration_time_millis = expiration_time_millis
        # The key name.
        self.key = key
        # The ID of the data node on the instance.
        self.node_id = node_id
        # The data type of the instance.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bytes is not None:
            result['Bytes'] = self.bytes

        if self.count is not None:
            result['Count'] = self.count

        if self.db is not None:
            result['Db'] = self.db

        if self.encoding is not None:
            result['Encoding'] = self.encoding

        if self.expiration_time_millis is not None:
            result['ExpirationTimeMillis'] = self.expiration_time_millis

        if self.key is not None:
            result['Key'] = self.key

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Db') is not None:
            self.db = m.get('Db')

        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')

        if m.get('ExpirationTimeMillis') is not None:
            self.expiration_time_millis = m.get('ExpirationTimeMillis')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeCacheAnalysisJobResponseBodyDataBigKeys(DaraModel):
    def __init__(
        self,
        key_info: List[main_models.DescribeCacheAnalysisJobResponseBodyDataBigKeysKeyInfo] = None,
    ):
        self.key_info = key_info

    def validate(self):
        if self.key_info:
            for v1 in self.key_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KeyInfo'] = []
        if self.key_info is not None:
            for k1 in self.key_info:
                result['KeyInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key_info = []
        if m.get('KeyInfo') is not None:
            for k1 in m.get('KeyInfo'):
                temp_model = main_models.DescribeCacheAnalysisJobResponseBodyDataBigKeysKeyInfo()
                self.key_info.append(temp_model.from_map(k1))

        return self

class DescribeCacheAnalysisJobResponseBodyDataBigKeysKeyInfo(DaraModel):
    def __init__(
        self,
        bytes: int = None,
        count: int = None,
        db: int = None,
        encoding: str = None,
        expiration_time_millis: int = None,
        key: str = None,
        node_id: str = None,
        type: str = None,
    ):
        # The number of bytes that are occupied by the key.
        self.bytes = bytes
        # The number of elements in the key.
        self.count = count
        # The database name.
        self.db = db
        # The data type of the key.
        self.encoding = encoding
        # The time when the key expires. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. A value of 0 indicates that the key never expires.
        self.expiration_time_millis = expiration_time_millis
        # The key name.
        self.key = key
        # The ID of the data node on the instance.
        self.node_id = node_id
        # The data type of the instance.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bytes is not None:
            result['Bytes'] = self.bytes

        if self.count is not None:
            result['Count'] = self.count

        if self.db is not None:
            result['Db'] = self.db

        if self.encoding is not None:
            result['Encoding'] = self.encoding

        if self.expiration_time_millis is not None:
            result['ExpirationTimeMillis'] = self.expiration_time_millis

        if self.key is not None:
            result['Key'] = self.key

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Db') is not None:
            self.db = m.get('Db')

        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')

        if m.get('ExpirationTimeMillis') is not None:
            self.expiration_time_millis = m.get('ExpirationTimeMillis')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

