# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPayerForAccountResponseBody(DaraModel):
    def __init__(
        self,
        payer_account_id: str = None,
        payer_account_name: str = None,
        request_id: str = None,
    ):
        # The ID of the settlement account.
        self.payer_account_id = payer_account_id
        # The name of the settlement account.
        self.payer_account_name = payer_account_name
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.payer_account_id is not None:
            result['PayerAccountId'] = self.payer_account_id

        if self.payer_account_name is not None:
            result['PayerAccountName'] = self.payer_account_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PayerAccountId') is not None:
            self.payer_account_id = m.get('PayerAccountId')

        if m.get('PayerAccountName') is not None:
            self.payer_account_name = m.get('PayerAccountName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

