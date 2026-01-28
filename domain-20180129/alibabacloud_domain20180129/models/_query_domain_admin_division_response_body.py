# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class QueryDomainAdminDivisionResponseBody(DaraModel):
    def __init__(
        self,
        admin_divisions: main_models.QueryDomainAdminDivisionResponseBodyAdminDivisions = None,
        request_id: str = None,
    ):
        self.admin_divisions = admin_divisions
        self.request_id = request_id

    def validate(self):
        if self.admin_divisions:
            self.admin_divisions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_divisions is not None:
            result['AdminDivisions'] = self.admin_divisions.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminDivisions') is not None:
            temp_model = main_models.QueryDomainAdminDivisionResponseBodyAdminDivisions()
            self.admin_divisions = temp_model.from_map(m.get('AdminDivisions'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryDomainAdminDivisionResponseBodyAdminDivisions(DaraModel):
    def __init__(
        self,
        admin_division: List[main_models.QueryDomainAdminDivisionResponseBodyAdminDivisionsAdminDivision] = None,
    ):
        self.admin_division = admin_division

    def validate(self):
        if self.admin_division:
            for v1 in self.admin_division:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AdminDivision'] = []
        if self.admin_division is not None:
            for k1 in self.admin_division:
                result['AdminDivision'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.admin_division = []
        if m.get('AdminDivision') is not None:
            for k1 in m.get('AdminDivision'):
                temp_model = main_models.QueryDomainAdminDivisionResponseBodyAdminDivisionsAdminDivision()
                self.admin_division.append(temp_model.from_map(k1))

        return self

class QueryDomainAdminDivisionResponseBodyAdminDivisionsAdminDivision(DaraModel):
    def __init__(
        self,
        children: main_models.QueryDomainAdminDivisionResponseBodyAdminDivisionsAdminDivisionChildren = None,
        division_name: str = None,
    ):
        self.children = children
        self.division_name = division_name

    def validate(self):
        if self.children:
            self.children.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.children is not None:
            result['Children'] = self.children.to_map()

        if self.division_name is not None:
            result['DivisionName'] = self.division_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Children') is not None:
            temp_model = main_models.QueryDomainAdminDivisionResponseBodyAdminDivisionsAdminDivisionChildren()
            self.children = temp_model.from_map(m.get('Children'))

        if m.get('DivisionName') is not None:
            self.division_name = m.get('DivisionName')

        return self

class QueryDomainAdminDivisionResponseBodyAdminDivisionsAdminDivisionChildren(DaraModel):
    def __init__(
        self,
        children: List[main_models.QueryDomainAdminDivisionResponseBodyAdminDivisionsAdminDivisionChildrenChildren] = None,
    ):
        self.children = children

    def validate(self):
        if self.children:
            for v1 in self.children:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Children'] = []
        if self.children is not None:
            for k1 in self.children:
                result['Children'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children = []
        if m.get('Children') is not None:
            for k1 in m.get('Children'):
                temp_model = main_models.QueryDomainAdminDivisionResponseBodyAdminDivisionsAdminDivisionChildrenChildren()
                self.children.append(temp_model.from_map(k1))

        return self

class QueryDomainAdminDivisionResponseBodyAdminDivisionsAdminDivisionChildrenChildren(DaraModel):
    def __init__(
        self,
        child_division_name: str = None,
    ):
        self.child_division_name = child_division_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.child_division_name is not None:
            result['ChildDivisionName'] = self.child_division_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChildDivisionName') is not None:
            self.child_division_name = m.get('ChildDivisionName')

        return self

