# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRerunWorkflowInstancesResultRequest(DaraModel):
    def __init__(
        self,
        operation_id: str = None,
    ):
        # The operation ID used to asynchronously query the result of the workflow instance rerun. This value is obtained from the RerunWorkflowInstances operation.
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

