# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeVsDomainReqBpsDataResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        req_bps_data_per_interval: main_models.DescribeVsDomainReqBpsDataResponseBodyReqBpsDataPerInterval = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.req_bps_data_per_interval = req_bps_data_per_interval
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.req_bps_data_per_interval:
            self.req_bps_data_per_interval.validate()

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

        if self.req_bps_data_per_interval is not None:
            result['ReqBpsDataPerInterval'] = self.req_bps_data_per_interval.to_map()

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

        if m.get('ReqBpsDataPerInterval') is not None:
            temp_model = main_models.DescribeVsDomainReqBpsDataResponseBodyReqBpsDataPerInterval()
            self.req_bps_data_per_interval = temp_model.from_map(m.get('ReqBpsDataPerInterval'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeVsDomainReqBpsDataResponseBodyReqBpsDataPerInterval(DaraModel):
    def __init__(
        self,
        data_module: List[main_models.DescribeVsDomainReqBpsDataResponseBodyReqBpsDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for v1 in self.data_module:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataModule'] = []
        if self.data_module is not None:
            for k1 in self.data_module:
                result['DataModule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k1 in m.get('DataModule'):
                temp_model = main_models.DescribeVsDomainReqBpsDataResponseBodyReqBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k1))

        return self

class DescribeVsDomainReqBpsDataResponseBodyReqBpsDataPerIntervalDataModule(DaraModel):
    def __init__(
        self,
        req_bps_value: str = None,
        time_stamp: str = None,
    ):
        self.req_bps_value = req_bps_value
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.req_bps_value is not None:
            result['ReqBpsValue'] = self.req_bps_value

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReqBpsValue') is not None:
            self.req_bps_value = m.get('ReqBpsValue')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

