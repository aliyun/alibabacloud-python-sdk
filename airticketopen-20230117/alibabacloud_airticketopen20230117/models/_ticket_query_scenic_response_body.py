# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class TicketQueryScenicResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.TicketQueryScenicResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.TicketQueryScenicResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class TicketQueryScenicResponseBodyData(DaraModel):
    def __init__(
        self,
        scenic: main_models.TicketQueryScenicResponseBodyDataScenic = None,
    ):
        self.scenic = scenic

    def validate(self):
        if self.scenic:
            self.scenic.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scenic is not None:
            result['Scenic'] = self.scenic.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Scenic') is not None:
            temp_model = main_models.TicketQueryScenicResponseBodyDataScenic()
            self.scenic = temp_model.from_map(m.get('Scenic'))

        return self

class TicketQueryScenicResponseBodyDataScenic(DaraModel):
    def __init__(
        self,
        address: str = None,
        city: str = None,
        country: str = None,
        description: str = None,
        images: List[str] = None,
        latitude: float = None,
        level: str = None,
        longitude: float = None,
        name: str = None,
        opening_time: str = None,
        phone: str = None,
        preferential_policy: str = None,
        province: str = None,
        residence_time: str = None,
        scenic_id: int = None,
        timezone: str = None,
    ):
        self.address = address
        self.city = city
        self.country = country
        self.description = description
        self.images = images
        self.latitude = latitude
        self.level = level
        self.longitude = longitude
        self.name = name
        self.opening_time = opening_time
        self.phone = phone
        self.preferential_policy = preferential_policy
        self.province = province
        self.residence_time = residence_time
        self.scenic_id = scenic_id
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.city is not None:
            result['City'] = self.city

        if self.country is not None:
            result['Country'] = self.country

        if self.description is not None:
            result['Description'] = self.description

        if self.images is not None:
            result['Images'] = self.images

        if self.latitude is not None:
            result['Latitude'] = self.latitude

        if self.level is not None:
            result['Level'] = self.level

        if self.longitude is not None:
            result['Longitude'] = self.longitude

        if self.name is not None:
            result['Name'] = self.name

        if self.opening_time is not None:
            result['OpeningTime'] = self.opening_time

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.preferential_policy is not None:
            result['PreferentialPolicy'] = self.preferential_policy

        if self.province is not None:
            result['Province'] = self.province

        if self.residence_time is not None:
            result['ResidenceTime'] = self.residence_time

        if self.scenic_id is not None:
            result['ScenicId'] = self.scenic_id

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Images') is not None:
            self.images = m.get('Images')

        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OpeningTime') is not None:
            self.opening_time = m.get('OpeningTime')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('PreferentialPolicy') is not None:
            self.preferential_policy = m.get('PreferentialPolicy')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('ResidenceTime') is not None:
            self.residence_time = m.get('ResidenceTime')

        if m.get('ScenicId') is not None:
            self.scenic_id = m.get('ScenicId')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        return self

