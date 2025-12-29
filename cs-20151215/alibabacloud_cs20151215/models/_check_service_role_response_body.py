# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class CheckServiceRoleResponseBody(DaraModel):
    def __init__(
        self,
        roles: List[main_models.CheckServiceRoleResponseBodyRoles] = None,
    ):
        # The check results.
        self.roles = roles

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
        result['roles'] = []
        if self.roles is not None:
            for k1 in self.roles:
                result['roles'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.roles = []
        if m.get('roles') is not None:
            for k1 in m.get('roles'):
                temp_model = main_models.CheckServiceRoleResponseBodyRoles()
                self.roles.append(temp_model.from_map(k1))

        return self

class CheckServiceRoleResponseBodyRoles(DaraModel):
    def __init__(
        self,
        granted: bool = None,
        message: str = None,
        name: str = None,
    ):
        # Indicates whether the service role is assigned to ACK.
        # 
        # Valid values:
        # 
        # *   true: The role is assigned to ACK.
        # *   false: The role is not assigned to ACK.
        self.granted = granted
        # The message that is displayed for a role that is not assigned to ACK.
        self.message = message
        # The name of the service role.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.granted is not None:
            result['granted'] = self.granted

        if self.message is not None:
            result['message'] = self.message

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('granted') is not None:
            self.granted = m.get('granted')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

