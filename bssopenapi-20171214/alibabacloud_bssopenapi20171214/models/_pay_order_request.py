# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class PayOrderRequest(DaraModel):
    def __init__(
        self,
        buyer_id: int = None,
        ec_id_account_ids: List[main_models.PayOrderRequestEcIdAccountIds] = None,
        nbid: str = None,
        order_id: int = None,
        pay_submit_uid: int = None,
        payer_id: int = None,
        token: str = None,
    ):
        # This parameter is required.
        self.buyer_id = buyer_id
        self.ec_id_account_ids = ec_id_account_ids
        self.nbid = nbid
        # This parameter is required.
        self.order_id = order_id
        # This parameter is required.
        self.pay_submit_uid = pay_submit_uid
        # This parameter is required.
        self.payer_id = payer_id
        # This parameter is required.
        self.token = token

    def validate(self):
        if self.ec_id_account_ids:
            for v1 in self.ec_id_account_ids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buyer_id is not None:
            result['BuyerId'] = self.buyer_id

        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k1 in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k1.to_map() if k1 else None)

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.pay_submit_uid is not None:
            result['PaySubmitUid'] = self.pay_submit_uid

        if self.payer_id is not None:
            result['PayerId'] = self.payer_id

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyerId') is not None:
            self.buyer_id = m.get('BuyerId')

        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k1 in m.get('EcIdAccountIds'):
                temp_model = main_models.PayOrderRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k1))

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('PaySubmitUid') is not None:
            self.pay_submit_uid = m.get('PaySubmitUid')

        if m.get('PayerId') is not None:
            self.payer_id = m.get('PayerId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

class PayOrderRequestEcIdAccountIds(DaraModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        self.account_ids = account_ids
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids

        if self.ec_id is not None:
            result['EcId'] = self.ec_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')

        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')

        return self

