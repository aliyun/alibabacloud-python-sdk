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
        # The application ID.
        self.app_id = app_id
        # The end time of the query. The end time must be later than the start time. The time range cannot exceed 31 days. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        self.end_time = end_time
        self.owner_id = owner_id
        # The storage region. By default, data of all regions is returned. You can specify multiple regions separated by commas (,).
        self.region = region
        # The start time of the query. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mmZ format. The time must be in UTC. If this parameter is left empty, data of the last 24 hours is returned by default.
        self.start_time = start_time
        # The storage class. By default, data of all storage classes is returned. Valid values:
        # - **IA**: Infrequent Access.
        # - **Archive**: Archive.
        # - **ColdArchive**: Cold Archive.
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

