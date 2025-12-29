# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class ImportRoomGenieScenesRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        room_no: str = None,
        scene_list: List[main_models.ImportRoomGenieScenesRequestSceneList] = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.room_no = room_no
        self.scene_list = scene_list

    def validate(self):
        if self.scene_list:
            for v1 in self.scene_list:
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
                temp_model = main_models.ImportRoomGenieScenesRequestSceneList()
                self.scene_list.append(temp_model.from_map(k1))

        return self

class ImportRoomGenieScenesRequestSceneList(DaraModel):
    def __init__(
        self,
        actions: List[main_models.ImportRoomGenieScenesRequestSceneListActions] = None,
        description: str = None,
        display: bool = None,
        icon: str = None,
        scene_name: str = None,
        trigger_logical: int = None,
        triggers: List[main_models.ImportRoomGenieScenesRequestSceneListTriggers] = None,
    ):
        # This parameter is required.
        self.actions = actions
        self.description = description
        # This parameter is required.
        self.display = display
        self.icon = icon
        # This parameter is required.
        self.scene_name = scene_name
        # This parameter is required.
        self.trigger_logical = trigger_logical
        # This parameter is required.
        self.triggers = triggers

    def validate(self):
        if self.actions:
            for v1 in self.actions:
                 if v1:
                    v1.validate()
        if self.triggers:
            for v1 in self.triggers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Actions'] = []
        if self.actions is not None:
            for k1 in self.actions:
                result['Actions'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.display is not None:
            result['Display'] = self.display

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        if self.trigger_logical is not None:
            result['TriggerLogical'] = self.trigger_logical

        result['Triggers'] = []
        if self.triggers is not None:
            for k1 in self.triggers:
                result['Triggers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k1 in m.get('Actions'):
                temp_model = main_models.ImportRoomGenieScenesRequestSceneListActions()
                self.actions.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        if m.get('TriggerLogical') is not None:
            self.trigger_logical = m.get('TriggerLogical')

        self.triggers = []
        if m.get('Triggers') is not None:
            for k1 in m.get('Triggers'):
                temp_model = main_models.ImportRoomGenieScenesRequestSceneListTriggers()
                self.triggers.append(temp_model.from_map(k1))

        return self

class ImportRoomGenieScenesRequestSceneListTriggers(DaraModel):
    def __init__(
        self,
        attribute_values: List[main_models.ImportRoomGenieScenesRequestSceneListTriggersAttributeValues] = None,
        corpus_list: List[str] = None,
        device: main_models.ImportRoomGenieScenesRequestSceneListTriggersDevice = None,
        type: int = None,
    ):
        self.attribute_values = attribute_values
        self.corpus_list = corpus_list
        self.device = device
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.attribute_values:
            for v1 in self.attribute_values:
                 if v1:
                    v1.validate()
        if self.device:
            self.device.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttributeValues'] = []
        if self.attribute_values is not None:
            for k1 in self.attribute_values:
                result['AttributeValues'].append(k1.to_map() if k1 else None)

        if self.corpus_list is not None:
            result['CorpusList'] = self.corpus_list

        if self.device is not None:
            result['Device'] = self.device.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attribute_values = []
        if m.get('AttributeValues') is not None:
            for k1 in m.get('AttributeValues'):
                temp_model = main_models.ImportRoomGenieScenesRequestSceneListTriggersAttributeValues()
                self.attribute_values.append(temp_model.from_map(k1))

        if m.get('CorpusList') is not None:
            self.corpus_list = m.get('CorpusList')

        if m.get('Device') is not None:
            temp_model = main_models.ImportRoomGenieScenesRequestSceneListTriggersDevice()
            self.device = temp_model.from_map(m.get('Device'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ImportRoomGenieScenesRequestSceneListTriggersDevice(DaraModel):
    def __init__(
        self,
        category: str = None,
        device_index: str = None,
        device_number: str = None,
    ):
        # This parameter is required.
        self.category = category
        self.device_index = device_index
        # This parameter is required.
        self.device_number = device_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.device_index is not None:
            result['DeviceIndex'] = self.device_index

        if self.device_number is not None:
            result['DeviceNumber'] = self.device_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DeviceIndex') is not None:
            self.device_index = m.get('DeviceIndex')

        if m.get('DeviceNumber') is not None:
            self.device_number = m.get('DeviceNumber')

        return self

class ImportRoomGenieScenesRequestSceneListTriggersAttributeValues(DaraModel):
    def __init__(
        self,
        attribute_name: str = None,
        attribute_value: str = None,
    ):
        # This parameter is required.
        self.attribute_name = attribute_name
        # This parameter is required.
        self.attribute_value = attribute_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name

        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')

        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')

        return self

class ImportRoomGenieScenesRequestSceneListActions(DaraModel):
    def __init__(
        self,
        attribute_values: List[main_models.ImportRoomGenieScenesRequestSceneListActionsAttributeValues] = None,
        device: main_models.ImportRoomGenieScenesRequestSceneListActionsDevice = None,
        reply: str = None,
        type: int = None,
    ):
        self.attribute_values = attribute_values
        self.device = device
        self.reply = reply
        self.type = type

    def validate(self):
        if self.attribute_values:
            for v1 in self.attribute_values:
                 if v1:
                    v1.validate()
        if self.device:
            self.device.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttributeValues'] = []
        if self.attribute_values is not None:
            for k1 in self.attribute_values:
                result['AttributeValues'].append(k1.to_map() if k1 else None)

        if self.device is not None:
            result['Device'] = self.device.to_map()

        if self.reply is not None:
            result['Reply'] = self.reply

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attribute_values = []
        if m.get('AttributeValues') is not None:
            for k1 in m.get('AttributeValues'):
                temp_model = main_models.ImportRoomGenieScenesRequestSceneListActionsAttributeValues()
                self.attribute_values.append(temp_model.from_map(k1))

        if m.get('Device') is not None:
            temp_model = main_models.ImportRoomGenieScenesRequestSceneListActionsDevice()
            self.device = temp_model.from_map(m.get('Device'))

        if m.get('Reply') is not None:
            self.reply = m.get('Reply')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ImportRoomGenieScenesRequestSceneListActionsDevice(DaraModel):
    def __init__(
        self,
        category: str = None,
        device_index: int = None,
        device_number: str = None,
        type: int = None,
    ):
        # This parameter is required.
        self.category = category
        self.device_index = device_index
        # This parameter is required.
        self.device_number = device_number
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.device_index is not None:
            result['DeviceIndex'] = self.device_index

        if self.device_number is not None:
            result['DeviceNumber'] = self.device_number

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DeviceIndex') is not None:
            self.device_index = m.get('DeviceIndex')

        if m.get('DeviceNumber') is not None:
            self.device_number = m.get('DeviceNumber')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ImportRoomGenieScenesRequestSceneListActionsAttributeValues(DaraModel):
    def __init__(
        self,
        attribute_name: str = None,
        attribute_value: str = None,
    ):
        # This parameter is required.
        self.attribute_name = attribute_name
        # This parameter is required.
        self.attribute_value = attribute_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name

        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')

        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')

        return self

