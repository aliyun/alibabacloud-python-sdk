# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddDeletionVideoTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        video_id: str = None,
        instance_id: str = None,
    ):
        self.client_token = client_token
        self.video_id = video_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class AddDeletionVideoTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: bool = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class AddDeletionVideoTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddDeletionVideoTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddDeletionVideoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSearchVideoTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        video_url: str = None,
        video_id: str = None,
        video_tags: str = None,
        return_video_number: int = None,
        query_tags: str = None,
        storage_type: int = None,
        callback_url: str = None,
        replace_storage_threshold: float = None,
        instance_id: str = None,
        description: str = None,
        search_type: int = None,
    ):
        self.client_token = client_token
        self.video_url = video_url
        self.video_id = video_id
        self.video_tags = video_tags
        self.return_video_number = return_video_number
        self.query_tags = query_tags
        self.storage_type = storage_type
        self.callback_url = callback_url
        self.replace_storage_threshold = replace_storage_threshold
        self.instance_id = instance_id
        self.description = description
        self.search_type = search_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.video_tags is not None:
            result['VideoTags'] = self.video_tags
        if self.return_video_number is not None:
            result['ReturnVideoNumber'] = self.return_video_number
        if self.query_tags is not None:
            result['QueryTags'] = self.query_tags
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.replace_storage_threshold is not None:
            result['ReplaceStorageThreshold'] = self.replace_storage_threshold
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.search_type is not None:
            result['SearchType'] = self.search_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('VideoTags') is not None:
            self.video_tags = m.get('VideoTags')
        if m.get('ReturnVideoNumber') is not None:
            self.return_video_number = m.get('ReturnVideoNumber')
        if m.get('QueryTags') is not None:
            self.query_tags = m.get('QueryTags')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('ReplaceStorageThreshold') is not None:
            self.replace_storage_threshold = m.get('ReplaceStorageThreshold')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SearchType') is not None:
            self.search_type = m.get('SearchType')
        return self


class AddSearchVideoTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class AddSearchVideoTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: AddSearchVideoTaskResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AddSearchVideoTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class AddSearchVideoTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddSearchVideoTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddSearchVideoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddStorageVideoTaskRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        video_url: str = None,
        video_id: str = None,
        video_tags: str = None,
        callback_url: str = None,
        description: str = None,
        storage_info: int = None,
        client_token: str = None,
    ):
        self.instance_id = instance_id
        self.video_url = video_url
        self.video_id = video_id
        self.video_tags = video_tags
        self.callback_url = callback_url
        self.description = description
        self.storage_info = storage_info
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.video_tags is not None:
            result['VideoTags'] = self.video_tags
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.description is not None:
            result['Description'] = self.description
        if self.storage_info is not None:
            result['StorageInfo'] = self.storage_info
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('VideoTags') is not None:
            self.video_tags = m.get('VideoTags')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('StorageInfo') is not None:
            self.storage_info = m.get('StorageInfo')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class AddStorageVideoTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class AddStorageVideoTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: AddStorageVideoTaskResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AddStorageVideoTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class AddStorageVideoTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddStorageVideoTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddStorageVideoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBatchTaskRequest(TeaModel):
    def __init__(
        self,
        batch_task_type: int = None,
        oss_bucket_name: str = None,
        oss_data_path: str = None,
        oss_meta_file: str = None,
        file_url: str = None,
        role_arn: str = None,
        instance_id: str = None,
        client_token: str = None,
    ):
        self.batch_task_type = batch_task_type
        self.oss_bucket_name = oss_bucket_name
        self.oss_data_path = oss_data_path
        self.oss_meta_file = oss_meta_file
        self.file_url = file_url
        self.role_arn = role_arn
        self.instance_id = instance_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_task_type is not None:
            result['BatchTaskType'] = self.batch_task_type
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_data_path is not None:
            result['OssDataPath'] = self.oss_data_path
        if self.oss_meta_file is not None:
            result['OssMetaFile'] = self.oss_meta_file
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchTaskType') is not None:
            self.batch_task_type = m.get('BatchTaskType')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssDataPath') is not None:
            self.oss_data_path = m.get('OssDataPath')
        if m.get('OssMetaFile') is not None:
            self.oss_meta_file = m.get('OssMetaFile')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateBatchTaskResponseBody(TeaModel):
    def __init__(
        self,
        task_id: int = None,
        request_id: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBatchTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateBatchTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateBatchTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        expire_time: int = None,
        create_time: int = None,
        bundling_type: str = None,
        video_info_update_time: int = None,
        instance_id: str = None,
        concurrency_number: int = None,
        region_id: str = None,
        video_number: int = None,
        instance_name: str = None,
        current_video_capacity: str = None,
        instance_status: int = None,
        max_video_capacity: str = None,
    ):
        self.expire_time = expire_time
        self.create_time = create_time
        self.bundling_type = bundling_type
        self.video_info_update_time = video_info_update_time
        self.instance_id = instance_id
        self.concurrency_number = concurrency_number
        self.region_id = region_id
        self.video_number = video_number
        self.instance_name = instance_name
        self.current_video_capacity = current_video_capacity
        self.instance_status = instance_status
        self.max_video_capacity = max_video_capacity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.bundling_type is not None:
            result['BundlingType'] = self.bundling_type
        if self.video_info_update_time is not None:
            result['VideoInfoUpdateTime'] = self.video_info_update_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.concurrency_number is not None:
            result['ConcurrencyNumber'] = self.concurrency_number
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.video_number is not None:
            result['VideoNumber'] = self.video_number
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.current_video_capacity is not None:
            result['CurrentVideoCapacity'] = self.current_video_capacity
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.max_video_capacity is not None:
            result['MaxVideoCapacity'] = self.max_video_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('BundlingType') is not None:
            self.bundling_type = m.get('BundlingType')
        if m.get('VideoInfoUpdateTime') is not None:
            self.video_info_update_time = m.get('VideoInfoUpdateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ConcurrencyNumber') is not None:
            self.concurrency_number = m.get('ConcurrencyNumber')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VideoNumber') is not None:
            self.video_number = m.get('VideoNumber')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('CurrentVideoCapacity') is not None:
            self.current_video_capacity = m.get('CurrentVideoCapacity')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('MaxVideoCapacity') is not None:
            self.max_video_capacity = m.get('MaxVideoCapacity')
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetInstanceResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStorageHistoryRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        video_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.video_id = video_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetStorageHistoryResponseBodyDataList(TeaModel):
    def __init__(
        self,
        storage_info: int = None,
        modified_time: int = None,
        description: str = None,
        video_id: str = None,
        storage_type: int = None,
        video_url: str = None,
    ):
        self.storage_info = storage_info
        self.modified_time = modified_time
        self.description = description
        self.video_id = video_id
        self.storage_type = storage_type
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.storage_info is not None:
            result['StorageInfo'] = self.storage_info
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.description is not None:
            result['Description'] = self.description
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StorageInfo') is not None:
            self.storage_info = m.get('StorageInfo')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class GetStorageHistoryResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[GetStorageHistoryResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.count = count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetStorageHistoryResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class GetStorageHistoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetStorageHistoryResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetStorageHistoryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetStorageHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetStorageHistoryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetStorageHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskStatusRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        task_id: str = None,
        instance_id: str = None,
    ):
        self.client_token = client_token
        self.task_id = task_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetTaskStatusResponseBodyTaskInfo(TeaModel):
    def __init__(
        self,
        status: int = None,
        storage_info: int = None,
        finish_time: int = None,
        video_id: str = None,
        query_tags: str = None,
        video_tags: str = None,
        error_info: str = None,
        resource_type: str = None,
        description: str = None,
        replace_storage_threshold: str = None,
        duration: float = None,
        analysis_use_time: int = None,
        task_id: int = None,
        resolution: str = None,
        process_result_oss: str = None,
        submit_time: int = None,
        video_url: str = None,
    ):
        self.status = status
        self.storage_info = storage_info
        self.finish_time = finish_time
        self.video_id = video_id
        self.query_tags = query_tags
        self.video_tags = video_tags
        self.error_info = error_info
        self.resource_type = resource_type
        self.description = description
        self.replace_storage_threshold = replace_storage_threshold
        self.duration = duration
        self.analysis_use_time = analysis_use_time
        self.task_id = task_id
        self.resolution = resolution
        self.process_result_oss = process_result_oss
        self.submit_time = submit_time
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_info is not None:
            result['StorageInfo'] = self.storage_info
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.query_tags is not None:
            result['QueryTags'] = self.query_tags
        if self.video_tags is not None:
            result['VideoTags'] = self.video_tags
        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.description is not None:
            result['Description'] = self.description
        if self.replace_storage_threshold is not None:
            result['ReplaceStorageThreshold'] = self.replace_storage_threshold
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.analysis_use_time is not None:
            result['AnalysisUseTime'] = self.analysis_use_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.process_result_oss is not None:
            result['ProcessResultOss'] = self.process_result_oss
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageInfo') is not None:
            self.storage_info = m.get('StorageInfo')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('QueryTags') is not None:
            self.query_tags = m.get('QueryTags')
        if m.get('VideoTags') is not None:
            self.video_tags = m.get('VideoTags')
        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ReplaceStorageThreshold') is not None:
            self.replace_storage_threshold = m.get('ReplaceStorageThreshold')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('AnalysisUseTime') is not None:
            self.analysis_use_time = m.get('AnalysisUseTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('ProcessResultOss') is not None:
            self.process_result_oss = m.get('ProcessResultOss')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class GetTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        task_info: GetTaskStatusResponseBodyTaskInfo = None,
        request_id: str = None,
        data: int = None,
    ):
        self.task_info = task_info
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.task_info:
            self.task_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_info is not None:
            result['TaskInfo'] = self.task_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskInfo') is not None:
            temp_model = GetTaskStatusResponseBodyTaskInfo()
            self.task_info = temp_model.from_map(m['TaskInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTaskStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBatchTaskRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        client_token: str = None,
        batch_task_type: str = None,
        status: str = None,
        instance_id: str = None,
        bucket_name: str = None,
        data_path: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.client_token = client_token
        self.batch_task_type = batch_task_type
        self.status = status
        self.instance_id = instance_id
        self.bucket_name = bucket_name
        self.data_path = data_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.batch_task_type is not None:
            result['BatchTaskType'] = self.batch_task_type
        if self.status is not None:
            result['Status'] = self.status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.data_path is not None:
            result['DataPath'] = self.data_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('BatchTaskType') is not None:
            self.batch_task_type = m.get('BatchTaskType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('DataPath') is not None:
            self.data_path = m.get('DataPath')
        return self


class ListBatchTaskResponseBodyDataList(TeaModel):
    def __init__(
        self,
        status: int = None,
        task_type: int = None,
        modified_time: int = None,
        process_message: str = None,
        bucket_name: str = None,
        meta_file: str = None,
        data_path: str = None,
        task_id: int = None,
        region_id: str = None,
    ):
        self.status = status
        self.task_type = task_type
        self.modified_time = modified_time
        self.process_message = process_message
        self.bucket_name = bucket_name
        self.meta_file = meta_file
        self.data_path = data_path
        self.task_id = task_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.process_message is not None:
            result['ProcessMessage'] = self.process_message
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.meta_file is not None:
            result['MetaFile'] = self.meta_file
        if self.data_path is not None:
            result['DataPath'] = self.data_path
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ProcessMessage') is not None:
            self.process_message = m.get('ProcessMessage')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('MetaFile') is not None:
            self.meta_file = m.get('MetaFile')
        if m.get('DataPath') is not None:
            self.data_path = m.get('DataPath')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListBatchTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListBatchTaskResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.count = count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListBatchTaskResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class ListBatchTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListBatchTaskResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListBatchTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListBatchTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListBatchTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListBatchTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_name: str = None,
        page_number: int = None,
        page_size: int = None,
        tags: str = None,
        status: int = None,
    ):
        self.client_token = client_token
        self.instance_name = instance_name
        self.page_number = page_number
        self.page_size = page_size
        self.tags = tags
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstancesResponseBodyDataListTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListInstancesResponseBodyDataList(TeaModel):
    def __init__(
        self,
        expired_time: str = None,
        create_time: int = None,
        instance_name: str = None,
        instance_status: int = None,
        tags: List[ListInstancesResponseBodyDataListTags] = None,
        instance_id: str = None,
    ):
        self.expired_time = expired_time
        self.create_time = create_time
        self.instance_name = instance_name
        self.instance_status = instance_status
        self.tags = tags
        self.instance_id = instance_id

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListInstancesResponseBodyDataListTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListInstancesResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.count = count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListInstancesResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListInstancesResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListInstancesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSearchVideoTasksRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        task_id: str = None,
        video_name: str = None,
        video_id: str = None,
        page_number: int = None,
        page_size: int = None,
        instance_id: str = None,
        status_list: str = None,
        search_type_list: str = None,
        description: str = None,
    ):
        self.client_token = client_token
        self.task_id = task_id
        self.video_name = video_name
        self.video_id = video_id
        self.page_number = page_number
        self.page_size = page_size
        self.instance_id = instance_id
        self.status_list = status_list
        self.search_type_list = search_type_list
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.video_name is not None:
            result['VideoName'] = self.video_name
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.search_type_list is not None:
            result['SearchTypeList'] = self.search_type_list
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('VideoName') is not None:
            self.video_name = m.get('VideoName')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('SearchTypeList') is not None:
            self.search_type_list = m.get('SearchTypeList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ListSearchVideoTasksResponseBodyDataTaskList(TeaModel):
    def __init__(
        self,
        status: int = None,
        storage_info: int = None,
        video_id: str = None,
        process_time: int = None,
        video_name: str = None,
        query_tags: str = None,
        storage_type: int = None,
        process_result_url: str = None,
        video_tags: str = None,
        error_detail: str = None,
        search_type: int = None,
        modified_time: int = None,
        description: str = None,
        replace_storage_threshold: str = None,
        remote_task_id: str = None,
        task_id: str = None,
        video_url: str = None,
    ):
        self.status = status
        self.storage_info = storage_info
        self.video_id = video_id
        self.process_time = process_time
        self.video_name = video_name
        self.query_tags = query_tags
        self.storage_type = storage_type
        self.process_result_url = process_result_url
        self.video_tags = video_tags
        self.error_detail = error_detail
        self.search_type = search_type
        self.modified_time = modified_time
        self.description = description
        self.replace_storage_threshold = replace_storage_threshold
        self.remote_task_id = remote_task_id
        self.task_id = task_id
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_info is not None:
            result['StorageInfo'] = self.storage_info
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.process_time is not None:
            result['ProcessTime'] = self.process_time
        if self.video_name is not None:
            result['VideoName'] = self.video_name
        if self.query_tags is not None:
            result['QueryTags'] = self.query_tags
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.process_result_url is not None:
            result['ProcessResultUrl'] = self.process_result_url
        if self.video_tags is not None:
            result['VideoTags'] = self.video_tags
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail
        if self.search_type is not None:
            result['SearchType'] = self.search_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.description is not None:
            result['Description'] = self.description
        if self.replace_storage_threshold is not None:
            result['ReplaceStorageThreshold'] = self.replace_storage_threshold
        if self.remote_task_id is not None:
            result['RemoteTaskId'] = self.remote_task_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageInfo') is not None:
            self.storage_info = m.get('StorageInfo')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('ProcessTime') is not None:
            self.process_time = m.get('ProcessTime')
        if m.get('VideoName') is not None:
            self.video_name = m.get('VideoName')
        if m.get('QueryTags') is not None:
            self.query_tags = m.get('QueryTags')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('ProcessResultUrl') is not None:
            self.process_result_url = m.get('ProcessResultUrl')
        if m.get('VideoTags') is not None:
            self.video_tags = m.get('VideoTags')
        if m.get('ErrorDetail') is not None:
            self.error_detail = m.get('ErrorDetail')
        if m.get('SearchType') is not None:
            self.search_type = m.get('SearchType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ReplaceStorageThreshold') is not None:
            self.replace_storage_threshold = m.get('ReplaceStorageThreshold')
        if m.get('RemoteTaskId') is not None:
            self.remote_task_id = m.get('RemoteTaskId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class ListSearchVideoTasksResponseBodyData(TeaModel):
    def __init__(
        self,
        task_list: List[ListSearchVideoTasksResponseBodyDataTaskList] = None,
        page_number: int = None,
        page_size: int = None,
        count: int = None,
    ):
        self.task_list = task_list
        self.page_number = page_number
        self.page_size = page_size
        self.count = count

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = ListSearchVideoTasksResponseBodyDataTaskList()
                self.task_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class ListSearchVideoTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListSearchVideoTasksResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListSearchVideoTasksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListSearchVideoTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSearchVideoTasksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSearchVideoTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStorageVideoTasksRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        task_id: str = None,
        video_name: str = None,
        video_id: str = None,
        page_number: int = None,
        page_size: int = None,
        instance_id: str = None,
        status_list: str = None,
        description: str = None,
        storage_info_list: str = None,
    ):
        self.client_token = client_token
        self.task_id = task_id
        self.video_name = video_name
        self.video_id = video_id
        self.page_number = page_number
        self.page_size = page_size
        self.instance_id = instance_id
        self.status_list = status_list
        self.description = description
        self.storage_info_list = storage_info_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.video_name is not None:
            result['VideoName'] = self.video_name
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.description is not None:
            result['Description'] = self.description
        if self.storage_info_list is not None:
            result['StorageInfoList'] = self.storage_info_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('VideoName') is not None:
            self.video_name = m.get('VideoName')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('StorageInfoList') is not None:
            self.storage_info_list = m.get('StorageInfoList')
        return self


class ListStorageVideoTasksResponseBodyDataTaskList(TeaModel):
    def __init__(
        self,
        status: str = None,
        storage_info: int = None,
        error_detail: str = None,
        modified_time: int = None,
        description: str = None,
        process_time: int = None,
        video_id: str = None,
        video_name: str = None,
        remote_task_id: str = None,
        task_id: int = None,
        video_url: str = None,
    ):
        self.status = status
        self.storage_info = storage_info
        self.error_detail = error_detail
        self.modified_time = modified_time
        self.description = description
        self.process_time = process_time
        self.video_id = video_id
        self.video_name = video_name
        self.remote_task_id = remote_task_id
        self.task_id = task_id
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_info is not None:
            result['StorageInfo'] = self.storage_info
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.description is not None:
            result['Description'] = self.description
        if self.process_time is not None:
            result['ProcessTime'] = self.process_time
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.video_name is not None:
            result['VideoName'] = self.video_name
        if self.remote_task_id is not None:
            result['RemoteTaskId'] = self.remote_task_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageInfo') is not None:
            self.storage_info = m.get('StorageInfo')
        if m.get('ErrorDetail') is not None:
            self.error_detail = m.get('ErrorDetail')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProcessTime') is not None:
            self.process_time = m.get('ProcessTime')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('VideoName') is not None:
            self.video_name = m.get('VideoName')
        if m.get('RemoteTaskId') is not None:
            self.remote_task_id = m.get('RemoteTaskId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class ListStorageVideoTasksResponseBodyData(TeaModel):
    def __init__(
        self,
        task_list: List[ListStorageVideoTasksResponseBodyDataTaskList] = None,
        page_number: int = None,
        page_size: int = None,
        count: int = None,
    ):
        self.task_list = task_list
        self.page_number = page_number
        self.page_size = page_size
        self.count = count

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = ListStorageVideoTasksResponseBodyDataTaskList()
                self.task_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class ListStorageVideoTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListStorageVideoTasksResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListStorageVideoTasksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListStorageVideoTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListStorageVideoTasksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListStorageVideoTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


