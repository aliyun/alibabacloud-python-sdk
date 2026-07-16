# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAlertSourceWithEventRequest(DaraModel):
    def __init__(
        self,
        incident_uuid: str = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
    ):
        # The globally unique ID of the event.
        self.incident_uuid = incident_uuid
        # The region where the Data Management center of Threat Analysis is located. Select a region based on the location of your assets. Valid values:
        # 
        # - cn-hangzhou: Your assets are in China.
        # 
        # - ap-southeast-1: Your assets are outside China.
        self.region_id = region_id
        # The ID of the member whose data you want to view. An administrator can use this parameter to switch to the perspective of a member.
        self.role_for = role_for
        # The type of the view.
        # 
        # - 0: The view of the current Alibaba Cloud account.
        # 
        # - 1: The view of all accounts that are managed by the enterprise.
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

