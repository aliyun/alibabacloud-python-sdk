# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTokenRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        pbc_id: int = None,
    ):
        self.account_id = account_id
        self.pbc_id = pbc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.pbc_id is not None:
            result['pbcId'] = self.pbc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('pbcId') is not None:
            self.pbc_id = m.get('pbcId')

        return self

