# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetYikeAgentJobEstimatedCreditResponseBody(DaraModel):
    def __init__(
        self,
        estimated_credit_cost: float = None,
        request_id: str = None,
    ):
        self.estimated_credit_cost = estimated_credit_cost
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.estimated_credit_cost is not None:
            result['EstimatedCreditCost'] = self.estimated_credit_cost

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EstimatedCreditCost') is not None:
            self.estimated_credit_cost = m.get('EstimatedCreditCost')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

