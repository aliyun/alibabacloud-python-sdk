# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUpdateTaskResultRequest(DaraModel):
    def __init__(
        self,
        operation_id: str = None,
    ):
        # The operation ID, which is used to query the result of the asynchronous node update. You can obtain this ID from the UpdateTaskAsync operation.
        # 
        # This parameter is required.
        self.operation_id = operation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')

        return self

