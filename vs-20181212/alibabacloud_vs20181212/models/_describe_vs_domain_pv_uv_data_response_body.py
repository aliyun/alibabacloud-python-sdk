# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeVsDomainPvUvDataResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        pv_uv_data_infos: main_models.DescribeVsDomainPvUvDataResponseBodyPvUvDataInfos = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.pv_uv_data_infos = pv_uv_data_infos
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.pv_uv_data_infos:
            self.pv_uv_data_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.pv_uv_data_infos is not None:
            result['PvUvDataInfos'] = self.pv_uv_data_infos.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PvUvDataInfos') is not None:
            temp_model = main_models.DescribeVsDomainPvUvDataResponseBodyPvUvDataInfos()
            self.pv_uv_data_infos = temp_model.from_map(m.get('PvUvDataInfos'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeVsDomainPvUvDataResponseBodyPvUvDataInfos(DaraModel):
    def __init__(
        self,
        pv_uv_data_info: List[main_models.DescribeVsDomainPvUvDataResponseBodyPvUvDataInfosPvUvDataInfo] = None,
    ):
        self.pv_uv_data_info = pv_uv_data_info

    def validate(self):
        if self.pv_uv_data_info:
            for v1 in self.pv_uv_data_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PvUvDataInfo'] = []
        if self.pv_uv_data_info is not None:
            for k1 in self.pv_uv_data_info:
                result['PvUvDataInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pv_uv_data_info = []
        if m.get('PvUvDataInfo') is not None:
            for k1 in m.get('PvUvDataInfo'):
                temp_model = main_models.DescribeVsDomainPvUvDataResponseBodyPvUvDataInfosPvUvDataInfo()
                self.pv_uv_data_info.append(temp_model.from_map(k1))

        return self

class DescribeVsDomainPvUvDataResponseBodyPvUvDataInfosPvUvDataInfo(DaraModel):
    def __init__(
        self,
        pv: str = None,
        time_stamp: str = None,
        uv: str = None,
    ):
        self.pv = pv
        self.time_stamp = time_stamp
        self.uv = uv

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pv is not None:
            result['PV'] = self.pv

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.uv is not None:
            result['UV'] = self.uv

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PV') is not None:
            self.pv = m.get('PV')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('UV') is not None:
            self.uv = m.get('UV')

        return self

