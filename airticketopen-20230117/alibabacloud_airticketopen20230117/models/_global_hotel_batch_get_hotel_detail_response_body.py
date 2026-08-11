# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class GlobalHotelBatchGetHotelDetailResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GlobalHotelBatchGetHotelDetailResponseBodyData = None,
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
        # Indicates whether the request was successful.
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
            temp_model = main_models.GlobalHotelBatchGetHotelDetailResponseBodyData()
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

class GlobalHotelBatchGetHotelDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        hotels: List[main_models.GlobalHotelBatchGetHotelDetailResponseBodyDataHotels] = None,
    ):
        # The list of hotel details.
        self.hotels = hotels

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hotels = []
        if m.get('Hotels') is not None:
            for k1 in m.get('Hotels'):
                temp_model = main_models.GlobalHotelBatchGetHotelDetailResponseBodyDataHotels()
                self.hotels.append(temp_model.from_map(k1))

        return self

class GlobalHotelBatchGetHotelDetailResponseBodyDataHotels(DaraModel):
    def __init__(
        self,
        address: str = None,
        check_in_time: str = None,
        check_out_time: str = None,
        city_name: str = None,
        country_name: str = None,
        description: str = None,
        error_code: str = None,
        error_message: str = None,
        facilities: List[main_models.GlobalHotelBatchGetHotelDetailResponseBodyDataHotelsFacilities] = None,
        hotel_name: str = None,
        hotel_name_cn: str = None,
        hotel_type: str = None,
        latitude: str = None,
        longitude: str = None,
        opening_time: int = None,
        pictures: List[main_models.GlobalHotelBatchGetHotelDetailResponseBodyDataHotelsPictures] = None,
        policies: List[main_models.GlobalHotelBatchGetHotelDetailResponseBodyDataHotelsPolicies] = None,
        position_type: str = None,
        renovation_time: int = None,
        room_types: List[main_models.GlobalHotelBatchGetHotelDetailResponseBodyDataHotelsRoomTypes] = None,
        standard_hotel_id: str = None,
        star: str = None,
        status: str = None,
        tel: str = None,
        timezone: str = None,
    ):
        # The address.
        self.address = address
        # The default check-in time.
        self.check_in_time = check_in_time
        # The default check-out time.
        self.check_out_time = check_out_time
        # The city name.
        self.city_name = city_name
        # The country name.
        self.country_name = country_name
        # The hotel description.
        self.description = description
        # The error code for the individual hotel.
        self.error_code = error_code
        # The error message for the individual hotel.
        self.error_message = error_message
        # The list of facilities.
        self.facilities = facilities
        # The hotel name.
        self.hotel_name = hotel_name
        # The Chinese hotel name.
        self.hotel_name_cn = hotel_name_cn
        # The hotel type (LUXURY/DELUXE/COMFORT).
        self.hotel_type = hotel_type
        # The latitude.
        self.latitude = latitude
        # The longitude.
        self.longitude = longitude
        # The opening year.
        self.opening_time = opening_time
        # The list of pictures.
        self.pictures = pictures
        # The hotel policy information.
        self.policies = policies
        # The source of the coordinates.
        self.position_type = position_type
        # The renovation year.
        self.renovation_time = renovation_time
        # The list of room types.
        self.room_types = room_types
        # The platform standard hotel ID.
        self.standard_hotel_id = standard_hotel_id
        # The star rating.
        self.star = star
        # The hotel status (ONLINE/OFFLINE).
        self.status = status
        # The phone number.
        self.tel = tel
        # The hotel time zone (IANA ID).
        self.timezone = timezone

    def validate(self):
        if self.facilities:
            for v1 in self.facilities:
                 if v1:
                    v1.validate()
        if self.pictures:
            for v1 in self.pictures:
                 if v1:
                    v1.validate()
        if self.policies:
            for v1 in self.policies:
                 if v1:
                    v1.validate()
        if self.room_types:
            for v1 in self.room_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.check_in_time is not None:
            result['CheckInTime'] = self.check_in_time

        if self.check_out_time is not None:
            result['CheckOutTime'] = self.check_out_time

        if self.city_name is not None:
            result['CityName'] = self.city_name

        if self.country_name is not None:
            result['CountryName'] = self.country_name

        if self.description is not None:
            result['Description'] = self.description

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        result['Facilities'] = []
        if self.facilities is not None:
            for k1 in self.facilities:
                result['Facilities'].append(k1.to_map() if k1 else None)

        if self.hotel_name is not None:
            result['HotelName'] = self.hotel_name

        if self.hotel_name_cn is not None:
            result['HotelNameCn'] = self.hotel_name_cn

        if self.hotel_type is not None:
            result['HotelType'] = self.hotel_type

        if self.latitude is not None:
            result['Latitude'] = self.latitude

        if self.longitude is not None:
            result['Longitude'] = self.longitude

        if self.opening_time is not None:
            result['OpeningTime'] = self.opening_time

        result['Pictures'] = []
        if self.pictures is not None:
            for k1 in self.pictures:
                result['Pictures'].append(k1.to_map() if k1 else None)

        result['Policies'] = []
        if self.policies is not None:
            for k1 in self.policies:
                result['Policies'].append(k1.to_map() if k1 else None)

        if self.position_type is not None:
            result['PositionType'] = self.position_type

        if self.renovation_time is not None:
            result['RenovationTime'] = self.renovation_time

        result['RoomTypes'] = []
        if self.room_types is not None:
            for k1 in self.room_types:
                result['RoomTypes'].append(k1.to_map() if k1 else None)

        if self.standard_hotel_id is not None:
            result['StandardHotelId'] = self.standard_hotel_id

        if self.star is not None:
            result['Star'] = self.star

        if self.status is not None:
            result['Status'] = self.status

        if self.tel is not None:
            result['Tel'] = self.tel

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('CheckInTime') is not None:
            self.check_in_time = m.get('CheckInTime')

        if m.get('CheckOutTime') is not None:
            self.check_out_time = m.get('CheckOutTime')

        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')

        if m.get('CountryName') is not None:
            self.country_name = m.get('CountryName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        self.facilities = []
        if m.get('Facilities') is not None:
            for k1 in m.get('Facilities'):
                temp_model = main_models.GlobalHotelBatchGetHotelDetailResponseBodyDataHotelsFacilities()
                self.facilities.append(temp_model.from_map(k1))

        if m.get('HotelName') is not None:
            self.hotel_name = m.get('HotelName')

        if m.get('HotelNameCn') is not None:
            self.hotel_name_cn = m.get('HotelNameCn')

        if m.get('HotelType') is not None:
            self.hotel_type = m.get('HotelType')

        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')

        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')

        if m.get('OpeningTime') is not None:
            self.opening_time = m.get('OpeningTime')

        self.pictures = []
        if m.get('Pictures') is not None:
            for k1 in m.get('Pictures'):
                temp_model = main_models.GlobalHotelBatchGetHotelDetailResponseBodyDataHotelsPictures()
                self.pictures.append(temp_model.from_map(k1))

        self.policies = []
        if m.get('Policies') is not None:
            for k1 in m.get('Policies'):
                temp_model = main_models.GlobalHotelBatchGetHotelDetailResponseBodyDataHotelsPolicies()
                self.policies.append(temp_model.from_map(k1))

        if m.get('PositionType') is not None:
            self.position_type = m.get('PositionType')

        if m.get('RenovationTime') is not None:
            self.renovation_time = m.get('RenovationTime')

        self.room_types = []
        if m.get('RoomTypes') is not None:
            for k1 in m.get('RoomTypes'):
                temp_model = main_models.GlobalHotelBatchGetHotelDetailResponseBodyDataHotelsRoomTypes()
                self.room_types.append(temp_model.from_map(k1))

        if m.get('StandardHotelId') is not None:
            self.standard_hotel_id = m.get('StandardHotelId')

        if m.get('Star') is not None:
            self.star = m.get('Star')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tel') is not None:
            self.tel = m.get('Tel')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        return self

class GlobalHotelBatchGetHotelDetailResponseBodyDataHotelsRoomTypes(DaraModel):
    def __init__(
        self,
        bed_type: List[main_models.GlobalHotelBatchGetHotelDetailResponseBodyDataHotelsRoomTypesBedType] = None,
        pictures: List[main_models.GlobalHotelBatchGetHotelDetailResponseBodyDataHotelsRoomTypesPictures] = None,
        room_name: str = None,
        room_name_cn: str = None,
        room_size: str = None,
        room_size_unit: str = None,
        standard_room_id: str = None,
        window_type: str = None,
        window_type_defect: str = None,
    ):
        # The list of bed types.
        self.bed_type = bed_type
        # The list of room type pictures.
        self.pictures = pictures
        # The room type name.
        self.room_name = room_name
        # The Chinese room type name (always in Chinese, regardless of the language parameter).
        self.room_name_cn = room_name_cn
        # The room area (passed through as-is, may be a range value).
        self.room_size = room_size
        # The area unit. Valid values: SQM (square meters) and SQFT (square feet). Default value: SQM.
        self.room_size_unit = room_size_unit
        # The platform standard room type ID.
        self.standard_room_id = standard_room_id
        # The window type. Valid values:
        # - 0: no window
        # - 1: with window
        # - 2: partially with window
        # - 3: opaque window
        # - 4: partially opaque window
        # - 5: floor-to-ceiling window
        self.window_type = window_type
        # The window defect code. Valid values:
        # - 0: window cannot be opened for ventilation
        # - 1: view is obstructed outside the window
        # - 2: window faces the interior of the hotel
        # - 3: window is located in a corridor or hallway
        # - 4: window can be opened for ventilation and faces an outdoor open environment
        self.window_type_defect = window_type_defect

    def validate(self):
        if self.bed_type:
            for v1 in self.bed_type:
                 if v1:
                    v1.validate()
        if self.pictures:
            for v1 in self.pictures:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BedType'] = []
        if self.bed_type is not None:
            for k1 in self.bed_type:
                result['BedType'].append(k1.to_map() if k1 else None)

        result['Pictures'] = []
        if self.pictures is not None:
            for k1 in self.pictures:
                result['Pictures'].append(k1.to_map() if k1 else None)

        if self.room_name is not None:
            result['RoomName'] = self.room_name

        if self.room_name_cn is not None:
            result['RoomNameCn'] = self.room_name_cn

        if self.room_size is not None:
            result['RoomSize'] = self.room_size

        if self.room_size_unit is not None:
            result['RoomSizeUnit'] = self.room_size_unit

        if self.standard_room_id is not None:
            result['StandardRoomId'] = self.standard_room_id

        if self.window_type is not None:
            result['WindowType'] = self.window_type

        if self.window_type_defect is not None:
            result['WindowTypeDefect'] = self.window_type_defect

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bed_type = []
        if m.get('BedType') is not None:
            for k1 in m.get('BedType'):
                temp_model = main_models.GlobalHotelBatchGetHotelDetailResponseBodyDataHotelsRoomTypesBedType()
                self.bed_type.append(temp_model.from_map(k1))

        self.pictures = []
        if m.get('Pictures') is not None:
            for k1 in m.get('Pictures'):
                temp_model = main_models.GlobalHotelBatchGetHotelDetailResponseBodyDataHotelsRoomTypesPictures()
                self.pictures.append(temp_model.from_map(k1))

        if m.get('RoomName') is not None:
            self.room_name = m.get('RoomName')

        if m.get('RoomNameCn') is not None:
            self.room_name_cn = m.get('RoomNameCn')

        if m.get('RoomSize') is not None:
            self.room_size = m.get('RoomSize')

        if m.get('RoomSizeUnit') is not None:
            self.room_size_unit = m.get('RoomSizeUnit')

        if m.get('StandardRoomId') is not None:
            self.standard_room_id = m.get('StandardRoomId')

        if m.get('WindowType') is not None:
            self.window_type = m.get('WindowType')

        if m.get('WindowTypeDefect') is not None:
            self.window_type_defect = m.get('WindowTypeDefect')

        return self

class GlobalHotelBatchGetHotelDetailResponseBodyDataHotelsRoomTypesPictures(DaraModel):
    def __init__(
        self,
        description: str = None,
        first_category_code: str = None,
        first_category_name: str = None,
        is_head_pic: bool = None,
        picture_id: str = None,
        second_category_code: str = None,
        second_category_name: str = None,
        url: str = None,
    ):
        # The picture description.
        self.description = description
        # The first-level category code.
        self.first_category_code = first_category_code
        # The first-level category name.
        self.first_category_name = first_category_name
        # Indicates whether the picture is the cover image.
        self.is_head_pic = is_head_pic
        # The picture ID (subject to the URL).
        self.picture_id = picture_id
        # The second-level category code.
        self.second_category_code = second_category_code
        # The second-level category name.
        self.second_category_name = second_category_name
        # The picture URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.first_category_code is not None:
            result['FirstCategoryCode'] = self.first_category_code

        if self.first_category_name is not None:
            result['FirstCategoryName'] = self.first_category_name

        if self.is_head_pic is not None:
            result['IsHeadPic'] = self.is_head_pic

        if self.picture_id is not None:
            result['PictureId'] = self.picture_id

        if self.second_category_code is not None:
            result['SecondCategoryCode'] = self.second_category_code

        if self.second_category_name is not None:
            result['SecondCategoryName'] = self.second_category_name

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FirstCategoryCode') is not None:
            self.first_category_code = m.get('FirstCategoryCode')

        if m.get('FirstCategoryName') is not None:
            self.first_category_name = m.get('FirstCategoryName')

        if m.get('IsHeadPic') is not None:
            self.is_head_pic = m.get('IsHeadPic')

        if m.get('PictureId') is not None:
            self.picture_id = m.get('PictureId')

        if m.get('SecondCategoryCode') is not None:
            self.second_category_code = m.get('SecondCategoryCode')

        if m.get('SecondCategoryName') is not None:
            self.second_category_name = m.get('SecondCategoryName')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class GlobalHotelBatchGetHotelDetailResponseBodyDataHotelsRoomTypesBedType(DaraModel):
    def __init__(
        self,
        bed_count: int = None,
        bed_size: str = None,
        bed_type: str = None,
    ):
        # The number of beds.
        self.bed_count = bed_count
        # The bed width in meters.
        self.bed_size = bed_size
        # The bed type name.
        self.bed_type = bed_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bed_count is not None:
            result['BedCount'] = self.bed_count

        if self.bed_size is not None:
            result['BedSize'] = self.bed_size

        if self.bed_type is not None:
            result['BedType'] = self.bed_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BedCount') is not None:
            self.bed_count = m.get('BedCount')

        if m.get('BedSize') is not None:
            self.bed_size = m.get('BedSize')

        if m.get('BedType') is not None:
            self.bed_type = m.get('BedType')

        return self

class GlobalHotelBatchGetHotelDetailResponseBodyDataHotelsPolicies(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        group_type_id: str = None,
        items: List[main_models.GlobalHotelBatchGetHotelDetailResponseBodyDataHotelsPoliciesItems] = None,
    ):
        # The group name.
        self.group_name = group_name
        # The group type ID.
        self.group_type_id = group_type_id
        # The list of policy items.
        self.items = items

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_type_id is not None:
            result['GroupTypeId'] = self.group_type_id

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupTypeId') is not None:
            self.group_type_id = m.get('GroupTypeId')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.GlobalHotelBatchGetHotelDetailResponseBodyDataHotelsPoliciesItems()
                self.items.append(temp_model.from_map(k1))

        return self

class GlobalHotelBatchGetHotelDetailResponseBodyDataHotelsPoliciesItems(DaraModel):
    def __init__(
        self,
        children: List[Any] = None,
        item_name: str = None,
        item_type_id: str = None,
        value: str = None,
    ):
        # The list of sub-items.
        self.children = children
        # The item name.
        self.item_name = item_name
        # The item type ID.
        self.item_type_id = item_type_id
        # The text value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.children is not None:
            result['Children'] = self.children

        if self.item_name is not None:
            result['ItemName'] = self.item_name

        if self.item_type_id is not None:
            result['ItemTypeId'] = self.item_type_id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Children') is not None:
            self.children = m.get('Children')

        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')

        if m.get('ItemTypeId') is not None:
            self.item_type_id = m.get('ItemTypeId')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GlobalHotelBatchGetHotelDetailResponseBodyDataHotelsPictures(DaraModel):
    def __init__(
        self,
        description: str = None,
        first_category_code: str = None,
        first_category_name: str = None,
        is_head_pic: bool = None,
        picture_id: str = None,
        second_category_code: str = None,
        second_category_name: str = None,
        url: str = None,
    ):
        # The picture description.
        self.description = description
        # The first-level category code.
        self.first_category_code = first_category_code
        # The first-level category name.
        self.first_category_name = first_category_name
        # Indicates whether the picture is the cover image.
        self.is_head_pic = is_head_pic
        # The picture ID (subject to the URL).
        self.picture_id = picture_id
        # The second-level category code.
        self.second_category_code = second_category_code
        # The second-level category name.
        self.second_category_name = second_category_name
        # The picture URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.first_category_code is not None:
            result['FirstCategoryCode'] = self.first_category_code

        if self.first_category_name is not None:
            result['FirstCategoryName'] = self.first_category_name

        if self.is_head_pic is not None:
            result['IsHeadPic'] = self.is_head_pic

        if self.picture_id is not None:
            result['PictureId'] = self.picture_id

        if self.second_category_code is not None:
            result['SecondCategoryCode'] = self.second_category_code

        if self.second_category_name is not None:
            result['SecondCategoryName'] = self.second_category_name

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FirstCategoryCode') is not None:
            self.first_category_code = m.get('FirstCategoryCode')

        if m.get('FirstCategoryName') is not None:
            self.first_category_name = m.get('FirstCategoryName')

        if m.get('IsHeadPic') is not None:
            self.is_head_pic = m.get('IsHeadPic')

        if m.get('PictureId') is not None:
            self.picture_id = m.get('PictureId')

        if m.get('SecondCategoryCode') is not None:
            self.second_category_code = m.get('SecondCategoryCode')

        if m.get('SecondCategoryName') is not None:
            self.second_category_name = m.get('SecondCategoryName')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class GlobalHotelBatchGetHotelDetailResponseBodyDataHotelsFacilities(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        type: str = None,
    ):
        # The facility description.
        self.description = description
        # The facility name.
        self.name = name
        # The facility type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

