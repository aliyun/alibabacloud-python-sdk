# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class DescribeSiteTimeSeriesDataResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeSiteTimeSeriesDataResponseBodyData] = None,
        end_time: str = None,
        interval: int = None,
        request_id: str = None,
        sampling_rate: float = None,
        start_time: str = None,
        summarized_data: List[main_models.DescribeSiteTimeSeriesDataResponseBodySummarizedData] = None,
    ):
        # Returned data.
        self.data = data
        # The end time for fetching the data.
        # 
        # The date format follows ISO8601 notation and uses UTC+0, formatted as yyyy-MM-ddTHH:mm:ssZ.
        self.end_time = end_time
        # The granularity of the data, in seconds.
        self.interval = interval
        # The request ID.
        self.request_id = request_id
        # The sampling rate, in %.
        self.sampling_rate = sampling_rate
        # The start time for fetching the data.
        # 
        # The date format follows ISO8601 notation and uses UTC+0, formatted as yyyy-MM-ddTHH:mm:ssZ.
        self.start_time = start_time
        # Aggregated query data.
        self.summarized_data = summarized_data

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.summarized_data:
            for v1 in self.summarized_data:
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

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sampling_rate is not None:
            result['SamplingRate'] = self.sampling_rate

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        result['SummarizedData'] = []
        if self.summarized_data is not None:
            for k1 in self.summarized_data:
                result['SummarizedData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeSiteTimeSeriesDataResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SamplingRate') is not None:
            self.sampling_rate = m.get('SamplingRate')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        self.summarized_data = []
        if m.get('SummarizedData') is not None:
            for k1 in m.get('SummarizedData'):
                temp_model = main_models.DescribeSiteTimeSeriesDataResponseBodySummarizedData()
                self.summarized_data.append(temp_model.from_map(k1))

        return self

class DescribeSiteTimeSeriesDataResponseBodySummarizedData(DaraModel):
    def __init__(
        self,
        agg_method: str = None,
        dimension_name: str = None,
        dimension_value: str = None,
        field_name: str = None,
        value: Any = None,
    ):
        # The aggregation method used.
        self.agg_method = agg_method
        # The dimension of the aggregated data being queried.
        self.dimension_name = dimension_name
        # The value of the aggregated dimension being queried.
        self.dimension_value = dimension_value
        # The value of the aggregated metric being queried.
        self.field_name = field_name
        # The aggregated value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agg_method is not None:
            result['AggMethod'] = self.agg_method

        if self.dimension_name is not None:
            result['DimensionName'] = self.dimension_name

        if self.dimension_value is not None:
            result['DimensionValue'] = self.dimension_value

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggMethod') is not None:
            self.agg_method = m.get('AggMethod')

        if m.get('DimensionName') is not None:
            self.dimension_name = m.get('DimensionName')

        if m.get('DimensionValue') is not None:
            self.dimension_value = m.get('DimensionValue')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeSiteTimeSeriesDataResponseBodyData(DaraModel):
    def __init__(
        self,
        detail_data: List[main_models.DescribeSiteTimeSeriesDataResponseBodyDataDetailData] = None,
        dimension_name: str = None,
        dimension_value: str = None,
        field_name: str = None,
    ):
        # Returned data.
        self.detail_data = detail_data
        # Query dimension.
        self.dimension_name = dimension_name
        # Query dimension value.
        self.dimension_value = dimension_value
        # Query metric value.
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

        if self.dimension_value is not None:
            result['DimensionValue'] = self.dimension_value

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail_data = []
        if m.get('DetailData') is not None:
            for k1 in m.get('DetailData'):
                temp_model = main_models.DescribeSiteTimeSeriesDataResponseBodyDataDetailData()
                self.detail_data.append(temp_model.from_map(k1))

        if m.get('DimensionName') is not None:
            self.dimension_name = m.get('DimensionName')

        if m.get('DimensionValue') is not None:
            self.dimension_value = m.get('DimensionValue')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        return self

class DescribeSiteTimeSeriesDataResponseBodyDataDetailData(DaraModel):
    def __init__(
        self,
        time_stamp: str = None,
        value: Any = None,
    ):
        # Start timestamp of the time slice.
        self.time_stamp = time_stamp
        # Value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

