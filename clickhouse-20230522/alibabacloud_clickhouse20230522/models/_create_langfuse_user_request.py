# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLangfuseUserRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        email: str = None,
        name: str = None,
        org_role: str = None,
        organization_id: str = None,
        password: str = None,
        region_id: str = None,
    ):
        # The Langfuse instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The email address of the user.
        # 
        # This parameter is required.
        self.email = email
        # The username.
        # 
        # This parameter is required.
        self.name = name
        # The role of the user in the organization.
        self.org_role = org_role
        # The Langfuse organization ID.
        self.organization_id = organization_id
        # The password of the user account. The password must meet the following requirements:
        # 
        # - Contains at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # 
        # - The following special characters are supported: !@#$%^&*()_+-=
        # 
        # - The password must be 8 to 32 characters in length.
        # 
        # This parameter is required.
        self.password = password
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

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

        if self.name is not None:
            result['Name'] = self.name

        if self.org_role is not None:
            result['OrgRole'] = self.org_role

        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id

        if self.password is not None:
            result['Password'] = self.password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OrgRole') is not None:
            self.org_role = m.get('OrgRole')

        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

