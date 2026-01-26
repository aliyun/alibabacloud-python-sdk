# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GetSyntheticTaskMonitorsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetSyntheticTaskMonitorsResponseBodyData] = None,
        msg: str = None,
        request_id: str = None,
    ):
        # The status code returned.
        # 
        # *   1001: The request was successful.
        # *   1002: The request failed.
        # *   1003: Parameter errors occurred.
        # *   1004: Authentication failed.
        # *   1006: The task does not exist.
        # *   1099: Internal errors occurred.
        self.code = code
        # The details of the monitoring point.
        self.data = data
        # The message that is returned when the request failed.
        self.msg = msg
        # The ID of the request.
        self.request_id = request_id

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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetSyntheticTaskMonitorsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetSyntheticTaskMonitorsResponseBodyData(DaraModel):
    def __init__(
        self,
        busy: int = None,
        city: str = None,
        city_code: int = None,
        client_type: int = None,
        district: str = None,
        net_service_id: int = None,
        net_service_name: str = None,
    ):
        # The task status.
        # 
        # *   0: active
        # *   1: busy
        self.busy = busy
        # The name of the city to which the monitoring point belongs.
        self.city = city
        # The ID of the city to which the monitoring point belongs.
        self.city_code = city_code
        # The client type:
        # 
        # *   1: IDC
        # *   2: Last mile
        self.client_type = client_type
        # The region to which the monitoring point belongs.
        self.district = district
        # The ID of the carrier.
        self.net_service_id = net_service_id
        # The name of the carrier.
        self.net_service_name = net_service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.busy is not None:
            result['Busy'] = self.busy

        if self.city is not None:
            result['City'] = self.city

        if self.city_code is not None:
            result['CityCode'] = self.city_code

        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.district is not None:
            result['District'] = self.district

        if self.net_service_id is not None:
            result['NetServiceId'] = self.net_service_id

        if self.net_service_name is not None:
            result['NetServiceName'] = self.net_service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Busy') is not None:
            self.busy = m.get('Busy')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')

        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('District') is not None:
            self.district = m.get('District')

        if m.get('NetServiceId') is not None:
            self.net_service_id = m.get('NetServiceId')

        if m.get('NetServiceName') is not None:
            self.net_service_name = m.get('NetServiceName')

        return self

