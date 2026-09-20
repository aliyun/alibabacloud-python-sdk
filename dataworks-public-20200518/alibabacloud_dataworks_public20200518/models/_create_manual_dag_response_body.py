# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateManualDagResponseBody(DaraModel):
    def __init__(
        self,
        dag_id: int = None,
        request_id: str = None,
    ):
        # The instance ID of the dagrun for the manual business process. You can use this DagId with the corresponding operation to query the detailed information and status of the internal node instances of this manual business process execution.
        self.dag_id = dag_id
        # The unique request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

