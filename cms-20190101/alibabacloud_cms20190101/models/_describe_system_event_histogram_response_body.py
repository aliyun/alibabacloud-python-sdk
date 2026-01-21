# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeSystemEventHistogramResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        system_event_histograms: main_models.DescribeSystemEventHistogramResponseBodySystemEventHistograms = None,
    ):
        # The response code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: true: The request was successful. false: The request failed.
        self.success = success
        # The information about the number of times the system event occurred during each interval of a time period.
        self.system_event_histograms = system_event_histograms

    def validate(self):
        if self.system_event_histograms:
            self.system_event_histograms.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.system_event_histograms is not None:
            result['SystemEventHistograms'] = self.system_event_histograms.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('SystemEventHistograms') is not None:
            temp_model = main_models.DescribeSystemEventHistogramResponseBodySystemEventHistograms()
            self.system_event_histograms = temp_model.from_map(m.get('SystemEventHistograms'))

        return self

class DescribeSystemEventHistogramResponseBodySystemEventHistograms(DaraModel):
    def __init__(
        self,
        system_event_histogram: List[main_models.DescribeSystemEventHistogramResponseBodySystemEventHistogramsSystemEventHistogram] = None,
    ):
        self.system_event_histogram = system_event_histogram

    def validate(self):
        if self.system_event_histogram:
            for v1 in self.system_event_histogram:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SystemEventHistogram'] = []
        if self.system_event_histogram is not None:
            for k1 in self.system_event_histogram:
                result['SystemEventHistogram'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.system_event_histogram = []
        if m.get('SystemEventHistogram') is not None:
            for k1 in m.get('SystemEventHistogram'):
                temp_model = main_models.DescribeSystemEventHistogramResponseBodySystemEventHistogramsSystemEventHistogram()
                self.system_event_histogram.append(temp_model.from_map(k1))

        return self

class DescribeSystemEventHistogramResponseBodySystemEventHistogramsSystemEventHistogram(DaraModel):
    def __init__(
        self,
        count: int = None,
        end_time: int = None,
        start_time: int = None,
    ):
        # The number of times the system event occurred.
        self.count = count
        # The end time.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.end_time = end_time
        # The start time.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

