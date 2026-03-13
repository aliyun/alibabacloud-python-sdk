# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class AirportSearchResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.AirportSearchResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        # module。
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
            temp_model = main_models.AirportSearchResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class AirportSearchResponseBodyModule(DaraModel):
    def __init__(
        self,
        cities: List[main_models.AirportSearchResponseBodyModuleCities] = None,
        nearby: bool = None,
    ):
        self.cities = cities
        self.nearby = nearby

    def validate(self):
        if self.cities:
            for v1 in self.cities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['cities'] = []
        if self.cities is not None:
            for k1 in self.cities:
                result['cities'].append(k1.to_map() if k1 else None)

        if self.nearby is not None:
            result['nearby'] = self.nearby

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cities = []
        if m.get('cities') is not None:
            for k1 in m.get('cities'):
                temp_model = main_models.AirportSearchResponseBodyModuleCities()
                self.cities.append(temp_model.from_map(k1))

        if m.get('nearby') is not None:
            self.nearby = m.get('nearby')

        return self

class AirportSearchResponseBodyModuleCities(DaraModel):
    def __init__(
        self,
        code: str = None,
        distance: int = None,
        name: str = None,
        travel_name: str = None,
    ):
        self.code = code
        self.distance = distance
        self.name = name
        self.travel_name = travel_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.distance is not None:
            result['distance'] = self.distance

        if self.name is not None:
            result['name'] = self.name

        if self.travel_name is not None:
            result['travel_name'] = self.travel_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('distance') is not None:
            self.distance = m.get('distance')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('travel_name') is not None:
            self.travel_name = m.get('travel_name')

        return self

