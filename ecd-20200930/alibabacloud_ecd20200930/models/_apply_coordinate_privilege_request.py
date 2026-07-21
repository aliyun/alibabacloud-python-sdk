# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplyCoordinatePrivilegeRequest(DaraModel):
    def __init__(
        self,
        co_id: str = None,
        end_user_id: str = None,
        region_id: str = None,
        user_type: str = None,
        uuid: str = None,
    ):
        # The coordination stream ID. This value is the `Coid` returned by the [ApplyCoordinationForMonitoring](~~ApplyCoordinationForMonitoring~~) operation.
        # 
        # This parameter is required.
        self.co_id = co_id
        # The username of the end user.
        self.end_user_id = end_user_id
        # The region ID. Call [DescribeRegions](~~DescribeRegions~~) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The type of the coordination user.
        # 
        # This parameter is required.
        self.user_type = user_type
        # The UUID (unique identifier) of the device.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.co_id is not None:
            result['CoId'] = self.co_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_type is not None:
            result['UserType'] = self.user_type

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoId') is not None:
            self.co_id = m.get('CoId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

