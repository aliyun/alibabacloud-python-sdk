# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListOrganizationalUnitsForApplicationResponseBody(DaraModel):
    def __init__(
        self,
        organizational_units: List[main_models.ListOrganizationalUnitsForApplicationResponseBodyOrganizationalUnits] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The IDs of the organizations that are allowed to access the application.
        self.organizational_units = organizational_units
        # The ID of the request.
        self.request_id = request_id
        # The total number of the returned entries.
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
                temp_model = main_models.ListOrganizationalUnitsForApplicationResponseBodyOrganizationalUnits()
                self.organizational_units.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListOrganizationalUnitsForApplicationResponseBodyOrganizationalUnits(DaraModel):
    def __init__(
        self,
        organizational_unit_id: str = None,
    ):
        # The ID of the organization that is allowed to access the application.
        self.organizational_unit_id = organizational_unit_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')

        return self

