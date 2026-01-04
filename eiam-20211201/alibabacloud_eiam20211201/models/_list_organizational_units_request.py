# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListOrganizationalUnitsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        organizational_unit_ids: List[str] = None,
        organizational_unit_name: str = None,
        organizational_unit_name_starts_with: str = None,
        page_number: int = None,
        page_size: int = None,
        parent_id: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The IDs of organizational units.
        self.organizational_unit_ids = organizational_unit_ids
        # The name of the organizational unit.
        self.organizational_unit_name = organizational_unit_name
        # Organization name, matching left
        self.organizational_unit_name_starts_with = organizational_unit_name_starts_with
        # The number of the page to return. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 20.
        self.page_size = page_size
        # The ID of the parent organizational unit.
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.organizational_unit_ids is not None:
            result['OrganizationalUnitIds'] = self.organizational_unit_ids

        if self.organizational_unit_name is not None:
            result['OrganizationalUnitName'] = self.organizational_unit_name

        if self.organizational_unit_name_starts_with is not None:
            result['OrganizationalUnitNameStartsWith'] = self.organizational_unit_name_starts_with

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrganizationalUnitIds') is not None:
            self.organizational_unit_ids = m.get('OrganizationalUnitIds')

        if m.get('OrganizationalUnitName') is not None:
            self.organizational_unit_name = m.get('OrganizationalUnitName')

        if m.get('OrganizationalUnitNameStartsWith') is not None:
            self.organizational_unit_name_starts_with = m.get('OrganizationalUnitNameStartsWith')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        return self

