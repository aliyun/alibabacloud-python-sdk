# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOrganizationalUnitRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        organizational_unit_external_id: str = None,
        organizational_unit_name: str = None,
        parent_id: str = None,
    ):
        # The description of the organizational unit.
        self.description = description
        # The external ID of the organizational unit. The external ID can be used to map external data to the data of the organizational unit in Employee Identity and Access Management (EIAM) of Identity as a Service (IDaaS). By default, the external ID is the organizational unit ID.
        # 
        # For organizational units with the same source type and source ID, each organizational unit has a unique external ID.
        self.organizational_unit_external_id = organizational_unit_external_id
        # The name of the organizational unit.
        # 
        # This parameter is required.
        self.organizational_unit_name = organizational_unit_name
        # The ID of the parent organizational unit.
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
            result['description'] = self.description

        if self.organizational_unit_external_id is not None:
            result['organizationalUnitExternalId'] = self.organizational_unit_external_id

        if self.organizational_unit_name is not None:
            result['organizationalUnitName'] = self.organizational_unit_name

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('organizationalUnitExternalId') is not None:
            self.organizational_unit_external_id = m.get('organizationalUnitExternalId')

        if m.get('organizationalUnitName') is not None:
            self.organizational_unit_name = m.get('organizationalUnitName')

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        return self

