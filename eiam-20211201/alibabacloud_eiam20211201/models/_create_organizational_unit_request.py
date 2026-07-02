# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOrganizationalUnitRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        organizational_unit_external_id: str = None,
        organizational_unit_name: str = None,
        parent_id: str = None,
    ):
        # The description. The maximum length is 256 characters.
        self.description = description
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # External ID of the organization, which is used for association with an external system. The default value is the organization ID. The maximum length is 64 characters.
        self.organizational_unit_external_id = organizational_unit_external_id
        # Organization name. The maximum length is 64 characters.
        # 
        # This parameter is required.
        self.organizational_unit_name = organizational_unit_name
        # Parent organization ID.
        # 
        # This parameter is required.
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.organizational_unit_external_id is not None:
            result['OrganizationalUnitExternalId'] = self.organizational_unit_external_id

        if self.organizational_unit_name is not None:
            result['OrganizationalUnitName'] = self.organizational_unit_name

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrganizationalUnitExternalId') is not None:
            self.organizational_unit_external_id = m.get('OrganizationalUnitExternalId')

        if m.get('OrganizationalUnitName') is not None:
            self.organizational_unit_name = m.get('OrganizationalUnitName')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        return self

