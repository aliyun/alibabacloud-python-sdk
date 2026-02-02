# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListJobHistoryRequest(DaraModel):
    def __init__(
        self,
        count: int = None,
        marker: str = None,
        runtime_id: int = None,
    ):
        # Specifies the number of running records of the migration task to be returned.\\
        # Valid values: 0 - 1000.\\
        # Default value: 1000.
        self.count = count
        # The marker after which the running history of the task is listed.\\
        # By default, this parameter is left empty.
        self.marker = marker
        # The execution ID of the task. If you specify an execution ID, only the running history related to the execution ID is listed.
        self.runtime_id = runtime_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['count'] = self.count

        if self.marker is not None:
            result['marker'] = self.marker

        if self.runtime_id is not None:
            result['runtimeId'] = self.runtime_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('marker') is not None:
            self.marker = m.get('marker')

        if m.get('runtimeId') is not None:
            self.runtime_id = m.get('runtimeId')

        return self

