# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class GetHotelOrderDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[main_models.GetHotelOrderDetailResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.GetHotelOrderDetailResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class GetHotelOrderDetailResponseBodyResult(DaraModel):
    def __init__(
        self,
        apply_amt: int = None,
        gmt_create: int = None,
        item_url: str = None,
        name: str = None,
        quantity: int = None,
    ):
        self.apply_amt = apply_amt
        self.gmt_create = gmt_create
        self.item_url = item_url
        self.name = name
        self.quantity = quantity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_amt is not None:
            result['ApplyAmt'] = self.apply_amt

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.item_url is not None:
            result['ItemUrl'] = self.item_url

        if self.name is not None:
            result['Name'] = self.name

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyAmt') is not None:
            self.apply_amt = m.get('ApplyAmt')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('ItemUrl') is not None:
            self.item_url = m.get('ItemUrl')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        return self

