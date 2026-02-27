# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hologram20220601 import models as main_models
from darabonba.model import DaraModel

class ListBackupDataResponseBody(DaraModel):
    def __init__(
        self,
        backup_data_list: List[main_models.ListBackupDataResponseBodyBackupDataList] = None,
        request_id: str = None,
    ):
        # The backups.
        self.backup_data_list = backup_data_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.backup_data_list:
            for v1 in self.backup_data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BackupDataList'] = []
        if self.backup_data_list is not None:
            for k1 in self.backup_data_list:
                result['BackupDataList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup_data_list = []
        if m.get('BackupDataList') is not None:
            for k1 in m.get('BackupDataList'):
                temp_model = main_models.ListBackupDataResponseBodyBackupDataList()
                self.backup_data_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListBackupDataResponseBodyBackupDataList(DaraModel):
    def __init__(
        self,
        backup_type: str = None,
        cold_data_size: int = None,
        data_desc: str = None,
        data_gran: str = None,
        data_size: int = None,
        data_time: str = None,
        end_time: str = None,
        id: int = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_region: str = None,
        instance_type: str = None,
        instance_zone_id: str = None,
        snapshot_region: str = None,
        snapshot_zone_id: str = None,
        start_time: str = None,
        status: str = None,
        trigger_type: str = None,
    ):
        # The backup type. In general, the following two types are supported: local backup and remote backup. In the local backup type, snapshots reside in the same region as your instance. The following two sub-types are available: full (single backup, single replica) and redundant (zone-redundant storage, multiple replicas). In the remote backup type, snapshots and your instance reside in different regions. Remote backups are the replicas of the backups of the full or redundant type in another region. The values local and remote do not represent specific types, but are used only for data filtering. The value local indicates all local backups, and the value remote indicates all remote backups.
        self.backup_type = backup_type
        # The size of cold data. Unit: bytes.
        self.cold_data_size = cold_data_size
        # The description of the backup data.
        self.data_desc = data_desc
        # The backup granularity.
        # 
        # Valid values:
        # 
        # *   instance
        self.data_gran = data_gran
        # The size of the backup data. Unit: bytes.
        self.data_size = data_size
        # The snapshot time. The value format of this parameter follows the same standard as that of the StartTime parameter.
        self.data_time = data_time
        # The end time of the backup task. The value format of this parameter follows the same standard as that of the StartTime parameter.
        self.end_time = end_time
        # The unique ID of the backup.
        self.id = id
        # The instance ID.
        self.instance_id = instance_id
        # The name of the instance.
        self.instance_name = instance_name
        # The region in which the instance resides.
        self.instance_region = instance_region
        # The type of the instance.
        # 
        # Valid values:
        # 
        # *   Warehouse: virtual warehouse instance
        # *   Standard: general-purpose instance
        self.instance_type = instance_type
        # The zone in which the instance resides.
        self.instance_zone_id = instance_zone_id
        # The region in which the backup data resides.
        self.snapshot_region = snapshot_region
        # The zone in which the backup data resides. In zone-redundant storage mode, backup data is stored in different zones, including the current zone.
        self.snapshot_zone_id = snapshot_zone_id
        # The start time of the backup task. The time follows the ISO 8601 standard in the YYYY-MM-DDTHH:mm:ss.SSSTZ format. The time is displayed in UTC (the same below).
        self.start_time = start_time
        # The status of the backup task.
        # 
        # Valid values:
        # 
        # *   processing
        # *   completed
        # *   failed
        self.status = status
        # The mode in which the backup task is triggered.
        # 
        # Valid values:
        # 
        # *   scheduled: periodic backup
        # *   manual: manual backup
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.cold_data_size is not None:
            result['ColdDataSize'] = self.cold_data_size

        if self.data_desc is not None:
            result['DataDesc'] = self.data_desc

        if self.data_gran is not None:
            result['DataGran'] = self.data_gran

        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.data_time is not None:
            result['DataTime'] = self.data_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_region is not None:
            result['InstanceRegion'] = self.instance_region

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.instance_zone_id is not None:
            result['InstanceZoneId'] = self.instance_zone_id

        if self.snapshot_region is not None:
            result['SnapshotRegion'] = self.snapshot_region

        if self.snapshot_zone_id is not None:
            result['SnapshotZoneId'] = self.snapshot_zone_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('ColdDataSize') is not None:
            self.cold_data_size = m.get('ColdDataSize')

        if m.get('DataDesc') is not None:
            self.data_desc = m.get('DataDesc')

        if m.get('DataGran') is not None:
            self.data_gran = m.get('DataGran')

        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('DataTime') is not None:
            self.data_time = m.get('DataTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceRegion') is not None:
            self.instance_region = m.get('InstanceRegion')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InstanceZoneId') is not None:
            self.instance_zone_id = m.get('InstanceZoneId')

        if m.get('SnapshotRegion') is not None:
            self.snapshot_region = m.get('SnapshotRegion')

        if m.get('SnapshotZoneId') is not None:
            self.snapshot_zone_id = m.get('SnapshotZoneId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        return self

