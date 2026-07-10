# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLangfuseOrgMembershipRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        email: str = None,
        organization_id: str = None,
        region_id: str = None,
        role: str = None,
    ):
        # The Langfuse instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The email address of the user.
        # 
        # This parameter is required.
        self.email = email
        # The Langfuse organization ID.
        # 
        # This parameter is required.
        self.organization_id = organization_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The role of the user in the organization.
        # 
        # This parameter is required.
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.email is not None:
            result['Email'] = self.email

        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

