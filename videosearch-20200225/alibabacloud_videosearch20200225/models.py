# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import List
except ImportError:
    pass


class GetStorageHistoryRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, video_id=None, page_number=None, page_size=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.video_id = video_id        # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.video_id, 'video_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['InstanceId'] = self.instance_id
        result['VideoId'] = self.video_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.instance_id = map.get('InstanceId')
        self.video_id = map.get('VideoId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class GetStorageHistoryResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: GetStorageHistoryResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GetStorageHistoryResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetStorageHistoryResponseDataList(TeaModel):
    def __init__(self, video_id=None, description=None, storage_type=None, storage_info=None, modified_time=None,
                 video_url=None):
        self.video_id = video_id        # type: str
        self.description = description  # type: str
        self.storage_type = storage_type  # type: int
        self.storage_info = storage_info  # type: int
        self.modified_time = modified_time  # type: int
        self.video_url = video_url      # type: str

    def validate(self):
        self.validate_required(self.video_id, 'video_id')
        self.validate_required(self.description, 'description')
        self.validate_required(self.storage_type, 'storage_type')
        self.validate_required(self.storage_info, 'storage_info')
        self.validate_required(self.modified_time, 'modified_time')
        self.validate_required(self.video_url, 'video_url')

    def to_map(self):
        result = {}
        result['VideoId'] = self.video_id
        result['Description'] = self.description
        result['StorageType'] = self.storage_type
        result['StorageInfo'] = self.storage_info
        result['ModifiedTime'] = self.modified_time
        result['VideoUrl'] = self.video_url
        return result

    def from_map(self, map={}):
        self.video_id = map.get('VideoId')
        self.description = map.get('Description')
        self.storage_type = map.get('StorageType')
        self.storage_info = map.get('StorageInfo')
        self.modified_time = map.get('ModifiedTime')
        self.video_url = map.get('VideoUrl')
        return self


class GetStorageHistoryResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, count=None, list=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.count = count              # type: int
        self.list = list                # type: List[GetStorageHistoryResponseDataList]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.count, 'count')
        self.validate_required(self.list, 'list')
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['Count'] = self.count
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        else:
            result['List'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.count = map.get('Count')
        self.list = []
        if map.get('List') is not None:
            for k in map.get('List'):
                temp_model = GetStorageHistoryResponseDataList()
                self.list.append(temp_model.from_map(k))
        else:
            self.list = None
        return self


class AddStorageVideoTaskRequest(TeaModel):
    def __init__(self, instance_id=None, video_url=None, video_id=None, video_tags=None, callback_url=None,
                 description=None, storage_info=None, client_token=None):
        self.instance_id = instance_id  # type: str
        self.video_url = video_url      # type: str
        self.video_id = video_id        # type: str
        self.video_tags = video_tags    # type: str
        self.callback_url = callback_url  # type: str
        self.description = description  # type: str
        self.storage_info = storage_info  # type: int
        self.client_token = client_token  # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.video_url, 'video_url')
        self.validate_required(self.video_id, 'video_id')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['VideoUrl'] = self.video_url
        result['VideoId'] = self.video_id
        result['VideoTags'] = self.video_tags
        result['CallbackUrl'] = self.callback_url
        result['Description'] = self.description
        result['StorageInfo'] = self.storage_info
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.video_url = map.get('VideoUrl')
        self.video_id = map.get('VideoId')
        self.video_tags = map.get('VideoTags')
        self.callback_url = map.get('CallbackUrl')
        self.description = map.get('Description')
        self.storage_info = map.get('StorageInfo')
        self.client_token = map.get('ClientToken')
        return self


class AddStorageVideoTaskResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: AddStorageVideoTaskResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = AddStorageVideoTaskResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class AddStorageVideoTaskResponseData(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = {}
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.task_id = map.get('TaskId')
        return self


class AddDeletionVideoTaskRequest(TeaModel):
    def __init__(self, client_token=None, video_id=None, instance_id=None):
        self.client_token = client_token  # type: str
        self.video_id = video_id        # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['VideoId'] = self.video_id
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.video_id = map.get('VideoId')
        self.instance_id = map.get('InstanceId')
        return self


class AddDeletionVideoTaskResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.data = map.get('Data')
        return self


class GetTaskStatusRequest(TeaModel):
    def __init__(self, client_token=None, task_id=None, instance_id=None):
        self.client_token = client_token  # type: str
        self.task_id = task_id          # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['TaskId'] = self.task_id
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.task_id = map.get('TaskId')
        self.instance_id = map.get('InstanceId')
        return self


class GetTaskStatusResponse(TeaModel):
    def __init__(self, request_id=None, data=None, task_info=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: int
        self.task_info = task_info      # type: GetTaskStatusResponseTaskInfo

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        self.validate_required(self.task_info, 'task_info')
        if self.task_info:
            self.task_info.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Data'] = self.data
        if self.task_info is not None:
            result['TaskInfo'] = self.task_info.to_map()
        else:
            result['TaskInfo'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.data = map.get('Data')
        if map.get('TaskInfo') is not None:
            temp_model = GetTaskStatusResponseTaskInfo()
            self.task_info = temp_model.from_map(map['TaskInfo'])
        else:
            self.task_info = None
        return self


class GetTaskStatusResponseTaskInfo(TeaModel):
    def __init__(self, analysis_use_time=None, duration=None, process_result_oss=None, resolution=None, status=None,
                 submit_time=None, finish_time=None, task_id=None, error_info=None, storage_info=None, description=None,
                 video_id=None, video_tags=None, video_url=None, query_tags=None, resource_type=None,
                 replace_storage_threshold=None):
        self.analysis_use_time = analysis_use_time  # type: int
        self.duration = duration        # type: float
        self.process_result_oss = process_result_oss  # type: str
        self.resolution = resolution    # type: str
        self.status = status            # type: int
        self.submit_time = submit_time  # type: int
        self.finish_time = finish_time  # type: int
        self.task_id = task_id          # type: int
        self.error_info = error_info    # type: str
        self.storage_info = storage_info  # type: int
        self.description = description  # type: str
        self.video_id = video_id        # type: str
        self.video_tags = video_tags    # type: str
        self.video_url = video_url      # type: str
        self.query_tags = query_tags    # type: str
        self.resource_type = resource_type  # type: str
        self.replace_storage_threshold = replace_storage_threshold  # type: str

    def validate(self):
        self.validate_required(self.analysis_use_time, 'analysis_use_time')
        self.validate_required(self.duration, 'duration')
        self.validate_required(self.process_result_oss, 'process_result_oss')
        self.validate_required(self.resolution, 'resolution')
        self.validate_required(self.status, 'status')
        self.validate_required(self.submit_time, 'submit_time')
        self.validate_required(self.finish_time, 'finish_time')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.error_info, 'error_info')
        self.validate_required(self.storage_info, 'storage_info')
        self.validate_required(self.description, 'description')
        self.validate_required(self.video_id, 'video_id')
        self.validate_required(self.video_tags, 'video_tags')
        self.validate_required(self.video_url, 'video_url')
        self.validate_required(self.query_tags, 'query_tags')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.replace_storage_threshold, 'replace_storage_threshold')

    def to_map(self):
        result = {}
        result['AnalysisUseTime'] = self.analysis_use_time
        result['Duration'] = self.duration
        result['ProcessResultOss'] = self.process_result_oss
        result['Resolution'] = self.resolution
        result['Status'] = self.status
        result['SubmitTime'] = self.submit_time
        result['FinishTime'] = self.finish_time
        result['TaskId'] = self.task_id
        result['ErrorInfo'] = self.error_info
        result['StorageInfo'] = self.storage_info
        result['Description'] = self.description
        result['VideoId'] = self.video_id
        result['VideoTags'] = self.video_tags
        result['VideoUrl'] = self.video_url
        result['QueryTags'] = self.query_tags
        result['ResourceType'] = self.resource_type
        result['ReplaceStorageThreshold'] = self.replace_storage_threshold
        return result

    def from_map(self, map={}):
        self.analysis_use_time = map.get('AnalysisUseTime')
        self.duration = map.get('Duration')
        self.process_result_oss = map.get('ProcessResultOss')
        self.resolution = map.get('Resolution')
        self.status = map.get('Status')
        self.submit_time = map.get('SubmitTime')
        self.finish_time = map.get('FinishTime')
        self.task_id = map.get('TaskId')
        self.error_info = map.get('ErrorInfo')
        self.storage_info = map.get('StorageInfo')
        self.description = map.get('Description')
        self.video_id = map.get('VideoId')
        self.video_tags = map.get('VideoTags')
        self.video_url = map.get('VideoUrl')
        self.query_tags = map.get('QueryTags')
        self.resource_type = map.get('ResourceType')
        self.replace_storage_threshold = map.get('ReplaceStorageThreshold')
        return self


class AddSearchVideoTaskRequest(TeaModel):
    def __init__(self, client_token=None, video_url=None, video_id=None, video_tags=None, return_video_number=None,
                 query_tags=None, storage_type=None, callback_url=None, replace_storage_threshold=None, instance_id=None,
                 description=None, search_type=None):
        self.client_token = client_token  # type: str
        self.video_url = video_url      # type: str
        self.video_id = video_id        # type: str
        self.video_tags = video_tags    # type: str
        self.return_video_number = return_video_number  # type: int
        self.query_tags = query_tags    # type: str
        self.storage_type = storage_type  # type: int
        self.callback_url = callback_url  # type: str
        self.replace_storage_threshold = replace_storage_threshold  # type: float
        self.instance_id = instance_id  # type: str
        self.description = description  # type: str
        self.search_type = search_type  # type: int

    def validate(self):
        self.validate_required(self.video_url, 'video_url')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['VideoUrl'] = self.video_url
        result['VideoId'] = self.video_id
        result['VideoTags'] = self.video_tags
        result['ReturnVideoNumber'] = self.return_video_number
        result['QueryTags'] = self.query_tags
        result['StorageType'] = self.storage_type
        result['CallbackUrl'] = self.callback_url
        result['ReplaceStorageThreshold'] = self.replace_storage_threshold
        result['InstanceId'] = self.instance_id
        result['Description'] = self.description
        result['SearchType'] = self.search_type
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.video_url = map.get('VideoUrl')
        self.video_id = map.get('VideoId')
        self.video_tags = map.get('VideoTags')
        self.return_video_number = map.get('ReturnVideoNumber')
        self.query_tags = map.get('QueryTags')
        self.storage_type = map.get('StorageType')
        self.callback_url = map.get('CallbackUrl')
        self.replace_storage_threshold = map.get('ReplaceStorageThreshold')
        self.instance_id = map.get('InstanceId')
        self.description = map.get('Description')
        self.search_type = map.get('SearchType')
        return self


class AddSearchVideoTaskResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: AddSearchVideoTaskResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = AddSearchVideoTaskResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class AddSearchVideoTaskResponseData(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = {}
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.task_id = map.get('TaskId')
        return self


