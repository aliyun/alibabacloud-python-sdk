# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeSharedBackupsResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeSharedBackupsResponseBodyItems] = None,
        page_number: str = None,
        page_record_count: str = None,
        request_id: str = None,
        total_record_count: str = None,
    ):
        # A list of shared backup sets.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries on the current page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total record count.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeSharedBackupsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeSharedBackupsResponseBodyItems(DaraModel):
    def __init__(
        self,
        backup_end_time: str = None,
        backup_id: str = None,
        backup_method: str = None,
        backup_mode: str = None,
        backup_set_size: str = None,
        backup_start_time: str = None,
        backup_status: str = None,
        backup_type: str = None,
        backups_level: str = None,
        consistent_time: str = None,
        dbcluster_id: str = None,
        dbtype: str = None,
        dbversion: str = None,
        pay_type: str = None,
        region_id: str = None,
        serverless_type: str = None,
        share_type: str = None,
        sharer_uid: str = None,
    ):
        # The end time of the backup, in UTC.
        self.backup_end_time = backup_end_time
        # The backup set ID.
        self.backup_id = backup_id
        # The backup method. Only snapshot backup is supported. The value is fixed to **Snapshot**.
        self.backup_method = backup_method
        # The backup mode. Valid values:
        # 
        # - **Automated**: automated backup
        # 
        # - **Manual**: manual backup
        self.backup_mode = backup_mode
        # The size of the backup set, in bytes.
        self.backup_set_size = backup_set_size
        # The start time of the backup, in UTC.
        self.backup_start_time = backup_start_time
        # The backup status. Valid values:
        # 
        # - **Success**: The backup is complete.
        # 
        # - **Failed**: The backup failed.
        self.backup_status = backup_status
        # The backup type. Only full backups are supported. The value is fixed to **FullBackup**.
        self.backup_type = backup_type
        # The backup level. Valid values:
        # 
        # - **Level-1**: Level-1 backup.
        # 
        # - **Level-2**: Level-2 backup.
        self.backups_level = backups_level
        # The UNIX timestamp of the consistent snapshot, in seconds.
        self.consistent_time = consistent_time
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The database engine type.
        self.dbtype = dbtype
        # The database engine version.
        self.dbversion = dbversion
        # The billing method. Valid values:
        # 
        # - **Postpaid**: pay-as-you-go.
        # 
        # - **Prepaid**: prepaid (subscription)
        self.pay_type = pay_type
        # The region ID.
        self.region_id = region_id
        # The Serverless type. A value of **AgileServerless** indicates a Serverless cluster, while an empty value indicates a standard cluster.
        self.serverless_type = serverless_type
        # The share type.
        self.share_type = share_type
        # The UID of the account that shared the backup set.
        self.sharer_uid = sharer_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time

        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method

        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode

        if self.backup_set_size is not None:
            result['BackupSetSize'] = self.backup_set_size

        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time

        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.backups_level is not None:
            result['BackupsLevel'] = self.backups_level

        if self.consistent_time is not None:
            result['ConsistentTime'] = self.consistent_time

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.serverless_type is not None:
            result['ServerlessType'] = self.serverless_type

        if self.share_type is not None:
            result['ShareType'] = self.share_type

        if self.sharer_uid is not None:
            result['SharerUID'] = self.sharer_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')

        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')

        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('BackupSetSize') is not None:
            self.backup_set_size = m.get('BackupSetSize')

        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')

        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('BackupsLevel') is not None:
            self.backups_level = m.get('BackupsLevel')

        if m.get('ConsistentTime') is not None:
            self.consistent_time = m.get('ConsistentTime')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServerlessType') is not None:
            self.serverless_type = m.get('ServerlessType')

        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')

        if m.get('SharerUID') is not None:
            self.sharer_uid = m.get('SharerUID')

        return self

