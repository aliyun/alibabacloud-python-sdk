# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateBackupPolicyRequest(DaraModel):
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
        region_id: str = None,
        remove_log_retention: int = None,
    ):
        self.backup_period = backup_period
        self.backup_plan_begin = backup_plan_begin
        self.backup_set_retention = backup_set_retention
        self.backup_type = backup_type
        self.backup_way = backup_way
        self.cold_data_backup_interval = cold_data_backup_interval
        self.cold_data_backup_retention = cold_data_backup_retention
        self.cross_region_data_backup_retention = cross_region_data_backup_retention
        self.cross_region_log_backup_retention = cross_region_log_backup_retention
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        self.dest_cross_region = dest_cross_region
        self.force_clean_on_high_space_usage = force_clean_on_high_space_usage
        self.is_cross_region_data_backup_enabled = is_cross_region_data_backup_enabled
        self.is_cross_region_log_backup_enabled = is_cross_region_log_backup_enabled
        self.is_enabled = is_enabled
        self.local_log_retention = local_log_retention
        self.local_log_retention_number = local_log_retention_number
        self.log_local_retention_space = log_local_retention_space
        # This parameter is required.
        self.region_id = region_id
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RemoveLogRetention') is not None:
            self.remove_log_retention = m.get('RemoveLogRetention')

        return self

