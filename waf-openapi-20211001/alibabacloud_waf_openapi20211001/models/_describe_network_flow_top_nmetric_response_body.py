# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeNetworkFlowTopNMetricResponseBody(DaraModel):
    def __init__(
        self,
        network_flow_top_nvalues: List[main_models.DescribeNetworkFlowTopNMetricResponseBodyNetworkFlowTopNValues] = None,
        request_id: str = None,
        top_nmeta_data: main_models.DescribeNetworkFlowTopNMetricResponseBodyTopNMetaData = None,
    ):
        # The top statistical data array returned.
        self.network_flow_top_nvalues = network_flow_top_nvalues
        # The ID of the request.
        self.request_id = request_id
        # The metadata of the returned data.
        self.top_nmeta_data = top_nmeta_data

    def validate(self):
        if self.network_flow_top_nvalues:
            for v1 in self.network_flow_top_nvalues:
                 if v1:
                    v1.validate()
        if self.top_nmeta_data:
            self.top_nmeta_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkFlowTopNValues'] = []
        if self.network_flow_top_nvalues is not None:
            for k1 in self.network_flow_top_nvalues:
                result['NetworkFlowTopNValues'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.top_nmeta_data is not None:
            result['TopNMetaData'] = self.top_nmeta_data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_flow_top_nvalues = []
        if m.get('NetworkFlowTopNValues') is not None:
            for k1 in m.get('NetworkFlowTopNValues'):
                temp_model = main_models.DescribeNetworkFlowTopNMetricResponseBodyNetworkFlowTopNValues()
                self.network_flow_top_nvalues.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TopNMetaData') is not None:
            temp_model = main_models.DescribeNetworkFlowTopNMetricResponseBodyTopNMetaData()
            self.top_nmeta_data = temp_model.from_map(m.get('TopNMetaData'))

        return self

class DescribeNetworkFlowTopNMetricResponseBodyTopNMetaData(DaraModel):
    def __init__(
        self,
        date_range: main_models.DescribeNetworkFlowTopNMetricResponseBodyTopNMetaDataDateRange = None,
        units: str = None,
    ):
        # The query time range.
        self.date_range = date_range
        # The unit of the returned data. It is fixed as requests.
        self.units = units

    def validate(self):
        if self.date_range:
            self.date_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date_range is not None:
            result['DateRange'] = self.date_range.to_map()

        if self.units is not None:
            result['Units'] = self.units

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateRange') is not None:
            temp_model = main_models.DescribeNetworkFlowTopNMetricResponseBodyTopNMetaDataDateRange()
            self.date_range = temp_model.from_map(m.get('DateRange'))

        if m.get('Units') is not None:
            self.units = m.get('Units')

        return self

class DescribeNetworkFlowTopNMetricResponseBodyTopNMetaDataDateRange(DaraModel):
    def __init__(
        self,
        end_date: int = None,
        start_date: int = None,
    ):
        # The end time of the query range (Unix timestamp, seconds). Same as the EndDate request parameter.
        self.end_date = end_date
        # The start time of the query range (Unix timestamp, seconds). Same as the StartDate request parameter.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

class DescribeNetworkFlowTopNMetricResponseBodyNetworkFlowTopNValues(DaraModel):
    def __init__(
        self,
        attribute: str = None,
        name: str = None,
        value: int = None,
    ):
        # Returns additional information, such as the country, province, or city to which an IP address belongs.
        self.attribute = attribute
        # The value of this field varies depending on the queried Metric.
        self.name = name
        # Counts for top ranking.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute is not None:
            result['Attribute'] = self.attribute

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attribute') is not None:
            self.attribute = m.get('Attribute')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

