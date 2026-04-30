# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ClientBalanceDTO(DaraModel):
    def __init__(
        self,
        balance: float = None,
        balance_type: str = None,
        client_id: int = None,
        enable_balance: bool = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
    ):
        self.balance = balance
        self.balance_type = balance_type
        self.client_id = client_id
        self.enable_balance = enable_balance
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        # ID
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.balance is not None:
            result['balance'] = self.balance

        if self.balance_type is not None:
            result['balanceType'] = self.balance_type

        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.enable_balance is not None:
            result['enableBalance'] = self.enable_balance

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('balance') is not None:
            self.balance = m.get('balance')

        if m.get('balanceType') is not None:
            self.balance_type = m.get('balanceType')

        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('enableBalance') is not None:
            self.enable_balance = m.get('enableBalance')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        return self

