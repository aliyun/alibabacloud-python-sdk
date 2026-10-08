# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHistoryEventsStatRequest(DaraModel):
    def __init__(
        self,
        archive_status: str = None,
        from_start_time: str = None,
        region_id: str = None,
        security_token: str = None,
        to_start_time: str = None,
    ):
        # The event status. Valid values:
        # - **Archived**: archived.
        # - **UnArchived**: not archived.
        # - **All**: all events.
        self.archive_status = archive_status
        # The beginning of the time range for the task start time. Only tasks whose start time is later than this time are queried. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. The earliest supported time is 30 days before the current time. If the specified time is more than 30 days before the current time, it is automatically converted to 30 days before the current time.
        self.from_start_time = from_start_time
        # The region ID. You can call DescribeRegions to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.security_token = security_token
        # The end of the time range for the task start time. Only tasks whose start time is earlier than this time are queried. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.to_start_time = to_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.archive_status is not None:
            result['ArchiveStatus'] = self.archive_status

        if self.from_start_time is not None:
            result['FromStartTime'] = self.from_start_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.to_start_time is not None:
            result['ToStartTime'] = self.to_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveStatus') is not None:
            self.archive_status = m.get('ArchiveStatus')

        if m.get('FromStartTime') is not None:
            self.from_start_time = m.get('FromStartTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('ToStartTime') is not None:
            self.to_start_time = m.get('ToStartTime')

        return self

