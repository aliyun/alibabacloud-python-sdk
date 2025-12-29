# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class PushVoiceBoxCommandsRequest(DaraModel):
    def __init__(
        self,
        commands: List[main_models.PushVoiceBoxCommandsRequestCommands] = None,
        hotel_id: str = None,
        room_no: str = None,
    ):
        # This parameter is required.
        self.commands = commands
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.room_no = room_no

    def validate(self):
        if self.commands:
            for v1 in self.commands:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Commands'] = []
        if self.commands is not None:
            for k1 in self.commands:
                result['Commands'].append(k1.to_map() if k1 else None)

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.room_no is not None:
            result['RoomNo'] = self.room_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.commands = []
        if m.get('Commands') is not None:
            for k1 in m.get('Commands'):
                temp_model = main_models.PushVoiceBoxCommandsRequestCommands()
                self.commands.append(temp_model.from_map(k1))

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')

        return self

class PushVoiceBoxCommandsRequestCommands(DaraModel):
    def __init__(
        self,
        command_domain: str = None,
        command_name: str = None,
        payload: str = None,
    ):
        # This parameter is required.
        self.command_domain = command_domain
        # This parameter is required.
        self.command_name = command_name
        self.payload = payload

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_domain is not None:
            result['CommandDomain'] = self.command_domain

        if self.command_name is not None:
            result['CommandName'] = self.command_name

        if self.payload is not None:
            result['Payload'] = self.payload

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandDomain') is not None:
            self.command_domain = m.get('CommandDomain')

        if m.get('CommandName') is not None:
            self.command_name = m.get('CommandName')

        if m.get('Payload') is not None:
            self.payload = m.get('Payload')

        return self

