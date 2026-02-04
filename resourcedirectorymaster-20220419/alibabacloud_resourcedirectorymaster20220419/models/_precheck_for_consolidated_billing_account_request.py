# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PrecheckForConsolidatedBillingAccountRequest(DaraModel):
    def __init__(
        self,
        billing_account_id: str = None,
    ):
        # The ID of the management account or member to be used as a main financial account.
        # 
        # This parameter is required.
        self.billing_account_id = billing_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_account_id is not None:
            result['BillingAccountId'] = self.billing_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingAccountId') is not None:
            self.billing_account_id = m.get('BillingAccountId')

        return self

