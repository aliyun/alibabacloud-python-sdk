# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OpenStructSaseDepartment(DaraModel):
    def __init__(
        self,
        department_id: str = None,
        full_department_id_path: str = None,
        full_dn: str = None,
        idp_id: int = None,
        name: str = None,
        parent_department_id: str = None,
    ):
        self.department_id = department_id
        self.full_department_id_path = full_department_id_path
        self.full_dn = full_dn
        self.idp_id = idp_id
        self.name = name
        self.parent_department_id = parent_department_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id

        if self.full_department_id_path is not None:
            result['FullDepartmentIdPath'] = self.full_department_id_path

        if self.full_dn is not None:
            result['FullDn'] = self.full_dn

        if self.idp_id is not None:
            result['IdpId'] = self.idp_id

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_department_id is not None:
            result['ParentDepartmentId'] = self.parent_department_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')

        if m.get('FullDepartmentIdPath') is not None:
            self.full_department_id_path = m.get('FullDepartmentIdPath')

        if m.get('FullDn') is not None:
            self.full_dn = m.get('FullDn')

        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentDepartmentId') is not None:
            self.parent_department_id = m.get('ParentDepartmentId')

        return self

