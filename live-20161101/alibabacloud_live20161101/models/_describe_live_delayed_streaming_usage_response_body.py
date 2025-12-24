# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveDelayedStreamingUsageResponseBody(DaraModel):
    def __init__(
        self,
        delay_data: main_models.DescribeLiveDelayedStreamingUsageResponseBodyDelayData = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The details about the stream delay usage data.
        self.delay_data = delay_data
        # The end of the time range during which the data was queried.
        self.end_time = end_time
        # The request ID.
        self.request_id = request_id
        # The beginning of the time range during which the data was queried.
        self.start_time = start_time

    def validate(self):
        if self.delay_data:
            self.delay_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delay_data is not None:
            result['DelayData'] = self.delay_data.to_map()

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelayData') is not None:
            temp_model = main_models.DescribeLiveDelayedStreamingUsageResponseBodyDelayData()
            self.delay_data = temp_model.from_map(m.get('DelayData'))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeLiveDelayedStreamingUsageResponseBodyDelayData(DaraModel):
    def __init__(
        self,
        delay_data_item: List[main_models.DescribeLiveDelayedStreamingUsageResponseBodyDelayDataDelayDataItem] = None,
    ):
        self.delay_data_item = delay_data_item

    def validate(self):
        if self.delay_data_item:
            for v1 in self.delay_data_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DelayDataItem'] = []
        if self.delay_data_item is not None:
            for k1 in self.delay_data_item:
                result['DelayDataItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delay_data_item = []
        if m.get('DelayDataItem') is not None:
            for k1 in m.get('DelayDataItem'):
                temp_model = main_models.DescribeLiveDelayedStreamingUsageResponseBodyDelayDataDelayDataItem()
                self.delay_data_item.append(temp_model.from_map(k1))

        return self

class DescribeLiveDelayedStreamingUsageResponseBodyDelayDataDelayDataItem(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        duration: int = None,
        region: str = None,
        stream_name: str = None,
        time_stamp: str = None,
    ):
        # The domain name. If SplitBy is set to domain, the data returned is grouped by domain name.
        self.domain_name = domain_name
        # The duration of stream delay.
        self.duration = duration
        # The ID of the region. If SplitBy is set to region, the data returned is grouped by region.
        self.region = region
        # The name of the stream. If SplitBy is set to stream, the data returned is grouped by stream.
        self.stream_name = stream_name
        # The timestamp of the data returned.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.region is not None:
            result['Region'] = self.region

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

