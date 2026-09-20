# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupsRequest(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        cluster_id: str = None,
        end_time: str = None,
        end_time_utc: str = None,
        page_number: str = None,
        page_size: str = None,
        start_time: str = None,
        start_time_utc: str = None,
    ):
        # The ID of the backup to query.
        self.backup_id = backup_id
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The end time of the backup query. Format: yyyy-MM-dd HH:mm.
        self.end_time = end_time
        # The end time of the backup query in UTC. The end time must be later than the start time. Format: yyyy-MM-ddTHH:mmZ.
        self.end_time_utc = end_time_utc
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The start time of the backup query. Format: yyyy-MM-dd HH:mm.
        self.start_time = start_time
        # The start time of the backup query in UTC. Format: yyyy-MM-ddTHH:mmZ.
        self.start_time_utc = start_time_utc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.end_time_utc is not None:
            result['EndTimeUTC'] = self.end_time_utc

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.start_time_utc is not None:
            result['StartTimeUTC'] = self.start_time_utc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EndTimeUTC') is not None:
            self.end_time_utc = m.get('EndTimeUTC')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StartTimeUTC') is not None:
            self.start_time_utc = m.get('StartTimeUTC')

        return self

