# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dbs20190306 import models as main_models
from darabonba.model import DaraModel

class DescribeRestoreTaskListResponseBody(DaraModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        items: main_models.DescribeRestoreTaskListResponseBodyItems = None,
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
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The total number of restore jobs.
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
            temp_model = main_models.DescribeRestoreTaskListResponseBodyItems()
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

class DescribeRestoreTaskListResponseBodyItems(DaraModel):
    def __init__(
        self,
        restore_task_detail: List[main_models.DescribeRestoreTaskListResponseBodyItemsRestoreTaskDetail] = None,
    ):
        self.restore_task_detail = restore_task_detail

    def validate(self):
        if self.restore_task_detail:
            for v1 in self.restore_task_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RestoreTaskDetail'] = []
        if self.restore_task_detail is not None:
            for k1 in self.restore_task_detail:
                result['RestoreTaskDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.restore_task_detail = []
        if m.get('RestoreTaskDetail') is not None:
            for k1 in m.get('RestoreTaskDetail'):
                temp_model = main_models.DescribeRestoreTaskListResponseBodyItemsRestoreTaskDetail()
                self.restore_task_detail.append(temp_model.from_map(k1))

        return self

class DescribeRestoreTaskListResponseBodyItemsRestoreTaskDetail(DaraModel):
    def __init__(
        self,
        backup_gateway_id: int = None,
        backup_gateway_identifier: str = None,
        backup_plan_id: str = None,
        backup_set_id: str = None,
        backup_source_oss_region: str = None,
        continuous_restore_progress: int = None,
        cross_aliyun_id: str = None,
        cross_role_name: str = None,
        destination_endpoint_database_name: str = None,
        destination_endpoint_enable_ssl: str = None,
        destination_endpoint_host: str = None,
        destination_endpoint_instance_id: str = None,
        destination_endpoint_instance_type: str = None,
        destination_endpoint_ip_port: str = None,
        destination_endpoint_oracle_sid: str = None,
        destination_endpoint_port: str = None,
        destination_endpoint_region: str = None,
        destination_endpoint_user_name: str = None,
        err_message: str = None,
        full_data_restore_progress: int = None,
        full_stru_after_restore_progress: int = None,
        full_strufore_restore_progress: int = None,
        physical_backup_recover_progress: int = None,
        physical_database_online_progress: int = None,
        physical_full_and_increment_backup_recover_progress: int = None,
        physical_full_backup_recover_progress: int = None,
        physical_increment_backup_recover_progress: int = None,
        restore_destination_mode: str = None,
        restore_dir: str = None,
        restore_objects: str = None,
        restore_status: str = None,
        restore_task_create_time: int = None,
        restore_task_finish_time: int = None,
        restore_task_id: str = None,
        restore_task_name: str = None,
        restore_time: int = None,
    ):
        self.backup_gateway_id = backup_gateway_id
        self.backup_gateway_identifier = backup_gateway_identifier
        self.backup_plan_id = backup_plan_id
        self.backup_set_id = backup_set_id
        self.backup_source_oss_region = backup_source_oss_region
        self.continuous_restore_progress = continuous_restore_progress
        self.cross_aliyun_id = cross_aliyun_id
        self.cross_role_name = cross_role_name
        self.destination_endpoint_database_name = destination_endpoint_database_name
        self.destination_endpoint_enable_ssl = destination_endpoint_enable_ssl
        self.destination_endpoint_host = destination_endpoint_host
        self.destination_endpoint_instance_id = destination_endpoint_instance_id
        self.destination_endpoint_instance_type = destination_endpoint_instance_type
        self.destination_endpoint_ip_port = destination_endpoint_ip_port
        self.destination_endpoint_oracle_sid = destination_endpoint_oracle_sid
        self.destination_endpoint_port = destination_endpoint_port
        self.destination_endpoint_region = destination_endpoint_region
        self.destination_endpoint_user_name = destination_endpoint_user_name
        self.err_message = err_message
        self.full_data_restore_progress = full_data_restore_progress
        self.full_stru_after_restore_progress = full_stru_after_restore_progress
        self.full_strufore_restore_progress = full_strufore_restore_progress
        self.physical_backup_recover_progress = physical_backup_recover_progress
        self.physical_database_online_progress = physical_database_online_progress
        self.physical_full_and_increment_backup_recover_progress = physical_full_and_increment_backup_recover_progress
        self.physical_full_backup_recover_progress = physical_full_backup_recover_progress
        self.physical_increment_backup_recover_progress = physical_increment_backup_recover_progress
        self.restore_destination_mode = restore_destination_mode
        self.restore_dir = restore_dir
        self.restore_objects = restore_objects
        self.restore_status = restore_status
        self.restore_task_create_time = restore_task_create_time
        self.restore_task_finish_time = restore_task_finish_time
        self.restore_task_id = restore_task_id
        self.restore_task_name = restore_task_name
        self.restore_time = restore_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id

        if self.backup_gateway_identifier is not None:
            result['BackupGatewayIdentifier'] = self.backup_gateway_identifier

        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id

        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id

        if self.backup_source_oss_region is not None:
            result['BackupSourceOssRegion'] = self.backup_source_oss_region

        if self.continuous_restore_progress is not None:
            result['ContinuousRestoreProgress'] = self.continuous_restore_progress

        if self.cross_aliyun_id is not None:
            result['CrossAliyunId'] = self.cross_aliyun_id

        if self.cross_role_name is not None:
            result['CrossRoleName'] = self.cross_role_name

        if self.destination_endpoint_database_name is not None:
            result['DestinationEndpointDatabaseName'] = self.destination_endpoint_database_name

        if self.destination_endpoint_enable_ssl is not None:
            result['DestinationEndpointEnableSsl'] = self.destination_endpoint_enable_ssl

        if self.destination_endpoint_host is not None:
            result['DestinationEndpointHost'] = self.destination_endpoint_host

        if self.destination_endpoint_instance_id is not None:
            result['DestinationEndpointInstanceID'] = self.destination_endpoint_instance_id

        if self.destination_endpoint_instance_type is not None:
            result['DestinationEndpointInstanceType'] = self.destination_endpoint_instance_type

        if self.destination_endpoint_ip_port is not None:
            result['DestinationEndpointIpPort'] = self.destination_endpoint_ip_port

        if self.destination_endpoint_oracle_sid is not None:
            result['DestinationEndpointOracleSID'] = self.destination_endpoint_oracle_sid

        if self.destination_endpoint_port is not None:
            result['DestinationEndpointPort'] = self.destination_endpoint_port

        if self.destination_endpoint_region is not None:
            result['DestinationEndpointRegion'] = self.destination_endpoint_region

        if self.destination_endpoint_user_name is not None:
            result['DestinationEndpointUserName'] = self.destination_endpoint_user_name

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.full_data_restore_progress is not None:
            result['FullDataRestoreProgress'] = self.full_data_restore_progress

        if self.full_stru_after_restore_progress is not None:
            result['FullStruAfterRestoreProgress'] = self.full_stru_after_restore_progress

        if self.full_strufore_restore_progress is not None:
            result['FullStruforeRestoreProgress'] = self.full_strufore_restore_progress

        if self.physical_backup_recover_progress is not None:
            result['PhysicalBackupRecoverProgress'] = self.physical_backup_recover_progress

        if self.physical_database_online_progress is not None:
            result['PhysicalDatabaseOnlineProgress'] = self.physical_database_online_progress

        if self.physical_full_and_increment_backup_recover_progress is not None:
            result['PhysicalFullAndIncrementBackupRecoverProgress'] = self.physical_full_and_increment_backup_recover_progress

        if self.physical_full_backup_recover_progress is not None:
            result['PhysicalFullBackupRecoverProgress'] = self.physical_full_backup_recover_progress

        if self.physical_increment_backup_recover_progress is not None:
            result['PhysicalIncrementBackupRecoverProgress'] = self.physical_increment_backup_recover_progress

        if self.restore_destination_mode is not None:
            result['RestoreDestinationMode'] = self.restore_destination_mode

        if self.restore_dir is not None:
            result['RestoreDir'] = self.restore_dir

        if self.restore_objects is not None:
            result['RestoreObjects'] = self.restore_objects

        if self.restore_status is not None:
            result['RestoreStatus'] = self.restore_status

        if self.restore_task_create_time is not None:
            result['RestoreTaskCreateTime'] = self.restore_task_create_time

        if self.restore_task_finish_time is not None:
            result['RestoreTaskFinishTime'] = self.restore_task_finish_time

        if self.restore_task_id is not None:
            result['RestoreTaskId'] = self.restore_task_id

        if self.restore_task_name is not None:
            result['RestoreTaskName'] = self.restore_task_name

        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')

        if m.get('BackupGatewayIdentifier') is not None:
            self.backup_gateway_identifier = m.get('BackupGatewayIdentifier')

        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')

        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')

        if m.get('BackupSourceOssRegion') is not None:
            self.backup_source_oss_region = m.get('BackupSourceOssRegion')

        if m.get('ContinuousRestoreProgress') is not None:
            self.continuous_restore_progress = m.get('ContinuousRestoreProgress')

        if m.get('CrossAliyunId') is not None:
            self.cross_aliyun_id = m.get('CrossAliyunId')

        if m.get('CrossRoleName') is not None:
            self.cross_role_name = m.get('CrossRoleName')

        if m.get('DestinationEndpointDatabaseName') is not None:
            self.destination_endpoint_database_name = m.get('DestinationEndpointDatabaseName')

        if m.get('DestinationEndpointEnableSsl') is not None:
            self.destination_endpoint_enable_ssl = m.get('DestinationEndpointEnableSsl')

        if m.get('DestinationEndpointHost') is not None:
            self.destination_endpoint_host = m.get('DestinationEndpointHost')

        if m.get('DestinationEndpointInstanceID') is not None:
            self.destination_endpoint_instance_id = m.get('DestinationEndpointInstanceID')

        if m.get('DestinationEndpointInstanceType') is not None:
            self.destination_endpoint_instance_type = m.get('DestinationEndpointInstanceType')

        if m.get('DestinationEndpointIpPort') is not None:
            self.destination_endpoint_ip_port = m.get('DestinationEndpointIpPort')

        if m.get('DestinationEndpointOracleSID') is not None:
            self.destination_endpoint_oracle_sid = m.get('DestinationEndpointOracleSID')

        if m.get('DestinationEndpointPort') is not None:
            self.destination_endpoint_port = m.get('DestinationEndpointPort')

        if m.get('DestinationEndpointRegion') is not None:
            self.destination_endpoint_region = m.get('DestinationEndpointRegion')

        if m.get('DestinationEndpointUserName') is not None:
            self.destination_endpoint_user_name = m.get('DestinationEndpointUserName')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('FullDataRestoreProgress') is not None:
            self.full_data_restore_progress = m.get('FullDataRestoreProgress')

        if m.get('FullStruAfterRestoreProgress') is not None:
            self.full_stru_after_restore_progress = m.get('FullStruAfterRestoreProgress')

        if m.get('FullStruforeRestoreProgress') is not None:
            self.full_strufore_restore_progress = m.get('FullStruforeRestoreProgress')

        if m.get('PhysicalBackupRecoverProgress') is not None:
            self.physical_backup_recover_progress = m.get('PhysicalBackupRecoverProgress')

        if m.get('PhysicalDatabaseOnlineProgress') is not None:
            self.physical_database_online_progress = m.get('PhysicalDatabaseOnlineProgress')

        if m.get('PhysicalFullAndIncrementBackupRecoverProgress') is not None:
            self.physical_full_and_increment_backup_recover_progress = m.get('PhysicalFullAndIncrementBackupRecoverProgress')

        if m.get('PhysicalFullBackupRecoverProgress') is not None:
            self.physical_full_backup_recover_progress = m.get('PhysicalFullBackupRecoverProgress')

        if m.get('PhysicalIncrementBackupRecoverProgress') is not None:
            self.physical_increment_backup_recover_progress = m.get('PhysicalIncrementBackupRecoverProgress')

        if m.get('RestoreDestinationMode') is not None:
            self.restore_destination_mode = m.get('RestoreDestinationMode')

        if m.get('RestoreDir') is not None:
            self.restore_dir = m.get('RestoreDir')

        if m.get('RestoreObjects') is not None:
            self.restore_objects = m.get('RestoreObjects')

        if m.get('RestoreStatus') is not None:
            self.restore_status = m.get('RestoreStatus')

        if m.get('RestoreTaskCreateTime') is not None:
            self.restore_task_create_time = m.get('RestoreTaskCreateTime')

        if m.get('RestoreTaskFinishTime') is not None:
            self.restore_task_finish_time = m.get('RestoreTaskFinishTime')

        if m.get('RestoreTaskId') is not None:
            self.restore_task_id = m.get('RestoreTaskId')

        if m.get('RestoreTaskName') is not None:
            self.restore_task_name = m.get('RestoreTaskName')

        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')

        return self

