# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainBpsDataByTimeStampResponseBody(DaraModel):
    def __init__(
        self,
        bps_data_list: main_models.DescribeDomainBpsDataByTimeStampResponseBodyBpsDataList = None,
        domain_name: str = None,
        request_id: str = None,
        time_stamp: str = None,
    ):
        self.bps_data_list = bps_data_list
        # The accelerated domain name.
        self.domain_name = domain_name
        # The ID of the request.
        self.request_id = request_id
        # The point in time.
        self.time_stamp = time_stamp

    def validate(self):
        if self.bps_data_list:
            self.bps_data_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bps_data_list is not None:
            result['BpsDataList'] = self.bps_data_list.to_map()

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BpsDataList') is not None:
            temp_model = main_models.DescribeDomainBpsDataByTimeStampResponseBodyBpsDataList()
            self.bps_data_list = temp_model.from_map(m.get('BpsDataList'))

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

class DescribeDomainBpsDataByTimeStampResponseBodyBpsDataList(DaraModel):
    def __init__(
        self,
        bps_data_model: List[main_models.DescribeDomainBpsDataByTimeStampResponseBodyBpsDataListBpsDataModel] = None,
    ):
        self.bps_data_model = bps_data_model

    def validate(self):
        if self.bps_data_model:
            for v1 in self.bps_data_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BpsDataModel'] = []
        if self.bps_data_model is not None:
            for k1 in self.bps_data_model:
                result['BpsDataModel'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bps_data_model = []
        if m.get('BpsDataModel') is not None:
            for k1 in m.get('BpsDataModel'):
                temp_model = main_models.DescribeDomainBpsDataByTimeStampResponseBodyBpsDataListBpsDataModel()
                self.bps_data_model.append(temp_model.from_map(k1))

        return self

class DescribeDomainBpsDataByTimeStampResponseBodyBpsDataListBpsDataModel(DaraModel):
    def __init__(
        self,
        bps: int = None,
        isp_name: str = None,
        location_name: str = None,
        time_stamp: str = None,
    ):
        self.bps = bps
        self.isp_name = isp_name
        self.location_name = location_name
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bps is not None:
            result['Bps'] = self.bps

        if self.isp_name is not None:
            result['IspName'] = self.isp_name

        if self.location_name is not None:
            result['LocationName'] = self.location_name

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')

        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')

        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

