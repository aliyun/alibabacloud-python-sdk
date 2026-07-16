# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dsw20220101 import models as main_models
from darabonba.model import DaraModel

class ListTempFilesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        quota: main_models.ListTempFilesResponseBodyQuota = None,
        request_id: str = None,
        success: bool = None,
        temp_files: List[main_models.ListTempFilesResponseBodyTempFiles] = None,
        total_count: int = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.quota = quota
        self.request_id = request_id
        self.success = success
        self.temp_files = temp_files
        self.total_count = total_count

    def validate(self):
        if self.quota:
            self.quota.validate()
        if self.temp_files:
            for v1 in self.temp_files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.quota is not None:
            result['Quota'] = self.quota.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        result['TempFiles'] = []
        if self.temp_files is not None:
            for k1 in self.temp_files:
                result['TempFiles'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Quota') is not None:
            temp_model = main_models.ListTempFilesResponseBodyQuota()
            self.quota = temp_model.from_map(m.get('Quota'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        self.temp_files = []
        if m.get('TempFiles') is not None:
            for k1 in m.get('TempFiles'):
                temp_model = main_models.ListTempFilesResponseBodyTempFiles()
                self.temp_files.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTempFilesResponseBodyTempFiles(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        capacity: int = None,
        description: str = None,
        download_url: str = None,
        gmt_create_time: str = None,
        gmt_expired_time: str = None,
        gmt_modified_time: str = None,
        instance_id: str = None,
        name: str = None,
        owner_id: str = None,
        prefix: str = None,
        status: str = None,
        task_id: str = None,
        type: str = None,
        upload_url: str = None,
        user_id: str = None,
        uuid: str = None,
    ):
        self.bandwidth = bandwidth
        self.capacity = capacity
        self.description = description
        self.download_url = download_url
        self.gmt_create_time = gmt_create_time
        self.gmt_expired_time = gmt_expired_time
        self.gmt_modified_time = gmt_modified_time
        self.instance_id = instance_id
        self.name = name
        # Owner Id
        self.owner_id = owner_id
        self.prefix = prefix
        self.status = status
        self.task_id = task_id
        self.type = type
        self.upload_url = upload_url
        self.user_id = user_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.description is not None:
            result['Description'] = self.description

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_expired_time is not None:
            result['GmtExpiredTime'] = self.gmt_expired_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.type is not None:
            result['Type'] = self.type

        if self.upload_url is not None:
            result['UploadUrl'] = self.upload_url

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtExpiredTime') is not None:
            self.gmt_expired_time = m.get('GmtExpiredTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UploadUrl') is not None:
            self.upload_url = m.get('UploadUrl')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class ListTempFilesResponseBodyQuota(DaraModel):
    def __init__(
        self,
        total_capacity: int = None,
        total_file_num: int = None,
        used_capacity: int = None,
        used_file_num: int = None,
    ):
        self.total_capacity = total_capacity
        self.total_file_num = total_file_num
        self.used_capacity = used_capacity
        self.used_file_num = used_file_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.total_capacity is not None:
            result['TotalCapacity'] = self.total_capacity

        if self.total_file_num is not None:
            result['TotalFileNum'] = self.total_file_num

        if self.used_capacity is not None:
            result['UsedCapacity'] = self.used_capacity

        if self.used_file_num is not None:
            result['UsedFileNum'] = self.used_file_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCapacity') is not None:
            self.total_capacity = m.get('TotalCapacity')

        if m.get('TotalFileNum') is not None:
            self.total_file_num = m.get('TotalFileNum')

        if m.get('UsedCapacity') is not None:
            self.used_capacity = m.get('UsedCapacity')

        if m.get('UsedFileNum') is not None:
            self.used_file_num = m.get('UsedFileNum')

        return self

