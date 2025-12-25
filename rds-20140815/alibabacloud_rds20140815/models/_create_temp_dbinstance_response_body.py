# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTempDBInstanceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        temp_dbinstance_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The temporary instance ID.
        self.temp_dbinstance_id = temp_dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.temp_dbinstance_id is not None:
            result['TempDBInstanceId'] = self.temp_dbinstance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TempDBInstanceId') is not None:
            self.temp_dbinstance_id = m.get('TempDBInstanceId')

        return self

