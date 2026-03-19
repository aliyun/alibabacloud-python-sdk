# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dbs20190306 import models as main_models
from darabonba.model import DaraModel

class DescribeIncrementBackupListResponseBody(DaraModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        items: main_models.DescribeIncrementBackupListResponseBodyItems = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        self.items = items
        # The page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # 
        # - **false**: The request failed.
        self.success = success
        # The total number of incremental backup tasks.
        self.total_elements = total_elements
        # The total number of pages.
        self.total_pages = total_pages

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeIncrementBackupListResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class DescribeIncrementBackupListResponseBodyItems(DaraModel):
    def __init__(
        self,
        increment_backup_file: List[main_models.DescribeIncrementBackupListResponseBodyItemsIncrementBackupFile] = None,
    ):
        self.increment_backup_file = increment_backup_file

    def validate(self):
        if self.increment_backup_file:
            for v1 in self.increment_backup_file:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IncrementBackupFile'] = []
        if self.increment_backup_file is not None:
            for k1 in self.increment_backup_file:
                result['IncrementBackupFile'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.increment_backup_file = []
        if m.get('IncrementBackupFile') is not None:
            for k1 in m.get('IncrementBackupFile'):
                temp_model = main_models.DescribeIncrementBackupListResponseBodyItemsIncrementBackupFile()
                self.increment_backup_file.append(temp_model.from_map(k1))

        return self

class DescribeIncrementBackupListResponseBodyItemsIncrementBackupFile(DaraModel):
    def __init__(
        self,
        backup_set_expired_time: int = None,
        backup_set_id: str = None,
        backup_set_job_id: str = None,
        backup_size: int = None,
        backup_status: str = None,
        end_time: int = None,
        source_endpoint_host: str = None,
        source_endpoint_instance_id: str = None,
        source_endpoint_instance_type: str = None,
        source_endpoint_ip_port: str = None,
        source_endpoint_port: str = None,
        source_endpoint_region: str = None,
        start_time: int = None,
        storage_method: str = None,
    ):
        self.backup_set_expired_time = backup_set_expired_time
        self.backup_set_id = backup_set_id
        self.backup_set_job_id = backup_set_job_id
        self.backup_size = backup_size
        self.backup_status = backup_status
        self.end_time = end_time
        self.source_endpoint_host = source_endpoint_host
        self.source_endpoint_instance_id = source_endpoint_instance_id
        self.source_endpoint_instance_type = source_endpoint_instance_type
        self.source_endpoint_ip_port = source_endpoint_ip_port
        self.source_endpoint_port = source_endpoint_port
        self.source_endpoint_region = source_endpoint_region
        self.start_time = start_time
        self.storage_method = storage_method

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_set_expired_time is not None:
            result['BackupSetExpiredTime'] = self.backup_set_expired_time

        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id

        if self.backup_set_job_id is not None:
            result['BackupSetJobId'] = self.backup_set_job_id

        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size

        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.source_endpoint_host is not None:
            result['SourceEndpointHost'] = self.source_endpoint_host

        if self.source_endpoint_instance_id is not None:
            result['SourceEndpointInstanceId'] = self.source_endpoint_instance_id

        if self.source_endpoint_instance_type is not None:
            result['SourceEndpointInstanceType'] = self.source_endpoint_instance_type

        if self.source_endpoint_ip_port is not None:
            result['SourceEndpointIpPort'] = self.source_endpoint_ip_port

        if self.source_endpoint_port is not None:
            result['SourceEndpointPort'] = self.source_endpoint_port

        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.storage_method is not None:
            result['StorageMethod'] = self.storage_method

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetExpiredTime') is not None:
            self.backup_set_expired_time = m.get('BackupSetExpiredTime')

        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')

        if m.get('BackupSetJobId') is not None:
            self.backup_set_job_id = m.get('BackupSetJobId')

        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')

        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('SourceEndpointHost') is not None:
            self.source_endpoint_host = m.get('SourceEndpointHost')

        if m.get('SourceEndpointInstanceId') is not None:
            self.source_endpoint_instance_id = m.get('SourceEndpointInstanceId')

        if m.get('SourceEndpointInstanceType') is not None:
            self.source_endpoint_instance_type = m.get('SourceEndpointInstanceType')

        if m.get('SourceEndpointIpPort') is not None:
            self.source_endpoint_ip_port = m.get('SourceEndpointIpPort')

        if m.get('SourceEndpointPort') is not None:
            self.source_endpoint_port = m.get('SourceEndpointPort')

        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StorageMethod') is not None:
            self.storage_method = m.get('StorageMethod')

        return self

