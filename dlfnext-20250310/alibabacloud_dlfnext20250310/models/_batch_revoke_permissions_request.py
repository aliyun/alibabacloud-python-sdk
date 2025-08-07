# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 
from alibabacloud_dlfnext20250310 import models as main_models 
from typing import List


class BatchRevokePermissionsRequest(DaraModel):
    def __init__(
        self,
        permissions: List[main_models.Permission] = None,
    ):
        self.permissions = permissions

    def validate(self):
        if self.permissions:
            for v1 in self.permissions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['permissions'] = []
        if self.permissions is not None:
            for k1 in self.permissions:
                result['permissions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.permissions = []
        if m.get('permissions') is not None:
            for k1 in m.get('permissions'):
                temp_model = main_models.Permission()
                self.permissions.append(temp_model.from_map(k1))

        return self

