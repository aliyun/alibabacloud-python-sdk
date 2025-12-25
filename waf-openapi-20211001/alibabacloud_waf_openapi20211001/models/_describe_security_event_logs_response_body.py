# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeSecurityEventLogsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        security_event_logs: List[Any] = None,
        security_event_logs_total_count: int = None,
        security_event_meta_data: main_models.DescribeSecurityEventLogsResponseBodySecurityEventMetaData = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The attack logs returned.
        self.security_event_logs = security_event_logs
        # The total number of logs returned.
        self.security_event_logs_total_count = security_event_logs_total_count
        # The metadata of the time series data returned.
        self.security_event_meta_data = security_event_meta_data

    def validate(self):
        if self.security_event_meta_data:
            self.security_event_meta_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_event_logs is not None:
            result['SecurityEventLogs'] = self.security_event_logs

        if self.security_event_logs_total_count is not None:
            result['SecurityEventLogsTotalCount'] = self.security_event_logs_total_count

        if self.security_event_meta_data is not None:
            result['SecurityEventMetaData'] = self.security_event_meta_data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityEventLogs') is not None:
            self.security_event_logs = m.get('SecurityEventLogs')

        if m.get('SecurityEventLogsTotalCount') is not None:
            self.security_event_logs_total_count = m.get('SecurityEventLogsTotalCount')

        if m.get('SecurityEventMetaData') is not None:
            temp_model = main_models.DescribeSecurityEventLogsResponseBodySecurityEventMetaData()
            self.security_event_meta_data = temp_model.from_map(m.get('SecurityEventMetaData'))

        return self

class DescribeSecurityEventLogsResponseBodySecurityEventMetaData(DaraModel):
    def __init__(
        self,
        date_range: main_models.DescribeSecurityEventLogsResponseBodySecurityEventMetaDataDateRange = None,
        units: str = None,
    ):
        # The time range that is used for the query.
        self.date_range = date_range
        # The unit of the statistics returned. The value is fixed as requests.
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
            temp_model = main_models.DescribeSecurityEventLogsResponseBodySecurityEventMetaDataDateRange()
            self.date_range = temp_model.from_map(m.get('DateRange'))

        if m.get('Units') is not None:
            self.units = m.get('Units')

        return self

class DescribeSecurityEventLogsResponseBodySecurityEventMetaDataDateRange(DaraModel):
    def __init__(
        self,
        end_date: int = None,
        start_date: int = None,
    ):
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds. This value is the same as the value of EndDate in the request parameters.
        self.end_date = end_date
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds. This value is the same as the value of StartDate in the request parameters.
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

