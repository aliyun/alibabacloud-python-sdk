# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckBudgetNameExistsResponseBody(DaraModel):
    def __init__(
        self,
        budget_name: str = None,
        exists: bool = None,
        request_id: str = None,
    ):
        self.budget_name = budget_name
        self.exists = exists
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.budget_name is not None:
            result['BudgetName'] = self.budget_name

        if self.exists is not None:
            result['Exists'] = self.exists

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BudgetName') is not None:
            self.budget_name = m.get('BudgetName')

        if m.get('Exists') is not None:
            self.exists = m.get('Exists')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

