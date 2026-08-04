# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterExportMemberBalanceOrdersRequest(DaraModel):
    def __init__(
        self,
        balance_type: str = None,
        direction: str = None,
    ):
        # The balance type filter. Valid values: permanent and monthly.
        self.balance_type = balance_type
        # The change direction filter. Valid values: in and out.
        self.direction = direction

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.balance_type is not None:
            result['balanceType'] = self.balance_type

        if self.direction is not None:
            result['direction'] = self.direction

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('balanceType') is not None:
            self.balance_type = m.get('balanceType')

        if m.get('direction') is not None:
            self.direction = m.get('direction')

        return self

