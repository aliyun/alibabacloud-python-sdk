# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class HotelIndexInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.HotelIndexInfoResponseBodyModule = None,
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
            temp_model = main_models.HotelIndexInfoResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class HotelIndexInfoResponseBodyModule(DaraModel):
    def __init__(
        self,
        items: List[main_models.HotelIndexInfoResponseBodyModuleItems] = None,
        page_size: int = None,
        page_token: str = None,
    ):
        self.items = items
        self.page_size = page_size
        self.page_token = page_token

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

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.page_token is not None:
            result['page_token'] = self.page_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.HotelIndexInfoResponseBodyModuleItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('page_token') is not None:
            self.page_token = m.get('page_token')

        return self

class HotelIndexInfoResponseBodyModuleItems(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        hotel_status: str = None,
    ):
        self.hotel_id = hotel_id
        self.hotel_status = hotel_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['hotel_id'] = self.hotel_id

        if self.hotel_status is not None:
            result['hotel_status'] = self.hotel_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hotel_id') is not None:
            self.hotel_id = m.get('hotel_id')

        if m.get('hotel_status') is not None:
            self.hotel_status = m.get('hotel_status')

        return self

