# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserLogserviceStatusResponseBody(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        in_debt: bool = None,
        in_debt_overdue: bool = None,
        on_service: bool = None,
        request_id: str = None,
    ):
        # Indicates whether Log Service is activated.
        # 
        # *   true
        # *   false
        self.enabled = enabled
        # Indicates whether your Log Service has overdue payments.
        # 
        # *   true
        # *   false
        self.in_debt = in_debt
        # Indicates whether an overdue payment of your Log Service has passed the grace period.
        # 
        # *   true
        # *   false
        self.in_debt_overdue = in_debt_overdue
        # Indicates whether Log Service is available.
        # 
        # *   true
        # *   false
        self.on_service = on_service
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.in_debt is not None:
            result['InDebt'] = self.in_debt

        if self.in_debt_overdue is not None:
            result['InDebtOverdue'] = self.in_debt_overdue

        if self.on_service is not None:
            result['OnService'] = self.on_service

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('InDebt') is not None:
            self.in_debt = m.get('InDebt')

        if m.get('InDebtOverdue') is not None:
            self.in_debt_overdue = m.get('InDebtOverdue')

        if m.get('OnService') is not None:
            self.on_service = m.get('OnService')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

