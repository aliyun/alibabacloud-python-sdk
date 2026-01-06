# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAuditLogConfigResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        update_succeed: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the status of SQL audit is updated. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.update_succeed = update_succeed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.update_succeed is not None:
            result['UpdateSucceed'] = self.update_succeed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UpdateSucceed') is not None:
            self.update_succeed = m.get('UpdateSucceed')

        return self

