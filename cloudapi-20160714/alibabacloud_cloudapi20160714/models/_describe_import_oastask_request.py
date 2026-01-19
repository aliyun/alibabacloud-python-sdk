# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeImportOASTaskRequest(DaraModel):
    def __init__(
        self,
        operation_id: str = None,
        security_token: str = None,
    ):
        # The ID of the asynchronous API import task that was generated during the import operation. This ID is used to query the execution status of the API import task.
        # 
        # This parameter is required.
        self.operation_id = operation_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

