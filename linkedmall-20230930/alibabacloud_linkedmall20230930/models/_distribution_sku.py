# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DistributionSku(DaraModel):
    def __init__(
        self,
        alias_title: str = None,
        bar_code: str = None,
        credit_period: int = None,
        dx_price: int = None,
        has_credit: bool = None,
        has_invoice: bool = None,
        jx_price: int = None,
        pic_url: str = None,
        quantity: int = None,
        sku_id: str = None,
        sku_status: str = None,
        tax_code: str = None,
        tax_rate: int = None,
        title: str = None,
    ):
        self.alias_title = alias_title
        self.bar_code = bar_code
        self.credit_period = credit_period
        self.dx_price = dx_price
        self.has_credit = has_credit
        self.has_invoice = has_invoice
        self.jx_price = jx_price
        self.pic_url = pic_url
        self.quantity = quantity
        self.sku_id = sku_id
        self.sku_status = sku_status
        self.tax_code = tax_code
        self.tax_rate = tax_rate
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_title is not None:
            result['aliasTitle'] = self.alias_title

        if self.bar_code is not None:
            result['barCode'] = self.bar_code

        if self.credit_period is not None:
            result['creditPeriod'] = self.credit_period

        if self.dx_price is not None:
            result['dxPrice'] = self.dx_price

        if self.has_credit is not None:
            result['hasCredit'] = self.has_credit

        if self.has_invoice is not None:
            result['hasInvoice'] = self.has_invoice

        if self.jx_price is not None:
            result['jxPrice'] = self.jx_price

        if self.pic_url is not None:
            result['picUrl'] = self.pic_url

        if self.quantity is not None:
            result['quantity'] = self.quantity

        if self.sku_id is not None:
            result['skuId'] = self.sku_id

        if self.sku_status is not None:
            result['skuStatus'] = self.sku_status

        if self.tax_code is not None:
            result['taxCode'] = self.tax_code

        if self.tax_rate is not None:
            result['taxRate'] = self.tax_rate

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliasTitle') is not None:
            self.alias_title = m.get('aliasTitle')

        if m.get('barCode') is not None:
            self.bar_code = m.get('barCode')

        if m.get('creditPeriod') is not None:
            self.credit_period = m.get('creditPeriod')

        if m.get('dxPrice') is not None:
            self.dx_price = m.get('dxPrice')

        if m.get('hasCredit') is not None:
            self.has_credit = m.get('hasCredit')

        if m.get('hasInvoice') is not None:
            self.has_invoice = m.get('hasInvoice')

        if m.get('jxPrice') is not None:
            self.jx_price = m.get('jxPrice')

        if m.get('picUrl') is not None:
            self.pic_url = m.get('picUrl')

        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')

        if m.get('skuId') is not None:
            self.sku_id = m.get('skuId')

        if m.get('skuStatus') is not None:
            self.sku_status = m.get('skuStatus')

        if m.get('taxCode') is not None:
            self.tax_code = m.get('taxCode')

        if m.get('taxRate') is not None:
            self.tax_rate = m.get('taxRate')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

