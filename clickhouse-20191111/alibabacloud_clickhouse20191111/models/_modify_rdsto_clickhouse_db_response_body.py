# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRDSToClickhouseDbResponseBody(DaraModel):
    def __init__(
        self,
        error_code: int = None,
        error_msg: str = None,
        request_id: str = None,
        status: int = None,
    ):
        # The error code.
        self.error_code = error_code
        # *   If the value **1** is returned for the **Status** parameter, the system does not return the ErrorMsg parameter.
        # *   If the value **0** is returned for the **Status** parameter, the ErrorMsg parameter returns the cause for the modification failure.
        self.error_msg = error_msg
        # The request ID.
        self.request_id = request_id
        # Indicates whether the modification was successful. Valid values:
        # 
        # *   **1**: The modification was successful.
        # *   **0**: The modification failed.
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

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

