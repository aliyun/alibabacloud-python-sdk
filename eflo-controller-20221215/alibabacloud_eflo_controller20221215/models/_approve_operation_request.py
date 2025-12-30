# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApproveOperationRequest(DaraModel):
    def __init__(
        self,
        node_id: str = None,
        operation_type: str = None,
    ):
        # The node ID.
        self.node_id = node_id
        # The O\\&M operation type
        # 
        # Valid value:
        # 
        # *   RepairMachine
        self.operation_type = operation_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        return self

