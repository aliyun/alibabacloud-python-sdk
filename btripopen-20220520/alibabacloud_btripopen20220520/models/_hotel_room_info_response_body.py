# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class HotelRoomInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: List[main_models.HotelRoomInfoResponseBodyModule] = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        # requestId
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            for v1 in self.module:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        result['module'] = []
        if self.module is not None:
            for k1 in self.module:
                result['module'].append(k1.to_map() if k1 else None)

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

        self.module = []
        if m.get('module') is not None:
            for k1 in m.get('module'):
                temp_model = main_models.HotelRoomInfoResponseBodyModule()
                self.module.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class HotelRoomInfoResponseBodyModule(DaraModel):
    def __init__(
        self,
        bed_info_group_list: List[main_models.HotelRoomInfoResponseBodyModuleBedInfoGroupList] = None,
        bed_infos: List[main_models.HotelRoomInfoResponseBodyModuleBedInfos] = None,
        extra_bed: int = None,
        extra_bed_desc: str = None,
        floor: str = None,
        internet_way: str = None,
        max_occupancy: int = None,
        room_desc: str = None,
        room_facilities: str = None,
        room_facility_list: List[str] = None,
        room_id: str = None,
        room_image: str = None,
        room_images: List[main_models.HotelRoomInfoResponseBodyModuleRoomImages] = None,
        room_name: str = None,
        room_type: int = None,
        roomarea: str = None,
        rooms: int = None,
        smoke: str = None,
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
        self.room_desc = room_desc
        self.room_facilities = room_facilities
        self.room_facility_list = room_facility_list
        self.room_id = room_id
        self.room_image = room_image
        self.room_images = room_images
        self.room_name = room_name
        self.room_type = room_type
        self.roomarea = roomarea
        self.rooms = rooms
        self.smoke = smoke
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
        if self.room_images:
            for v1 in self.room_images:
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

        if self.room_desc is not None:
            result['room_desc'] = self.room_desc

        if self.room_facilities is not None:
            result['room_facilities'] = self.room_facilities

        if self.room_facility_list is not None:
            result['room_facility_list'] = self.room_facility_list

        if self.room_id is not None:
            result['room_id'] = self.room_id

        if self.room_image is not None:
            result['room_image'] = self.room_image

        result['room_images'] = []
        if self.room_images is not None:
            for k1 in self.room_images:
                result['room_images'].append(k1.to_map() if k1 else None)

        if self.room_name is not None:
            result['room_name'] = self.room_name

        if self.room_type is not None:
            result['room_type'] = self.room_type

        if self.roomarea is not None:
            result['roomarea'] = self.roomarea

        if self.rooms is not None:
            result['rooms'] = self.rooms

        if self.smoke is not None:
            result['smoke'] = self.smoke

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
                temp_model = main_models.HotelRoomInfoResponseBodyModuleBedInfoGroupList()
                self.bed_info_group_list.append(temp_model.from_map(k1))

        self.bed_infos = []
        if m.get('bed_infos') is not None:
            for k1 in m.get('bed_infos'):
                temp_model = main_models.HotelRoomInfoResponseBodyModuleBedInfos()
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

        if m.get('room_desc') is not None:
            self.room_desc = m.get('room_desc')

        if m.get('room_facilities') is not None:
            self.room_facilities = m.get('room_facilities')

        if m.get('room_facility_list') is not None:
            self.room_facility_list = m.get('room_facility_list')

        if m.get('room_id') is not None:
            self.room_id = m.get('room_id')

        if m.get('room_image') is not None:
            self.room_image = m.get('room_image')

        self.room_images = []
        if m.get('room_images') is not None:
            for k1 in m.get('room_images'):
                temp_model = main_models.HotelRoomInfoResponseBodyModuleRoomImages()
                self.room_images.append(temp_model.from_map(k1))

        if m.get('room_name') is not None:
            self.room_name = m.get('room_name')

        if m.get('room_type') is not None:
            self.room_type = m.get('room_type')

        if m.get('roomarea') is not None:
            self.roomarea = m.get('roomarea')

        if m.get('rooms') is not None:
            self.rooms = m.get('rooms')

        if m.get('smoke') is not None:
            self.smoke = m.get('smoke')

        if m.get('window') is not None:
            self.window = m.get('window')

        if m.get('window_bad') is not None:
            self.window_bad = m.get('window_bad')

        if m.get('window_view') is not None:
            self.window_view = m.get('window_view')

        return self

class HotelRoomInfoResponseBodyModuleRoomImages(DaraModel):
    def __init__(
        self,
        bed_infos_2: str = None,
        tag: int = None,
        url: str = None,
    ):
        self.bed_infos_2 = bed_infos_2
        self.tag = tag
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bed_infos_2 is not None:
            result['bed_infos2'] = self.bed_infos_2

        if self.tag is not None:
            result['tag'] = self.tag

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bed_infos2') is not None:
            self.bed_infos_2 = m.get('bed_infos2')

        if m.get('tag') is not None:
            self.tag = m.get('tag')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class HotelRoomInfoResponseBodyModuleBedInfos(DaraModel):
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

class HotelRoomInfoResponseBodyModuleBedInfoGroupList(DaraModel):
    def __init__(
        self,
        bed_infos: List[main_models.HotelRoomInfoResponseBodyModuleBedInfoGroupListBedInfos] = None,
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
        result['bed_infos'] = []
        if self.bed_infos is not None:
            for k1 in self.bed_infos:
                result['bed_infos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bed_infos = []
        if m.get('bed_infos') is not None:
            for k1 in m.get('bed_infos'):
                temp_model = main_models.HotelRoomInfoResponseBodyModuleBedInfoGroupListBedInfos()
                self.bed_infos.append(temp_model.from_map(k1))

        return self

class HotelRoomInfoResponseBodyModuleBedInfoGroupListBedInfos(DaraModel):
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

