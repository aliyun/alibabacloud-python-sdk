# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class PushHotelMessageRequest(DaraModel):
    def __init__(
        self,
        push_hotel_message_req: main_models.PushHotelMessageRequestPushHotelMessageReq = None,
    ):
        # pushHotelMessageReq
        # 
        # This parameter is required.
        self.push_hotel_message_req = push_hotel_message_req

    def validate(self):
        if self.push_hotel_message_req:
            self.push_hotel_message_req.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.push_hotel_message_req is not None:
            result['PushHotelMessageReq'] = self.push_hotel_message_req.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushHotelMessageReq') is not None:
            temp_model = main_models.PushHotelMessageRequestPushHotelMessageReq()
            self.push_hotel_message_req = temp_model.from_map(m.get('PushHotelMessageReq'))

        return self

class PushHotelMessageRequestPushHotelMessageReq(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        param_map: Dict[str, str] = None,
        room_no: str = None,
        template_id: int = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        self.param_map = param_map
        # This parameter is required.
        self.room_no = room_no
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.param_map is not None:
            result['ParamMap'] = self.param_map

        if self.room_no is not None:
            result['RoomNo'] = self.room_no

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('ParamMap') is not None:
            self.param_map = m.get('ParamMap')

        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

