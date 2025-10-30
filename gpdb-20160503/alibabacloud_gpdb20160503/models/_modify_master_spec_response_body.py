# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyMasterSpecResponseBody(DaraModel):
    def __init__(
        self,
        db_instance_id: str = None,
        error_message: str = None,
        request_id: str = None,
        status: bool = None,
    ):
        # The instance ID.
        self.db_instance_id = db_instance_id
        # The returned message.
        # 
        # This parameter is returned only if the request fails.
        self.error_message = error_message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **false**
        # *   **true**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

