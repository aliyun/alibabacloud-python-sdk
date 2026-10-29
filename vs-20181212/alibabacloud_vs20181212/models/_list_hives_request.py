# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHivesRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        hive_id: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
    ):
        # The end time. The time follows the ISO 8601 standard and must be in UTC. Format: yyyy-MM-ddTHH:mm:ssZ.
        self.end_time = end_time
        # The ID of the cloud application service group.
        self.hive_id = hive_id
        # The name.
        self.name = name
        # The page number of the list to query. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # Settings for the number of entries per page during paging in a paged query. Maximum value: 100. Default value: 10.
        self.page_size = page_size
        # The creation time. The time follows the ISO 8601 standard and includes the time zone offset. Format: YYYY-MM-DDTHH:mm:ss+HH:mm.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.hive_id is not None:
            result['HiveId'] = self.hive_id

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('HiveId') is not None:
            self.hive_id = m.get('HiveId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

