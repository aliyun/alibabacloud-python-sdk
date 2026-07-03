# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEntityInfoRequest(DaraModel):
    def __init__(
        self,
        entity_id: int = None,
        entity_identity: str = None,
        incident_uuid: str = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
        sophon_task_id: str = None,
    ):
        # The logical ID of the entity.
        self.entity_id = entity_id
        # The feature value of the entity. You can perform a fuzzy search for the entity.
        self.entity_identity = entity_identity
        # The globally unique UUID of the event.
        self.incident_uuid = incident_uuid
        # The region of the Data Management center. Select a region based on the region where your assets are located. Valid values:
        # 
        # - cn-hangzhou: Your assets are in the Chinese mainland or China (Hong Kong).
        # 
        # - ap-southeast-1: Your assets are in a region outside China.
        self.region_id = region_id
        # The user ID of the member. The administrator can use this ID to switch to the view of this member.
        self.role_for = role_for
        # The view type.
        # 
        # - 0: the view of the current Alibaba Cloud account.
        # 
        # - 1: the view of all accounts that belong to the enterprise.
        self.role_type = role_type
        # The ID of the SOAR response policy.
        self.sophon_task_id = sophon_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.entity_identity is not None:
            result['EntityIdentity'] = self.entity_identity

        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.sophon_task_id is not None:
            result['SophonTaskId'] = self.sophon_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('EntityIdentity') is not None:
            self.entity_identity = m.get('EntityIdentity')

        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('SophonTaskId') is not None:
            self.sophon_task_id = m.get('SophonTaskId')

        return self

