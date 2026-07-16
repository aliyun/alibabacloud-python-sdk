# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeAlertSourceRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        level: List[str] = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
        start_time: int = None,
    ):
        # The end of the query time range. The value is a UNIX timestamp in milliseconds.
        self.end_time = end_time
        # The threat levels. Valid values:
        # 
        # - `serious`: High
        # 
        # - `suspicious`: Medium
        # 
        # - `remind`: Low
        self.level = level
        # The region of the data management center for threat analysis. Select the data management center that corresponds to the region where your assets are located. Valid values:
        # 
        # - `cn-hangzhou`: for assets in the Chinese mainland and Hong Kong (China).
        # 
        # - `ap-southeast-1`: for assets in regions outside the Chinese mainland.
        self.region_id = region_id
        # The user ID of the member whose data you want to view. An administrator uses this parameter to view data from the perspective of a specific member.
        self.role_for = role_for
        # The type of view. Valid values:
        # 
        # - `0`: View data for the current Alibaba Cloud account.
        # 
        # - `1`: View data for all accounts in the enterprise.
        self.role_type = role_type
        # The start of the query time range. The value is a UNIX timestamp in milliseconds.
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

        if self.level is not None:
            result['Level'] = self.level

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

