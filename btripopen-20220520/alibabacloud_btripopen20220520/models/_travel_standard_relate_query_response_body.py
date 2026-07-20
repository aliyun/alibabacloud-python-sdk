# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TravelStandardRelateQueryResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        module: main_models.TravelStandardRelateQueryResponseBodyModule = None,
        request_id: str = None,
        result_code: int = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.message = message
        self.module = module
        self.request_id = request_id
        self.result_code = result_code
        self.success = success
        # traceId
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['message'] = self.message

        if self.module is not None:
            result['module'] = self.module.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result_code is not None:
            result['resultCode'] = self.result_code

        if self.success is not None:
            result['success'] = self.success

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('module') is not None:
            temp_model = main_models.TravelStandardRelateQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('resultCode') is not None:
            self.result_code = m.get('resultCode')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class TravelStandardRelateQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        reserve_bind_entity_list: List[main_models.TravelStandardRelateQueryResponseBodyModuleReserveBindEntityList] = None,
        total: int = None,
    ):
        self.reserve_bind_entity_list = reserve_bind_entity_list
        self.total = total

    def validate(self):
        if self.reserve_bind_entity_list:
            for v1 in self.reserve_bind_entity_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['reserve_bind_entity_list'] = []
        if self.reserve_bind_entity_list is not None:
            for k1 in self.reserve_bind_entity_list:
                result['reserve_bind_entity_list'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.reserve_bind_entity_list = []
        if m.get('reserve_bind_entity_list') is not None:
            for k1 in m.get('reserve_bind_entity_list'):
                temp_model = main_models.TravelStandardRelateQueryResponseBodyModuleReserveBindEntityList()
                self.reserve_bind_entity_list.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class TravelStandardRelateQueryResponseBodyModuleReserveBindEntityList(DaraModel):
    def __init__(
        self,
        entity_id: str = None,
        entity_name: str = None,
        entity_type: str = None,
    ):
        self.entity_id = entity_id
        self.entity_name = entity_name
        self.entity_type = entity_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_id is not None:
            result['entity_id'] = self.entity_id

        if self.entity_name is not None:
            result['entity_name'] = self.entity_name

        if self.entity_type is not None:
            result['entity_type'] = self.entity_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entity_id') is not None:
            self.entity_id = m.get('entity_id')

        if m.get('entity_name') is not None:
            self.entity_name = m.get('entity_name')

        if m.get('entity_type') is not None:
            self.entity_type = m.get('entity_type')

        return self

