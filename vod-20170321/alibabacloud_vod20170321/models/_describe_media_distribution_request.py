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
        # The end time of the creation time. The end time must be later than the start time. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. The maximum time span between the start time and end time is six months.
        self.end_time = end_time
        # The statistical interval. Default value: day. Valid values:
        # - hour: Hour. Statistics are collected based on the natural hours of the start time and end time.
        # - day: Day. Statistics are collected based on the natural days of the start time and end time.
        # - week: Week. Statistics are collected based on the natural weeks of the start time and end time.
        # - month: Month. Statistics are collected based on the natural months of the start time and end time.
        self.interval = interval
        # The start time of the creation time. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. The maximum time span between the start time and end time is six months.
        self.start_time = start_time
        # The storage class. Valid values:
        # - Standard: Standard storage.
        # - IA: Infrequent access.
        # - Archive: Archive storage.
        # - ColdArchive: Cold archive storage.
        # - SourceIA: Infrequent access for source files.
        # - SourceArchive: Archive storage for source files.
        # - SourceColdArchive: Cold archive storage for source files.
        # - Changing: The storage type of the media asset is being changed.
        # - SourceChanging: The storage type of the source file is being changed.
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

