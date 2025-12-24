# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeUpBpsPeakDataResponseBody(DaraModel):
    def __init__(
        self,
        describe_up_peak_traffics: main_models.DescribeUpBpsPeakDataResponseBodyDescribeUpPeakTraffics = None,
        request_id: str = None,
    ):
        # The information about peak inbound bandwidth on each day.
        self.describe_up_peak_traffics = describe_up_peak_traffics
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.describe_up_peak_traffics:
            self.describe_up_peak_traffics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.describe_up_peak_traffics is not None:
            result['DescribeUpPeakTraffics'] = self.describe_up_peak_traffics.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DescribeUpPeakTraffics') is not None:
            temp_model = main_models.DescribeUpBpsPeakDataResponseBodyDescribeUpPeakTraffics()
            self.describe_up_peak_traffics = temp_model.from_map(m.get('DescribeUpPeakTraffics'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUpBpsPeakDataResponseBodyDescribeUpPeakTraffics(DaraModel):
    def __init__(
        self,
        describe_up_peak_traffic: List[main_models.DescribeUpBpsPeakDataResponseBodyDescribeUpPeakTrafficsDescribeUpPeakTraffic] = None,
    ):
        self.describe_up_peak_traffic = describe_up_peak_traffic

    def validate(self):
        if self.describe_up_peak_traffic:
            for v1 in self.describe_up_peak_traffic:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DescribeUpPeakTraffic'] = []
        if self.describe_up_peak_traffic is not None:
            for k1 in self.describe_up_peak_traffic:
                result['DescribeUpPeakTraffic'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.describe_up_peak_traffic = []
        if m.get('DescribeUpPeakTraffic') is not None:
            for k1 in m.get('DescribeUpPeakTraffic'):
                temp_model = main_models.DescribeUpBpsPeakDataResponseBodyDescribeUpPeakTrafficsDescribeUpPeakTraffic()
                self.describe_up_peak_traffic.append(temp_model.from_map(k1))

        return self

class DescribeUpBpsPeakDataResponseBodyDescribeUpPeakTrafficsDescribeUpPeakTraffic(DaraModel):
    def __init__(
        self,
        band_width: str = None,
        peak_time: str = None,
        query_time: str = None,
        stat_name: str = None,
    ):
        # The daily peak inbound bandwidth.
        self.band_width = band_width
        # The time when the daily peak bandwidth is reached.
        self.peak_time = peak_time
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

        if m.get('QueryTime') is not None:
            self.query_time = m.get('QueryTime')

        if m.get('StatName') is not None:
            self.stat_name = m.get('StatName')

        return self

