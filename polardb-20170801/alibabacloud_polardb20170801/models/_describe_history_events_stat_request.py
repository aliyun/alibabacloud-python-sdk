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
        to_start_time: str = None,
    ):
        # The archive status of the events. Valid values:
        # - Archived: The events are archived.
        # - UnArchived: The events are not archived.
        # - All: All events.
        self.archive_status = archive_status
        # The start time of the time range for task start times to query, in the YYYY-MM-DDThh:mm:ssZ format (UTC).
        self.from_start_time = from_start_time
        # The ID of the region where the events are located.
        self.region_id = region_id
        # The end time of the time range for task start times to query, in the YYYY-MM-DDThh:mm:ssZ format (UTC).
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

        if m.get('ToStartTime') is not None:
            self.to_start_time = m.get('ToStartTime')

        return self

