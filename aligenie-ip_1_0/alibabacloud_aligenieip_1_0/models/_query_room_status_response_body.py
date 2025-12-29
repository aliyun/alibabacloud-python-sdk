# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class QueryRoomStatusResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.QueryRoomStatusResponseBodyResult = None,
        status_code: int = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.QueryRoomStatusResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

class QueryRoomStatusResponseBodyResult(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        room_no: str = None,
        scene_list: List[main_models.QueryRoomStatusResponseBodyResultSceneList] = None,
        status_list: List[main_models.QueryRoomStatusResponseBodyResultStatusList] = None,
    ):
        self.hotel_id = hotel_id
        self.room_no = room_no
        self.scene_list = scene_list
        self.status_list = status_list

    def validate(self):
        if self.scene_list:
            for v1 in self.scene_list:
                 if v1:
                    v1.validate()
        if self.status_list:
            for v1 in self.status_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.room_no is not None:
            result['RoomNo'] = self.room_no

        result['SceneList'] = []
        if self.scene_list is not None:
            for k1 in self.scene_list:
                result['SceneList'].append(k1.to_map() if k1 else None)

        result['StatusList'] = []
        if self.status_list is not None:
            for k1 in self.status_list:
                result['StatusList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')

        self.scene_list = []
        if m.get('SceneList') is not None:
            for k1 in m.get('SceneList'):
                temp_model = main_models.QueryRoomStatusResponseBodyResultSceneList()
                self.scene_list.append(temp_model.from_map(k1))

        self.status_list = []
        if m.get('StatusList') is not None:
            for k1 in m.get('StatusList'):
                temp_model = main_models.QueryRoomStatusResponseBodyResultStatusList()
                self.status_list.append(temp_model.from_map(k1))

        return self

class QueryRoomStatusResponseBodyResultStatusList(DaraModel):
    def __init__(
        self,
        status_name: str = None,
        status_value: str = None,
        update_time: str = None,
    ):
        self.status_name = status_name
        self.status_value = status_value
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status_name is not None:
            result['StatusName'] = self.status_name

        if self.status_value is not None:
            result['StatusValue'] = self.status_value

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')

        if m.get('StatusValue') is not None:
            self.status_value = m.get('StatusValue')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class QueryRoomStatusResponseBodyResultSceneList(DaraModel):
    def __init__(
        self,
        scene_name: str = None,
    ):
        self.scene_name = scene_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        return self

