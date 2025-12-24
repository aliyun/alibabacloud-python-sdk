# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLivePushProxyUsageDataResponseBody(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        push_proxy_data: main_models.DescribeLivePushProxyUsageDataResponseBodyPushProxyData = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The end time.
        self.end_time = end_time
        # The usage data of live center stream relay.
        self.push_proxy_data = push_proxy_data
        # The request ID.
        self.request_id = request_id
        # The start time.
        self.start_time = start_time

    def validate(self):
        if self.push_proxy_data:
            self.push_proxy_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.push_proxy_data is not None:
            result['PushProxyData'] = self.push_proxy_data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PushProxyData') is not None:
            temp_model = main_models.DescribeLivePushProxyUsageDataResponseBodyPushProxyData()
            self.push_proxy_data = temp_model.from_map(m.get('PushProxyData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeLivePushProxyUsageDataResponseBodyPushProxyData(DaraModel):
    def __init__(
        self,
        push_proxy_data_item: List[main_models.DescribeLivePushProxyUsageDataResponseBodyPushProxyDataPushProxyDataItem] = None,
    ):
        self.push_proxy_data_item = push_proxy_data_item

    def validate(self):
        if self.push_proxy_data_item:
            for v1 in self.push_proxy_data_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PushProxyDataItem'] = []
        if self.push_proxy_data_item is not None:
            for k1 in self.push_proxy_data_item:
                result['PushProxyDataItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.push_proxy_data_item = []
        if m.get('PushProxyDataItem') is not None:
            for k1 in m.get('PushProxyDataItem'):
                temp_model = main_models.DescribeLivePushProxyUsageDataResponseBodyPushProxyDataPushProxyDataItem()
                self.push_proxy_data_item.append(temp_model.from_map(k1))

        return self

class DescribeLivePushProxyUsageDataResponseBodyPushProxyDataPushProxyDataItem(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        region: str = None,
        stream_count: int = None,
        time_stamp: str = None,
    ):
        # The domain name. If the value of SplitBy includes domain, the returned data is grouped by domain name.
        self.domain_name = domain_name
        # The ID of the region. If the value of SplitBy includes region, the returned data is grouped by region.
        self.region = region
        # The peak number of live center stream relay channels.
        self.stream_count = stream_count
        # The timestamp of the returned data.
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

        if self.region is not None:
            result['Region'] = self.region

        if self.stream_count is not None:
            result['StreamCount'] = self.stream_count

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('StreamCount') is not None:
            self.stream_count = m.get('StreamCount')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

