# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWorkflowInstancesResponseBody(DaraModel):
    def __init__(
        self,
        operation_id: str = None,
        request_id: str = None,
    ):
        # The ID of the operation. You can use this field to query the results of the creation operation through the GetCreateWorkflowInstancesResult interface.
        self.operation_id = operation_id
        # The ID of the request. It is used to locate logs and troubleshoot problems.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

