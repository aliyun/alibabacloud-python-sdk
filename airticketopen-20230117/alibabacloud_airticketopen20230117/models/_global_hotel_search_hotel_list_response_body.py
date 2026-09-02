# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class GlobalHotelSearchHotelListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GlobalHotelSearchHotelListResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        tracer_id: str = None,
    ):
        # The business data.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The unique request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # traceId
        self.tracer_id = tracer_id

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

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GlobalHotelSearchHotelListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class GlobalHotelSearchHotelListResponseBodyData(DaraModel):
    def __init__(
        self,
        hotels: List[main_models.GlobalHotelSearchHotelListResponseBodyDataHotels] = None,
        total: int = None,
    ):
        # The list of hotels.
        self.hotels = hotels
        # The total number of hotels.
        self.total = total

    def validate(self):
        if self.hotels:
            for v1 in self.hotels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Hotels'] = []
        if self.hotels is not None:
            for k1 in self.hotels:
                result['Hotels'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hotels = []
        if m.get('Hotels') is not None:
            for k1 in m.get('Hotels'):
                temp_model = main_models.GlobalHotelSearchHotelListResponseBodyDataHotels()
                self.hotels.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GlobalHotelSearchHotelListResponseBodyDataHotels(DaraModel):
    def __init__(
        self,
        city_name: str = None,
        country_name: str = None,
        hotel_name: str = None,
        standard_hotel_id: str = None,
        status: str = None,
    ):
        # The city name.
        self.city_name = city_name
        # The country name.
        self.country_name = country_name
        # The hotel name.
        self.hotel_name = hotel_name
        # The platform standard hotel ID.
        self.standard_hotel_id = standard_hotel_id
        # The hotel status. Valid values: ONLINE and OFFLINE.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city_name is not None:
            result['CityName'] = self.city_name

        if self.country_name is not None:
            result['CountryName'] = self.country_name

        if self.hotel_name is not None:
            result['HotelName'] = self.hotel_name

        if self.standard_hotel_id is not None:
            result['StandardHotelId'] = self.standard_hotel_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')

        if m.get('CountryName') is not None:
            self.country_name = m.get('CountryName')

        if m.get('HotelName') is not None:
            self.hotel_name = m.get('HotelName')

        if m.get('StandardHotelId') is not None:
            self.standard_hotel_id = m.get('StandardHotelId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

