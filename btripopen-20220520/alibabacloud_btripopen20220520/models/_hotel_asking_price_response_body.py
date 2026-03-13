# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class HotelAskingPriceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.HotelAskingPriceResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.module is not None:
            result['module'] = self.module.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('module') is not None:
            temp_model = main_models.HotelAskingPriceResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class HotelAskingPriceResponseBodyModule(DaraModel):
    def __init__(
        self,
        hotel_asking_price_details: List[main_models.HotelAskingPriceResponseBodyModuleHotelAskingPriceDetails] = None,
    ):
        self.hotel_asking_price_details = hotel_asking_price_details

    def validate(self):
        if self.hotel_asking_price_details:
            for v1 in self.hotel_asking_price_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['hotel_asking_price_details'] = []
        if self.hotel_asking_price_details is not None:
            for k1 in self.hotel_asking_price_details:
                result['hotel_asking_price_details'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hotel_asking_price_details = []
        if m.get('hotel_asking_price_details') is not None:
            for k1 in m.get('hotel_asking_price_details'):
                temp_model = main_models.HotelAskingPriceResponseBodyModuleHotelAskingPriceDetails()
                self.hotel_asking_price_details.append(temp_model.from_map(k1))

        return self

class HotelAskingPriceResponseBodyModuleHotelAskingPriceDetails(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        hotel_address: str = None,
        hotel_code: str = None,
        hotel_name: str = None,
        is_protocol: bool = None,
        min_price: float = None,
        original_min_price: float = None,
    ):
        self.city_code = city_code
        self.hotel_address = hotel_address
        self.hotel_code = hotel_code
        self.hotel_name = hotel_name
        self.is_protocol = is_protocol
        self.min_price = min_price
        self.original_min_price = original_min_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.hotel_address is not None:
            result['hotel_address'] = self.hotel_address

        if self.hotel_code is not None:
            result['hotel_code'] = self.hotel_code

        if self.hotel_name is not None:
            result['hotel_name'] = self.hotel_name

        if self.is_protocol is not None:
            result['is_protocol'] = self.is_protocol

        if self.min_price is not None:
            result['min_price'] = self.min_price

        if self.original_min_price is not None:
            result['original_min_price'] = self.original_min_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('hotel_address') is not None:
            self.hotel_address = m.get('hotel_address')

        if m.get('hotel_code') is not None:
            self.hotel_code = m.get('hotel_code')

        if m.get('hotel_name') is not None:
            self.hotel_name = m.get('hotel_name')

        if m.get('is_protocol') is not None:
            self.is_protocol = m.get('is_protocol')

        if m.get('min_price') is not None:
            self.min_price = m.get('min_price')

        if m.get('original_min_price') is not None:
            self.original_min_price = m.get('original_min_price')

        return self

