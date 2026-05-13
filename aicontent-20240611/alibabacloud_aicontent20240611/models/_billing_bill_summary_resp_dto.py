# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class BillingBillSummaryRespDTO(DaraModel):
    def __init__(
        self,
        points: List[main_models.BillingBillSummaryPointDTO] = None,
        total_amount: float = None,
    ):
        self.points = points
        self.total_amount = total_amount

    def validate(self):
        if self.points:
            for v1 in self.points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['points'] = []
        if self.points is not None:
            for k1 in self.points:
                result['points'].append(k1.to_map() if k1 else None)

        if self.total_amount is not None:
            result['totalAmount'] = self.total_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.points = []
        if m.get('points') is not None:
            for k1 in m.get('points'):
                temp_model = main_models.BillingBillSummaryPointDTO()
                self.points.append(temp_model.from_map(k1))

        if m.get('totalAmount') is not None:
            self.total_amount = m.get('totalAmount')

        return self

