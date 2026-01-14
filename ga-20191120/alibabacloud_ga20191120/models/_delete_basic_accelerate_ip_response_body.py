# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteBasicAccelerateIpResponseBody(DaraModel):
    def __init__(
        self,
        accelerate_ip_id: str = None,
        request_id: str = None,
    ):
        # The ID of the accelerated IP address that is deleted.
        self.accelerate_ip_id = accelerate_ip_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerate_ip_id is not None:
            result['AccelerateIpId'] = self.accelerate_ip_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateIpId') is not None:
            self.accelerate_ip_id = m.get('AccelerateIpId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

