# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMediaDistributionRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        interval: str = None,
        start_time: str = None,
        storage_class: str = None,
    ):
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. The maximum time range to query is 6 months.
        self.end_time = end_time
        # The statistical interval. Default value: day. Valid values:
        # 
        # *   hour: natural hour of the start and end time.
        # *   day: natural day of the start and end time.
        # *   week: natural week of the start and end time.
        # *   month: natural month of the start and end time.
        self.interval = interval
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. The maximum time range to query is 6 months.
        self.start_time = start_time
        # The hierarchical storage type. Valid values:
        # 
        # *   Standard
        # *   IA
        # *   Archive
        # *   ColdArchive
        # *   SourceIA
        # *   SourceArchive
        # *   SourceColdArchive
        # *   Changing
        # *   SourceChanging
        self.storage_class = storage_class

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        return self

