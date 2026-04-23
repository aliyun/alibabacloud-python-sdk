# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribeVodDomainMax95BpsDataResponseBody(DaraModel):
    def __init__(
        self,
        detail_data: main_models.DescribeVodDomainMax95BpsDataResponseBodyDetailData = None,
        domain_name: str = None,
        domestic_max_95bps: str = None,
        end_time: str = None,
        max_95bps: str = None,
        overseas_max_95bps: str = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.detail_data = detail_data
        # The domain name for CDN.
        self.domain_name = domain_name
        # The 95th percentile bandwidth in the Chinese mainland.
        self.domestic_max_95bps = domestic_max_95bps
        # The end of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # >  The end time must be later than the start time.
        self.end_time = end_time
        # The 95th percentile bandwidth.
        self.max_95bps = max_95bps
        # The 95th percentile bandwidth outside the Chinese mainland.
        self.overseas_max_95bps = overseas_max_95bps
        # The request ID.
        self.request_id = request_id
        # The beginning of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time

    def validate(self):
        if self.detail_data:
            self.detail_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail_data is not None:
            result['DetailData'] = self.detail_data.to_map()

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domestic_max_95bps is not None:
            result['DomesticMax95Bps'] = self.domestic_max_95bps

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.max_95bps is not None:
            result['Max95Bps'] = self.max_95bps

        if self.overseas_max_95bps is not None:
            result['OverseasMax95Bps'] = self.overseas_max_95bps

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailData') is not None:
            temp_model = main_models.DescribeVodDomainMax95BpsDataResponseBodyDetailData()
            self.detail_data = temp_model.from_map(m.get('DetailData'))

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomesticMax95Bps') is not None:
            self.domestic_max_95bps = m.get('DomesticMax95Bps')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Max95Bps') is not None:
            self.max_95bps = m.get('Max95Bps')

        if m.get('OverseasMax95Bps') is not None:
            self.overseas_max_95bps = m.get('OverseasMax95Bps')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeVodDomainMax95BpsDataResponseBodyDetailData(DaraModel):
    def __init__(
        self,
        max_95detail: List[main_models.DescribeVodDomainMax95BpsDataResponseBodyDetailDataMax95Detail] = None,
    ):
        self.max_95detail = max_95detail

    def validate(self):
        if self.max_95detail:
            for v1 in self.max_95detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Max95Detail'] = []
        if self.max_95detail is not None:
            for k1 in self.max_95detail:
                result['Max95Detail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.max_95detail = []
        if m.get('Max95Detail') is not None:
            for k1 in m.get('Max95Detail'):
                temp_model = main_models.DescribeVodDomainMax95BpsDataResponseBodyDetailDataMax95Detail()
                self.max_95detail.append(temp_model.from_map(k1))

        return self

class DescribeVodDomainMax95BpsDataResponseBodyDetailDataMax95Detail(DaraModel):
    def __init__(
        self,
        area: str = None,
        max_95bps: float = None,
        max_95bps_peak_time: str = None,
        time_stamp: str = None,
    ):
        self.area = area
        self.max_95bps = max_95bps
        self.max_95bps_peak_time = max_95bps_peak_time
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area

        if self.max_95bps is not None:
            result['Max95Bps'] = self.max_95bps

        if self.max_95bps_peak_time is not None:
            result['Max95BpsPeakTime'] = self.max_95bps_peak_time

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('Max95Bps') is not None:
            self.max_95bps = m.get('Max95Bps')

        if m.get('Max95BpsPeakTime') is not None:
            self.max_95bps_peak_time = m.get('Max95BpsPeakTime')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

