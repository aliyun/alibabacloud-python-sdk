# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHybridCloudProtectableCountResponseBody(DaraModel):
    def __init__(
        self,
        protectable_count: int = None,
        request_id: str = None,
    ):
        # The number of protection nodes that can be added to the hybrid cloud cluster.
        self.protectable_count = protectable_count
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.protectable_count is not None:
            result['ProtectableCount'] = self.protectable_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProtectableCount') is not None:
            self.protectable_count = m.get('ProtectableCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

