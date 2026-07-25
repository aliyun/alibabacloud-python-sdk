# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetYikeJobCreditResponseBody(DaraModel):
    def __init__(
        self,
        credit_status: str = None,
        job_credit_cost: float = None,
        job_id: str = None,
        request_id: str = None,
    ):
        self.credit_status = credit_status
        self.job_credit_cost = job_credit_cost
        self.job_id = job_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credit_status is not None:
            result['CreditStatus'] = self.credit_status

        if self.job_credit_cost is not None:
            result['JobCreditCost'] = self.job_credit_cost

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreditStatus') is not None:
            self.credit_status = m.get('CreditStatus')

        if m.get('JobCreditCost') is not None:
            self.job_credit_cost = m.get('JobCreditCost')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

