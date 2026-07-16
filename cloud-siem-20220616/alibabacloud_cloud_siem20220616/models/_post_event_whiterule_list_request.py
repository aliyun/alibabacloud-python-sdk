# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PostEventWhiteruleListRequest(DaraModel):
    def __init__(
        self,
        incident_uuid: str = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
        whiterule_list: str = None,
    ):
        # The globally unique ID of the event.
        self.incident_uuid = incident_uuid
        # The region where the threat analysis feature is deployed. Select the region where your assets are located. Valid values:
        # 
        # - cn-hangzhou: For assets in the Chinese mainland or China (Hong Kong).
        # 
        # - ap-southeast-1: For assets in regions outside the Chinese mainland.
        self.region_id = region_id
        # The ID of a member account. An administrator can use this parameter to switch to the perspective of the member account.
        self.role_for = role_for
        # The account scope to which the rule applies. Valid values:
        # 
        # - 0: The current Alibaba Cloud account.
        # 
        # - 1: All accounts within the enterprise.
        self.role_type = role_type
        # The alert whitelisting rule, which is a JSON object.
        # 
        # This parameter is required.
        self.whiterule_list = whiterule_list

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

        if self.whiterule_list is not None:
            result['WhiteruleList'] = self.whiterule_list

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

        if m.get('WhiteruleList') is not None:
            self.whiterule_list = m.get('WhiteruleList')

        return self

