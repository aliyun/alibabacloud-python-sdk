# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupPolicyResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeBackupPolicyResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response body.
        self.data = data
        # The message returned. If the request is successful, success is returned. If the request fails, the corresponding error code is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
        if m.get('Data') is not None:
            temp_model = main_models.DescribeBackupPolicyResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeBackupPolicyResponseBodyData(DaraModel):
    def __init__(
        self,
        backup_period: str = None,
        backup_plan_begin: str = None,
        backup_set_retention: int = None,
        backup_type: str = None,
        backup_way: str = None,
        cold_data_backup_interval: int = None,
        cold_data_backup_retention: int = None,
        cross_region_data_backup_retention: int = None,
        cross_region_filter_value: str = None,
        cross_region_log_backup_retention: int = None,
        dbinstance_name: str = None,
        dest_cross_region: str = None,
        force_clean_on_high_space_usage: int = None,
        is_cross_region_data_backup_enabled: bool = None,
        is_cross_region_log_backup_enabled: bool = None,
        is_enabled: int = None,
        local_log_retention: int = None,
        local_log_retention_number: int = None,
        log_local_retention_space: int = None,
        remove_log_retention: int = None,
    ):
        # The backup cycle. You must specify at least 2 days. The value is a 7-digit string. Each digit from left to right indicates whether backup is enabled from Monday to Sunday. A value of 0 indicates that backup is disabled, and a value of 1 indicates that backup is enabled:
        # 
        # - First digit: Monday
        # - Second digit: Tuesday
        # - Third digit: Wednesday
        # - Fourth digit: Thursday
        # - Fifth digit: Friday
        # - Sixth digit: Saturday
        # - Seventh digit: Sunday
        self.backup_period = backup_period
        # The start time of the daily backup, in UTC.
        self.backup_plan_begin = backup_plan_begin
        # The retention period of backup sets, in days.
        self.backup_set_retention = backup_set_retention
        # The backup type. A value of 0 indicates quick backup.
        self.backup_type = backup_type
        # The backup method. Valid values:
        # 
        # - **P**: physical backup
        # - **L**: logical backup
        self.backup_way = backup_way
        # The interval for cold data backups, in days. Valid values: 1 to 59.
        self.cold_data_backup_interval = cold_data_backup_interval
        # The retention period of cold data backups, in days.
        self.cold_data_backup_retention = cold_data_backup_retention
        # The retention period of cross-region data backups, in days.
        self.cross_region_data_backup_retention = cross_region_data_backup_retention
        # The number of days selected for cross-region backups.
        self.cross_region_filter_value = cross_region_filter_value
        # The retention period of cross-region log backups, in days.
        self.cross_region_log_backup_retention = cross_region_log_backup_retention
        # The name of the instance.
        self.dbinstance_name = dbinstance_name
        # The destination region for cross-region backups.
        self.dest_cross_region = dest_cross_region
        # Indicates whether binary logs are forcibly cleared when the space usage of the instance is excessively high. A value of 1 indicates yes, and a value of 0 indicates no.
        self.force_clean_on_high_space_usage = force_clean_on_high_space_usage
        # Indicates whether cross-region data backup is enabled. Default value: false.
        self.is_cross_region_data_backup_enabled = is_cross_region_data_backup_enabled
        # Indicates whether cross-region log backup is enabled. Default value: false.
        self.is_cross_region_log_backup_enabled = is_cross_region_log_backup_enabled
        # Indicates whether backup is enabled. The value is fixed as 1, which indicates that backup is enabled.
        self.is_enabled = is_enabled
        # The retention period of local log backups, in hours. Valid values: 0 to 7 × 24. A value of 0 indicates that local log backups are not retained. Default value: 7.
        self.local_log_retention = local_log_retention
        # The number of local binary logs to retain. Valid values: 6 to 100. Default value: 60.
        self.local_log_retention_number = local_log_retention_number
        # The maximum space usage of binary logs. The parameter value ranges from 0 to 50. This is a loop space. Default value: 30.
        self.log_local_retention_space = log_local_retention_space
        # The retention period of remote log backups, in days. Valid values: 7 to 730. Default value: 7.
        self.remove_log_retention = remove_log_retention

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period

        if self.backup_plan_begin is not None:
            result['BackupPlanBegin'] = self.backup_plan_begin

        if self.backup_set_retention is not None:
            result['BackupSetRetention'] = self.backup_set_retention

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.backup_way is not None:
            result['BackupWay'] = self.backup_way

        if self.cold_data_backup_interval is not None:
            result['ColdDataBackupInterval'] = self.cold_data_backup_interval

        if self.cold_data_backup_retention is not None:
            result['ColdDataBackupRetention'] = self.cold_data_backup_retention

        if self.cross_region_data_backup_retention is not None:
            result['CrossRegionDataBackupRetention'] = self.cross_region_data_backup_retention

        if self.cross_region_filter_value is not None:
            result['CrossRegionFilterValue'] = self.cross_region_filter_value

        if self.cross_region_log_backup_retention is not None:
            result['CrossRegionLogBackupRetention'] = self.cross_region_log_backup_retention

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.dest_cross_region is not None:
            result['DestCrossRegion'] = self.dest_cross_region

        if self.force_clean_on_high_space_usage is not None:
            result['ForceCleanOnHighSpaceUsage'] = self.force_clean_on_high_space_usage

        if self.is_cross_region_data_backup_enabled is not None:
            result['IsCrossRegionDataBackupEnabled'] = self.is_cross_region_data_backup_enabled

        if self.is_cross_region_log_backup_enabled is not None:
            result['IsCrossRegionLogBackupEnabled'] = self.is_cross_region_log_backup_enabled

        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled

        if self.local_log_retention is not None:
            result['LocalLogRetention'] = self.local_log_retention

        if self.local_log_retention_number is not None:
            result['LocalLogRetentionNumber'] = self.local_log_retention_number

        if self.log_local_retention_space is not None:
            result['LogLocalRetentionSpace'] = self.log_local_retention_space

        if self.remove_log_retention is not None:
            result['RemoveLogRetention'] = self.remove_log_retention

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')

        if m.get('BackupPlanBegin') is not None:
            self.backup_plan_begin = m.get('BackupPlanBegin')

        if m.get('BackupSetRetention') is not None:
            self.backup_set_retention = m.get('BackupSetRetention')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('BackupWay') is not None:
            self.backup_way = m.get('BackupWay')

        if m.get('ColdDataBackupInterval') is not None:
            self.cold_data_backup_interval = m.get('ColdDataBackupInterval')

        if m.get('ColdDataBackupRetention') is not None:
            self.cold_data_backup_retention = m.get('ColdDataBackupRetention')

        if m.get('CrossRegionDataBackupRetention') is not None:
            self.cross_region_data_backup_retention = m.get('CrossRegionDataBackupRetention')

        if m.get('CrossRegionFilterValue') is not None:
            self.cross_region_filter_value = m.get('CrossRegionFilterValue')

        if m.get('CrossRegionLogBackupRetention') is not None:
            self.cross_region_log_backup_retention = m.get('CrossRegionLogBackupRetention')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DestCrossRegion') is not None:
            self.dest_cross_region = m.get('DestCrossRegion')

        if m.get('ForceCleanOnHighSpaceUsage') is not None:
            self.force_clean_on_high_space_usage = m.get('ForceCleanOnHighSpaceUsage')

        if m.get('IsCrossRegionDataBackupEnabled') is not None:
            self.is_cross_region_data_backup_enabled = m.get('IsCrossRegionDataBackupEnabled')

        if m.get('IsCrossRegionLogBackupEnabled') is not None:
            self.is_cross_region_log_backup_enabled = m.get('IsCrossRegionLogBackupEnabled')

        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')

        if m.get('LocalLogRetention') is not None:
            self.local_log_retention = m.get('LocalLogRetention')

        if m.get('LocalLogRetentionNumber') is not None:
            self.local_log_retention_number = m.get('LocalLogRetentionNumber')

        if m.get('LogLocalRetentionSpace') is not None:
            self.log_local_retention_space = m.get('LogLocalRetentionSpace')

        if m.get('RemoveLogRetention') is not None:
            self.remove_log_retention = m.get('RemoveLogRetention')

        return self

