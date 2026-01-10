# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class TriggerConfig(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        methods: List[str] = None,
    ):
        self.auth_type = auth_type
        self.methods = methods

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_type is not None:
            result['authType'] = self.auth_type

        if self.methods is not None:
            result['methods'] = self.methods

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')

        if m.get('methods') is not None:
            self.methods = m.get('methods')

        return self

