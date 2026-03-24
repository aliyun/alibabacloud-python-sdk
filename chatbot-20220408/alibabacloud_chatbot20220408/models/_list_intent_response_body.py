# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_chatbot20220408 import models as main_models
from darabonba.model import DaraModel

class ListIntentResponseBody(DaraModel):
    def __init__(
        self,
        intents: List[main_models.ListIntentResponseBodyIntents] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.intents = intents
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.intents:
            for v1 in self.intents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Intents'] = []
        if self.intents is not None:
            for k1 in self.intents:
                result['Intents'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.intents = []
        if m.get('Intents') is not None:
            for k1 in m.get('Intents'):
                temp_model = main_models.ListIntentResponseBodyIntents()
                self.intents.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListIntentResponseBodyIntents(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        create_time: str = None,
        create_user_id: str = None,
        create_user_name: str = None,
        intent_id: int = None,
        intent_name: str = None,
        modify_time: str = None,
        modify_user_id: str = None,
        modify_user_name: str = None,
        slot_infos: List[main_models.ListIntentResponseBodyIntentsSlotInfos] = None,
    ):
        self.alias_name = alias_name
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.intent_id = intent_id
        self.intent_name = intent_name
        self.modify_time = modify_time
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.slot_infos = slot_infos

    def validate(self):
        if self.slot_infos:
            for v1 in self.slot_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id

        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name

        if self.intent_id is not None:
            result['IntentId'] = self.intent_id

        if self.intent_name is not None:
            result['IntentName'] = self.intent_name

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id

        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name

        result['SlotInfos'] = []
        if self.slot_infos is not None:
            for k1 in self.slot_infos:
                result['SlotInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')

        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')

        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')

        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')

        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')

        self.slot_infos = []
        if m.get('SlotInfos') is not None:
            for k1 in m.get('SlotInfos'):
                temp_model = main_models.ListIntentResponseBodyIntentsSlotInfos()
                self.slot_infos.append(temp_model.from_map(k1))

        return self

class ListIntentResponseBodyIntentsSlotInfos(DaraModel):
    def __init__(
        self,
        array: bool = None,
        encrypt: bool = None,
        interactive: bool = None,
        name: str = None,
        slot_id: str = None,
        value: str = None,
    ):
        self.array = array
        self.encrypt = encrypt
        self.interactive = interactive
        self.name = name
        self.slot_id = slot_id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.array is not None:
            result['Array'] = self.array

        if self.encrypt is not None:
            result['Encrypt'] = self.encrypt

        if self.interactive is not None:
            result['Interactive'] = self.interactive

        if self.name is not None:
            result['Name'] = self.name

        if self.slot_id is not None:
            result['SlotId'] = self.slot_id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Array') is not None:
            self.array = m.get('Array')

        if m.get('Encrypt') is not None:
            self.encrypt = m.get('Encrypt')

        if m.get('Interactive') is not None:
            self.interactive = m.get('Interactive')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

