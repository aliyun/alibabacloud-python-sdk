# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeSecurityEventTopNMetricResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        security_event_top_nvalues: List[main_models.DescribeSecurityEventTopNMetricResponseBodySecurityEventTopNValues] = None,
        top_nmeta_data: main_models.DescribeSecurityEventTopNMetricResponseBodyTopNMetaData = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The top N data entries returned.
        self.security_event_top_nvalues = security_event_top_nvalues
        # The metadata of the data entries returned.
        self.top_nmeta_data = top_nmeta_data

    def validate(self):
        if self.security_event_top_nvalues:
            for v1 in self.security_event_top_nvalues:
                 if v1:
                    v1.validate()
        if self.top_nmeta_data:
            self.top_nmeta_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SecurityEventTopNValues'] = []
        if self.security_event_top_nvalues is not None:
            for k1 in self.security_event_top_nvalues:
                result['SecurityEventTopNValues'].append(k1.to_map() if k1 else None)

        if self.top_nmeta_data is not None:
            result['TopNMetaData'] = self.top_nmeta_data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.security_event_top_nvalues = []
        if m.get('SecurityEventTopNValues') is not None:
            for k1 in m.get('SecurityEventTopNValues'):
                temp_model = main_models.DescribeSecurityEventTopNMetricResponseBodySecurityEventTopNValues()
                self.security_event_top_nvalues.append(temp_model.from_map(k1))

        if m.get('TopNMetaData') is not None:
            temp_model = main_models.DescribeSecurityEventTopNMetricResponseBodyTopNMetaData()
            self.top_nmeta_data = temp_model.from_map(m.get('TopNMetaData'))

        return self

class DescribeSecurityEventTopNMetricResponseBodyTopNMetaData(DaraModel):
    def __init__(
        self,
        date_range: main_models.DescribeSecurityEventTopNMetricResponseBodyTopNMetaDataDateRange = None,
        units: str = None,
    ):
        # The time range that is used for the query.
        self.date_range = date_range
        # The unit of the statistics returned. It is fixed as requests.
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
            temp_model = main_models.DescribeSecurityEventTopNMetricResponseBodyTopNMetaDataDateRange()
            self.date_range = temp_model.from_map(m.get('DateRange'))

        if m.get('Units') is not None:
            self.units = m.get('Units')

        return self

class DescribeSecurityEventTopNMetricResponseBodyTopNMetaDataDateRange(DaraModel):
    def __init__(
        self,
        end_date: int = None,
        start_date: int = None,
    ):
        # The end of the time range to query. The value is a Unix timestamp. Unit: seconds. This value is the same as the value of EndDate in the request parameters.
        self.end_date = end_date
        # The beginning of the time range to query. The value is a Unix timestamp. Unit: seconds. This value is the same as the value of StartDate in the request parameters.
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

class DescribeSecurityEventTopNMetricResponseBodySecurityEventTopNValues(DaraModel):
    def __init__(
        self,
        attribute: str = None,
        name: str = None,
        value: int = None,
    ):
        # The additional information, such as the protection module for a protection rule whose ID is returned.
        self.attribute = attribute
        # The field value, which varies based on the metric.
        self.name = name
        # The count for the data entry.
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

