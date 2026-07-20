# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class HotelStaticInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.HotelStaticInfoResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        # module
        self.module = module
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.module is not None:
            result['module'] = self.module.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('module') is not None:
            temp_model = main_models.HotelStaticInfoResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class HotelStaticInfoResponseBodyModule(DaraModel):
    def __init__(
        self,
        hotel_static_infos: List[main_models.HotelStaticInfoResponseBodyModuleHotelStaticInfos] = None,
    ):
        self.hotel_static_infos = hotel_static_infos

    def validate(self):
        if self.hotel_static_infos:
            for v1 in self.hotel_static_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['hotel_static_infos'] = []
        if self.hotel_static_infos is not None:
            for k1 in self.hotel_static_infos:
                result['hotel_static_infos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hotel_static_infos = []
        if m.get('hotel_static_infos') is not None:
            for k1 in m.get('hotel_static_infos'):
                temp_model = main_models.HotelStaticInfoResponseBodyModuleHotelStaticInfos()
                self.hotel_static_infos.append(temp_model.from_map(k1))

        return self

class HotelStaticInfoResponseBodyModuleHotelStaticInfos(DaraModel):
    def __init__(
        self,
        block_room_type_information: Dict[str, str] = None,
        brand: str = None,
        brand_name: str = None,
        city_code: str = None,
        city_name: str = None,
        country: str = None,
        country_code: str = None,
        description: str = None,
        district: str = None,
        district_name: str = None,
        expand_info: main_models.HotelStaticInfoResponseBodyModuleHotelStaticInfosExpandInfo = None,
        hotel_address: str = None,
        hotel_en_address: str = None,
        hotel_en_name: str = None,
        hotel_id: str = None,
        hotel_name: str = None,
        hotel_open_time: str = None,
        hotel_phones: str = None,
        hotel_policies: str = None,
        hotelfax: str = None,
        hotelpics: str = None,
        imageinfos: List[main_models.HotelStaticInfoResponseBodyModuleHotelStaticInfosImageinfos] = None,
        invoice_provider_method: str = None,
        invoice_types: List[int] = None,
        location: str = None,
        province: str = None,
        province_name: str = None,
        rating_average: str = None,
        room_infos: List[main_models.HotelStaticInfoResponseBodyModuleHotelStaticInfosRoomInfos] = None,
        star: str = None,
        star_rate: str = None,
        status: str = None,
        themes: str = None,
        visa_reminding: bool = None,
    ):
        self.block_room_type_information = block_room_type_information
        self.brand = brand
        self.brand_name = brand_name
        self.city_code = city_code
        self.city_name = city_name
        self.country = country
        self.country_code = country_code
        self.description = description
        self.district = district
        self.district_name = district_name
        self.expand_info = expand_info
        self.hotel_address = hotel_address
        self.hotel_en_address = hotel_en_address
        self.hotel_en_name = hotel_en_name
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name
        self.hotel_open_time = hotel_open_time
        self.hotel_phones = hotel_phones
        self.hotel_policies = hotel_policies
        self.hotelfax = hotelfax
        self.hotelpics = hotelpics
        self.imageinfos = imageinfos
        self.invoice_provider_method = invoice_provider_method
        self.invoice_types = invoice_types
        self.location = location
        self.province = province
        self.province_name = province_name
        self.rating_average = rating_average
        self.room_infos = room_infos
        self.star = star
        self.star_rate = star_rate
        self.status = status
        self.themes = themes
        self.visa_reminding = visa_reminding

    def validate(self):
        if self.expand_info:
            self.expand_info.validate()
        if self.imageinfos:
            for v1 in self.imageinfos:
                 if v1:
                    v1.validate()
        if self.room_infos:
            for v1 in self.room_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_room_type_information is not None:
            result['block_room_type_information'] = self.block_room_type_information

        if self.brand is not None:
            result['brand'] = self.brand

        if self.brand_name is not None:
            result['brand_name'] = self.brand_name

        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.city_name is not None:
            result['city_name'] = self.city_name

        if self.country is not None:
            result['country'] = self.country

        if self.country_code is not None:
            result['country_code'] = self.country_code

        if self.description is not None:
            result['description'] = self.description

        if self.district is not None:
            result['district'] = self.district

        if self.district_name is not None:
            result['district_name'] = self.district_name

        if self.expand_info is not None:
            result['expand_info'] = self.expand_info.to_map()

        if self.hotel_address is not None:
            result['hotel_address'] = self.hotel_address

        if self.hotel_en_address is not None:
            result['hotel_en_address'] = self.hotel_en_address

        if self.hotel_en_name is not None:
            result['hotel_en_name'] = self.hotel_en_name

        if self.hotel_id is not None:
            result['hotel_id'] = self.hotel_id

        if self.hotel_name is not None:
            result['hotel_name'] = self.hotel_name

        if self.hotel_open_time is not None:
            result['hotel_open_time'] = self.hotel_open_time

        if self.hotel_phones is not None:
            result['hotel_phones'] = self.hotel_phones

        if self.hotel_policies is not None:
            result['hotel_policies'] = self.hotel_policies

        if self.hotelfax is not None:
            result['hotelfax'] = self.hotelfax

        if self.hotelpics is not None:
            result['hotelpics'] = self.hotelpics

        result['imageinfos'] = []
        if self.imageinfos is not None:
            for k1 in self.imageinfos:
                result['imageinfos'].append(k1.to_map() if k1 else None)

        if self.invoice_provider_method is not None:
            result['invoice_provider_method'] = self.invoice_provider_method

        if self.invoice_types is not None:
            result['invoice_types'] = self.invoice_types

        if self.location is not None:
            result['location'] = self.location

        if self.province is not None:
            result['province'] = self.province

        if self.province_name is not None:
            result['province_name'] = self.province_name

        if self.rating_average is not None:
            result['rating_average'] = self.rating_average

        result['room_infos'] = []
        if self.room_infos is not None:
            for k1 in self.room_infos:
                result['room_infos'].append(k1.to_map() if k1 else None)

        if self.star is not None:
            result['star'] = self.star

        if self.star_rate is not None:
            result['star_rate'] = self.star_rate

        if self.status is not None:
            result['status'] = self.status

        if self.themes is not None:
            result['themes'] = self.themes

        if self.visa_reminding is not None:
            result['visa_reminding'] = self.visa_reminding

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('block_room_type_information') is not None:
            self.block_room_type_information = m.get('block_room_type_information')

        if m.get('brand') is not None:
            self.brand = m.get('brand')

        if m.get('brand_name') is not None:
            self.brand_name = m.get('brand_name')

        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('city_name') is not None:
            self.city_name = m.get('city_name')

        if m.get('country') is not None:
            self.country = m.get('country')

        if m.get('country_code') is not None:
            self.country_code = m.get('country_code')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('district') is not None:
            self.district = m.get('district')

        if m.get('district_name') is not None:
            self.district_name = m.get('district_name')

        if m.get('expand_info') is not None:
            temp_model = main_models.HotelStaticInfoResponseBodyModuleHotelStaticInfosExpandInfo()
            self.expand_info = temp_model.from_map(m.get('expand_info'))

        if m.get('hotel_address') is not None:
            self.hotel_address = m.get('hotel_address')

        if m.get('hotel_en_address') is not None:
            self.hotel_en_address = m.get('hotel_en_address')

        if m.get('hotel_en_name') is not None:
            self.hotel_en_name = m.get('hotel_en_name')

        if m.get('hotel_id') is not None:
            self.hotel_id = m.get('hotel_id')

        if m.get('hotel_name') is not None:
            self.hotel_name = m.get('hotel_name')

        if m.get('hotel_open_time') is not None:
            self.hotel_open_time = m.get('hotel_open_time')

        if m.get('hotel_phones') is not None:
            self.hotel_phones = m.get('hotel_phones')

        if m.get('hotel_policies') is not None:
            self.hotel_policies = m.get('hotel_policies')

        if m.get('hotelfax') is not None:
            self.hotelfax = m.get('hotelfax')

        if m.get('hotelpics') is not None:
            self.hotelpics = m.get('hotelpics')

        self.imageinfos = []
        if m.get('imageinfos') is not None:
            for k1 in m.get('imageinfos'):
                temp_model = main_models.HotelStaticInfoResponseBodyModuleHotelStaticInfosImageinfos()
                self.imageinfos.append(temp_model.from_map(k1))

        if m.get('invoice_provider_method') is not None:
            self.invoice_provider_method = m.get('invoice_provider_method')

        if m.get('invoice_types') is not None:
            self.invoice_types = m.get('invoice_types')

        if m.get('location') is not None:
            self.location = m.get('location')

        if m.get('province') is not None:
            self.province = m.get('province')

        if m.get('province_name') is not None:
            self.province_name = m.get('province_name')

        if m.get('rating_average') is not None:
            self.rating_average = m.get('rating_average')

        self.room_infos = []
        if m.get('room_infos') is not None:
            for k1 in m.get('room_infos'):
                temp_model = main_models.HotelStaticInfoResponseBodyModuleHotelStaticInfosRoomInfos()
                self.room_infos.append(temp_model.from_map(k1))

        if m.get('star') is not None:
            self.star = m.get('star')

        if m.get('star_rate') is not None:
            self.star_rate = m.get('star_rate')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('themes') is not None:
            self.themes = m.get('themes')

        if m.get('visa_reminding') is not None:
            self.visa_reminding = m.get('visa_reminding')

        return self

class HotelStaticInfoResponseBodyModuleHotelStaticInfosRoomInfos(DaraModel):
    def __init__(
        self,
        bed_info_group_list: List[main_models.HotelStaticInfoResponseBodyModuleHotelStaticInfosRoomInfosBedInfoGroupList] = None,
        bed_infos: List[main_models.HotelStaticInfoResponseBodyModuleHotelStaticInfosRoomInfosBedInfos] = None,
        extra_bed: int = None,
        extra_bed_desc: str = None,
        floor: str = None,
        internet_way: str = None,
        max_occupancy: int = None,
        room_facilities: str = None,
        room_facility_list: List[str] = None,
        room_id: str = None,
        room_image: str = None,
        room_images: List[str] = None,
        room_name: str = None,
        room_type: int = None,
        roomarea: str = None,
        rooms: int = None,
        window: str = None,
        window_bad: str = None,
        window_view: str = None,
    ):
        self.bed_info_group_list = bed_info_group_list
        self.bed_infos = bed_infos
        self.extra_bed = extra_bed
        self.extra_bed_desc = extra_bed_desc
        self.floor = floor
        self.internet_way = internet_way
        self.max_occupancy = max_occupancy
        self.room_facilities = room_facilities
        self.room_facility_list = room_facility_list
        self.room_id = room_id
        self.room_image = room_image
        self.room_images = room_images
        self.room_name = room_name
        self.room_type = room_type
        self.roomarea = roomarea
        self.rooms = rooms
        self.window = window
        self.window_bad = window_bad
        self.window_view = window_view

    def validate(self):
        if self.bed_info_group_list:
            for v1 in self.bed_info_group_list:
                 if v1:
                    v1.validate()
        if self.bed_infos:
            for v1 in self.bed_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['bed_info_group_list'] = []
        if self.bed_info_group_list is not None:
            for k1 in self.bed_info_group_list:
                result['bed_info_group_list'].append(k1.to_map() if k1 else None)

        result['bed_infos'] = []
        if self.bed_infos is not None:
            for k1 in self.bed_infos:
                result['bed_infos'].append(k1.to_map() if k1 else None)

        if self.extra_bed is not None:
            result['extra_bed'] = self.extra_bed

        if self.extra_bed_desc is not None:
            result['extra_bed_desc'] = self.extra_bed_desc

        if self.floor is not None:
            result['floor'] = self.floor

        if self.internet_way is not None:
            result['internet_way'] = self.internet_way

        if self.max_occupancy is not None:
            result['max_occupancy'] = self.max_occupancy

        if self.room_facilities is not None:
            result['room_facilities'] = self.room_facilities

        if self.room_facility_list is not None:
            result['room_facility_list'] = self.room_facility_list

        if self.room_id is not None:
            result['room_id'] = self.room_id

        if self.room_image is not None:
            result['room_image'] = self.room_image

        if self.room_images is not None:
            result['room_images'] = self.room_images

        if self.room_name is not None:
            result['room_name'] = self.room_name

        if self.room_type is not None:
            result['room_type'] = self.room_type

        if self.roomarea is not None:
            result['roomarea'] = self.roomarea

        if self.rooms is not None:
            result['rooms'] = self.rooms

        if self.window is not None:
            result['window'] = self.window

        if self.window_bad is not None:
            result['window_bad'] = self.window_bad

        if self.window_view is not None:
            result['window_view'] = self.window_view

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bed_info_group_list = []
        if m.get('bed_info_group_list') is not None:
            for k1 in m.get('bed_info_group_list'):
                temp_model = main_models.HotelStaticInfoResponseBodyModuleHotelStaticInfosRoomInfosBedInfoGroupList()
                self.bed_info_group_list.append(temp_model.from_map(k1))

        self.bed_infos = []
        if m.get('bed_infos') is not None:
            for k1 in m.get('bed_infos'):
                temp_model = main_models.HotelStaticInfoResponseBodyModuleHotelStaticInfosRoomInfosBedInfos()
                self.bed_infos.append(temp_model.from_map(k1))

        if m.get('extra_bed') is not None:
            self.extra_bed = m.get('extra_bed')

        if m.get('extra_bed_desc') is not None:
            self.extra_bed_desc = m.get('extra_bed_desc')

        if m.get('floor') is not None:
            self.floor = m.get('floor')

        if m.get('internet_way') is not None:
            self.internet_way = m.get('internet_way')

        if m.get('max_occupancy') is not None:
            self.max_occupancy = m.get('max_occupancy')

        if m.get('room_facilities') is not None:
            self.room_facilities = m.get('room_facilities')

        if m.get('room_facility_list') is not None:
            self.room_facility_list = m.get('room_facility_list')

        if m.get('room_id') is not None:
            self.room_id = m.get('room_id')

        if m.get('room_image') is not None:
            self.room_image = m.get('room_image')

        if m.get('room_images') is not None:
            self.room_images = m.get('room_images')

        if m.get('room_name') is not None:
            self.room_name = m.get('room_name')

        if m.get('room_type') is not None:
            self.room_type = m.get('room_type')

        if m.get('roomarea') is not None:
            self.roomarea = m.get('roomarea')

        if m.get('rooms') is not None:
            self.rooms = m.get('rooms')

        if m.get('window') is not None:
            self.window = m.get('window')

        if m.get('window_bad') is not None:
            self.window_bad = m.get('window_bad')

        if m.get('window_view') is not None:
            self.window_view = m.get('window_view')

        return self

class HotelStaticInfoResponseBodyModuleHotelStaticInfosRoomInfosBedInfos(DaraModel):
    def __init__(
        self,
        bed_desc: str = None,
        bed_num: int = None,
        bed_size: str = None,
        bed_type: str = None,
        length: str = None,
        width: str = None,
    ):
        self.bed_desc = bed_desc
        self.bed_num = bed_num
        self.bed_size = bed_size
        self.bed_type = bed_type
        self.length = length
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bed_desc is not None:
            result['bed_desc'] = self.bed_desc

        if self.bed_num is not None:
            result['bed_num'] = self.bed_num

        if self.bed_size is not None:
            result['bed_size'] = self.bed_size

        if self.bed_type is not None:
            result['bed_type'] = self.bed_type

        if self.length is not None:
            result['length'] = self.length

        if self.width is not None:
            result['width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bed_desc') is not None:
            self.bed_desc = m.get('bed_desc')

        if m.get('bed_num') is not None:
            self.bed_num = m.get('bed_num')

        if m.get('bed_size') is not None:
            self.bed_size = m.get('bed_size')

        if m.get('bed_type') is not None:
            self.bed_type = m.get('bed_type')

        if m.get('length') is not None:
            self.length = m.get('length')

        if m.get('width') is not None:
            self.width = m.get('width')

        return self

class HotelStaticInfoResponseBodyModuleHotelStaticInfosRoomInfosBedInfoGroupList(DaraModel):
    def __init__(
        self,
        bed_infos: List[main_models.HotelStaticInfoResponseBodyModuleHotelStaticInfosRoomInfosBedInfoGroupListBedInfos] = None,
    ):
        self.bed_infos = bed_infos

    def validate(self):
        if self.bed_infos:
            for v1 in self.bed_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['bed_Infos'] = []
        if self.bed_infos is not None:
            for k1 in self.bed_infos:
                result['bed_Infos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bed_infos = []
        if m.get('bed_Infos') is not None:
            for k1 in m.get('bed_Infos'):
                temp_model = main_models.HotelStaticInfoResponseBodyModuleHotelStaticInfosRoomInfosBedInfoGroupListBedInfos()
                self.bed_infos.append(temp_model.from_map(k1))

        return self

class HotelStaticInfoResponseBodyModuleHotelStaticInfosRoomInfosBedInfoGroupListBedInfos(DaraModel):
    def __init__(
        self,
        bed_desc: str = None,
        bed_num: int = None,
        bed_size: str = None,
        bed_type: str = None,
        length: str = None,
        width: str = None,
    ):
        self.bed_desc = bed_desc
        self.bed_num = bed_num
        self.bed_size = bed_size
        self.bed_type = bed_type
        self.length = length
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bed_desc is not None:
            result['bed_desc'] = self.bed_desc

        if self.bed_num is not None:
            result['bed_num'] = self.bed_num

        if self.bed_size is not None:
            result['bed_size'] = self.bed_size

        if self.bed_type is not None:
            result['bed_type'] = self.bed_type

        if self.length is not None:
            result['length'] = self.length

        if self.width is not None:
            result['width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bed_desc') is not None:
            self.bed_desc = m.get('bed_desc')

        if m.get('bed_num') is not None:
            self.bed_num = m.get('bed_num')

        if m.get('bed_size') is not None:
            self.bed_size = m.get('bed_size')

        if m.get('bed_type') is not None:
            self.bed_type = m.get('bed_type')

        if m.get('length') is not None:
            self.length = m.get('length')

        if m.get('width') is not None:
            self.width = m.get('width')

        return self

class HotelStaticInfoResponseBodyModuleHotelStaticInfosImageinfos(DaraModel):
    def __init__(
        self,
        desc: str = None,
        tag: int = None,
        url: str = None,
    ):
        self.desc = desc
        self.tag = tag
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['desc'] = self.desc

        if self.tag is not None:
            result['tag'] = self.tag

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('tag') is not None:
            self.tag = m.get('tag')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class HotelStaticInfoResponseBodyModuleHotelStaticInfosExpandInfo(DaraModel):
    def __init__(
        self,
        check_in: str = None,
        check_out: str = None,
        decorate_time: str = None,
        floors: str = None,
        hotel_facilities: List[str] = None,
        hotel_type: int = None,
        opening_time: str = None,
        room_facilities: List[str] = None,
        rooms: int = None,
        service: List[str] = None,
        theme_tag: str = None,
    ):
        self.check_in = check_in
        self.check_out = check_out
        self.decorate_time = decorate_time
        self.floors = floors
        self.hotel_facilities = hotel_facilities
        self.hotel_type = hotel_type
        self.opening_time = opening_time
        self.room_facilities = room_facilities
        self.rooms = rooms
        self.service = service
        self.theme_tag = theme_tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_in is not None:
            result['check_in'] = self.check_in

        if self.check_out is not None:
            result['check_out'] = self.check_out

        if self.decorate_time is not None:
            result['decorate_time'] = self.decorate_time

        if self.floors is not None:
            result['floors'] = self.floors

        if self.hotel_facilities is not None:
            result['hotel_facilities'] = self.hotel_facilities

        if self.hotel_type is not None:
            result['hotel_type'] = self.hotel_type

        if self.opening_time is not None:
            result['opening_time'] = self.opening_time

        if self.room_facilities is not None:
            result['room_facilities'] = self.room_facilities

        if self.rooms is not None:
            result['rooms'] = self.rooms

        if self.service is not None:
            result['service'] = self.service

        if self.theme_tag is not None:
            result['theme_tag'] = self.theme_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('check_in') is not None:
            self.check_in = m.get('check_in')

        if m.get('check_out') is not None:
            self.check_out = m.get('check_out')

        if m.get('decorate_time') is not None:
            self.decorate_time = m.get('decorate_time')

        if m.get('floors') is not None:
            self.floors = m.get('floors')

        if m.get('hotel_facilities') is not None:
            self.hotel_facilities = m.get('hotel_facilities')

        if m.get('hotel_type') is not None:
            self.hotel_type = m.get('hotel_type')

        if m.get('opening_time') is not None:
            self.opening_time = m.get('opening_time')

        if m.get('room_facilities') is not None:
            self.room_facilities = m.get('room_facilities')

        if m.get('rooms') is not None:
            self.rooms = m.get('rooms')

        if m.get('service') is not None:
            self.service = m.get('service')

        if m.get('theme_tag') is not None:
            self.theme_tag = m.get('theme_tag')

        return self

