# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserDcdnIpaStatusResponseBody(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        in_debt: bool = None,
        in_debt_overdue: bool = None,
        on_service: bool = None,
        request_id: str = None,
    ):
        # Indicates whether the IPA service is activated.
        self.enabled = enabled
        # Indicates whether you have overdue payments.
        self.in_debt = in_debt
        # Indicates whether the grace period for your overdue payments expired.
        self.in_debt_overdue = in_debt_overdue
        # Indicates whether the IPA service is available. The IPA service is available when no payment is overdue.
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

