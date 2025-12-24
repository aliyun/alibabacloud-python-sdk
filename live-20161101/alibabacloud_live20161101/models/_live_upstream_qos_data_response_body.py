# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class LiveUpstreamQosDataResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.LiveUpstreamQosDataResponseBodyData] = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.data = data
        self.end_time = end_time
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.LiveUpstreamQosDataResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class LiveUpstreamQosDataResponseBodyData(DaraModel):
    def __init__(
        self,
        cdn_domain: str = None,
        cdn_isp: str = None,
        cdn_ocid: str = None,
        cdn_province: str = None,
        detail_data: List[main_models.LiveUpstreamQosDataResponseBodyDataDetailData] = None,
        kwai_sidc: str = None,
        kwai_tsc: int = None,
        upstream_domain: str = None,
    ):
        self.cdn_domain = cdn_domain
        self.cdn_isp = cdn_isp
        self.cdn_ocid = cdn_ocid
        self.cdn_province = cdn_province
        self.detail_data = detail_data
        self.kwai_sidc = kwai_sidc
        self.kwai_tsc = kwai_tsc
        self.upstream_domain = upstream_domain

    def validate(self):
        if self.detail_data:
            for v1 in self.detail_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cdn_domain is not None:
            result['CdnDomain'] = self.cdn_domain

        if self.cdn_isp is not None:
            result['CdnIsp'] = self.cdn_isp

        if self.cdn_ocid is not None:
            result['CdnOcid'] = self.cdn_ocid

        if self.cdn_province is not None:
            result['CdnProvince'] = self.cdn_province

        result['DetailData'] = []
        if self.detail_data is not None:
            for k1 in self.detail_data:
                result['DetailData'].append(k1.to_map() if k1 else None)

        if self.kwai_sidc is not None:
            result['KwaiSidc'] = self.kwai_sidc

        if self.kwai_tsc is not None:
            result['KwaiTsc'] = self.kwai_tsc

        if self.upstream_domain is not None:
            result['UpstreamDomain'] = self.upstream_domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnDomain') is not None:
            self.cdn_domain = m.get('CdnDomain')

        if m.get('CdnIsp') is not None:
            self.cdn_isp = m.get('CdnIsp')

        if m.get('CdnOcid') is not None:
            self.cdn_ocid = m.get('CdnOcid')

        if m.get('CdnProvince') is not None:
            self.cdn_province = m.get('CdnProvince')

        self.detail_data = []
        if m.get('DetailData') is not None:
            for k1 in m.get('DetailData'):
                temp_model = main_models.LiveUpstreamQosDataResponseBodyDataDetailData()
                self.detail_data.append(temp_model.from_map(k1))

        if m.get('KwaiSidc') is not None:
            self.kwai_sidc = m.get('KwaiSidc')

        if m.get('KwaiTsc') is not None:
            self.kwai_tsc = m.get('KwaiTsc')

        if m.get('UpstreamDomain') is not None:
            self.upstream_domain = m.get('UpstreamDomain')

        return self

class LiveUpstreamQosDataResponseBodyDataDetailData(DaraModel):
    def __init__(
        self,
        connect_dur: int = None,
        connect_failed_count: int = None,
        count: int = None,
        first_data_dur: int = None,
        first_data_failed_count: int = None,
        first_frame_dur: int = None,
        first_frame_success_count: int = None,
        status_code_2xx: int = None,
        status_code_3xx: int = None,
        status_code_4xx: int = None,
        status_code_5xx: int = None,
        timestamp: str = None,
    ):
        self.connect_dur = connect_dur
        self.connect_failed_count = connect_failed_count
        self.count = count
        self.first_data_dur = first_data_dur
        self.first_data_failed_count = first_data_failed_count
        self.first_frame_dur = first_frame_dur
        self.first_frame_success_count = first_frame_success_count
        self.status_code_2xx = status_code_2xx
        self.status_code_3xx = status_code_3xx
        self.status_code_4xx = status_code_4xx
        self.status_code_5xx = status_code_5xx
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_dur is not None:
            result['ConnectDur'] = self.connect_dur

        if self.connect_failed_count is not None:
            result['ConnectFailedCount'] = self.connect_failed_count

        if self.count is not None:
            result['Count'] = self.count

        if self.first_data_dur is not None:
            result['FirstDataDur'] = self.first_data_dur

        if self.first_data_failed_count is not None:
            result['FirstDataFailedCount'] = self.first_data_failed_count

        if self.first_frame_dur is not None:
            result['FirstFrameDur'] = self.first_frame_dur

        if self.first_frame_success_count is not None:
            result['FirstFrameSuccessCount'] = self.first_frame_success_count

        if self.status_code_2xx is not None:
            result['StatusCode2Xx'] = self.status_code_2xx

        if self.status_code_3xx is not None:
            result['StatusCode3Xx'] = self.status_code_3xx

        if self.status_code_4xx is not None:
            result['StatusCode4Xx'] = self.status_code_4xx

        if self.status_code_5xx is not None:
            result['StatusCode5Xx'] = self.status_code_5xx

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectDur') is not None:
            self.connect_dur = m.get('ConnectDur')

        if m.get('ConnectFailedCount') is not None:
            self.connect_failed_count = m.get('ConnectFailedCount')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('FirstDataDur') is not None:
            self.first_data_dur = m.get('FirstDataDur')

        if m.get('FirstDataFailedCount') is not None:
            self.first_data_failed_count = m.get('FirstDataFailedCount')

        if m.get('FirstFrameDur') is not None:
            self.first_frame_dur = m.get('FirstFrameDur')

        if m.get('FirstFrameSuccessCount') is not None:
            self.first_frame_success_count = m.get('FirstFrameSuccessCount')

        if m.get('StatusCode2Xx') is not None:
            self.status_code_2xx = m.get('StatusCode2Xx')

        if m.get('StatusCode3Xx') is not None:
            self.status_code_3xx = m.get('StatusCode3Xx')

        if m.get('StatusCode4Xx') is not None:
            self.status_code_4xx = m.get('StatusCode4Xx')

        if m.get('StatusCode5Xx') is not None:
            self.status_code_5xx = m.get('StatusCode5Xx')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

