# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class BatchGetHotelDetailResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.BatchGetHotelDetailResponseBodyData = None,
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
            temp_model = main_models.BatchGetHotelDetailResponseBodyData()
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

class BatchGetHotelDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        hotels: List[main_models.BatchGetHotelDetailResponseBodyDataHotels] = None,
    ):
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
                temp_model = main_models.BatchGetHotelDetailResponseBodyDataHotels()
                self.hotels.append(temp_model.from_map(k1))

        return self

class BatchGetHotelDetailResponseBodyDataHotels(DaraModel):
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
        facilities: List[main_models.BatchGetHotelDetailResponseBodyDataHotelsFacilities] = None,
        hotel_name: str = None,
        hotel_name_cn: str = None,
        hotel_type: str = None,
        latitude: str = None,
        longitude: str = None,
        opening_time: int = None,
        pictures: List[main_models.BatchGetHotelDetailResponseBodyDataHotelsPictures] = None,
        policies: List[main_models.BatchGetHotelDetailResponseBodyDataHotelsPolicies] = None,
        position_type: str = None,
        renovation_time: int = None,
        room_types: List[main_models.BatchGetHotelDetailResponseBodyDataHotelsRoomTypes] = None,
        standard_hotel_id: str = None,
        star: str = None,
        status: str = None,
        tel: str = None,
        timezone: str = None,
    ):
        self.address = address
        self.check_in_time = check_in_time
        self.check_out_time = check_out_time
        self.city_name = city_name
        self.country_name = country_name
        self.description = description
        self.error_code = error_code
        self.error_message = error_message
        self.facilities = facilities
        self.hotel_name = hotel_name
        self.hotel_name_cn = hotel_name_cn
        self.hotel_type = hotel_type
        self.latitude = latitude
        self.longitude = longitude
        self.opening_time = opening_time
        self.pictures = pictures
        self.policies = policies
        self.position_type = position_type
        self.renovation_time = renovation_time
        self.room_types = room_types
        self.standard_hotel_id = standard_hotel_id
        self.star = star
        self.status = status
        self.tel = tel
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
                temp_model = main_models.BatchGetHotelDetailResponseBodyDataHotelsFacilities()
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
                temp_model = main_models.BatchGetHotelDetailResponseBodyDataHotelsPictures()
                self.pictures.append(temp_model.from_map(k1))

        self.policies = []
        if m.get('Policies') is not None:
            for k1 in m.get('Policies'):
                temp_model = main_models.BatchGetHotelDetailResponseBodyDataHotelsPolicies()
                self.policies.append(temp_model.from_map(k1))

        if m.get('PositionType') is not None:
            self.position_type = m.get('PositionType')

        if m.get('RenovationTime') is not None:
            self.renovation_time = m.get('RenovationTime')

        self.room_types = []
        if m.get('RoomTypes') is not None:
            for k1 in m.get('RoomTypes'):
                temp_model = main_models.BatchGetHotelDetailResponseBodyDataHotelsRoomTypes()
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

class BatchGetHotelDetailResponseBodyDataHotelsRoomTypes(DaraModel):
    def __init__(
        self,
        bed_type: List[main_models.BatchGetHotelDetailResponseBodyDataHotelsRoomTypesBedType] = None,
        pictures: List[main_models.BatchGetHotelDetailResponseBodyDataHotelsRoomTypesPictures] = None,
        room_name: str = None,
        room_name_cn: str = None,
        room_size: float = None,
        room_size_unit: str = None,
        standard_room_id: str = None,
        window_type: str = None,
        window_type_defect: str = None,
    ):
        self.bed_type = bed_type
        self.pictures = pictures
        self.room_name = room_name
        self.room_name_cn = room_name_cn
        self.room_size = room_size
        self.room_size_unit = room_size_unit
        self.standard_room_id = standard_room_id
        self.window_type = window_type
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
                temp_model = main_models.BatchGetHotelDetailResponseBodyDataHotelsRoomTypesBedType()
                self.bed_type.append(temp_model.from_map(k1))

        self.pictures = []
        if m.get('Pictures') is not None:
            for k1 in m.get('Pictures'):
                temp_model = main_models.BatchGetHotelDetailResponseBodyDataHotelsRoomTypesPictures()
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

class BatchGetHotelDetailResponseBodyDataHotelsRoomTypesPictures(DaraModel):
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
        self.description = description
        self.first_category_code = first_category_code
        self.first_category_name = first_category_name
        self.is_head_pic = is_head_pic
        self.picture_id = picture_id
        self.second_category_code = second_category_code
        self.second_category_name = second_category_name
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

class BatchGetHotelDetailResponseBodyDataHotelsRoomTypesBedType(DaraModel):
    def __init__(
        self,
        bed_count: int = None,
        bed_size: str = None,
        bed_type: str = None,
    ):
        self.bed_count = bed_count
        self.bed_size = bed_size
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

class BatchGetHotelDetailResponseBodyDataHotelsPolicies(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        group_type_id: str = None,
        items: List[main_models.BatchGetHotelDetailResponseBodyDataHotelsPoliciesItems] = None,
    ):
        self.group_name = group_name
        self.group_type_id = group_type_id
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
                temp_model = main_models.BatchGetHotelDetailResponseBodyDataHotelsPoliciesItems()
                self.items.append(temp_model.from_map(k1))

        return self

class BatchGetHotelDetailResponseBodyDataHotelsPoliciesItems(DaraModel):
    def __init__(
        self,
        children: List[Any] = None,
        item_name: str = None,
        item_type_id: str = None,
        value: str = None,
    ):
        self.children = children
        self.item_name = item_name
        self.item_type_id = item_type_id
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

class BatchGetHotelDetailResponseBodyDataHotelsPictures(DaraModel):
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
        self.description = description
        self.first_category_code = first_category_code
        self.first_category_name = first_category_name
        self.is_head_pic = is_head_pic
        self.picture_id = picture_id
        self.second_category_code = second_category_code
        self.second_category_name = second_category_name
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

class BatchGetHotelDetailResponseBodyDataHotelsFacilities(DaraModel):
    def __init__(
        self,
        description: str = None,
        facility_id: str = None,
        name: str = None,
    ):
        self.description = description
        self.facility_id = facility_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.facility_id is not None:
            result['FacilityId'] = self.facility_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FacilityId') is not None:
            self.facility_id = m.get('FacilityId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

