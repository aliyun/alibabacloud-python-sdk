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
        # The list of organizational units.
        self.organizational_units = organizational_units
        # The request ID.
        self.request_id = request_id
        # The total number of entries that are returned. This value is the total number of matched entries. The maximum number of entries that can be returned in a single request is specified by PageSize.
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
        # The time when the organizational unit was created. The value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time
        # The description of the organizational unit.
        self.description = description
        # The instance ID.
        self.instance_id = instance_id
        # Indicates whether the organizational unit is a leaf node. A value of true indicates that the organizational unit has no child nodes. A value of false indicates that the organizational unit has child nodes.
        self.leaf = leaf
        # The external ID of the organizational unit. This ID is used to map the data of the organizational unit to the data of an external system. By default, the value of this parameter is the organizational unit ID.
        # 
        # Note: The external ID must be unique within the same source type and source ID.
        self.organizational_unit_external_id = organizational_unit_external_id
        # The organizational unit ID.
        self.organizational_unit_id = organizational_unit_id
        # The name of the organizational unit.
        self.organizational_unit_name = organizational_unit_name
        # The source ID of the organizational unit.
        self.organizational_unit_source_id = organizational_unit_source_id
        # The source type of the organizational unit. Valid values:
        # 
        # - build_in: The organizational unit is created in IDaaS.
        # - ding_talk: The organizational unit is imported from DingTalk.
        # - ad: The organizational unit is imported from Active Directory (AD).
        # - ldap: The organizational unit is imported from a Lightweight Directory Access Protocol (LDAP) directory.
        # - we_com: The organizational unit is imported from WeCom.
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

