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
        # The custom unique business identifier on the merchant side, which is used for subsequent troubleshooting. It supports a combination of letters and digits and can be up to 32 characters in length. Make sure that the value is unique.
        self.merchant_biz_id = merchant_biz_id
        # The unique identifier of the entire authentication process. You must call the Initialize operation to obtain this value.
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

