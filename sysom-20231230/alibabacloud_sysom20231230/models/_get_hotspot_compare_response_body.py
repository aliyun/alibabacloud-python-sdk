# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class GetHotspotCompareResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetHotspotCompareResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

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

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetHotspotCompareResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetHotspotCompareResponseBodyData(DaraModel):
    def __init__(
        self,
        flame: main_models.GetHotspotCompareResponseBodyDataFlame = None,
        series_instance_1: main_models.GetHotspotCompareResponseBodyDataSeriesInstance1 = None,
        series_instance_2: main_models.GetHotspotCompareResponseBodyDataSeriesInstance2 = None,
    ):
        self.flame = flame
        self.series_instance_1 = series_instance_1
        self.series_instance_2 = series_instance_2

    def validate(self):
        if self.flame:
            self.flame.validate()
        if self.series_instance_1:
            self.series_instance_1.validate()
        if self.series_instance_2:
            self.series_instance_2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flame is not None:
            result['flame'] = self.flame.to_map()

        if self.series_instance_1 is not None:
            result['series_instance1'] = self.series_instance_1.to_map()

        if self.series_instance_2 is not None:
            result['series_instance2'] = self.series_instance_2.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flame') is not None:
            temp_model = main_models.GetHotspotCompareResponseBodyDataFlame()
            self.flame = temp_model.from_map(m.get('flame'))

        if m.get('series_instance1') is not None:
            temp_model = main_models.GetHotspotCompareResponseBodyDataSeriesInstance1()
            self.series_instance_1 = temp_model.from_map(m.get('series_instance1'))

        if m.get('series_instance2') is not None:
            temp_model = main_models.GetHotspotCompareResponseBodyDataSeriesInstance2()
            self.series_instance_2 = temp_model.from_map(m.get('series_instance2'))

        return self

class GetHotspotCompareResponseBodyDataSeriesInstance2(DaraModel):
    def __init__(
        self,
        columns: List[str] = None,
        values: List[List[str]] = None,
    ):
        self.columns = columns
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.columns is not None:
            result['columns'] = self.columns

        if self.values is not None:
            result['values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columns') is not None:
            self.columns = m.get('columns')

        if m.get('values') is not None:
            self.values = m.get('values')

        return self

class GetHotspotCompareResponseBodyDataSeriesInstance1(DaraModel):
    def __init__(
        self,
        columns: List[str] = None,
        values: List[List[str]] = None,
    ):
        self.columns = columns
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.columns is not None:
            result['columns'] = self.columns

        if self.values is not None:
            result['values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columns') is not None:
            self.columns = m.get('columns')

        if m.get('values') is not None:
            self.values = m.get('values')

        return self

class GetHotspotCompareResponseBodyDataFlame(DaraModel):
    def __init__(
        self,
        columns: List[str] = None,
        values: List[List[str]] = None,
    ):
        self.columns = columns
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.columns is not None:
            result['columns'] = self.columns

        if self.values is not None:
            result['values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columns') is not None:
            self.columns = m.get('columns')

        if m.get('values') is not None:
            self.values = m.get('values')

        return self

