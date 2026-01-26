# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GetSyntheticMonitorsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.GetSyntheticMonitorsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The list of monitoring points.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
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

        if self.message is not None:
            result['Message'] = self.message

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
                temp_model = main_models.GetSyntheticMonitorsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetSyntheticMonitorsResponseBodyData(DaraModel):
    def __init__(
        self,
        available: str = None,
        can_be_selected: bool = None,
        city: str = None,
        city_code: str = None,
        client_type: int = None,
        country: str = None,
        ipv_6: int = None,
        operator: str = None,
        operator_code: str = None,
        region: str = None,
    ):
        # Indicates whether the monitoring point is available. Valid values: true and false.
        self.available = available
        # Indicates whether the monitoring point is selected. Valid values: true and false.
        self.can_be_selected = can_be_selected
        # The city.
        self.city = city
        # The city code.
        self.city_code = city_code
        # The client type of the monitoring point. Valid values: 1: data center. 2: Internet. 3: mobile device. 4: ECS instance.
        self.client_type = client_type
        # The country.
        self.country = country
        # Indicates whether IPv6 is supported. Valid values: 0: IPv6 is not supported. 1: IPv6 is supported.
        self.ipv_6 = ipv_6
        # The carrier.
        self.operator = operator
        # The carrier code.
        self.operator_code = operator_code
        # The region.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available is not None:
            result['Available'] = self.available

        if self.can_be_selected is not None:
            result['CanBeSelected'] = self.can_be_selected

        if self.city is not None:
            result['City'] = self.city

        if self.city_code is not None:
            result['CityCode'] = self.city_code

        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.country is not None:
            result['Country'] = self.country

        if self.ipv_6 is not None:
            result['Ipv6'] = self.ipv_6

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.operator_code is not None:
            result['OperatorCode'] = self.operator_code

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Available') is not None:
            self.available = m.get('Available')

        if m.get('CanBeSelected') is not None:
            self.can_be_selected = m.get('CanBeSelected')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')

        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('Ipv6') is not None:
            self.ipv_6 = m.get('Ipv6')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('OperatorCode') is not None:
            self.operator_code = m.get('OperatorCode')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

