# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstanceSwitchLogRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-mm-dd*T*hh:mm*Z format. The time must be in UTC. The end time must be later than the start time.
        self.end_time = end_time
        # The number of the page to return. The value must be an integer that is greater than 0 and less than or equal to the maximum value supported by the integer data type. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: **30, 50, and 100**. Default value: **30**.
        self.page_size = page_size
        self.resource_owner_id = resource_owner_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-mm-dd*T*hh:mm*Z format. The time must be in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

