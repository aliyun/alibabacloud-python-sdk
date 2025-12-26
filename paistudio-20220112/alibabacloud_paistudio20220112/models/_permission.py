# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Permission(DaraModel):
    def __init__(
        self,
        is_enabled: bool = None,
        resource_type: str = None,
    ):
        self.is_enabled = is_enabled
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

