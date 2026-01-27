# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupDataListRequest(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        backup_method: str = None,
        backup_mode: str = None,
        backup_scale: str = None,
        backup_status: str = None,
        backup_type: str = None,
        data_source_id: str = None,
        end_time: str = None,
        instance_is_deleted: bool = None,
        instance_name: str = None,
        instance_region: str = None,
        page_number: int = None,
        page_size: int = None,
        region_code: str = None,
        scene_type: str = None,
        start_time: str = None,
    ):
        # The ID of the backup set.
        self.backup_id = backup_id
        # The backup method. Valid values:
        # 
        # *   **Physical**
        # *   **Logical**
        # *   **Snapshot**
        self.backup_method = backup_method
        # The backup mode. Valid values:
        # 
        # *   **Automated**
        # *   **Manual**
        self.backup_mode = backup_mode
        # The backup scale. Valid values:
        # 
        # *   **DBInstance**
        # *   **DBTable**
        self.backup_scale = backup_scale
        # The status of the backup set. Valid values:
        # 
        # *   **OK**: The backup succeeded.
        # *   **ERROR**: The backup failed.
        self.backup_status = backup_status
        # The backup type. Valid values:
        # 
        # *   **FullBackup**
        # *   **IncrementBackup**
        self.backup_type = backup_type
        # This is a reserved parameter.
        self.data_source_id = data_source_id
        # The end of the time range to query. The end time must be later than the start time. The time follows the yyyy-MM-ddTHH:mm:ssZ format and is displayed in UTC.
        self.end_time = end_time
        # Specifies whether the cluster is deleted. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.instance_is_deleted = instance_is_deleted
        # The ID of the PolarDB for MySQL cluster.
        self.instance_name = instance_name
        # The region in which the original cluster resides.
        self.instance_region = instance_region
        # The page number. The value must be a positive integer that does not exceed the maximum value of the INTEGER data type. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The region in which the backup set resides.
        self.region_code = region_code
        # The type of the backup scenario. Set the value to **LEVEL_1**, which indicates the level-1 backup of the region in which the PolarDB for MySQL cluster resides.
        self.scene_type = scene_type
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method

        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode

        if self.backup_scale is not None:
            result['BackupScale'] = self.backup_scale

        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_is_deleted is not None:
            result['InstanceIsDeleted'] = self.instance_is_deleted

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_region is not None:
            result['InstanceRegion'] = self.instance_region

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_code is not None:
            result['RegionCode'] = self.region_code

        if self.scene_type is not None:
            result['SceneType'] = self.scene_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')

        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('BackupScale') is not None:
            self.backup_scale = m.get('BackupScale')

        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceIsDeleted') is not None:
            self.instance_is_deleted = m.get('InstanceIsDeleted')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceRegion') is not None:
            self.instance_region = m.get('InstanceRegion')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')

        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

