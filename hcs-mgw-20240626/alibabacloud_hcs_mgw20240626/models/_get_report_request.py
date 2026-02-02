# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetReportRequest(DaraModel):
    def __init__(
        self,
        runtime_id: int = None,
        version: str = None,
    ):
        # The execution ID of the migration task.
        self.runtime_id = runtime_id
        # The ID of the migration task.
        # 
        # This parameter is required.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.runtime_id is not None:
            result['runtimeId'] = self.runtime_id

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('runtimeId') is not None:
            self.runtime_id = m.get('runtimeId')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

