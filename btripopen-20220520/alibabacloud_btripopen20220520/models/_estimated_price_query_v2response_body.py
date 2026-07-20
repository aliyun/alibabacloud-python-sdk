# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class EstimatedPriceQueryV2ResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        module: List[main_models.EstimatedPriceQueryV2ResponseBodyModule] = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The status code.
        self.code = code
        # The response data.
        self.module = module
        # The unique identifier of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # traceId
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            for v1 in self.module:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['module'] = []
        if self.module is not None:
            for k1 in self.module:
                result['module'].append(k1.to_map() if k1 else None)

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

        self.module = []
        if m.get('module') is not None:
            for k1 in m.get('module'):
                temp_model = main_models.EstimatedPriceQueryV2ResponseBodyModule()
                self.module.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class EstimatedPriceQueryV2ResponseBodyModule(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        price_map: Dict[str, main_models.ModulePriceMapValue] = None,
        type: str = None,
    ):
        # The category, such as flight, hotel, or train.
        self.biz_type = biz_type
        # The price map. Key: min and max.
        self.price_map = price_map
        # The type, such as economy class, business class, first class, G/D train, other, or travel standard.
        self.type = type

    def validate(self):
        if self.price_map:
            for v1 in self.price_map.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['biz_type'] = self.biz_type

        result['price_map'] = {}
        if self.price_map is not None:
            for k1, v1 in self.price_map.items():
                result['price_map'][k1] = v1.to_map() if v1 else None

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('biz_type') is not None:
            self.biz_type = m.get('biz_type')

        self.price_map = {}
        if m.get('price_map') is not None:
            for k1, v1 in m.get('price_map').items():
                temp_model = main_models.ModulePriceMapValue()
                self.price_map[k1] = temp_model.from_map(v1)

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

