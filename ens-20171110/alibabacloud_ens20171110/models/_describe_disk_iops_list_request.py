# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDiskIopsListRequest(DaraModel):
    def __init__(
        self,
        disk_id: str = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # The ID of the disk. Format: d-\\*\\*\\*\\*\\*\\*\\*\\*\\*\\*\\*.
        # 
        # This parameter is required.
        self.disk_id = disk_id
        # The beginning of the time range to query. Specify the time in the format of yyyy-MM-dd HH:mm:ss. The time range specified by the StartTime and EndTime parameters cannot exceed one day for a query.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The beginning of the time range to query. Specify the time in the format of yyyy-MM-dd HH:mm:ss.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

