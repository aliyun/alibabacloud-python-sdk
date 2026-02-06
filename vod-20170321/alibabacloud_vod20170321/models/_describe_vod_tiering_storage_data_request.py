# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVodTieringStorageDataRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        end_time: str = None,
        owner_id: int = None,
        region: str = None,
        start_time: str = None,
        storage_class: str = None,
    ):
        self.app_id = app_id
        # The end time at which data is obtained. The end time must be later than the start time. The difference cannot exceed 31 days. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        self.end_time = end_time
        self.owner_id = owner_id
        # The region in which you want to query data. If you leave this parameter empty, data in all regions is returned. Separate multiple regions with commas (,).
        self.region = region
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. If you leave this parameter empty, data in the last 24 hours is queried.
        self.start_time = start_time
        # The storage type. By default, all storage types are returned. Valid values:
        # 
        # *   **IA**
        # *   **Archive**
        # *   **ColdArchive**
        self.storage_class = storage_class

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region is not None:
            result['Region'] = self.region

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        return self

