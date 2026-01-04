# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListOrganizationalUnitParentsResponseBody(DaraModel):
    def __init__(
        self,
        parents: List[main_models.ListOrganizationalUnitParentsResponseBodyParents] = None,
        request_id: str = None,
    ):
        # The parent organizations.
        self.parents = parents
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.parents:
            for v1 in self.parents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Parents'] = []
        if self.parents is not None:
            for k1 in self.parents:
                result['Parents'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parents = []
        if m.get('Parents') is not None:
            for k1 in m.get('Parents'):
                temp_model = main_models.ListOrganizationalUnitParentsResponseBodyParents()
                self.parents.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListOrganizationalUnitParentsResponseBodyParents(DaraModel):
    def __init__(
        self,
        organizational_unit_id: str = None,
        parent_id: str = None,
    ):
        # The organization ID.
        self.organizational_unit_id = organizational_unit_id
        # The parent organization ID.
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        return self

