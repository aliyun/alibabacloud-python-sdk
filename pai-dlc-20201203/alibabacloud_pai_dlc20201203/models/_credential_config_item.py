# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class CredentialConfigItem(DaraModel):
    def __init__(
        self,
        key: str = None,
        roles: List[main_models.CredentialRole] = None,
        type: str = None,
    ):
        self.key = key
        self.roles = roles
        self.type = type

    def validate(self):
        if self.roles:
            for v1 in self.roles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        result['Roles'] = []
        if self.roles is not None:
            for k1 in self.roles:
                result['Roles'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        self.roles = []
        if m.get('Roles') is not None:
            for k1 in m.get('Roles'):
                temp_model = main_models.CredentialRole()
                self.roles.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

