# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetDataShareInstanceResponseBody(DaraModel):
    def __init__(
        self,
        err_message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The error message returned if the operation fails.
        self.err_message = err_message
        # The ID of the request.
        self.request_id = request_id
        # The state of the operation. Valid values:
        # 
        # *   **success**: The operation is successful.
        # *   **failed**: The operation fails.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

