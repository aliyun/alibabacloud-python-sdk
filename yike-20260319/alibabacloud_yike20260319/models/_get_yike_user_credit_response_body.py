# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetYikeUserCreditResponseBody(DaraModel):
    def __init__(
        self,
        credit_total: str = None,
        credit_usage: str = None,
        request_id: str = None,
    ):
        self.credit_total = credit_total
        self.credit_usage = credit_usage
        # RequestId
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credit_total is not None:
            result['CreditTotal'] = self.credit_total

        if self.credit_usage is not None:
            result['CreditUsage'] = self.credit_usage

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreditTotal') is not None:
            self.credit_total = m.get('CreditTotal')

        if m.get('CreditUsage') is not None:
            self.credit_usage = m.get('CreditUsage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

