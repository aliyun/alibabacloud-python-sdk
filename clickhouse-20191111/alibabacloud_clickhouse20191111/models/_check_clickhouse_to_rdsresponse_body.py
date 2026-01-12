# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckClickhouseToRDSResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        request_id: str = None,
        status: bool = None,
    ):
        # *   When the value **true** is returned for the **Status** parameter, the system does not return the ErrorCode parameter.
        # *   When the value **false** is returned for the **Status** parameter, the system returns for the ErrorCode parameter the reason why the ApsaraDB for ClickHouse cluster cannot be connected to the ApsaraDB RDS for MySQL instance.
        self.error_code = error_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the ApsaraDB for ClickHouse cluster can be connected to the ApsaraDB RDS for MySQL instance.
        # 
        # *   **true**: The ApsaraDB for ClickHouse cluster can be connected to the ApsaraDB RDS for MySQL instance.
        # *   **false**: The ApsaraDB for ClickHouse cluster cannot be connected to the ApsaraDB RDS for MySQL instance.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

