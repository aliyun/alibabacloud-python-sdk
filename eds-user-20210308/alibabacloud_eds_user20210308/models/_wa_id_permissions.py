# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_user20210308 import models as main_models
from darabonba.model import DaraModel

class WaIdPermissions(DaraModel):
    def __init__(
        self,
        code: str = None,
        is_basic_child: bool = None,
        name: str = None,
        sub_permissions: List[main_models.WaIdPermissions] = None,
        type: str = None,
    ):
        self.code = code
        self.is_basic_child = is_basic_child
        self.name = name
        self.sub_permissions = sub_permissions
        self.type = type

    def validate(self):
        if self.sub_permissions:
            for v1 in self.sub_permissions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.is_basic_child is not None:
            result['IsBasicChild'] = self.is_basic_child

        if self.name is not None:
            result['Name'] = self.name

        result['SubPermissions'] = []
        if self.sub_permissions is not None:
            for k1 in self.sub_permissions:
                result['SubPermissions'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsBasicChild') is not None:
            self.is_basic_child = m.get('IsBasicChild')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.sub_permissions = []
        if m.get('SubPermissions') is not None:
            for k1 in m.get('SubPermissions'):
                temp_model = main_models.WaIdPermissions()
                self.sub_permissions.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

