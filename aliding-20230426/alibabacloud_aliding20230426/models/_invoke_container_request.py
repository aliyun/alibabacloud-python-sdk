# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InvokeContainerRequest(DaraModel):
    def __init__(
        self,
        operation_id: str = None,
        params: str = None,
    ):
        # This parameter is required.
        self.operation_id = operation_id
        self.params = params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation_id is not None:
            result['operationId'] = self.operation_id

        if self.params is not None:
            result['params'] = self.params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operationId') is not None:
            self.operation_id = m.get('operationId')

        if m.get('params') is not None:
            self.params = m.get('params')

        return self

