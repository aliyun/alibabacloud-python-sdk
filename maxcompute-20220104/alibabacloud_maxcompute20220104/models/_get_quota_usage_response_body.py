# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class GetQuotaUsageResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetQuotaUsageResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.http_code = http_code
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetQuotaUsageResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetQuotaUsageResponseBodyData(DaraModel):
    def __init__(
        self,
        metrics: Dict[str, Any] = None,
        plot: List[main_models.GetQuotaUsageResponseBodyDataPlot] = None,
    ):
        self.metrics = metrics
        self.plot = plot

    def validate(self):
        if self.plot:
            for v1 in self.plot:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metrics is not None:
            result['metrics'] = self.metrics

        result['plot'] = []
        if self.plot is not None:
            for k1 in self.plot:
                result['plot'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metrics') is not None:
            self.metrics = m.get('metrics')

        self.plot = []
        if m.get('plot') is not None:
            for k1 in m.get('plot'):
                temp_model = main_models.GetQuotaUsageResponseBodyDataPlot()
                self.plot.append(temp_model.from_map(k1))

        return self

class GetQuotaUsageResponseBodyDataPlot(DaraModel):
    def __init__(
        self,
        title: str = None,
        type: str = None,
        y_axis: List[str] = None,
    ):
        self.title = title
        self.type = type
        self.y_axis = y_axis

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        if self.y_axis is not None:
            result['yAxis'] = self.y_axis

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('yAxis') is not None:
            self.y_axis = m.get('yAxis')

        return self

