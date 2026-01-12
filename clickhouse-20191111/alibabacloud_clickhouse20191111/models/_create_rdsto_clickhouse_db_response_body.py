# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateRDSToClickhouseDbResponseBody(DaraModel):
    def __init__(
        self,
        error_msg: str = None,
        repeated_dbs: List[str] = None,
        request_id: str = None,
        status: int = None,
    ):
        # If the value of the **Status** parameter is -1, the cause of the creation failure is returned.
        self.error_msg = error_msg
        # Duplicate tables in the synchronization task.
        self.repeated_dbs = repeated_dbs
        # The request ID.
        self.request_id = request_id
        # Indicates whether the synchronization task was created. Valid values:
        # 
        # *   **1**: Created.
        # *   **0**: Creation failed. The tables in the synchronization task are duplicate. The duplicate tables are returned for the **RepeatedDbs** parameter.
        # *   **-1**: Creation failed. The cause why the creation failed is returned for the **ErrorMsg** parameter.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.repeated_dbs is not None:
            result['RepeatedDbs'] = self.repeated_dbs

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('RepeatedDbs') is not None:
            self.repeated_dbs = m.get('RepeatedDbs')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

