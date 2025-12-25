# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRCVClusterResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        vcluster_status: str = None,
    ):
        self.request_id = request_id
        self.vcluster_status = vcluster_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.vcluster_status is not None:
            result['VClusterStatus'] = self.vcluster_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VClusterStatus') is not None:
            self.vcluster_status = m.get('VClusterStatus')

        return self

