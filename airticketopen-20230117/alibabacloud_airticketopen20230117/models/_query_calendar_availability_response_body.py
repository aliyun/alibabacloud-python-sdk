# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class QueryCalendarAvailabilityResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.QueryCalendarAvailabilityResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        tracer_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success
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
            temp_model = main_models.QueryCalendarAvailabilityResponseBodyData()
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

class QueryCalendarAvailabilityResponseBodyData(DaraModel):
    def __init__(
        self,
        failed_hotels: List[main_models.QueryCalendarAvailabilityResponseBodyDataFailedHotels] = None,
        hotels: Dict[str, List[main_models.DataHotelsValue]] = None,
        tracer_id: str = None,
    ):
        self.failed_hotels = failed_hotels
        self.hotels = hotels
        self.tracer_id = tracer_id

    def validate(self):
        if self.failed_hotels:
            for v1 in self.failed_hotels:
                 if v1:
                    v1.validate()
        if self.hotels:
            for v1 in self.hotels.values():
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FailedHotels'] = []
        if self.failed_hotels is not None:
            for k1 in self.failed_hotels:
                result['FailedHotels'].append(k1.to_map() if k1 else None)

        result['Hotels'] = {}
        if self.hotels is not None:
            for k1, v1 in self.hotels.items():
                l1 = []
                for k2 in v1:
                    l1.append(k2.to_map() if k2 else None)
                result['Hotels'][k1] = l1

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_hotels = []
        if m.get('FailedHotels') is not None:
            for k1 in m.get('FailedHotels'):
                temp_model = main_models.QueryCalendarAvailabilityResponseBodyDataFailedHotels()
                self.failed_hotels.append(temp_model.from_map(k1))

        self.hotels = {}
        if m.get('Hotels') is not None:
            for k1, v1 in m.get('Hotels').items():
                l1 = []
                for k2 in v1:
                    temp_model = main_models.DataHotelsValue()
                    l1.append(temp_model.from_map(k2))
                self.hotels[k1] = l1

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class QueryCalendarAvailabilityResponseBodyDataFailedHotels(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        standard_hotel_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.standard_hotel_id = standard_hotel_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.standard_hotel_id is not None:
            result['StandardHotelId'] = self.standard_hotel_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('StandardHotelId') is not None:
            self.standard_hotel_id = m.get('StandardHotelId')

        return self

