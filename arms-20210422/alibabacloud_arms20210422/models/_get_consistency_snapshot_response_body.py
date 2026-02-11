# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetConsistencySnapshotResponseBody(DaraModel):
    def __init__(
        self,
        consistency_result_json_str: str = None,
        request_id: str = None,
    ):
        self.consistency_result_json_str = consistency_result_json_str
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consistency_result_json_str is not None:
            result['ConsistencyResultJsonStr'] = self.consistency_result_json_str

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsistencyResultJsonStr') is not None:
            self.consistency_result_json_str = m.get('ConsistencyResultJsonStr')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

