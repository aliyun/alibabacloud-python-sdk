# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class CreateCacheAnalysisJobResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateCacheAnalysisJobResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The detailed information.
        self.data = data
        # The returned message.
        # 
        # >  If the request was successful, **Successful** is returned. If the request failed, an error message such as an error code is returned.
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
            temp_model = main_models.CreateCacheAnalysisJobResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateCacheAnalysisJobResponseBodyData(DaraModel):
    def __init__(
        self,
        big_keys: main_models.CreateCacheAnalysisJobResponseBodyDataBigKeys = None,
        instance_id: str = None,
        job_id: str = None,
        message: str = None,
        node_id: str = None,
        task_state: str = None,
    ):
        # The number of elements in the key.
        self.big_keys = big_keys
        # The instance ID.
        self.instance_id = instance_id
        # The ID of the cache analysis task.
        # 
        # >  This parameter can be used to query a specific cache analysis task. When you call the CreateCacheAnalysisJob operation, it takes some time to create a cache analysis task. As a result, the analysis results cannot be immediately returned. You can call the [DescribeCacheAnalysisJob](https://help.aliyun.com/document_detail/180983.html) operation to query the analysis results of the specified cache analysis task.
        self.job_id = job_id
        # The returned message.
        # 
        # >  If the request was successful, **Successful** is returned. If the request failed, an error message such as an error code is returned.
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

    def validate(self):
        if self.big_keys:
            self.big_keys.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.big_keys is not None:
            result['BigKeys'] = self.big_keys.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.message is not None:
            result['Message'] = self.message

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.task_state is not None:
            result['TaskState'] = self.task_state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BigKeys') is not None:
            temp_model = main_models.CreateCacheAnalysisJobResponseBodyDataBigKeys()
            self.big_keys = temp_model.from_map(m.get('BigKeys'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')

        return self

class CreateCacheAnalysisJobResponseBodyDataBigKeys(DaraModel):
    def __init__(
        self,
        key_info: List[main_models.CreateCacheAnalysisJobResponseBodyDataBigKeysKeyInfo] = None,
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
                temp_model = main_models.CreateCacheAnalysisJobResponseBodyDataBigKeysKeyInfo()
                self.key_info.append(temp_model.from_map(k1))

        return self

class CreateCacheAnalysisJobResponseBodyDataBigKeysKeyInfo(DaraModel):
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
        # The name of the database.
        self.db = db
        # The data type of the key.
        self.encoding = encoding
        # The expiration period of the key. Unit: milliseconds. A value of 0 indicates that the key does not expire.
        self.expiration_time_millis = expiration_time_millis
        # The name of the key.
        self.key = key
        # The ID of the data node on the instance.
        self.node_id = node_id
        # The data type of the ApsaraDB for Redis instance.
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

