# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckVerifyLogRequest(DaraModel):
    def __init__(
        self,
        merchant_biz_id: str = None,
        transaction_id: str = None,
    ):
        # The merchant-side custom business unique identifier, used for subsequent troubleshooting. The value supports a combination of letters and numbers with a maximum length of 32 characters. Ensure that the value is unique.
        self.merchant_biz_id = merchant_biz_id
        # The unique identifier of the entire authentication process. Obtain this value by calling the Initialize operation.
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id

        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')

        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')

        return self

