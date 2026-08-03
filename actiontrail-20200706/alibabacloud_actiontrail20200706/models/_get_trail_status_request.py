# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTrailStatusRequest(DaraModel):
    def __init__(
        self,
        is_organization_trail: bool = None,
        name: str = None,
    ):
        # Specifies whether to query the status of a multi-account trail. Valid values:
        # 
        # - true: Query the status of a multi-account trail.
        # 
        # - false: Query the status of a single-account trail. It is the default value.
        self.is_organization_trail = is_organization_trail
        # The name of the trail.
        # 
        # The name must be 6 to 36 characters in length. The name must start with a lowercase letter and can contain lowercase letters, digits, hyphens (-), and underscores (_).
        # 
        # > The name must be unique within your Alibaba Cloud account.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_organization_trail is not None:
            result['IsOrganizationTrail'] = self.is_organization_trail

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsOrganizationTrail') is not None:
            self.is_organization_trail = m.get('IsOrganizationTrail')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

