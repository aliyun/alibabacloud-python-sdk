# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateScanRequest(DaraModel):
    def __init__(
        self,
        code_bundle_id: int = None,
        kind: str = None,
        task_name: str = None,
    ):
        # The code package ID.
        # 
        # This parameter is required.
        self.code_bundle_id = code_bundle_id
        # The type. Valid values:
        # * full: full data
        # * incremental: incremental
        # 
        # This parameter is required.
        self.kind = kind
        # The task name.
        # 
        # This parameter is required.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_bundle_id is not None:
            result['codeBundleId'] = self.code_bundle_id

        if self.kind is not None:
            result['kind'] = self.kind

        if self.task_name is not None:
            result['taskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeBundleId') is not None:
            self.code_bundle_id = m.get('codeBundleId')

        if m.get('kind') is not None:
            self.kind = m.get('kind')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        return self

