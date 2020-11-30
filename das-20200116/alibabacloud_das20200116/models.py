# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import List
except ImportError:
    pass


class GetEventOverviewRequest(TeaModel):
    def __init__(self, instance_id=None, start_time=None, end_time=None, min_level=None):
        self.instance_id = instance_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.min_level = min_level      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.min_level is not None:
            result['MinLevel'] = self.min_level
        return result

    def from_map(self, map={}):
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        if map.get('MinLevel') is not None:
            self.min_level = map.get('MinLevel')
        return self


class GetEventOverviewResponse(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code                # type: str
        self.data = data                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.success = success          # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, map={}):
        if map.get('Code') is not None:
            self.code = map.get('Code')
        if map.get('Data') is not None:
            self.data = map.get('Data')
        if map.get('Message') is not None:
            self.message = map.get('Message')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Success') is not None:
            self.success = map.get('Success')
        return self


class DescribeHotKeysRequest(TeaModel):
    def __init__(self, instance_id=None, node_id=None):
        self.instance_id = instance_id  # type: str
        self.node_id = node_id          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, map={}):
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('NodeId') is not None:
            self.node_id = map.get('NodeId')
        return self


class DescribeHotKeysResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.success = success          # type: str
        self.data = data                # type: DescribeHotKeysResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('Code') is not None:
            self.code = map.get('Code')
        if map.get('Message') is not None:
            self.message = map.get('Message')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Success') is not None:
            self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = DescribeHotKeysResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class DescribeHotKeysResponseDataHotKey(TeaModel):
    def __init__(self, db=None, key_type=None, size=None, hot=None, key=None):
        self.db = db                    # type: int
        self.key_type = key_type        # type: str
        self.size = size                # type: int
        self.hot = hot                  # type: str
        self.key = key                  # type: str

    def validate(self):
        self.validate_required(self.db, 'db')
        self.validate_required(self.key_type, 'key_type')
        self.validate_required(self.size, 'size')
        self.validate_required(self.hot, 'hot')
        self.validate_required(self.key, 'key')

    def to_map(self):
        result = {}
        if self.db is not None:
            result['Db'] = self.db
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.size is not None:
            result['Size'] = self.size
        if self.hot is not None:
            result['Hot'] = self.hot
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, map={}):
        if map.get('Db') is not None:
            self.db = map.get('Db')
        if map.get('KeyType') is not None:
            self.key_type = map.get('KeyType')
        if map.get('Size') is not None:
            self.size = map.get('Size')
        if map.get('Hot') is not None:
            self.hot = map.get('Hot')
        if map.get('Key') is not None:
            self.key = map.get('Key')
        return self


class DescribeHotKeysResponseData(TeaModel):
    def __init__(self, hot_key=None):
        self.hot_key = hot_key          # type: List[DescribeHotKeysResponseDataHotKey]

    def validate(self):
        self.validate_required(self.hot_key, 'hot_key')
        if self.hot_key:
            for k in self.hot_key:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['HotKey'] = []
        if self.hot_key is not None:
            for k in self.hot_key:
                result['HotKey'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.hot_key = []
        if map.get('HotKey') is not None:
            for k in map.get('HotKey'):
                temp_model = DescribeHotKeysResponseDataHotKey()
                self.hot_key.append(temp_model.from_map(k))
        return self


class GetAutonomousNotifyEventDetailRequest(TeaModel):
    def __init__(self, context=None, instance_id=None, span_id=None):
        self.context = context          # type: str
        self.instance_id = instance_id  # type: str
        self.span_id = span_id          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.context is not None:
            result['__context'] = self.context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.span_id is not None:
            result['SpanId'] = self.span_id
        return result

    def from_map(self, map={}):
        if map.get('__context') is not None:
            self.context = map.get('__context')
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('SpanId') is not None:
            self.span_id = map.get('SpanId')
        return self


class GetAutonomousNotifyEventDetailResponse(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code                # type: str
        self.data = data                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.success = success          # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, map={}):
        if map.get('Code') is not None:
            self.code = map.get('Code')
        if map.get('Data') is not None:
            self.data = map.get('Data')
        if map.get('Message') is not None:
            self.message = map.get('Message')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Success') is not None:
            self.success = map.get('Success')
        return self


class GetAutonomousNotifyEventsRequest(TeaModel):
    def __init__(self, context=None, instance_id=None, start_time=None, end_time=None, node_id=None,
                 event_context=None, level=None, min_level=None, page_offset=None, page_size=None):
        self.context = context          # type: str
        self.instance_id = instance_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.node_id = node_id          # type: str
        self.event_context = event_context  # type: str
        self.level = level              # type: str
        self.min_level = min_level      # type: str
        self.page_offset = page_offset  # type: str
        self.page_size = page_size      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.context is not None:
            result['__context'] = self.context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.event_context is not None:
            result['EventContext'] = self.event_context
        if self.level is not None:
            result['Level'] = self.level
        if self.min_level is not None:
            result['MinLevel'] = self.min_level
        if self.page_offset is not None:
            result['PageOffset'] = self.page_offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        if map.get('__context') is not None:
            self.context = map.get('__context')
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        if map.get('NodeId') is not None:
            self.node_id = map.get('NodeId')
        if map.get('EventContext') is not None:
            self.event_context = map.get('EventContext')
        if map.get('Level') is not None:
            self.level = map.get('Level')
        if map.get('MinLevel') is not None:
            self.min_level = map.get('MinLevel')
        if map.get('PageOffset') is not None:
            self.page_offset = map.get('PageOffset')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        return self


class GetAutonomousNotifyEventsResponse(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code                # type: str
        self.data = data                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.success = success          # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, map={}):
        if map.get('Code') is not None:
            self.code = map.get('Code')
        if map.get('Data') is not None:
            self.data = map.get('Data')
        if map.get('Message') is not None:
            self.message = map.get('Message')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Success') is not None:
            self.success = map.get('Success')
        return self


class CreateCacheAnalysisJobRequest(TeaModel):
    def __init__(self, instance_id=None, node_id=None):
        self.instance_id = instance_id  # type: str
        self.node_id = node_id          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, map={}):
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('NodeId') is not None:
            self.node_id = map.get('NodeId')
        return self


class CreateCacheAnalysisJobResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.success = success          # type: str
        self.data = data                # type: CreateCacheAnalysisJobResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('Code') is not None:
            self.code = map.get('Code')
        if map.get('Message') is not None:
            self.message = map.get('Message')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Success') is not None:
            self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = CreateCacheAnalysisJobResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class CreateCacheAnalysisJobResponseDataBigKeysKeyInfo(TeaModel):
    def __init__(self, count=None, bytes=None, db=None, encoding=None, expiration_time_millis=None, key=None,
                 node_id=None, type=None):
        self.count = count              # type: int
        self.bytes = bytes              # type: int
        self.db = db                    # type: int
        self.encoding = encoding        # type: str
        self.expiration_time_millis = expiration_time_millis  # type: int
        self.key = key                  # type: str
        self.node_id = node_id          # type: str
        self.type = type                # type: str

    def validate(self):
        self.validate_required(self.count, 'count')
        self.validate_required(self.bytes, 'bytes')
        self.validate_required(self.db, 'db')
        self.validate_required(self.encoding, 'encoding')
        self.validate_required(self.expiration_time_millis, 'expiration_time_millis')
        self.validate_required(self.key, 'key')
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        if self.count is not None:
            result['Count'] = self.count
        if self.bytes is not None:
            result['Bytes'] = self.bytes
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

    def from_map(self, map={}):
        if map.get('Count') is not None:
            self.count = map.get('Count')
        if map.get('Bytes') is not None:
            self.bytes = map.get('Bytes')
        if map.get('Db') is not None:
            self.db = map.get('Db')
        if map.get('Encoding') is not None:
            self.encoding = map.get('Encoding')
        if map.get('ExpirationTimeMillis') is not None:
            self.expiration_time_millis = map.get('ExpirationTimeMillis')
        if map.get('Key') is not None:
            self.key = map.get('Key')
        if map.get('NodeId') is not None:
            self.node_id = map.get('NodeId')
        if map.get('Type') is not None:
            self.type = map.get('Type')
        return self


class CreateCacheAnalysisJobResponseDataBigKeys(TeaModel):
    def __init__(self, key_info=None):
        self.key_info = key_info        # type: List[CreateCacheAnalysisJobResponseDataBigKeysKeyInfo]

    def validate(self):
        self.validate_required(self.key_info, 'key_info')
        if self.key_info:
            for k in self.key_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['KeyInfo'] = []
        if self.key_info is not None:
            for k in self.key_info:
                result['KeyInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.key_info = []
        if map.get('KeyInfo') is not None:
            for k in map.get('KeyInfo'):
                temp_model = CreateCacheAnalysisJobResponseDataBigKeysKeyInfo()
                self.key_info.append(temp_model.from_map(k))
        return self


class CreateCacheAnalysisJobResponseData(TeaModel):
    def __init__(self, job_id=None, instance_id=None, node_id=None, task_state=None, message=None, big_keys=None):
        self.job_id = job_id            # type: str
        self.instance_id = instance_id  # type: str
        self.node_id = node_id          # type: str
        self.task_state = task_state    # type: str
        self.message = message          # type: str
        self.big_keys = big_keys        # type: CreateCacheAnalysisJobResponseDataBigKeys

    def validate(self):
        self.validate_required(self.job_id, 'job_id')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.task_state, 'task_state')
        self.validate_required(self.message, 'message')
        self.validate_required(self.big_keys, 'big_keys')
        if self.big_keys:
            self.big_keys.validate()

    def to_map(self):
        result = {}
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.task_state is not None:
            result['TaskState'] = self.task_state
        if self.message is not None:
            result['Message'] = self.message
        if self.big_keys is not None:
            result['BigKeys'] = self.big_keys.to_map()
        return result

    def from_map(self, map={}):
        if map.get('JobId') is not None:
            self.job_id = map.get('JobId')
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('NodeId') is not None:
            self.node_id = map.get('NodeId')
        if map.get('TaskState') is not None:
            self.task_state = map.get('TaskState')
        if map.get('Message') is not None:
            self.message = map.get('Message')
        if map.get('BigKeys') is not None:
            temp_model = CreateCacheAnalysisJobResponseDataBigKeys()
            self.big_keys = temp_model.from_map(map['BigKeys'])
        return self


class DescribeCacheAnalysisJobsRequest(TeaModel):
    def __init__(self, instance_id=None, start_time=None, end_time=None, page_no=None, page_size=None):
        self.instance_id = instance_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_no = page_no          # type: str
        self.page_size = page_size      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        if map.get('PageNo') is not None:
            self.page_no = map.get('PageNo')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        return self


class DescribeCacheAnalysisJobsResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.success = success          # type: str
        self.data = data                # type: DescribeCacheAnalysisJobsResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('Code') is not None:
            self.code = map.get('Code')
        if map.get('Message') is not None:
            self.message = map.get('Message')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Success') is not None:
            self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = DescribeCacheAnalysisJobsResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class DescribeCacheAnalysisJobsResponseDataListCacheAnalysisJobBigKeysKeyInfo(TeaModel):
    def __init__(self, count=None, bytes=None, db=None, encoding=None, expiration_time_millis=None, key=None,
                 node_id=None, type=None):
        self.count = count              # type: int
        self.bytes = bytes              # type: int
        self.db = db                    # type: int
        self.encoding = encoding        # type: str
        self.expiration_time_millis = expiration_time_millis  # type: int
        self.key = key                  # type: str
        self.node_id = node_id          # type: str
        self.type = type                # type: str

    def validate(self):
        self.validate_required(self.count, 'count')
        self.validate_required(self.bytes, 'bytes')
        self.validate_required(self.db, 'db')
        self.validate_required(self.encoding, 'encoding')
        self.validate_required(self.expiration_time_millis, 'expiration_time_millis')
        self.validate_required(self.key, 'key')
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        if self.count is not None:
            result['Count'] = self.count
        if self.bytes is not None:
            result['Bytes'] = self.bytes
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

    def from_map(self, map={}):
        if map.get('Count') is not None:
            self.count = map.get('Count')
        if map.get('Bytes') is not None:
            self.bytes = map.get('Bytes')
        if map.get('Db') is not None:
            self.db = map.get('Db')
        if map.get('Encoding') is not None:
            self.encoding = map.get('Encoding')
        if map.get('ExpirationTimeMillis') is not None:
            self.expiration_time_millis = map.get('ExpirationTimeMillis')
        if map.get('Key') is not None:
            self.key = map.get('Key')
        if map.get('NodeId') is not None:
            self.node_id = map.get('NodeId')
        if map.get('Type') is not None:
            self.type = map.get('Type')
        return self


class DescribeCacheAnalysisJobsResponseDataListCacheAnalysisJobBigKeys(TeaModel):
    def __init__(self, key_info=None):
        self.key_info = key_info        # type: List[DescribeCacheAnalysisJobsResponseDataListCacheAnalysisJobBigKeysKeyInfo]

    def validate(self):
        self.validate_required(self.key_info, 'key_info')
        if self.key_info:
            for k in self.key_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['KeyInfo'] = []
        if self.key_info is not None:
            for k in self.key_info:
                result['KeyInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.key_info = []
        if map.get('KeyInfo') is not None:
            for k in map.get('KeyInfo'):
                temp_model = DescribeCacheAnalysisJobsResponseDataListCacheAnalysisJobBigKeysKeyInfo()
                self.key_info.append(temp_model.from_map(k))
        return self


class DescribeCacheAnalysisJobsResponseDataListCacheAnalysisJob(TeaModel):
    def __init__(self, job_id=None, instance_id=None, node_id=None, task_state=None, message=None, big_keys=None):
        self.job_id = job_id            # type: str
        self.instance_id = instance_id  # type: str
        self.node_id = node_id          # type: str
        self.task_state = task_state    # type: str
        self.message = message          # type: str
        self.big_keys = big_keys        # type: DescribeCacheAnalysisJobsResponseDataListCacheAnalysisJobBigKeys

    def validate(self):
        self.validate_required(self.job_id, 'job_id')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.task_state, 'task_state')
        self.validate_required(self.message, 'message')
        self.validate_required(self.big_keys, 'big_keys')
        if self.big_keys:
            self.big_keys.validate()

    def to_map(self):
        result = {}
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.task_state is not None:
            result['TaskState'] = self.task_state
        if self.message is not None:
            result['Message'] = self.message
        if self.big_keys is not None:
            result['BigKeys'] = self.big_keys.to_map()
        return result

    def from_map(self, map={}):
        if map.get('JobId') is not None:
            self.job_id = map.get('JobId')
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('NodeId') is not None:
            self.node_id = map.get('NodeId')
        if map.get('TaskState') is not None:
            self.task_state = map.get('TaskState')
        if map.get('Message') is not None:
            self.message = map.get('Message')
        if map.get('BigKeys') is not None:
            temp_model = DescribeCacheAnalysisJobsResponseDataListCacheAnalysisJobBigKeys()
            self.big_keys = temp_model.from_map(map['BigKeys'])
        return self


class DescribeCacheAnalysisJobsResponseDataList(TeaModel):
    def __init__(self, cache_analysis_job=None):
        self.cache_analysis_job = cache_analysis_job  # type: List[DescribeCacheAnalysisJobsResponseDataListCacheAnalysisJob]

    def validate(self):
        self.validate_required(self.cache_analysis_job, 'cache_analysis_job')
        if self.cache_analysis_job:
            for k in self.cache_analysis_job:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['CacheAnalysisJob'] = []
        if self.cache_analysis_job is not None:
            for k in self.cache_analysis_job:
                result['CacheAnalysisJob'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.cache_analysis_job = []
        if map.get('CacheAnalysisJob') is not None:
            for k in map.get('CacheAnalysisJob'):
                temp_model = DescribeCacheAnalysisJobsResponseDataListCacheAnalysisJob()
                self.cache_analysis_job.append(temp_model.from_map(k))
        return self


class DescribeCacheAnalysisJobsResponseData(TeaModel):
    def __init__(self, total=None, page_no=None, page_size=None, extra=None, list=None):
        self.total = total              # type: int
        self.page_no = page_no          # type: int
        self.page_size = page_size      # type: int
        self.extra = extra              # type: str
        self.list = list                # type: DescribeCacheAnalysisJobsResponseDataList

    def validate(self):
        self.validate_required(self.total, 'total')
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.extra, 'extra')
        self.validate_required(self.list, 'list')
        if self.list:
            self.list.validate()

    def to_map(self):
        result = {}
        if self.total is not None:
            result['Total'] = self.total
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.list is not None:
            result['List'] = self.list.to_map()
        return result

    def from_map(self, map={}):
        if map.get('Total') is not None:
            self.total = map.get('Total')
        if map.get('PageNo') is not None:
            self.page_no = map.get('PageNo')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('Extra') is not None:
            self.extra = map.get('Extra')
        if map.get('List') is not None:
            temp_model = DescribeCacheAnalysisJobsResponseDataList()
            self.list = temp_model.from_map(map['List'])
        return self


class DescribeCacheAnalysisJobRequest(TeaModel):
    def __init__(self, instance_id=None, job_id=None):
        self.instance_id = instance_id  # type: str
        self.job_id = job_id            # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, map={}):
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('JobId') is not None:
            self.job_id = map.get('JobId')
        return self


class DescribeCacheAnalysisJobResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.success = success          # type: str
        self.data = data                # type: DescribeCacheAnalysisJobResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('Code') is not None:
            self.code = map.get('Code')
        if map.get('Message') is not None:
            self.message = map.get('Message')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Success') is not None:
            self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = DescribeCacheAnalysisJobResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class DescribeCacheAnalysisJobResponseDataBigKeysKeyInfo(TeaModel):
    def __init__(self, count=None, bytes=None, db=None, encoding=None, expiration_time_millis=None, key=None,
                 node_id=None, type=None):
        self.count = count              # type: int
        self.bytes = bytes              # type: int
        self.db = db                    # type: int
        self.encoding = encoding        # type: str
        self.expiration_time_millis = expiration_time_millis  # type: int
        self.key = key                  # type: str
        self.node_id = node_id          # type: str
        self.type = type                # type: str

    def validate(self):
        self.validate_required(self.count, 'count')
        self.validate_required(self.bytes, 'bytes')
        self.validate_required(self.db, 'db')
        self.validate_required(self.encoding, 'encoding')
        self.validate_required(self.expiration_time_millis, 'expiration_time_millis')
        self.validate_required(self.key, 'key')
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        if self.count is not None:
            result['Count'] = self.count
        if self.bytes is not None:
            result['Bytes'] = self.bytes
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

    def from_map(self, map={}):
        if map.get('Count') is not None:
            self.count = map.get('Count')
        if map.get('Bytes') is not None:
            self.bytes = map.get('Bytes')
        if map.get('Db') is not None:
            self.db = map.get('Db')
        if map.get('Encoding') is not None:
            self.encoding = map.get('Encoding')
        if map.get('ExpirationTimeMillis') is not None:
            self.expiration_time_millis = map.get('ExpirationTimeMillis')
        if map.get('Key') is not None:
            self.key = map.get('Key')
        if map.get('NodeId') is not None:
            self.node_id = map.get('NodeId')
        if map.get('Type') is not None:
            self.type = map.get('Type')
        return self


class DescribeCacheAnalysisJobResponseDataBigKeys(TeaModel):
    def __init__(self, key_info=None):
        self.key_info = key_info        # type: List[DescribeCacheAnalysisJobResponseDataBigKeysKeyInfo]

    def validate(self):
        self.validate_required(self.key_info, 'key_info')
        if self.key_info:
            for k in self.key_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['KeyInfo'] = []
        if self.key_info is not None:
            for k in self.key_info:
                result['KeyInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.key_info = []
        if map.get('KeyInfo') is not None:
            for k in map.get('KeyInfo'):
                temp_model = DescribeCacheAnalysisJobResponseDataBigKeysKeyInfo()
                self.key_info.append(temp_model.from_map(k))
        return self


class DescribeCacheAnalysisJobResponseDataKeyPrefixesPrefix(TeaModel):
    def __init__(self, prefix=None, type=None, bytes=None, key_num=None, count=None):
        self.prefix = prefix            # type: str
        self.type = type                # type: str
        self.bytes = bytes              # type: int
        self.key_num = key_num          # type: int
        self.count = count              # type: int

    def validate(self):
        self.validate_required(self.prefix, 'prefix')
        self.validate_required(self.type, 'type')
        self.validate_required(self.bytes, 'bytes')
        self.validate_required(self.key_num, 'key_num')
        self.validate_required(self.count, 'count')

    def to_map(self):
        result = {}
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.type is not None:
            result['Type'] = self.type
        if self.bytes is not None:
            result['Bytes'] = self.bytes
        if self.key_num is not None:
            result['KeyNum'] = self.key_num
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, map={}):
        if map.get('Prefix') is not None:
            self.prefix = map.get('Prefix')
        if map.get('Type') is not None:
            self.type = map.get('Type')
        if map.get('Bytes') is not None:
            self.bytes = map.get('Bytes')
        if map.get('KeyNum') is not None:
            self.key_num = map.get('KeyNum')
        if map.get('Count') is not None:
            self.count = map.get('Count')
        return self


class DescribeCacheAnalysisJobResponseDataKeyPrefixes(TeaModel):
    def __init__(self, prefix=None):
        self.prefix = prefix            # type: List[DescribeCacheAnalysisJobResponseDataKeyPrefixesPrefix]

    def validate(self):
        self.validate_required(self.prefix, 'prefix')
        if self.prefix:
            for k in self.prefix:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Prefix'] = []
        if self.prefix is not None:
            for k in self.prefix:
                result['Prefix'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.prefix = []
        if map.get('Prefix') is not None:
            for k in map.get('Prefix'):
                temp_model = DescribeCacheAnalysisJobResponseDataKeyPrefixesPrefix()
                self.prefix.append(temp_model.from_map(k))
        return self


class DescribeCacheAnalysisJobResponseData(TeaModel):
    def __init__(self, job_id=None, instance_id=None, node_id=None, task_state=None, message=None, big_keys=None,
                 key_prefixes=None):
        self.job_id = job_id            # type: str
        self.instance_id = instance_id  # type: str
        self.node_id = node_id          # type: str
        self.task_state = task_state    # type: str
        self.message = message          # type: str
        self.big_keys = big_keys        # type: DescribeCacheAnalysisJobResponseDataBigKeys
        self.key_prefixes = key_prefixes  # type: DescribeCacheAnalysisJobResponseDataKeyPrefixes

    def validate(self):
        self.validate_required(self.job_id, 'job_id')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.task_state, 'task_state')
        self.validate_required(self.message, 'message')
        self.validate_required(self.big_keys, 'big_keys')
        if self.big_keys:
            self.big_keys.validate()
        self.validate_required(self.key_prefixes, 'key_prefixes')
        if self.key_prefixes:
            self.key_prefixes.validate()

    def to_map(self):
        result = {}
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.task_state is not None:
            result['TaskState'] = self.task_state
        if self.message is not None:
            result['Message'] = self.message
        if self.big_keys is not None:
            result['BigKeys'] = self.big_keys.to_map()
        if self.key_prefixes is not None:
            result['KeyPrefixes'] = self.key_prefixes.to_map()
        return result

    def from_map(self, map={}):
        if map.get('JobId') is not None:
            self.job_id = map.get('JobId')
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('NodeId') is not None:
            self.node_id = map.get('NodeId')
        if map.get('TaskState') is not None:
            self.task_state = map.get('TaskState')
        if map.get('Message') is not None:
            self.message = map.get('Message')
        if map.get('BigKeys') is not None:
            temp_model = DescribeCacheAnalysisJobResponseDataBigKeys()
            self.big_keys = temp_model.from_map(map['BigKeys'])
        if map.get('KeyPrefixes') is not None:
            temp_model = DescribeCacheAnalysisJobResponseDataKeyPrefixes()
            self.key_prefixes = temp_model.from_map(map['KeyPrefixes'])
        return self


class DescribeDiagnosticReportListRequest(TeaModel):
    def __init__(self, uid=None, access_key=None, signature=None, timestamp=None, context=None, skip_auth=None,
                 user_id=None, dbinstance_id=None, page_no=None, page_size=None, start_time=None, end_time=None):
        self.uid = uid                  # type: str
        self.access_key = access_key    # type: str
        self.signature = signature      # type: str
        self.timestamp = timestamp      # type: str
        self.context = context          # type: str
        self.skip_auth = skip_auth      # type: str
        self.user_id = user_id          # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.page_no = page_no          # type: str
        self.page_size = page_size      # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.context is not None:
            result['__context'] = self.context
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        if map.get('Uid') is not None:
            self.uid = map.get('Uid')
        if map.get('accessKey') is not None:
            self.access_key = map.get('accessKey')
        if map.get('signature') is not None:
            self.signature = map.get('signature')
        if map.get('timestamp') is not None:
            self.timestamp = map.get('timestamp')
        if map.get('__context') is not None:
            self.context = map.get('__context')
        if map.get('skipAuth') is not None:
            self.skip_auth = map.get('skipAuth')
        if map.get('UserId') is not None:
            self.user_id = map.get('UserId')
        if map.get('DBInstanceId') is not None:
            self.dbinstance_id = map.get('DBInstanceId')
        if map.get('PageNo') is not None:
            self.page_no = map.get('PageNo')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        return self


class DescribeDiagnosticReportListResponse(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None, synchro=None):
        self.code = code                # type: str
        self.data = data                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.success = success          # type: str
        self.synchro = synchro          # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.synchro, 'synchro')

    def to_map(self):
        result = {}
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, map={}):
        if map.get('Code') is not None:
            self.code = map.get('Code')
        if map.get('Data') is not None:
            self.data = map.get('Data')
        if map.get('Message') is not None:
            self.message = map.get('Message')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Success') is not None:
            self.success = map.get('Success')
        if map.get('Synchro') is not None:
            self.synchro = map.get('Synchro')
        return self


class CreateDiagnosticReportRequest(TeaModel):
    def __init__(self, uid=None, access_key=None, signature=None, timestamp=None, context=None, skip_auth=None,
                 user_id=None, dbinstance_id=None, start_time=None, end_time=None):
        self.uid = uid                  # type: str
        self.access_key = access_key    # type: str
        self.signature = signature      # type: str
        self.timestamp = timestamp      # type: str
        self.context = context          # type: str
        self.skip_auth = skip_auth      # type: str
        self.user_id = user_id          # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.context is not None:
            result['__context'] = self.context
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        if map.get('Uid') is not None:
            self.uid = map.get('Uid')
        if map.get('accessKey') is not None:
            self.access_key = map.get('accessKey')
        if map.get('signature') is not None:
            self.signature = map.get('signature')
        if map.get('timestamp') is not None:
            self.timestamp = map.get('timestamp')
        if map.get('__context') is not None:
            self.context = map.get('__context')
        if map.get('skipAuth') is not None:
            self.skip_auth = map.get('skipAuth')
        if map.get('UserId') is not None:
            self.user_id = map.get('UserId')
        if map.get('DBInstanceId') is not None:
            self.dbinstance_id = map.get('DBInstanceId')
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        return self


class CreateDiagnosticReportResponse(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None, synchro=None):
        self.code = code                # type: str
        self.data = data                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.success = success          # type: str
        self.synchro = synchro          # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.synchro, 'synchro')

    def to_map(self):
        result = {}
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, map={}):
        if map.get('Code') is not None:
            self.code = map.get('Code')
        if map.get('Data') is not None:
            self.data = map.get('Data')
        if map.get('Message') is not None:
            self.message = map.get('Message')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Success') is not None:
            self.success = map.get('Success')
        if map.get('Synchro') is not None:
            self.synchro = map.get('Synchro')
        return self


class AccessHDMInstanceRequest(TeaModel):
    def __init__(self, uid=None, access_key=None, signature=None, timestamp=None, context=None, skip_auth=None,
                 user_id=None, instance_area=None, instance_id=None, ip=None, port=None, engine=None, username=None,
                 password=None, instance_alias=None, network_type=None, vpc_id=None, region=None, caller_bid=None,
                 tenant_id=None, owner_id_signature=None, caller_type=None, caller_uid=None, target=None, product=None,
                 external=None):
        self.uid = uid                  # type: str
        self.access_key = access_key    # type: str
        self.signature = signature      # type: str
        self.timestamp = timestamp      # type: str
        self.context = context          # type: str
        self.skip_auth = skip_auth      # type: str
        self.user_id = user_id          # type: str
        self.instance_area = instance_area  # type: str
        self.instance_id = instance_id  # type: str
        self.ip = ip                    # type: str
        self.port = port                # type: str
        self.engine = engine            # type: str
        self.username = username        # type: str
        self.password = password        # type: str
        self.instance_alias = instance_alias  # type: str
        self.network_type = network_type  # type: str
        self.vpc_id = vpc_id            # type: str
        self.region = region            # type: str
        self.caller_bid = caller_bid    # type: str
        self.tenant_id = tenant_id      # type: str
        self.owner_id_signature = owner_id_signature  # type: str
        self.caller_type = caller_type  # type: str
        self.caller_uid = caller_uid    # type: str
        self.target = target            # type: str
        self.product = product          # type: str
        self.external = external        # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.context is not None:
            result['__context'] = self.context
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.instance_area is not None:
            result['InstanceArea'] = self.instance_area
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.username is not None:
            result['Username'] = self.username
        if self.password is not None:
            result['Password'] = self.password
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.region is not None:
            result['Region'] = self.region
        if self.caller_bid is not None:
            result['CallerBid'] = self.caller_bid
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.owner_id_signature is not None:
            result['OwnerIdSignature'] = self.owner_id_signature
        if self.caller_type is not None:
            result['CallerType'] = self.caller_type
        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid
        if self.target is not None:
            result['Target'] = self.target
        if self.product is not None:
            result['Product'] = self.product
        if self.external is not None:
            result['External'] = self.external
        return result

    def from_map(self, map={}):
        if map.get('Uid') is not None:
            self.uid = map.get('Uid')
        if map.get('accessKey') is not None:
            self.access_key = map.get('accessKey')
        if map.get('signature') is not None:
            self.signature = map.get('signature')
        if map.get('timestamp') is not None:
            self.timestamp = map.get('timestamp')
        if map.get('__context') is not None:
            self.context = map.get('__context')
        if map.get('skipAuth') is not None:
            self.skip_auth = map.get('skipAuth')
        if map.get('UserId') is not None:
            self.user_id = map.get('UserId')
        if map.get('InstanceArea') is not None:
            self.instance_area = map.get('InstanceArea')
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('Ip') is not None:
            self.ip = map.get('Ip')
        if map.get('Port') is not None:
            self.port = map.get('Port')
        if map.get('Engine') is not None:
            self.engine = map.get('Engine')
        if map.get('Username') is not None:
            self.username = map.get('Username')
        if map.get('Password') is not None:
            self.password = map.get('Password')
        if map.get('InstanceAlias') is not None:
            self.instance_alias = map.get('InstanceAlias')
        if map.get('NetworkType') is not None:
            self.network_type = map.get('NetworkType')
        if map.get('VpcId') is not None:
            self.vpc_id = map.get('VpcId')
        if map.get('Region') is not None:
            self.region = map.get('Region')
        if map.get('CallerBid') is not None:
            self.caller_bid = map.get('CallerBid')
        if map.get('TenantId') is not None:
            self.tenant_id = map.get('TenantId')
        if map.get('OwnerIdSignature') is not None:
            self.owner_id_signature = map.get('OwnerIdSignature')
        if map.get('CallerType') is not None:
            self.caller_type = map.get('CallerType')
        if map.get('CallerUid') is not None:
            self.caller_uid = map.get('CallerUid')
        if map.get('Target') is not None:
            self.target = map.get('Target')
        if map.get('Product') is not None:
            self.product = map.get('Product')
        if map.get('External') is not None:
            self.external = map.get('External')
        return self


class AccessHDMInstanceResponse(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None, synchro=None):
        self.code = code                # type: str
        self.data = data                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.success = success          # type: str
        self.synchro = synchro          # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.synchro, 'synchro')

    def to_map(self):
        result = {}
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, map={}):
        if map.get('Code') is not None:
            self.code = map.get('Code')
        if map.get('Data') is not None:
            self.data = map.get('Data')
        if map.get('Message') is not None:
            self.message = map.get('Message')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Success') is not None:
            self.success = map.get('Success')
        if map.get('Synchro') is not None:
            self.synchro = map.get('Synchro')
        return self


class SyncHDMAliyunResourceRequest(TeaModel):
    def __init__(self, uid=None, access_key=None, signature=None, timestamp=None, context=None, skip_auth=None,
                 user_id=None, async_=None, wait_for_modify_security_ips=None, resource_types=None):
        self.uid = uid                  # type: str
        self.access_key = access_key    # type: str
        self.signature = signature      # type: str
        self.timestamp = timestamp      # type: str
        self.context = context          # type: str
        self.skip_auth = skip_auth      # type: str
        self.user_id = user_id          # type: str
        self.async_ = async_            # type: str
        self.wait_for_modify_security_ips = wait_for_modify_security_ips  # type: str
        self.resource_types = resource_types  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.context is not None:
            result['__context'] = self.context
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.wait_for_modify_security_ips is not None:
            result['WaitForModifySecurityIps'] = self.wait_for_modify_security_ips
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, map={}):
        if map.get('Uid') is not None:
            self.uid = map.get('Uid')
        if map.get('accessKey') is not None:
            self.access_key = map.get('accessKey')
        if map.get('signature') is not None:
            self.signature = map.get('signature')
        if map.get('timestamp') is not None:
            self.timestamp = map.get('timestamp')
        if map.get('__context') is not None:
            self.context = map.get('__context')
        if map.get('skipAuth') is not None:
            self.skip_auth = map.get('skipAuth')
        if map.get('UserId') is not None:
            self.user_id = map.get('UserId')
        if map.get('Async') is not None:
            self.async_ = map.get('Async')
        if map.get('WaitForModifySecurityIps') is not None:
            self.wait_for_modify_security_ips = map.get('WaitForModifySecurityIps')
        if map.get('ResourceTypes') is not None:
            self.resource_types = map.get('ResourceTypes')
        return self


class SyncHDMAliyunResourceResponse(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None, synchro=None):
        self.code = code                # type: str
        self.data = data                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.success = success          # type: str
        self.synchro = synchro          # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.synchro, 'synchro')

    def to_map(self):
        result = {}
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, map={}):
        if map.get('Code') is not None:
            self.code = map.get('Code')
        if map.get('Data') is not None:
            self.data = map.get('Data')
        if map.get('Message') is not None:
            self.message = map.get('Message')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Success') is not None:
            self.success = map.get('Success')
        if map.get('Synchro') is not None:
            self.synchro = map.get('Synchro')
        return self


class GetHDMLastAliyunResourceSyncResultRequest(TeaModel):
    def __init__(self, uid=None, access_key=None, signature=None, timestamp=None, context=None, skip_auth=None,
                 user_id=None):
        self.uid = uid                  # type: str
        self.access_key = access_key    # type: str
        self.signature = signature      # type: str
        self.timestamp = timestamp      # type: str
        self.context = context          # type: str
        self.skip_auth = skip_auth      # type: str
        self.user_id = user_id          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.context is not None:
            result['__context'] = self.context
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, map={}):
        if map.get('Uid') is not None:
            self.uid = map.get('Uid')
        if map.get('accessKey') is not None:
            self.access_key = map.get('accessKey')
        if map.get('signature') is not None:
            self.signature = map.get('signature')
        if map.get('timestamp') is not None:
            self.timestamp = map.get('timestamp')
        if map.get('__context') is not None:
            self.context = map.get('__context')
        if map.get('skipAuth') is not None:
            self.skip_auth = map.get('skipAuth')
        if map.get('UserId') is not None:
            self.user_id = map.get('UserId')
        return self


class GetHDMLastAliyunResourceSyncResultResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, synchro=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.success = success          # type: str
        self.synchro = synchro          # type: str
        self.data = data                # type: GetHDMLastAliyunResourceSyncResultResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.synchro, 'synchro')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('Code') is not None:
            self.code = map.get('Code')
        if map.get('Message') is not None:
            self.message = map.get('Message')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Success') is not None:
            self.success = map.get('Success')
        if map.get('Synchro') is not None:
            self.synchro = map.get('Synchro')
        if map.get('Data') is not None:
            temp_model = GetHDMLastAliyunResourceSyncResultResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class GetHDMLastAliyunResourceSyncResultResponseDataSubResultsResourceSyncSubResult(TeaModel):
    def __init__(self, resource_type=None, sync_count=None, success=None, err_msg=None):
        self.resource_type = resource_type  # type: str
        self.sync_count = sync_count    # type: int
        self.success = success          # type: bool
        self.err_msg = err_msg          # type: str

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.sync_count, 'sync_count')
        self.validate_required(self.success, 'success')
        self.validate_required(self.err_msg, 'err_msg')

    def to_map(self):
        result = {}
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.sync_count is not None:
            result['SyncCount'] = self.sync_count
        if self.success is not None:
            result['Success'] = self.success
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        return result

    def from_map(self, map={}):
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        if map.get('SyncCount') is not None:
            self.sync_count = map.get('SyncCount')
        if map.get('Success') is not None:
            self.success = map.get('Success')
        if map.get('ErrMsg') is not None:
            self.err_msg = map.get('ErrMsg')
        return self


class GetHDMLastAliyunResourceSyncResultResponseDataSubResults(TeaModel):
    def __init__(self, resource_sync_sub_result=None):
        self.resource_sync_sub_result = resource_sync_sub_result  # type: List[GetHDMLastAliyunResourceSyncResultResponseDataSubResultsResourceSyncSubResult]

    def validate(self):
        self.validate_required(self.resource_sync_sub_result, 'resource_sync_sub_result')
        if self.resource_sync_sub_result:
            for k in self.resource_sync_sub_result:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ResourceSyncSubResult'] = []
        if self.resource_sync_sub_result is not None:
            for k in self.resource_sync_sub_result:
                result['ResourceSyncSubResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.resource_sync_sub_result = []
        if map.get('ResourceSyncSubResult') is not None:
            for k in map.get('ResourceSyncSubResult'):
                temp_model = GetHDMLastAliyunResourceSyncResultResponseDataSubResultsResourceSyncSubResult()
                self.resource_sync_sub_result.append(temp_model.from_map(k))
        return self


class GetHDMLastAliyunResourceSyncResultResponseData(TeaModel):
    def __init__(self, sync_status=None, error_msg=None, results=None, sub_results=None):
        self.sync_status = sync_status  # type: str
        self.error_msg = error_msg      # type: str
        self.results = results          # type: str
        self.sub_results = sub_results  # type: GetHDMLastAliyunResourceSyncResultResponseDataSubResults

    def validate(self):
        self.validate_required(self.sync_status, 'sync_status')
        self.validate_required(self.error_msg, 'error_msg')
        self.validate_required(self.results, 'results')
        self.validate_required(self.sub_results, 'sub_results')
        if self.sub_results:
            self.sub_results.validate()

    def to_map(self):
        result = {}
        if self.sync_status is not None:
            result['SyncStatus'] = self.sync_status
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.results is not None:
            result['Results'] = self.results
        if self.sub_results is not None:
            result['SubResults'] = self.sub_results.to_map()
        return result

    def from_map(self, map={}):
        if map.get('SyncStatus') is not None:
            self.sync_status = map.get('SyncStatus')
        if map.get('ErrorMsg') is not None:
            self.error_msg = map.get('ErrorMsg')
        if map.get('Results') is not None:
            self.results = map.get('Results')
        if map.get('SubResults') is not None:
            temp_model = GetHDMLastAliyunResourceSyncResultResponseDataSubResults()
            self.sub_results = temp_model.from_map(map['SubResults'])
        return self


class GetEndpointSwitchTaskRequest(TeaModel):
    def __init__(self, uid=None, access_key=None, signature=None, timestamp=None, context=None, skip_auth=None,
                 user_id=None, task_id=None):
        self.uid = uid                  # type: str
        self.access_key = access_key    # type: str
        self.signature = signature      # type: str
        self.timestamp = timestamp      # type: str
        self.context = context          # type: str
        self.skip_auth = skip_auth      # type: str
        self.user_id = user_id          # type: str
        self.task_id = task_id          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.context is not None:
            result['__context'] = self.context
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        if map.get('Uid') is not None:
            self.uid = map.get('Uid')
        if map.get('accessKey') is not None:
            self.access_key = map.get('accessKey')
        if map.get('signature') is not None:
            self.signature = map.get('signature')
        if map.get('timestamp') is not None:
            self.timestamp = map.get('timestamp')
        if map.get('__context') is not None:
            self.context = map.get('__context')
        if map.get('skipAuth') is not None:
            self.skip_auth = map.get('skipAuth')
        if map.get('UserId') is not None:
            self.user_id = map.get('UserId')
        if map.get('TaskId') is not None:
            self.task_id = map.get('TaskId')
        return self


class GetEndpointSwitchTaskResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, synchro=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.success = success          # type: str
        self.synchro = synchro          # type: str
        self.data = data                # type: GetEndpointSwitchTaskResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.synchro, 'synchro')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('Code') is not None:
            self.code = map.get('Code')
        if map.get('Message') is not None:
            self.message = map.get('Message')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Success') is not None:
            self.success = map.get('Success')
        if map.get('Synchro') is not None:
            self.synchro = map.get('Synchro')
        if map.get('Data') is not None:
            temp_model = GetEndpointSwitchTaskResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class GetEndpointSwitchTaskResponseData(TeaModel):
    def __init__(self, account_id=None, db_link_id=None, task_id=None, status=None, ori_uuid=None, uuid=None,
                 err_msg=None):
        self.account_id = account_id    # type: str
        self.db_link_id = db_link_id    # type: int
        self.task_id = task_id          # type: str
        self.status = status            # type: str
        self.ori_uuid = ori_uuid        # type: str
        self.uuid = uuid                # type: str
        self.err_msg = err_msg          # type: str

    def validate(self):
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.db_link_id, 'db_link_id')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.ori_uuid, 'ori_uuid')
        self.validate_required(self.uuid, 'uuid')
        self.validate_required(self.err_msg, 'err_msg')

    def to_map(self):
        result = {}
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.db_link_id is not None:
            result['DbLinkId'] = self.db_link_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.status is not None:
            result['Status'] = self.status
        if self.ori_uuid is not None:
            result['OriUuid'] = self.ori_uuid
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        return result

    def from_map(self, map={}):
        if map.get('AccountId') is not None:
            self.account_id = map.get('AccountId')
        if map.get('DbLinkId') is not None:
            self.db_link_id = map.get('DbLinkId')
        if map.get('TaskId') is not None:
            self.task_id = map.get('TaskId')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('OriUuid') is not None:
            self.ori_uuid = map.get('OriUuid')
        if map.get('Uuid') is not None:
            self.uuid = map.get('Uuid')
        if map.get('ErrMsg') is not None:
            self.err_msg = map.get('ErrMsg')
        return self


class GetHDMAliyunResourceSyncResultRequest(TeaModel):
    def __init__(self, uid=None, access_key=None, signature=None, timestamp=None, context=None, skip_auth=None,
                 user_id=None, task_id=None):
        self.uid = uid                  # type: str
        self.access_key = access_key    # type: str
        self.signature = signature      # type: str
        self.timestamp = timestamp      # type: str
        self.context = context          # type: str
        self.skip_auth = skip_auth      # type: str
        self.user_id = user_id          # type: str
        self.task_id = task_id          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.context is not None:
            result['__context'] = self.context
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        if map.get('Uid') is not None:
            self.uid = map.get('Uid')
        if map.get('accessKey') is not None:
            self.access_key = map.get('accessKey')
        if map.get('signature') is not None:
            self.signature = map.get('signature')
        if map.get('timestamp') is not None:
            self.timestamp = map.get('timestamp')
        if map.get('__context') is not None:
            self.context = map.get('__context')
        if map.get('skipAuth') is not None:
            self.skip_auth = map.get('skipAuth')
        if map.get('UserId') is not None:
            self.user_id = map.get('UserId')
        if map.get('TaskId') is not None:
            self.task_id = map.get('TaskId')
        return self


class GetHDMAliyunResourceSyncResultResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, synchro=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.success = success          # type: str
        self.synchro = synchro          # type: str
        self.data = data                # type: GetHDMAliyunResourceSyncResultResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.synchro, 'synchro')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('Code') is not None:
            self.code = map.get('Code')
        if map.get('Message') is not None:
            self.message = map.get('Message')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Success') is not None:
            self.success = map.get('Success')
        if map.get('Synchro') is not None:
            self.synchro = map.get('Synchro')
        if map.get('Data') is not None:
            temp_model = GetHDMAliyunResourceSyncResultResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class GetHDMAliyunResourceSyncResultResponseDataSubResultsResourceSyncSubResult(TeaModel):
    def __init__(self, resource_type=None, sync_count=None, success=None, err_msg=None):
        self.resource_type = resource_type  # type: str
        self.sync_count = sync_count    # type: int
        self.success = success          # type: bool
        self.err_msg = err_msg          # type: str

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.sync_count, 'sync_count')
        self.validate_required(self.success, 'success')
        self.validate_required(self.err_msg, 'err_msg')

    def to_map(self):
        result = {}
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.sync_count is not None:
            result['SyncCount'] = self.sync_count
        if self.success is not None:
            result['Success'] = self.success
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        return result

    def from_map(self, map={}):
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        if map.get('SyncCount') is not None:
            self.sync_count = map.get('SyncCount')
        if map.get('Success') is not None:
            self.success = map.get('Success')
        if map.get('ErrMsg') is not None:
            self.err_msg = map.get('ErrMsg')
        return self


class GetHDMAliyunResourceSyncResultResponseDataSubResults(TeaModel):
    def __init__(self, resource_sync_sub_result=None):
        self.resource_sync_sub_result = resource_sync_sub_result  # type: List[GetHDMAliyunResourceSyncResultResponseDataSubResultsResourceSyncSubResult]

    def validate(self):
        self.validate_required(self.resource_sync_sub_result, 'resource_sync_sub_result')
        if self.resource_sync_sub_result:
            for k in self.resource_sync_sub_result:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ResourceSyncSubResult'] = []
        if self.resource_sync_sub_result is not None:
            for k in self.resource_sync_sub_result:
                result['ResourceSyncSubResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.resource_sync_sub_result = []
        if map.get('ResourceSyncSubResult') is not None:
            for k in map.get('ResourceSyncSubResult'):
                temp_model = GetHDMAliyunResourceSyncResultResponseDataSubResultsResourceSyncSubResult()
                self.resource_sync_sub_result.append(temp_model.from_map(k))
        return self


class GetHDMAliyunResourceSyncResultResponseData(TeaModel):
    def __init__(self, sync_status=None, error_msg=None, results=None, sub_results=None):
        self.sync_status = sync_status  # type: str
        self.error_msg = error_msg      # type: str
        self.results = results          # type: str
        self.sub_results = sub_results  # type: GetHDMAliyunResourceSyncResultResponseDataSubResults

    def validate(self):
        self.validate_required(self.sync_status, 'sync_status')
        self.validate_required(self.error_msg, 'error_msg')
        self.validate_required(self.results, 'results')
        self.validate_required(self.sub_results, 'sub_results')
        if self.sub_results:
            self.sub_results.validate()

    def to_map(self):
        result = {}
        if self.sync_status is not None:
            result['SyncStatus'] = self.sync_status
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.results is not None:
            result['Results'] = self.results
        if self.sub_results is not None:
            result['SubResults'] = self.sub_results.to_map()
        return result

    def from_map(self, map={}):
        if map.get('SyncStatus') is not None:
            self.sync_status = map.get('SyncStatus')
        if map.get('ErrorMsg') is not None:
            self.error_msg = map.get('ErrorMsg')
        if map.get('Results') is not None:
            self.results = map.get('Results')
        if map.get('SubResults') is not None:
            temp_model = GetHDMAliyunResourceSyncResultResponseDataSubResults()
            self.sub_results = temp_model.from_map(map['SubResults'])
        return self


class AddHDMInstanceRequest(TeaModel):
    def __init__(self, uid=None, access_key=None, signature=None, timestamp=None, context=None, skip_auth=None,
                 user_id=None, instance_area=None, instance_id=None, ip=None, port=None, engine=None, username=None,
                 password=None, instance_alias=None, network_type=None, vpc_id=None, region=None, flush_account=None):
        self.uid = uid                  # type: str
        self.access_key = access_key    # type: str
        self.signature = signature      # type: str
        self.timestamp = timestamp      # type: str
        self.context = context          # type: str
        self.skip_auth = skip_auth      # type: str
        self.user_id = user_id          # type: str
        self.instance_area = instance_area  # type: str
        self.instance_id = instance_id  # type: str
        self.ip = ip                    # type: str
        self.port = port                # type: str
        self.engine = engine            # type: str
        self.username = username        # type: str
        self.password = password        # type: str
        self.instance_alias = instance_alias  # type: str
        self.network_type = network_type  # type: str
        self.vpc_id = vpc_id            # type: str
        self.region = region            # type: str
        self.flush_account = flush_account  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.context is not None:
            result['__context'] = self.context
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.instance_area is not None:
            result['InstanceArea'] = self.instance_area
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.username is not None:
            result['Username'] = self.username
        if self.password is not None:
            result['Password'] = self.password
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.region is not None:
            result['Region'] = self.region
        if self.flush_account is not None:
            result['FlushAccount'] = self.flush_account
        return result

    def from_map(self, map={}):
        if map.get('Uid') is not None:
            self.uid = map.get('Uid')
        if map.get('accessKey') is not None:
            self.access_key = map.get('accessKey')
        if map.get('signature') is not None:
            self.signature = map.get('signature')
        if map.get('timestamp') is not None:
            self.timestamp = map.get('timestamp')
        if map.get('__context') is not None:
            self.context = map.get('__context')
        if map.get('skipAuth') is not None:
            self.skip_auth = map.get('skipAuth')
        if map.get('UserId') is not None:
            self.user_id = map.get('UserId')
        if map.get('InstanceArea') is not None:
            self.instance_area = map.get('InstanceArea')
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('Ip') is not None:
            self.ip = map.get('Ip')
        if map.get('Port') is not None:
            self.port = map.get('Port')
        if map.get('Engine') is not None:
            self.engine = map.get('Engine')
        if map.get('Username') is not None:
            self.username = map.get('Username')
        if map.get('Password') is not None:
            self.password = map.get('Password')
        if map.get('InstanceAlias') is not None:
            self.instance_alias = map.get('InstanceAlias')
        if map.get('NetworkType') is not None:
            self.network_type = map.get('NetworkType')
        if map.get('VpcId') is not None:
            self.vpc_id = map.get('VpcId')
        if map.get('Region') is not None:
            self.region = map.get('Region')
        if map.get('FlushAccount') is not None:
            self.flush_account = map.get('FlushAccount')
        return self


class AddHDMInstanceResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, synchro=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.success = success          # type: str
        self.synchro = synchro          # type: str
        self.data = data                # type: AddHDMInstanceResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.synchro, 'synchro')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('Code') is not None:
            self.code = map.get('Code')
        if map.get('Message') is not None:
            self.message = map.get('Message')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Success') is not None:
            self.success = map.get('Success')
        if map.get('Synchro') is not None:
            self.synchro = map.get('Synchro')
        if map.get('Data') is not None:
            temp_model = AddHDMInstanceResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class AddHDMInstanceResponseData(TeaModel):
    def __init__(self, instance_id=None, vpc_id=None, ip=None, port=None, uuid=None, role=None, code=None, error=None,
                 tenant_id=None, owner_id=None, token=None, caller_uid=None):
        self.instance_id = instance_id  # type: str
        self.vpc_id = vpc_id            # type: str
        self.ip = ip                    # type: str
        self.port = port                # type: int
        self.uuid = uuid                # type: str
        self.role = role                # type: str
        self.code = code                # type: int
        self.error = error              # type: str
        self.tenant_id = tenant_id      # type: str
        self.owner_id = owner_id        # type: str
        self.token = token              # type: str
        self.caller_uid = caller_uid    # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.port, 'port')
        self.validate_required(self.uuid, 'uuid')
        self.validate_required(self.role, 'role')
        self.validate_required(self.code, 'code')
        self.validate_required(self.error, 'error')
        self.validate_required(self.tenant_id, 'tenant_id')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.token, 'token')
        self.validate_required(self.caller_uid, 'caller_uid')

    def to_map(self):
        result = {}
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.role is not None:
            result['Role'] = self.role
        if self.code is not None:
            result['Code'] = self.code
        if self.error is not None:
            result['Error'] = self.error
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.token is not None:
            result['Token'] = self.token
        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid
        return result

    def from_map(self, map={}):
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('VpcId') is not None:
            self.vpc_id = map.get('VpcId')
        if map.get('Ip') is not None:
            self.ip = map.get('Ip')
        if map.get('Port') is not None:
            self.port = map.get('Port')
        if map.get('Uuid') is not None:
            self.uuid = map.get('Uuid')
        if map.get('Role') is not None:
            self.role = map.get('Role')
        if map.get('Code') is not None:
            self.code = map.get('Code')
        if map.get('Error') is not None:
            self.error = map.get('Error')
        if map.get('TenantId') is not None:
            self.tenant_id = map.get('TenantId')
        if map.get('OwnerId') is not None:
            self.owner_id = map.get('OwnerId')
        if map.get('Token') is not None:
            self.token = map.get('Token')
        if map.get('CallerUid') is not None:
            self.caller_uid = map.get('CallerUid')
        return self


