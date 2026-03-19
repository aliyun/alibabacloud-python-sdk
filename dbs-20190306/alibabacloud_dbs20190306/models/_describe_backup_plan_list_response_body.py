# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dbs20190306 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupPlanListResponseBody(DaraModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        items: main_models.DescribeBackupPlanListResponseBodyItems = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        # Error code.
        self.err_code = err_code
        # Error message.
        self.err_message = err_message
        # HTTP status code.
        self.http_status_code = http_status_code
        self.items = items
        # Page number.
        self.page_num = page_num
        # Number of records per page.
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # Indicates whether the request succeeded.
        self.success = success
        # Total number of backup plans.
        self.total_elements = total_elements
        # Total number of pages.
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
            temp_model = main_models.DescribeBackupPlanListResponseBodyItems()
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

class DescribeBackupPlanListResponseBodyItems(DaraModel):
    def __init__(
        self,
        backup_plan_detail: List[main_models.DescribeBackupPlanListResponseBodyItemsBackupPlanDetail] = None,
    ):
        self.backup_plan_detail = backup_plan_detail

    def validate(self):
        if self.backup_plan_detail:
            for v1 in self.backup_plan_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BackupPlanDetail'] = []
        if self.backup_plan_detail is not None:
            for k1 in self.backup_plan_detail:
                result['BackupPlanDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup_plan_detail = []
        if m.get('BackupPlanDetail') is not None:
            for k1 in m.get('BackupPlanDetail'):
                temp_model = main_models.DescribeBackupPlanListResponseBodyItemsBackupPlanDetail()
                self.backup_plan_detail.append(temp_model.from_map(k1))

        return self

class DescribeBackupPlanListResponseBodyItemsBackupPlanDetail(DaraModel):
    def __init__(
        self,
        backup_gateway_id: int = None,
        backup_gateway_identifier: str = None,
        backup_method: str = None,
        backup_objects: str = None,
        backup_period: str = None,
        backup_plan_create_time: int = None,
        backup_plan_id: str = None,
        backup_plan_name: str = None,
        backup_plan_region: str = None,
        backup_plan_status: str = None,
        backup_retention_period: int = None,
        backup_set_download_dir: str = None,
        backup_set_download_full_data_format: str = None,
        backup_set_download_gateway_id: int = None,
        backup_set_download_increment_data_format: str = None,
        backup_set_download_target_type: str = None,
        backup_start_time: str = None,
        backup_storage_type: str = None,
        begin_timestamp_for_restore: int = None,
        cross_aliyun_id: str = None,
        cross_role_name: str = None,
        database_type: str = None,
        duplication_archive_period: int = None,
        duplication_infrequent_access_period: int = None,
        enable_backup_log: bool = None,
        enable_mysql_physical_backup_bin_log: bool = None,
        end_timestamp_for_restore: int = None,
        err_message: str = None,
        increment_backup_retention_period: str = None,
        increment_duplication_archive_period: str = None,
        increment_duplication_infrequent_access_period: str = None,
        instance_charge_type: str = None,
        instance_class: str = None,
        instance_expired_timestamp: int = None,
        log_backup_retention_period: str = None,
        log_duplication_archive_period: str = None,
        log_duplication_infrequent_access_period: str = None,
        ossbucket_name: str = None,
        ossbucket_region: str = None,
        open_backup_set_auto_download: bool = None,
        resource_group_id: str = None,
        source_endpoint_database_name: str = None,
        source_endpoint_enable_ssl: str = None,
        source_endpoint_host: str = None,
        source_endpoint_instance_id: str = None,
        source_endpoint_instance_type: str = None,
        source_endpoint_ip_port: str = None,
        source_endpoint_oracle_sid: str = None,
        source_endpoint_port: str = None,
        source_endpoint_region: str = None,
        source_endpoint_user_name: str = None,
        storage_encrypt_method: str = None,
    ):
        self.backup_gateway_id = backup_gateway_id
        self.backup_gateway_identifier = backup_gateway_identifier
        self.backup_method = backup_method
        self.backup_objects = backup_objects
        self.backup_period = backup_period
        self.backup_plan_create_time = backup_plan_create_time
        self.backup_plan_id = backup_plan_id
        self.backup_plan_name = backup_plan_name
        self.backup_plan_region = backup_plan_region
        self.backup_plan_status = backup_plan_status
        self.backup_retention_period = backup_retention_period
        self.backup_set_download_dir = backup_set_download_dir
        self.backup_set_download_full_data_format = backup_set_download_full_data_format
        self.backup_set_download_gateway_id = backup_set_download_gateway_id
        self.backup_set_download_increment_data_format = backup_set_download_increment_data_format
        self.backup_set_download_target_type = backup_set_download_target_type
        self.backup_start_time = backup_start_time
        self.backup_storage_type = backup_storage_type
        self.begin_timestamp_for_restore = begin_timestamp_for_restore
        self.cross_aliyun_id = cross_aliyun_id
        self.cross_role_name = cross_role_name
        self.database_type = database_type
        self.duplication_archive_period = duplication_archive_period
        self.duplication_infrequent_access_period = duplication_infrequent_access_period
        self.enable_backup_log = enable_backup_log
        self.enable_mysql_physical_backup_bin_log = enable_mysql_physical_backup_bin_log
        self.end_timestamp_for_restore = end_timestamp_for_restore
        self.err_message = err_message
        self.increment_backup_retention_period = increment_backup_retention_period
        self.increment_duplication_archive_period = increment_duplication_archive_period
        self.increment_duplication_infrequent_access_period = increment_duplication_infrequent_access_period
        self.instance_charge_type = instance_charge_type
        self.instance_class = instance_class
        self.instance_expired_timestamp = instance_expired_timestamp
        self.log_backup_retention_period = log_backup_retention_period
        self.log_duplication_archive_period = log_duplication_archive_period
        self.log_duplication_infrequent_access_period = log_duplication_infrequent_access_period
        self.ossbucket_name = ossbucket_name
        self.ossbucket_region = ossbucket_region
        self.open_backup_set_auto_download = open_backup_set_auto_download
        self.resource_group_id = resource_group_id
        self.source_endpoint_database_name = source_endpoint_database_name
        self.source_endpoint_enable_ssl = source_endpoint_enable_ssl
        self.source_endpoint_host = source_endpoint_host
        self.source_endpoint_instance_id = source_endpoint_instance_id
        self.source_endpoint_instance_type = source_endpoint_instance_type
        self.source_endpoint_ip_port = source_endpoint_ip_port
        self.source_endpoint_oracle_sid = source_endpoint_oracle_sid
        self.source_endpoint_port = source_endpoint_port
        self.source_endpoint_region = source_endpoint_region
        self.source_endpoint_user_name = source_endpoint_user_name
        self.storage_encrypt_method = storage_encrypt_method

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

        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method

        if self.backup_objects is not None:
            result['BackupObjects'] = self.backup_objects

        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period

        if self.backup_plan_create_time is not None:
            result['BackupPlanCreateTime'] = self.backup_plan_create_time

        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id

        if self.backup_plan_name is not None:
            result['BackupPlanName'] = self.backup_plan_name

        if self.backup_plan_region is not None:
            result['BackupPlanRegion'] = self.backup_plan_region

        if self.backup_plan_status is not None:
            result['BackupPlanStatus'] = self.backup_plan_status

        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period

        if self.backup_set_download_dir is not None:
            result['BackupSetDownloadDir'] = self.backup_set_download_dir

        if self.backup_set_download_full_data_format is not None:
            result['BackupSetDownloadFullDataFormat'] = self.backup_set_download_full_data_format

        if self.backup_set_download_gateway_id is not None:
            result['BackupSetDownloadGatewayId'] = self.backup_set_download_gateway_id

        if self.backup_set_download_increment_data_format is not None:
            result['BackupSetDownloadIncrementDataFormat'] = self.backup_set_download_increment_data_format

        if self.backup_set_download_target_type is not None:
            result['BackupSetDownloadTargetType'] = self.backup_set_download_target_type

        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time

        if self.backup_storage_type is not None:
            result['BackupStorageType'] = self.backup_storage_type

        if self.begin_timestamp_for_restore is not None:
            result['BeginTimestampForRestore'] = self.begin_timestamp_for_restore

        if self.cross_aliyun_id is not None:
            result['CrossAliyunId'] = self.cross_aliyun_id

        if self.cross_role_name is not None:
            result['CrossRoleName'] = self.cross_role_name

        if self.database_type is not None:
            result['DatabaseType'] = self.database_type

        if self.duplication_archive_period is not None:
            result['DuplicationArchivePeriod'] = self.duplication_archive_period

        if self.duplication_infrequent_access_period is not None:
            result['DuplicationInfrequentAccessPeriod'] = self.duplication_infrequent_access_period

        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log

        if self.enable_mysql_physical_backup_bin_log is not None:
            result['EnableMysqlPhysicalBackupBinLog'] = self.enable_mysql_physical_backup_bin_log

        if self.end_timestamp_for_restore is not None:
            result['EndTimestampForRestore'] = self.end_timestamp_for_restore

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.increment_backup_retention_period is not None:
            result['IncrementBackupRetentionPeriod'] = self.increment_backup_retention_period

        if self.increment_duplication_archive_period is not None:
            result['IncrementDuplicationArchivePeriod'] = self.increment_duplication_archive_period

        if self.increment_duplication_infrequent_access_period is not None:
            result['IncrementDuplicationInfrequentAccessPeriod'] = self.increment_duplication_infrequent_access_period

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.instance_expired_timestamp is not None:
            result['InstanceExpiredTimestamp'] = self.instance_expired_timestamp

        if self.log_backup_retention_period is not None:
            result['LogBackupRetentionPeriod'] = self.log_backup_retention_period

        if self.log_duplication_archive_period is not None:
            result['LogDuplicationArchivePeriod'] = self.log_duplication_archive_period

        if self.log_duplication_infrequent_access_period is not None:
            result['LogDuplicationInfrequentAccessPeriod'] = self.log_duplication_infrequent_access_period

        if self.ossbucket_name is not None:
            result['OSSBucketName'] = self.ossbucket_name

        if self.ossbucket_region is not None:
            result['OSSBucketRegion'] = self.ossbucket_region

        if self.open_backup_set_auto_download is not None:
            result['OpenBackupSetAutoDownload'] = self.open_backup_set_auto_download

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.source_endpoint_database_name is not None:
            result['SourceEndpointDatabaseName'] = self.source_endpoint_database_name

        if self.source_endpoint_enable_ssl is not None:
            result['SourceEndpointEnableSsl'] = self.source_endpoint_enable_ssl

        if self.source_endpoint_host is not None:
            result['SourceEndpointHost'] = self.source_endpoint_host

        if self.source_endpoint_instance_id is not None:
            result['SourceEndpointInstanceID'] = self.source_endpoint_instance_id

        if self.source_endpoint_instance_type is not None:
            result['SourceEndpointInstanceType'] = self.source_endpoint_instance_type

        if self.source_endpoint_ip_port is not None:
            result['SourceEndpointIpPort'] = self.source_endpoint_ip_port

        if self.source_endpoint_oracle_sid is not None:
            result['SourceEndpointOracleSID'] = self.source_endpoint_oracle_sid

        if self.source_endpoint_port is not None:
            result['SourceEndpointPort'] = self.source_endpoint_port

        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region

        if self.source_endpoint_user_name is not None:
            result['SourceEndpointUserName'] = self.source_endpoint_user_name

        if self.storage_encrypt_method is not None:
            result['StorageEncryptMethod'] = self.storage_encrypt_method

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')

        if m.get('BackupGatewayIdentifier') is not None:
            self.backup_gateway_identifier = m.get('BackupGatewayIdentifier')

        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')

        if m.get('BackupObjects') is not None:
            self.backup_objects = m.get('BackupObjects')

        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')

        if m.get('BackupPlanCreateTime') is not None:
            self.backup_plan_create_time = m.get('BackupPlanCreateTime')

        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')

        if m.get('BackupPlanName') is not None:
            self.backup_plan_name = m.get('BackupPlanName')

        if m.get('BackupPlanRegion') is not None:
            self.backup_plan_region = m.get('BackupPlanRegion')

        if m.get('BackupPlanStatus') is not None:
            self.backup_plan_status = m.get('BackupPlanStatus')

        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')

        if m.get('BackupSetDownloadDir') is not None:
            self.backup_set_download_dir = m.get('BackupSetDownloadDir')

        if m.get('BackupSetDownloadFullDataFormat') is not None:
            self.backup_set_download_full_data_format = m.get('BackupSetDownloadFullDataFormat')

        if m.get('BackupSetDownloadGatewayId') is not None:
            self.backup_set_download_gateway_id = m.get('BackupSetDownloadGatewayId')

        if m.get('BackupSetDownloadIncrementDataFormat') is not None:
            self.backup_set_download_increment_data_format = m.get('BackupSetDownloadIncrementDataFormat')

        if m.get('BackupSetDownloadTargetType') is not None:
            self.backup_set_download_target_type = m.get('BackupSetDownloadTargetType')

        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')

        if m.get('BackupStorageType') is not None:
            self.backup_storage_type = m.get('BackupStorageType')

        if m.get('BeginTimestampForRestore') is not None:
            self.begin_timestamp_for_restore = m.get('BeginTimestampForRestore')

        if m.get('CrossAliyunId') is not None:
            self.cross_aliyun_id = m.get('CrossAliyunId')

        if m.get('CrossRoleName') is not None:
            self.cross_role_name = m.get('CrossRoleName')

        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')

        if m.get('DuplicationArchivePeriod') is not None:
            self.duplication_archive_period = m.get('DuplicationArchivePeriod')

        if m.get('DuplicationInfrequentAccessPeriod') is not None:
            self.duplication_infrequent_access_period = m.get('DuplicationInfrequentAccessPeriod')

        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')

        if m.get('EnableMysqlPhysicalBackupBinLog') is not None:
            self.enable_mysql_physical_backup_bin_log = m.get('EnableMysqlPhysicalBackupBinLog')

        if m.get('EndTimestampForRestore') is not None:
            self.end_timestamp_for_restore = m.get('EndTimestampForRestore')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('IncrementBackupRetentionPeriod') is not None:
            self.increment_backup_retention_period = m.get('IncrementBackupRetentionPeriod')

        if m.get('IncrementDuplicationArchivePeriod') is not None:
            self.increment_duplication_archive_period = m.get('IncrementDuplicationArchivePeriod')

        if m.get('IncrementDuplicationInfrequentAccessPeriod') is not None:
            self.increment_duplication_infrequent_access_period = m.get('IncrementDuplicationInfrequentAccessPeriod')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('InstanceExpiredTimestamp') is not None:
            self.instance_expired_timestamp = m.get('InstanceExpiredTimestamp')

        if m.get('LogBackupRetentionPeriod') is not None:
            self.log_backup_retention_period = m.get('LogBackupRetentionPeriod')

        if m.get('LogDuplicationArchivePeriod') is not None:
            self.log_duplication_archive_period = m.get('LogDuplicationArchivePeriod')

        if m.get('LogDuplicationInfrequentAccessPeriod') is not None:
            self.log_duplication_infrequent_access_period = m.get('LogDuplicationInfrequentAccessPeriod')

        if m.get('OSSBucketName') is not None:
            self.ossbucket_name = m.get('OSSBucketName')

        if m.get('OSSBucketRegion') is not None:
            self.ossbucket_region = m.get('OSSBucketRegion')

        if m.get('OpenBackupSetAutoDownload') is not None:
            self.open_backup_set_auto_download = m.get('OpenBackupSetAutoDownload')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SourceEndpointDatabaseName') is not None:
            self.source_endpoint_database_name = m.get('SourceEndpointDatabaseName')

        if m.get('SourceEndpointEnableSsl') is not None:
            self.source_endpoint_enable_ssl = m.get('SourceEndpointEnableSsl')

        if m.get('SourceEndpointHost') is not None:
            self.source_endpoint_host = m.get('SourceEndpointHost')

        if m.get('SourceEndpointInstanceID') is not None:
            self.source_endpoint_instance_id = m.get('SourceEndpointInstanceID')

        if m.get('SourceEndpointInstanceType') is not None:
            self.source_endpoint_instance_type = m.get('SourceEndpointInstanceType')

        if m.get('SourceEndpointIpPort') is not None:
            self.source_endpoint_ip_port = m.get('SourceEndpointIpPort')

        if m.get('SourceEndpointOracleSID') is not None:
            self.source_endpoint_oracle_sid = m.get('SourceEndpointOracleSID')

        if m.get('SourceEndpointPort') is not None:
            self.source_endpoint_port = m.get('SourceEndpointPort')

        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')

        if m.get('SourceEndpointUserName') is not None:
            self.source_endpoint_user_name = m.get('SourceEndpointUserName')

        if m.get('StorageEncryptMethod') is not None:
            self.storage_encrypt_method = m.get('StorageEncryptMethod')

        return self

