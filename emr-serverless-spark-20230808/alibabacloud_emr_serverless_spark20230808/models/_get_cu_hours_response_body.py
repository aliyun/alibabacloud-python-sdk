# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class GetCuHoursResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetCuHoursResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
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

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetCuHoursResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetCuHoursResponseBodyData(DaraModel):
    def __init__(
        self,
        cu_hours: str = None,
    ):
        # The CU hours consumed by the specified queue during the query period. This value is an estimate and the final value is subject to the bill.
        self.cu_hours = cu_hours

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu_hours is not None:
            result['cuHours'] = self.cu_hours

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cuHours') is not None:
            self.cu_hours = m.get('cuHours')

        return self

