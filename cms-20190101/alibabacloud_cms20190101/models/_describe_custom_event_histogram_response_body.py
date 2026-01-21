# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeCustomEventHistogramResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        event_histograms: main_models.DescribeCustomEventHistogramResponseBodyEventHistograms = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The status code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The information about the number of times that the custom event occurred during each interval of the specified time period.
        self.event_histograms = event_histograms
        # The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: true and false.
        self.success = success

    def validate(self):
        if self.event_histograms:
            self.event_histograms.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.event_histograms is not None:
            result['EventHistograms'] = self.event_histograms.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EventHistograms') is not None:
            temp_model = main_models.DescribeCustomEventHistogramResponseBodyEventHistograms()
            self.event_histograms = temp_model.from_map(m.get('EventHistograms'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeCustomEventHistogramResponseBodyEventHistograms(DaraModel):
    def __init__(
        self,
        event_histogram: List[main_models.DescribeCustomEventHistogramResponseBodyEventHistogramsEventHistogram] = None,
    ):
        self.event_histogram = event_histogram

    def validate(self):
        if self.event_histogram:
            for v1 in self.event_histogram:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EventHistogram'] = []
        if self.event_histogram is not None:
            for k1 in self.event_histogram:
                result['EventHistogram'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_histogram = []
        if m.get('EventHistogram') is not None:
            for k1 in m.get('EventHistogram'):
                temp_model = main_models.DescribeCustomEventHistogramResponseBodyEventHistogramsEventHistogram()
                self.event_histogram.append(temp_model.from_map(k1))

        return self

class DescribeCustomEventHistogramResponseBodyEventHistogramsEventHistogram(DaraModel):
    def __init__(
        self,
        count: int = None,
        end_time: int = None,
        start_time: int = None,
    ):
        # The information about the number of times that the custom event occurred during an interval of the specified time period.
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

