# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAttackAnalysisMaxQpsResponseBody(DaraModel):
    def __init__(
        self,
        qps: int = None,
        request_id: str = None,
    ):
        # The peak queries per second (QPS) of DDoS attacks. Units: QPS.
        self.qps = qps
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.qps is not None:
            result['Qps'] = self.qps

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

