# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpsertUmodelCommonSchemaRefRequest(DaraModel):
    def __init__(
        self,
        group: str = None,
        version: str = None,
    ):
        # This parameter is required.
        self.group = group
        # This parameter is required.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group is not None:
            result['group'] = self.group

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group') is not None:
            self.group = m.get('group')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

