# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePayerForAccountRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        payer_account_id: str = None,
    ):
        # The Alibaba Cloud account ID of the member.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The ID of the billing account.
        # 
        # This parameter is required.
        self.payer_account_id = payer_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.payer_account_id is not None:
            result['PayerAccountId'] = self.payer_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('PayerAccountId') is not None:
            self.payer_account_id = m.get('PayerAccountId')

        return self

