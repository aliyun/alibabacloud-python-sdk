# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeUpPeakPublishStreamDataResponseBody(DaraModel):
    def __init__(
        self,
        describe_up_peak_publish_stream_datas: main_models.DescribeUpPeakPublishStreamDataResponseBodyDescribeUpPeakPublishStreamDatas = None,
        request_id: str = None,
    ):
        # The information about the peak number of concurrently ingested streams on each day.
        self.describe_up_peak_publish_stream_datas = describe_up_peak_publish_stream_datas
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.describe_up_peak_publish_stream_datas:
            self.describe_up_peak_publish_stream_datas.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.describe_up_peak_publish_stream_datas is not None:
            result['DescribeUpPeakPublishStreamDatas'] = self.describe_up_peak_publish_stream_datas.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DescribeUpPeakPublishStreamDatas') is not None:
            temp_model = main_models.DescribeUpPeakPublishStreamDataResponseBodyDescribeUpPeakPublishStreamDatas()
            self.describe_up_peak_publish_stream_datas = temp_model.from_map(m.get('DescribeUpPeakPublishStreamDatas'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUpPeakPublishStreamDataResponseBodyDescribeUpPeakPublishStreamDatas(DaraModel):
    def __init__(
        self,
        describe_up_peak_publish_stream_data: List[main_models.DescribeUpPeakPublishStreamDataResponseBodyDescribeUpPeakPublishStreamDatasDescribeUpPeakPublishStreamData] = None,
    ):
        self.describe_up_peak_publish_stream_data = describe_up_peak_publish_stream_data

    def validate(self):
        if self.describe_up_peak_publish_stream_data:
            for v1 in self.describe_up_peak_publish_stream_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DescribeUpPeakPublishStreamData'] = []
        if self.describe_up_peak_publish_stream_data is not None:
            for k1 in self.describe_up_peak_publish_stream_data:
                result['DescribeUpPeakPublishStreamData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.describe_up_peak_publish_stream_data = []
        if m.get('DescribeUpPeakPublishStreamData') is not None:
            for k1 in m.get('DescribeUpPeakPublishStreamData'):
                temp_model = main_models.DescribeUpPeakPublishStreamDataResponseBodyDescribeUpPeakPublishStreamDatasDescribeUpPeakPublishStreamData()
                self.describe_up_peak_publish_stream_data.append(temp_model.from_map(k1))

        return self

class DescribeUpPeakPublishStreamDataResponseBodyDescribeUpPeakPublishStreamDatasDescribeUpPeakPublishStreamData(DaraModel):
    def __init__(
        self,
        band_width: str = None,
        peak_time: str = None,
        publish_stream_num: int = None,
        query_time: str = None,
        stat_name: str = None,
    ):
        # The daily peak inbound bandwidth.
        self.band_width = band_width
        # The time when the daily peak number of concurrently ingested streams is reached.
        self.peak_time = peak_time
        # The daily peak number of concurrently ingested streams.
        self.publish_stream_num = publish_stream_num
        # The time queried on the day.
        self.query_time = query_time
        # The category of the statistical data. If the DomainSwitch parameter is set to on, the value of this parameter is the domain name. If the DomainSwitch parameter is set to off or not specified, the value of this parameter is the user ID.
        self.stat_name = stat_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.band_width is not None:
            result['BandWidth'] = self.band_width

        if self.peak_time is not None:
            result['PeakTime'] = self.peak_time

        if self.publish_stream_num is not None:
            result['PublishStreamNum'] = self.publish_stream_num

        if self.query_time is not None:
            result['QueryTime'] = self.query_time

        if self.stat_name is not None:
            result['StatName'] = self.stat_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandWidth') is not None:
            self.band_width = m.get('BandWidth')

        if m.get('PeakTime') is not None:
            self.peak_time = m.get('PeakTime')

        if m.get('PublishStreamNum') is not None:
            self.publish_stream_num = m.get('PublishStreamNum')

        if m.get('QueryTime') is not None:
            self.query_time = m.get('QueryTime')

        if m.get('StatName') is not None:
            self.stat_name = m.get('StatName')

        return self

