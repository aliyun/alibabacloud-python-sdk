# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListOrganizationalUnitsResponseBody(DaraModel):
    def __init__(
        self,
        organizational_units: List[main_models.ListOrganizationalUnitsResponseBodyOrganizationalUnits] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of data objects of organizational units.
        self.organizational_units = organizational_units
        # The ID of the request.
        self.request_id = request_id
        # The number of entries in the list.
        self.total_count = total_count

    def validate(self):
        if self.organizational_units:
            for v1 in self.organizational_units:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OrganizationalUnits'] = []
        if self.organizational_units is not None:
            for k1 in self.organizational_units:
                result['OrganizationalUnits'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.organizational_units = []
        if m.get('OrganizationalUnits') is not None:
            for k1 in m.get('OrganizationalUnits'):
                temp_model = main_models.ListOrganizationalUnitsResponseBodyOrganizationalUnits()
                self.organizational_units.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListOrganizationalUnitsResponseBodyOrganizationalUnits(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        instance_id: str = None,
        leaf: bool = None,
        organizational_unit_external_id: str = None,
        organizational_unit_id: str = None,
        organizational_unit_name: str = None,
        organizational_unit_source_id: str = None,
        organizational_unit_source_type: str = None,
        parent_id: str = None,
        update_time: int = None,
    ):
        # The time when the organizational unit was created. This value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time
        # The description of the organizational unit.
        self.description = description
        # The ID of the instance.
        self.instance_id = instance_id
        # Indicates whether the node is a leaf node.
        self.leaf = leaf
        # The external ID of the organizational unit. The external ID can be used by external data to map the data of the organizational unit in IDaaS EIAM. By default, the external ID is the organizational unit ID.
        # 
        # For organizational units with the same source type and source ID, each organizational unit has a unique external ID.
        self.organizational_unit_external_id = organizational_unit_external_id
        # The ID of the organizational unit.
        self.organizational_unit_id = organizational_unit_id
        # 组织名称。
        self.organizational_unit_name = organizational_unit_name
        # The source ID of the organizational unit.
        self.organizational_unit_source_id = organizational_unit_source_id
        # The source type of the organizational unit. Valid values:
        # 
        # *   build_in: The organizational unit was created in IDaaS.
        # *   ding_talk: The organizational unit was imported from DingTalk.
        # *   ad: The organizational unit was imported from Microsoft Active Directory (AD).
        # *   ldap: The organizational unit was imported from a Lightweight Directory Access Protocol (LDAP) service.
        self.organizational_unit_source_type = organizational_unit_source_type
        # The ID of the parent organizational unit.
        self.parent_id = parent_id
        # The time when the organizational unit was last updated. The value is a UNIX timestamp. Unit: milliseconds.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.leaf is not None:
            result['Leaf'] = self.leaf

        if self.organizational_unit_external_id is not None:
            result['OrganizationalUnitExternalId'] = self.organizational_unit_external_id

        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id

        if self.organizational_unit_name is not None:
            result['OrganizationalUnitName'] = self.organizational_unit_name

        if self.organizational_unit_source_id is not None:
            result['OrganizationalUnitSourceId'] = self.organizational_unit_source_id

        if self.organizational_unit_source_type is not None:
            result['OrganizationalUnitSourceType'] = self.organizational_unit_source_type

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Leaf') is not None:
            self.leaf = m.get('Leaf')

        if m.get('OrganizationalUnitExternalId') is not None:
            self.organizational_unit_external_id = m.get('OrganizationalUnitExternalId')

        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')

        if m.get('OrganizationalUnitName') is not None:
            self.organizational_unit_name = m.get('OrganizationalUnitName')

        if m.get('OrganizationalUnitSourceId') is not None:
            self.organizational_unit_source_id = m.get('OrganizationalUnitSourceId')

        if m.get('OrganizationalUnitSourceType') is not None:
            self.organizational_unit_source_type = m.get('OrganizationalUnitSourceType')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

