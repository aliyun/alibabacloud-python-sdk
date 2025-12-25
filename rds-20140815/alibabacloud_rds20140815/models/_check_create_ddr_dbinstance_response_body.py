# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckCreateDdrDBInstanceResponseBody(DaraModel):
    def __init__(
        self,
        is_valid: str = None,
        request_id: str = None,
    ):
        # Indicates whether the data of the source instance can be restored across regions. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_valid = is_valid
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_valid is not None:
            result['IsValid'] = self.is_valid

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsValid') is not None:
            self.is_valid = m.get('IsValid')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

