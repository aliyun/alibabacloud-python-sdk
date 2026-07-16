# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_openitag20220616 import models as main_models
from darabonba.model import DaraModel

class SimpleTenant(DaraModel):
    def __init__(
        self,
        creator: main_models.SimpleUser = None,
        description: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        modifier: main_models.SimpleUser = None,
        role: str = None,
        tenant_id: str = None,
        tenant_name: str = None,
        uuid: str = None,
    ):
        # Creator
        self.creator = creator
        # Description
        self.description = description
        # Creation Time
        self.gmt_create_time = gmt_create_time
        # Updated At
        self.gmt_modified_time = gmt_modified_time
        # Updated By Information
        self.modifier = modifier
        # Role Information
        self.role = role
        # Tenant ID
        self.tenant_id = tenant_id
        # Tenant Name
        self.tenant_name = tenant_name
        # Unique Identifier
        self.uuid = uuid

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.modifier:
            self.modifier.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['Creator'] = self.creator.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.modifier is not None:
            result['Modifier'] = self.modifier.to_map()

        if self.role is not None:
            result['Role'] = self.role

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name

        if self.uuid is not None:
            result['UUID'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            temp_model = main_models.SimpleUser()
            self.creator = temp_model.from_map(m.get('Creator'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('Modifier') is not None:
            temp_model = main_models.SimpleUser()
            self.modifier = temp_model.from_map(m.get('Modifier'))

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')

        if m.get('UUID') is not None:
            self.uuid = m.get('UUID')

        return self

