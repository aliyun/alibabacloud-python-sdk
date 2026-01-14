# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class GetAlipayTransferStatusResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetAlipayTransferStatusResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetAlipayTransferStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetAlipayTransferStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        alipay_order_detail: str = None,
        alipay_order_id: str = None,
        code: str = None,
        creator: str = None,
        main_account_id: str = None,
        modifier: str = None,
        qr_url: str = None,
        scope: str = None,
        status: int = None,
        title: str = None,
        trans_amount: str = None,
        wallet_item_code: str = None,
    ):
        self.account_id = account_id
        self.alipay_order_detail = alipay_order_detail
        self.alipay_order_id = alipay_order_id
        self.code = code
        self.creator = creator
        self.main_account_id = main_account_id
        self.modifier = modifier
        self.qr_url = qr_url
        self.scope = scope
        self.status = status
        self.title = title
        self.trans_amount = trans_amount
        self.wallet_item_code = wallet_item_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.alipay_order_detail is not None:
            result['alipayOrderDetail'] = self.alipay_order_detail

        if self.alipay_order_id is not None:
            result['alipayOrderId'] = self.alipay_order_id

        if self.code is not None:
            result['code'] = self.code

        if self.creator is not None:
            result['creator'] = self.creator

        if self.main_account_id is not None:
            result['mainAccountId'] = self.main_account_id

        if self.modifier is not None:
            result['modifier'] = self.modifier

        if self.qr_url is not None:
            result['qrURL'] = self.qr_url

        if self.scope is not None:
            result['scope'] = self.scope

        if self.status is not None:
            result['status'] = self.status

        if self.title is not None:
            result['title'] = self.title

        if self.trans_amount is not None:
            result['transAmount'] = self.trans_amount

        if self.wallet_item_code is not None:
            result['walletItemCode'] = self.wallet_item_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('alipayOrderDetail') is not None:
            self.alipay_order_detail = m.get('alipayOrderDetail')

        if m.get('alipayOrderId') is not None:
            self.alipay_order_id = m.get('alipayOrderId')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('mainAccountId') is not None:
            self.main_account_id = m.get('mainAccountId')

        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')

        if m.get('qrURL') is not None:
            self.qr_url = m.get('qrURL')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('transAmount') is not None:
            self.trans_amount = m.get('transAmount')

        if m.get('walletItemCode') is not None:
            self.wallet_item_code = m.get('walletItemCode')

        return self

