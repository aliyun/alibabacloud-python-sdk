# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20210422 import models as main_models
from darabonba.model import DaraModel

class CheckServiceLinkedRoleForDeletingResponseBody(DaraModel):
    def __init__(
        self,
        deletable: bool = None,
        request_id: str = None,
        role_usages: List[main_models.CheckServiceLinkedRoleForDeletingResponseBodyRoleUsages] = None,
    ):
        self.deletable = deletable
        self.request_id = request_id
        self.role_usages = role_usages

    def validate(self):
        if self.role_usages:
            for v1 in self.role_usages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deletable is not None:
            result['Deletable'] = self.deletable

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RoleUsages'] = []
        if self.role_usages is not None:
            for k1 in self.role_usages:
                result['RoleUsages'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Deletable') is not None:
            self.deletable = m.get('Deletable')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.role_usages = []
        if m.get('RoleUsages') is not None:
            for k1 in m.get('RoleUsages'):
                temp_model = main_models.CheckServiceLinkedRoleForDeletingResponseBodyRoleUsages()
                self.role_usages.append(temp_model.from_map(k1))

        return self



class CheckServiceLinkedRoleForDeletingResponseBodyRoleUsages(DaraModel):
    def __init__(
        self,
        region: str = None,
        resources: List[str] = None,
    ):
        self.region = region
        self.resources = resources

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region is not None:
            result['Region'] = self.region

        if self.resources is not None:
            result['Resources'] = self.resources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        return self

