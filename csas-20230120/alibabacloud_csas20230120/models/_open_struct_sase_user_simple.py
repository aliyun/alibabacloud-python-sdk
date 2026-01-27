# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class OpenStructSaseUserSimple(DaraModel):
    def __init__(
        self,
        departments: List[main_models.OpenStructSaseUserSimpleDepartments] = None,
        email: str = None,
        idp_config_id: str = None,
        sase_user_id: str = None,
        telephone: str = None,
        username: str = None,
    ):
        self.departments = departments
        self.email = email
        self.idp_config_id = idp_config_id
        self.sase_user_id = sase_user_id
        self.telephone = telephone
        self.username = username

    def validate(self):
        if self.departments:
            for v1 in self.departments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Departments'] = []
        if self.departments is not None:
            for k1 in self.departments:
                result['Departments'].append(k1.to_map() if k1 else None)

        if self.email is not None:
            result['Email'] = self.email

        if self.idp_config_id is not None:
            result['IdpConfigId'] = self.idp_config_id

        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id

        if self.telephone is not None:
            result['Telephone'] = self.telephone

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.departments = []
        if m.get('Departments') is not None:
            for k1 in m.get('Departments'):
                temp_model = main_models.OpenStructSaseUserSimpleDepartments()
                self.departments.append(temp_model.from_map(k1))

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('IdpConfigId') is not None:
            self.idp_config_id = m.get('IdpConfigId')

        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')

        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

class OpenStructSaseUserSimpleDepartments(DaraModel):
    def __init__(
        self,
        department_id: str = None,
        full_department_id_path: str = None,
        full_dn: str = None,
        name: str = None,
        parent_department_id: str = None,
    ):
        self.department_id = department_id
        self.full_department_id_path = full_department_id_path
        self.full_dn = full_dn
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

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentDepartmentId') is not None:
            self.parent_department_id = m.get('ParentDepartmentId')

        return self

