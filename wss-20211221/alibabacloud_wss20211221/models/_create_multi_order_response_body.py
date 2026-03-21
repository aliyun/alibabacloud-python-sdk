# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateMultiOrderResponseBody(DaraModel):
    def __init__(
        self,
        order_ids: List[int] = None,
        request_id: str = None,
    ):
        self.order_ids = order_ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

