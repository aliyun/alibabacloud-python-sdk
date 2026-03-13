# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TrainStopoverSearchResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: List[main_models.TrainStopoverSearchResponseBodyModule] = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        # module
        self.module = module
        self.request_id = request_id
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

        if self.message is not None:
            result['message'] = self.message

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

        if m.get('message') is not None:
            self.message = m.get('message')

        self.module = []
        if m.get('module') is not None:
            for k1 in m.get('module'):
                temp_model = main_models.TrainStopoverSearchResponseBodyModule()
                self.module.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class TrainStopoverSearchResponseBodyModule(DaraModel):
    def __init__(
        self,
        arr_time: str = None,
        dep_time: str = None,
        station_name: str = None,
        station_no: str = None,
        station_type: str = None,
        stop_over_time: str = None,
    ):
        self.arr_time = arr_time
        self.dep_time = dep_time
        self.station_name = station_name
        self.station_no = station_no
        self.station_type = station_type
        self.stop_over_time = stop_over_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.station_name is not None:
            result['station_name'] = self.station_name

        if self.station_no is not None:
            result['station_no'] = self.station_no

        if self.station_type is not None:
            result['station_type'] = self.station_type

        if self.stop_over_time is not None:
            result['stop_over_time'] = self.stop_over_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('station_name') is not None:
            self.station_name = m.get('station_name')

        if m.get('station_no') is not None:
            self.station_no = m.get('station_no')

        if m.get('station_type') is not None:
            self.station_type = m.get('station_type')

        if m.get('stop_over_time') is not None:
            self.stop_over_time = m.get('stop_over_time')

        return self

