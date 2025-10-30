# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDataBackupsRequest(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        backup_mode: str = None,
        backup_status: str = None,
        dbinstance_id: str = None,
        data_type: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
    ):
        # The ID of the backup set. If you specify BackupId, the details of the backup set are returned.
        # 
        # > You can call the [DescribeDataBackups](https://help.aliyun.com/document_detail/210093.html) operation to query the information about all backup sets of an instance, including backup set IDs.
        self.backup_id = backup_id
        # The backup mode. Valid values:
        # 
        # *   Automated
        # *   Manual
        # 
        # If you do not specify this parameter, all backup sets are returned.
        self.backup_mode = backup_mode
        # The state of the backup set. Valid values:
        # 
        # *   Success
        # *   Failed
        # 
        # If you do not specify this parameter, all backup sets are returned.
        self.backup_status = backup_status
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The backup type. Valid values:
        # 
        # *   **DATA**: full backup.
        # *   **RESTOREPOI**: point-in-time recovery backup.
        # 
        # If you do not specify this parameter, the backup sets of full backup are returned.
        self.data_type = data_type
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC.
        self.end_time = end_time
        # The page number. Pages start from page 1. Default value: 1
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   30
        # *   50
        # *   100
        # 
        # Default value: 30.
        self.page_size = page_size
        # The beginning of the time range to query. Specify the time in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC.
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

        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode

        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

