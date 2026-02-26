# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CustomPrompt(DaraModel):
    def __init__(
        self,
        role_definition: str = None,
    ):
        self.role_definition = role_definition

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role_definition is not None:
            result['RoleDefinition'] = self.role_definition

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleDefinition') is not None:
            self.role_definition = m.get('RoleDefinition')

        return self

