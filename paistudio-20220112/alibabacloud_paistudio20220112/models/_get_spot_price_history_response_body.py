# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class GetSpotPriceHistoryResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        spot_price_history: List[main_models.SpotPriceItem] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.spot_price_history = spot_price_history
        self.total_count = total_count

    def validate(self):
        if self.spot_price_history:
            for v1 in self.spot_price_history:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SpotPriceHistory'] = []
        if self.spot_price_history is not None:
            for k1 in self.spot_price_history:
                result['SpotPriceHistory'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.spot_price_history = []
        if m.get('SpotPriceHistory') is not None:
            for k1 in m.get('SpotPriceHistory'):
                temp_model = main_models.SpotPriceItem()
                self.spot_price_history.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

