# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDisposeStrategyPlaybookRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
        start_time: int = None,
    ):
        # The end time of the query, in milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The region where the data management center of threat detection and response is located. Select the management center based on the region of your assets. Valid values:
        # - cn-hangzhou: the asset belongs to the Chinese mainland or Hong Kong (China).
        # - ap-southeast-1: the asset belongs to a region outside China.
        self.region_id = region_id
        # The ID of the user to which the administrator switches the view.
        self.role_for = role_for
        # The view type. Valid values:
        # 
        # - 0: the view of the current Alibaba Cloud account.
        # - 1: the view of all accounts in the enterprise.
        self.role_type = role_type
        # The start time of the query, in milliseconds.
        # 
        # This parameter is required.
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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

