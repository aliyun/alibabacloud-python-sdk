# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListZonesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListZonesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # Returned data.
        self.data = data
        # Response message.
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListZonesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListZonesResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListZonesResponseBodyDataItems] = None,
    ):
        # List of availability zones.
        self.items = items

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListZonesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        return self

class ListZonesResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        support_qat: str = None,
        zone_id: str = None,
    ):
        self.support_qat = support_qat
        # 可用区ID。
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.support_qat is not None:
            result['supportQat'] = self.support_qat

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('supportQat') is not None:
            self.support_qat = m.get('supportQat')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

