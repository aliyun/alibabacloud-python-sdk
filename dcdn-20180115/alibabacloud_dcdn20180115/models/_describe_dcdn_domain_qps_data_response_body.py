# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnDomainQpsDataResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        qps_data_per_interval: main_models.DescribeDcdnDomainQpsDataResponseBodyQpsDataPerInterval = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The time interval between the data entries returned. Unit: seconds.
        self.data_interval = data_interval
        # The accelerated domain name.
        self.domain_name = domain_name
        # The end of the time range during which data was queried.
        self.end_time = end_time
        # The QPS returned at each time interval.
        self.qps_data_per_interval = qps_data_per_interval
        # The ID of the request.
        self.request_id = request_id
        # The start of the time range during which data was queried.
        self.start_time = start_time

    def validate(self):
        if self.qps_data_per_interval:
            self.qps_data_per_interval.validate()

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

        if self.qps_data_per_interval is not None:
            result['QpsDataPerInterval'] = self.qps_data_per_interval.to_map()

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

        if m.get('QpsDataPerInterval') is not None:
            temp_model = main_models.DescribeDcdnDomainQpsDataResponseBodyQpsDataPerInterval()
            self.qps_data_per_interval = temp_model.from_map(m.get('QpsDataPerInterval'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeDcdnDomainQpsDataResponseBodyQpsDataPerInterval(DaraModel):
    def __init__(
        self,
        data_module: List[main_models.DescribeDcdnDomainQpsDataResponseBodyQpsDataPerIntervalDataModule] = None,
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
                temp_model = main_models.DescribeDcdnDomainQpsDataResponseBodyQpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k1))

        return self

class DescribeDcdnDomainQpsDataResponseBodyQpsDataPerIntervalDataModule(DaraModel):
    def __init__(
        self,
        acc: float = None,
        dynamic_http_acc: float = None,
        dynamic_http_qps: float = None,
        dynamic_https_acc: float = None,
        dynamic_https_qps: float = None,
        qps: float = None,
        static_http_acc: float = None,
        static_http_qps: float = None,
        static_https_acc: float = None,
        static_https_qps: float = None,
        time_stamp: str = None,
    ):
        # The total number of requests.
        self.acc = acc
        # The number of requests for dynamic content delivery over HTTP.
        self.dynamic_http_acc = dynamic_http_acc
        # The QPS for dynamic content delivery over HTTP.
        self.dynamic_http_qps = dynamic_http_qps
        # The number of requests for dynamic content delivery over HTTPS.
        self.dynamic_https_acc = dynamic_https_acc
        # The QPS for dynamic content delivery over HTTPS.
        self.dynamic_https_qps = dynamic_https_qps
        # The total QPS.
        self.qps = qps
        # The number of requests for static content delivery over HTTP.
        self.static_http_acc = static_http_acc
        # The QPS for static content delivery over HTTP.
        self.static_http_qps = static_http_qps
        # The number of requests for static content delivery over HTTPS.
        self.static_https_acc = static_https_acc
        # The QPS for static content delivery over HTTPS.
        self.static_https_qps = static_https_qps
        # The timestamp of the returned data.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acc is not None:
            result['Acc'] = self.acc

        if self.dynamic_http_acc is not None:
            result['DynamicHttpAcc'] = self.dynamic_http_acc

        if self.dynamic_http_qps is not None:
            result['DynamicHttpQps'] = self.dynamic_http_qps

        if self.dynamic_https_acc is not None:
            result['DynamicHttpsAcc'] = self.dynamic_https_acc

        if self.dynamic_https_qps is not None:
            result['DynamicHttpsQps'] = self.dynamic_https_qps

        if self.qps is not None:
            result['Qps'] = self.qps

        if self.static_http_acc is not None:
            result['StaticHttpAcc'] = self.static_http_acc

        if self.static_http_qps is not None:
            result['StaticHttpQps'] = self.static_http_qps

        if self.static_https_acc is not None:
            result['StaticHttpsAcc'] = self.static_https_acc

        if self.static_https_qps is not None:
            result['StaticHttpsQps'] = self.static_https_qps

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acc') is not None:
            self.acc = m.get('Acc')

        if m.get('DynamicHttpAcc') is not None:
            self.dynamic_http_acc = m.get('DynamicHttpAcc')

        if m.get('DynamicHttpQps') is not None:
            self.dynamic_http_qps = m.get('DynamicHttpQps')

        if m.get('DynamicHttpsAcc') is not None:
            self.dynamic_https_acc = m.get('DynamicHttpsAcc')

        if m.get('DynamicHttpsQps') is not None:
            self.dynamic_https_qps = m.get('DynamicHttpsQps')

        if m.get('Qps') is not None:
            self.qps = m.get('Qps')

        if m.get('StaticHttpAcc') is not None:
            self.static_http_acc = m.get('StaticHttpAcc')

        if m.get('StaticHttpQps') is not None:
            self.static_http_qps = m.get('StaticHttpQps')

        if m.get('StaticHttpsAcc') is not None:
            self.static_https_acc = m.get('StaticHttpsAcc')

        if m.get('StaticHttpsQps') is not None:
            self.static_https_qps = m.get('StaticHttpsQps')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

