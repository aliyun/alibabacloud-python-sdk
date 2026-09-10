# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecDataCheckRunFailedRequest(DaraModel):
    def __init__(
        self,
        batch_id: int = None,
        type: int = None,
    ):
        # The batch ID returned by the ExecDataCheckSaveTask operation.
        # 
        # This parameter is required.
        self.batch_id = batch_id
        # The rerun type. Valid values:
        # 
        # - 0: Reruns only execution-failed subtasks.
        # - 1: Reruns execution-failed and validation-failed subtasks.
        # - 2: Reruns execution-failed and stopped subtasks.
        # 
        # Default value: 1.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['batchId'] = self.batch_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchId') is not None:
            self.batch_id = m.get('batchId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

