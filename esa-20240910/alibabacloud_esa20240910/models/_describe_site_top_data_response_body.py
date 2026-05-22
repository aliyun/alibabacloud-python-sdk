# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class DescribeSiteTopDataResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeSiteTopDataResponseBodyData] = None,
        end_time: str = None,
        request_id: str = None,
        sampling_rate: float = None,
        start_time: str = None,
    ):
        # The returned data.
        self.data = data
        # The end of the time range during which data was queried.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.end_time = end_time
        # The request ID.
        self.request_id = request_id
        # The sampling rate.
        self.sampling_rate = sampling_rate
        # The beginning of the time range during which data was queried.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.start_time = start_time

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sampling_rate is not None:
            result['SamplingRate'] = self.sampling_rate

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeSiteTopDataResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SamplingRate') is not None:
            self.sampling_rate = m.get('SamplingRate')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeSiteTopDataResponseBodyData(DaraModel):
    def __init__(
        self,
        detail_data: List[main_models.DescribeSiteTopDataResponseBodyDataDetailData] = None,
        dimension_name: str = None,
        field_name: str = None,
    ):
        # The returned data.
        self.detail_data = detail_data
        # The dimension at which data was queried.
        self.dimension_name = dimension_name
        # The metric name.
        self.field_name = field_name

    def validate(self):
        if self.detail_data:
            for v1 in self.detail_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DetailData'] = []
        if self.detail_data is not None:
            for k1 in self.detail_data:
                result['DetailData'].append(k1.to_map() if k1 else None)

        if self.dimension_name is not None:
            result['DimensionName'] = self.dimension_name

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail_data = []
        if m.get('DetailData') is not None:
            for k1 in m.get('DetailData'):
                temp_model = main_models.DescribeSiteTopDataResponseBodyDataDetailData()
                self.detail_data.append(temp_model.from_map(k1))

        if m.get('DimensionName') is not None:
            self.dimension_name = m.get('DimensionName')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        return self

class DescribeSiteTopDataResponseBodyDataDetailData(DaraModel):
    def __init__(
        self,
        dimension_value: str = None,
        value: Any = None,
    ):
        # The dimension value.
        self.dimension_value = dimension_value
        # The queried numeric value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimension_value is not None:
            result['DimensionValue'] = self.dimension_value

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DimensionValue') is not None:
            self.dimension_value = m.get('DimensionValue')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

