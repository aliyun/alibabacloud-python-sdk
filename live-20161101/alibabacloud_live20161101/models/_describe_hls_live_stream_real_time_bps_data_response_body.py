# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeHlsLiveStreamRealTimeBpsDataResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        time: str = None,
        usage_data: List[main_models.DescribeHlsLiveStreamRealTimeBpsDataResponseBodyUsageData] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The timestamp for which the data was queried.
        self.time = time
        # The usage data.
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for v1 in self.usage_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.time is not None:
            result['Time'] = self.time

        result['UsageData'] = []
        if self.usage_data is not None:
            for k1 in self.usage_data:
                result['UsageData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        self.usage_data = []
        if m.get('UsageData') is not None:
            for k1 in m.get('UsageData'):
                temp_model = main_models.DescribeHlsLiveStreamRealTimeBpsDataResponseBodyUsageData()
                self.usage_data.append(temp_model.from_map(k1))

        return self

class DescribeHlsLiveStreamRealTimeBpsDataResponseBodyUsageData(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        stream_infos: List[main_models.DescribeHlsLiveStreamRealTimeBpsDataResponseBodyUsageDataStreamInfos] = None,
    ):
        # The domain name.
        self.domain_name = domain_name
        # Details about the statistics on each HLS stream under the domain name.
        self.stream_infos = stream_infos

    def validate(self):
        if self.stream_infos:
            for v1 in self.stream_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        result['StreamInfos'] = []
        if self.stream_infos is not None:
            for k1 in self.stream_infos:
                result['StreamInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        self.stream_infos = []
        if m.get('StreamInfos') is not None:
            for k1 in m.get('StreamInfos'):
                temp_model = main_models.DescribeHlsLiveStreamRealTimeBpsDataResponseBodyUsageDataStreamInfos()
                self.stream_infos.append(temp_model.from_map(k1))

        return self

class DescribeHlsLiveStreamRealTimeBpsDataResponseBodyUsageDataStreamInfos(DaraModel):
    def __init__(
        self,
        infos: List[main_models.DescribeHlsLiveStreamRealTimeBpsDataResponseBodyUsageDataStreamInfosInfos] = None,
        stream_name: str = None,
    ):
        # The statistics on the HLS stream.
        self.infos = infos
        # The name of the stream.
        self.stream_name = stream_name

    def validate(self):
        if self.infos:
            for v1 in self.infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Infos'] = []
        if self.infos is not None:
            for k1 in self.infos:
                result['Infos'].append(k1.to_map() if k1 else None)

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.infos = []
        if m.get('Infos') is not None:
            for k1 in m.get('Infos'):
                temp_model = main_models.DescribeHlsLiveStreamRealTimeBpsDataResponseBodyUsageDataStreamInfosInfos()
                self.infos.append(temp_model.from_map(k1))

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

class DescribeHlsLiveStreamRealTimeBpsDataResponseBodyUsageDataStreamInfosInfos(DaraModel):
    def __init__(
        self,
        down_flow: float = None,
        online: float = None,
        rate: str = None,
    ):
        # The bandwidth. Unit: bit/s.
        self.down_flow = down_flow
        # The number of online users.
        self.online = online
        # The bitrate.
        self.rate = rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.down_flow is not None:
            result['DownFlow'] = self.down_flow

        if self.online is not None:
            result['Online'] = self.online

        if self.rate is not None:
            result['Rate'] = self.rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownFlow') is not None:
            self.down_flow = m.get('DownFlow')

        if m.get('Online') is not None:
            self.online = m.get('Online')

        if m.get('Rate') is not None:
            self.rate = m.get('Rate')

        return self

