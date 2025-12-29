# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckRecoveryConditionResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        is_valid: bool = None,
        request_id: str = None,
    ):
        # The instance ID
        self.dbinstance_name = dbinstance_name
        # Indicates whether the data of the instance can be restored. Valid values:
        # 
        # *   **true**: The data of the instance can be restored.
        # *   **false**: The data of the instance cannot be restored.
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
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.is_valid is not None:
            result['IsValid'] = self.is_valid

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('IsValid') is not None:
            self.is_valid = m.get('IsValid')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

