# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecMetaProfilingTaskRunRequest(DaraModel):
    def __init__(
        self,
        batch_no: str = None,
        component_id: int = None,
    ):
        self.batch_no = batch_no
        self.component_id = component_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_no is not None:
            result['batchNo'] = self.batch_no

        if self.component_id is not None:
            result['componentId'] = self.component_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchNo') is not None:
            self.batch_no = m.get('batchNo')

        if m.get('componentId') is not None:
            self.component_id = m.get('componentId')

        return self

