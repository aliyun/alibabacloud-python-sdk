# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class GetHotelOrderDetailRequest(DaraModel):
    def __init__(
        self,
        payload: main_models.GetHotelOrderDetailRequestPayload = None,
    ):
        # This parameter is required.
        self.payload = payload

    def validate(self):
        if self.payload:
            self.payload.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Payload') is not None:
            temp_model = main_models.GetHotelOrderDetailRequestPayload()
            self.payload = temp_model.from_map(m.get('Payload'))

        return self

class GetHotelOrderDetailRequestPayload(DaraModel):
    def __init__(
        self,
        order_no: str = None,
    ):
        # This parameter is required.
        self.order_no = order_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_no is not None:
            result['OrderNo'] = self.order_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderNo') is not None:
            self.order_no = m.get('OrderNo')

        return self

