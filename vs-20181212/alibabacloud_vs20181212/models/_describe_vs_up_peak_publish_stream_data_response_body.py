# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeVsUpPeakPublishStreamDataResponseBody(DaraModel):
    def __init__(
        self,
        describe_vs_up_peak_publish_stream_datas: main_models.DescribeVsUpPeakPublishStreamDataResponseBodyDescribeVsUpPeakPublishStreamDatas = None,
        request_id: str = None,
    ):
        self.describe_vs_up_peak_publish_stream_datas = describe_vs_up_peak_publish_stream_datas
        self.request_id = request_id

    def validate(self):
        if self.describe_vs_up_peak_publish_stream_datas:
            self.describe_vs_up_peak_publish_stream_datas.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.describe_vs_up_peak_publish_stream_datas is not None:
            result['DescribeVsUpPeakPublishStreamDatas'] = self.describe_vs_up_peak_publish_stream_datas.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DescribeVsUpPeakPublishStreamDatas') is not None:
            temp_model = main_models.DescribeVsUpPeakPublishStreamDataResponseBodyDescribeVsUpPeakPublishStreamDatas()
            self.describe_vs_up_peak_publish_stream_datas = temp_model.from_map(m.get('DescribeVsUpPeakPublishStreamDatas'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeVsUpPeakPublishStreamDataResponseBodyDescribeVsUpPeakPublishStreamDatas(DaraModel):
    def __init__(
        self,
        describe_vs_up_peak_publish_stream_data: List[main_models.DescribeVsUpPeakPublishStreamDataResponseBodyDescribeVsUpPeakPublishStreamDatasDescribeVsUpPeakPublishStreamData] = None,
    ):
        self.describe_vs_up_peak_publish_stream_data = describe_vs_up_peak_publish_stream_data

    def validate(self):
        if self.describe_vs_up_peak_publish_stream_data:
            for v1 in self.describe_vs_up_peak_publish_stream_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DescribeVsUpPeakPublishStreamData'] = []
        if self.describe_vs_up_peak_publish_stream_data is not None:
            for k1 in self.describe_vs_up_peak_publish_stream_data:
                result['DescribeVsUpPeakPublishStreamData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.describe_vs_up_peak_publish_stream_data = []
        if m.get('DescribeVsUpPeakPublishStreamData') is not None:
            for k1 in m.get('DescribeVsUpPeakPublishStreamData'):
                temp_model = main_models.DescribeVsUpPeakPublishStreamDataResponseBodyDescribeVsUpPeakPublishStreamDatasDescribeVsUpPeakPublishStreamData()
                self.describe_vs_up_peak_publish_stream_data.append(temp_model.from_map(k1))

        return self

class DescribeVsUpPeakPublishStreamDataResponseBodyDescribeVsUpPeakPublishStreamDatasDescribeVsUpPeakPublishStreamData(DaraModel):
    def __init__(
        self,
        band_width: str = None,
        peak_time: str = None,
        publish_stream_num: int = None,
        query_time: str = None,
        stat_name: str = None,
    ):
        self.band_width = band_width
        self.peak_time = peak_time
        self.publish_stream_num = publish_stream_num
        self.query_time = query_time
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

