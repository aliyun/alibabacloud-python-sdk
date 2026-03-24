# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_chatbot20220408 import models as main_models
from darabonba.model import DaraModel

class ListUserSayResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        user_says: List[main_models.ListUserSayResponseBodyUserSays] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.user_says = user_says

    def validate(self):
        if self.user_says:
            for v1 in self.user_says:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['UserSays'] = []
        if self.user_says is not None:
            for k1 in self.user_says:
                result['UserSays'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.user_says = []
        if m.get('UserSays') is not None:
            for k1 in m.get('UserSays'):
                temp_model = main_models.ListUserSayResponseBodyUserSays()
                self.user_says.append(temp_model.from_map(k1))

        return self

class ListUserSayResponseBodyUserSays(DaraModel):
    def __init__(
        self,
        content: str = None,
        create_time: str = None,
        intent_id: int = None,
        modify_time: str = None,
        slot_infos: List[main_models.ListUserSayResponseBodyUserSaysSlotInfos] = None,
        user_say_id: int = None,
    ):
        self.content = content
        self.create_time = create_time
        self.intent_id = intent_id
        self.modify_time = modify_time
        self.slot_infos = slot_infos
        self.user_say_id = user_say_id

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
        if self.content is not None:
            result['Content'] = self.content

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.intent_id is not None:
            result['IntentId'] = self.intent_id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        result['SlotInfos'] = []
        if self.slot_infos is not None:
            for k1 in self.slot_infos:
                result['SlotInfos'].append(k1.to_map() if k1 else None)

        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        self.slot_infos = []
        if m.get('SlotInfos') is not None:
            for k1 in m.get('SlotInfos'):
                temp_model = main_models.ListUserSayResponseBodyUserSaysSlotInfos()
                self.slot_infos.append(temp_model.from_map(k1))

        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')

        return self

class ListUserSayResponseBodyUserSaysSlotInfos(DaraModel):
    def __init__(
        self,
        end_index: int = None,
        slot_id: str = None,
        start_index: int = None,
    ):
        self.end_index = end_index
        self.slot_id = slot_id
        self.start_index = start_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_index is not None:
            result['EndIndex'] = self.end_index

        if self.slot_id is not None:
            result['SlotId'] = self.slot_id

        if self.start_index is not None:
            result['StartIndex'] = self.start_index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndIndex') is not None:
            self.end_index = m.get('EndIndex')

        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')

        if m.get('StartIndex') is not None:
            self.start_index = m.get('StartIndex')

        return self

