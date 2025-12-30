# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SubmitPurchaseInfoRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        purchase_currency: str = None,
        purchase_price: float = None,
        purchase_proofs: List[str] = None,
    ):
        self.biz_id = biz_id
        self.purchase_currency = purchase_currency
        self.purchase_price = purchase_price
        self.purchase_proofs = purchase_proofs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.purchase_currency is not None:
            result['PurchaseCurrency'] = self.purchase_currency

        if self.purchase_price is not None:
            result['PurchasePrice'] = self.purchase_price

        if self.purchase_proofs is not None:
            result['PurchaseProofs'] = self.purchase_proofs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('PurchaseCurrency') is not None:
            self.purchase_currency = m.get('PurchaseCurrency')

        if m.get('PurchasePrice') is not None:
            self.purchase_price = m.get('PurchasePrice')

        if m.get('PurchaseProofs') is not None:
            self.purchase_proofs = m.get('PurchaseProofs')

        return self

