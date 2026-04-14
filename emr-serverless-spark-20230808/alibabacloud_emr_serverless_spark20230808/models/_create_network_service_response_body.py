# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNetworkServiceResponseBody(DaraModel):
    def __init__(
        self,
        operation_id: str = None,
        request_id: str = None,
    ):
        # Workspace Id。
        self.operation_id = operation_id
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation_id is not None:
            result['operationId'] = self.operation_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operationId') is not None:
            self.operation_id = m.get('operationId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

