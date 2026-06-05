# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateHiveResponseBody(DaraModel):
    def __init__(
        self,
        hive_id: str = None,
        request_id: str = None,
    ):
        self.hive_id = hive_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hive_id is not None:
            result['HiveId'] = self.hive_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HiveId') is not None:
            self.hive_id = m.get('HiveId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

