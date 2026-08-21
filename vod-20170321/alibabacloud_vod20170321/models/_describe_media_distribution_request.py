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
        # The end time of CreationTime. The end time must be later than the start time. Format: yyyy-MM-ddTHH:mm:ssZ (UTC). The maximum time span between the start time and end time is six months.
        self.end_time = end_time
        # The statistical interval. Default value: day. Valid values:
        # - hour: by hour. Statistics are collected based on the calendar hours within the specified time range.
        # - day: by day. Statistics are collected based on the calendar days within the specified time range.
        # - week: by week. Statistics are collected based on the calendar weeks within the specified time range.
        # - month: by month. Statistics are collected based on the calendar months within the specified time range.
        self.interval = interval
        # The start time of CreationTime. Format: yyyy-MM-ddTHH:mm:ssZ (UTC). The maximum time span between the start time and end time is six months.
        self.start_time = start_time
        # The storage class. Valid values:
        # - Standard: standard storage.
        # - IA: Infrequent Access.
        # - Archive: Archive storage.
        # - ColdArchive: Cold Archive storage.
        # - SourceIA: Infrequent Access for source files.
        # - SourceArchive: Archive storage for source files.
        # - SourceColdArchive: Cold Archive storage for source files.
        # - Changing: the media asset storage class is being changed.
        # - SourceChanging: the source file storage class is being changed.
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

