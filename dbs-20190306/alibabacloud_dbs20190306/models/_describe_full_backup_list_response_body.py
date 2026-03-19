# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dbs20190306 import models as main_models
from darabonba.model import DaraModel

class DescribeFullBackupListResponseBody(DaraModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        items: main_models.DescribeFullBackupListResponseBodyItems = None,
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
        # Indicates whether the operation succeeded. Valid values:
        # 
        # - **true**: The operation succeeded.
        # 
        # - **false**: The operation failed.
        self.success = success
        # The total number of full backup jobs.
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
            temp_model = main_models.DescribeFullBackupListResponseBodyItems()
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

class DescribeFullBackupListResponseBodyItems(DaraModel):
    def __init__(
        self,
        full_backup_file: List[main_models.DescribeFullBackupListResponseBodyItemsFullBackupFile] = None,
    ):
        self.full_backup_file = full_backup_file

    def validate(self):
        if self.full_backup_file:
            for v1 in self.full_backup_file:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FullBackupFile'] = []
        if self.full_backup_file is not None:
            for k1 in self.full_backup_file:
                result['FullBackupFile'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.full_backup_file = []
        if m.get('FullBackupFile') is not None:
            for k1 in m.get('FullBackupFile'):
                temp_model = main_models.DescribeFullBackupListResponseBodyItemsFullBackupFile()
                self.full_backup_file.append(temp_model.from_map(k1))

        return self

class DescribeFullBackupListResponseBodyItemsFullBackupFile(DaraModel):
    def __init__(
        self,
        backup_gateway_identifier: str = None,
        backup_objects: str = None,
        backup_set_expired_time: int = None,
        backup_set_id: str = None,
        backup_size: int = None,
        backup_status: str = None,
        create_time: int = None,
        cross_aliyun_id: str = None,
        cross_role_name: str = None,
        end_time: int = None,
        err_message: str = None,
        finish_time: int = None,
        logical_full_backup_progress: int = None,
        logical_structure_backup_progress: int = None,
        source_endpoint_enable_ssl: str = None,
        source_endpoint_host: str = None,
        source_endpoint_instance_id: str = None,
        source_endpoint_instance_type: str = None,
        source_endpoint_ip_port: str = None,
        source_endpoint_port: str = None,
        source_endpoint_region: str = None,
        source_endpoint_user_name: str = None,
        start_time: int = None,
        storage_encrypt_method: str = None,
        storage_method: str = None,
    ):
        self.backup_gateway_identifier = backup_gateway_identifier
        self.backup_objects = backup_objects
        self.backup_set_expired_time = backup_set_expired_time
        self.backup_set_id = backup_set_id
        self.backup_size = backup_size
        self.backup_status = backup_status
        self.create_time = create_time
        self.cross_aliyun_id = cross_aliyun_id
        self.cross_role_name = cross_role_name
        self.end_time = end_time
        self.err_message = err_message
        self.finish_time = finish_time
        self.logical_full_backup_progress = logical_full_backup_progress
        self.logical_structure_backup_progress = logical_structure_backup_progress
        self.source_endpoint_enable_ssl = source_endpoint_enable_ssl
        self.source_endpoint_host = source_endpoint_host
        self.source_endpoint_instance_id = source_endpoint_instance_id
        self.source_endpoint_instance_type = source_endpoint_instance_type
        self.source_endpoint_ip_port = source_endpoint_ip_port
        self.source_endpoint_port = source_endpoint_port
        self.source_endpoint_region = source_endpoint_region
        self.source_endpoint_user_name = source_endpoint_user_name
        self.start_time = start_time
        self.storage_encrypt_method = storage_encrypt_method
        self.storage_method = storage_method

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_gateway_identifier is not None:
            result['BackupGatewayIdentifier'] = self.backup_gateway_identifier

        if self.backup_objects is not None:
            result['BackupObjects'] = self.backup_objects

        if self.backup_set_expired_time is not None:
            result['BackupSetExpiredTime'] = self.backup_set_expired_time

        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id

        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size

        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cross_aliyun_id is not None:
            result['CrossAliyunId'] = self.cross_aliyun_id

        if self.cross_role_name is not None:
            result['CrossRoleName'] = self.cross_role_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.logical_full_backup_progress is not None:
            result['LogicalFullBackupProgress'] = self.logical_full_backup_progress

        if self.logical_structure_backup_progress is not None:
            result['LogicalStructureBackupProgress'] = self.logical_structure_backup_progress

        if self.source_endpoint_enable_ssl is not None:
            result['SourceEndpointEnableSsl'] = self.source_endpoint_enable_ssl

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

        if self.source_endpoint_user_name is not None:
            result['SourceEndpointUserName'] = self.source_endpoint_user_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.storage_encrypt_method is not None:
            result['StorageEncryptMethod'] = self.storage_encrypt_method

        if self.storage_method is not None:
            result['StorageMethod'] = self.storage_method

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupGatewayIdentifier') is not None:
            self.backup_gateway_identifier = m.get('BackupGatewayIdentifier')

        if m.get('BackupObjects') is not None:
            self.backup_objects = m.get('BackupObjects')

        if m.get('BackupSetExpiredTime') is not None:
            self.backup_set_expired_time = m.get('BackupSetExpiredTime')

        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')

        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')

        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CrossAliyunId') is not None:
            self.cross_aliyun_id = m.get('CrossAliyunId')

        if m.get('CrossRoleName') is not None:
            self.cross_role_name = m.get('CrossRoleName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('LogicalFullBackupProgress') is not None:
            self.logical_full_backup_progress = m.get('LogicalFullBackupProgress')

        if m.get('LogicalStructureBackupProgress') is not None:
            self.logical_structure_backup_progress = m.get('LogicalStructureBackupProgress')

        if m.get('SourceEndpointEnableSsl') is not None:
            self.source_endpoint_enable_ssl = m.get('SourceEndpointEnableSsl')

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

        if m.get('SourceEndpointUserName') is not None:
            self.source_endpoint_user_name = m.get('SourceEndpointUserName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StorageEncryptMethod') is not None:
            self.storage_encrypt_method = m.get('StorageEncryptMethod')

        if m.get('StorageMethod') is not None:
            self.storage_method = m.get('StorageMethod')

        return self

