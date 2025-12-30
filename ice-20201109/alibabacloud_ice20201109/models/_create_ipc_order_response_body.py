# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateIpcOrderResponseBody(DaraModel):
    def __init__(
        self,
        purchase_status: str = None,
        request_id: str = None,
    ):
        self.purchase_status = purchase_status
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.purchase_status is not None:
            result['PurchaseStatus'] = self.purchase_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PurchaseStatus') is not None:
            self.purchase_status = m.get('PurchaseStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

