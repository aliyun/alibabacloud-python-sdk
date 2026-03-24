# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainDetailDataByLayerResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeDomainDetailDataByLayerResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # The number of queries per second.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeDomainDetailDataByLayerResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDomainDetailDataByLayerResponseBodyData(DaraModel):
    def __init__(
        self,
        data_module: List[main_models.DescribeDomainDetailDataByLayerResponseBodyDataDataModule] = None,
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
                temp_model = main_models.DescribeDomainDetailDataByLayerResponseBodyDataDataModule()
                self.data_module.append(temp_model.from_map(k1))

        return self

class DescribeDomainDetailDataByLayerResponseBodyDataDataModule(DaraModel):
    def __init__(
        self,
        acc: int = None,
        bps: float = None,
        domain_name: str = None,
        http_code: str = None,
        ipv_6acc: int = None,
        ipv_6bps: float = None,
        ipv_6qps: float = None,
        ipv_6traf: int = None,
        qps: float = None,
        time_stamp: str = None,
        traf: int = None,
    ):
        self.acc = acc
        self.bps = bps
        self.domain_name = domain_name
        self.http_code = http_code
        self.ipv_6acc = ipv_6acc
        self.ipv_6bps = ipv_6bps
        self.ipv_6qps = ipv_6qps
        self.ipv_6traf = ipv_6traf
        self.qps = qps
        self.time_stamp = time_stamp
        self.traf = traf

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acc is not None:
            result['Acc'] = self.acc

        if self.bps is not None:
            result['Bps'] = self.bps

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

        if self.ipv_6acc is not None:
            result['Ipv6Acc'] = self.ipv_6acc

        if self.ipv_6bps is not None:
            result['Ipv6Bps'] = self.ipv_6bps

        if self.ipv_6qps is not None:
            result['Ipv6Qps'] = self.ipv_6qps

        if self.ipv_6traf is not None:
            result['Ipv6Traf'] = self.ipv_6traf

        if self.qps is not None:
            result['Qps'] = self.qps

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.traf is not None:
            result['Traf'] = self.traf

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acc') is not None:
            self.acc = m.get('Acc')

        if m.get('Bps') is not None:
            self.bps = m.get('Bps')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('Ipv6Acc') is not None:
            self.ipv_6acc = m.get('Ipv6Acc')

        if m.get('Ipv6Bps') is not None:
            self.ipv_6bps = m.get('Ipv6Bps')

        if m.get('Ipv6Qps') is not None:
            self.ipv_6qps = m.get('Ipv6Qps')

        if m.get('Ipv6Traf') is not None:
            self.ipv_6traf = m.get('Ipv6Traf')

        if m.get('Qps') is not None:
            self.qps = m.get('Qps')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('Traf') is not None:
            self.traf = m.get('Traf')

        return self

