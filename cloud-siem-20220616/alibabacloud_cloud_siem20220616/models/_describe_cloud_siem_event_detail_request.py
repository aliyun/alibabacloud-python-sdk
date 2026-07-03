# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCloudSiemEventDetailRequest(DaraModel):
    def __init__(
        self,
        incident_uuid: str = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
    ):
        # The UUID of the event.
        # 
        # This parameter is required.
        self.incident_uuid = incident_uuid
        # The region of the data management center for Threat Analysis. Select the region where your assets are located. Valid values:
        # 
        # - cn-hangzhou: assets in the Chinese mainland and China (Hong Kong)
        # 
        # - ap-southeast-1: assets in regions outside the Chinese mainland
        self.region_id = region_id
        # The ID of the member account. An administrator can use this parameter to query data from the perspective of the member.
        self.role_for = role_for
        # The view type.
        # 
        # - 0: the view of the current Alibaba Cloud account.
        # 
        # - 1: the view of all accounts in your enterprise.
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

