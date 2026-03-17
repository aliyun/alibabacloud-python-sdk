# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCloudConnectNetworkUseLimitResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_amount: int = None,
        used_amount: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The maximum number of CCN instances that the current account can create in the specified region.
        self.total_amount = total_amount
        # The number of CCN instances that you have created.
        self.used_amount = used_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_amount is not None:
            result['TotalAmount'] = self.total_amount

        if self.used_amount is not None:
            result['UsedAmount'] = self.used_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalAmount') is not None:
            self.total_amount = m.get('TotalAmount')

        if m.get('UsedAmount') is not None:
            self.used_amount = m.get('UsedAmount')

        return self

