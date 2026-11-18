# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteModelGroupRequest(DaraModel):
    def __init__(
        self,
        expected_version: int = None,
    ):
        # The expected version. Only this version is deleted. API saved-state references prevent deletion, and authorization references are cleared.
        # 
        # This parameter is required.
        self.expected_version = expected_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expected_version is not None:
            result['expectedVersion'] = self.expected_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expectedVersion') is not None:
            self.expected_version = m.get('expectedVersion')

        return self

