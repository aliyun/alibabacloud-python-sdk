# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_chatbot20220408 import models as main_models
from darabonba.model import DaraModel

class NluResponseBody(DaraModel):
    def __init__(
        self,
        message_id: str = None,
        messages: List[main_models.NluResponseBodyMessages] = None,
        request_id: str = None,
    ):
        self.message_id = message_id
        self.messages = messages
        self.request_id = request_id

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message_id is not None:
            result['MessageId'] = self.message_id

        result['Messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['Messages'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        self.messages = []
        if m.get('Messages') is not None:
            for k1 in m.get('Messages'):
                temp_model = main_models.NluResponseBodyMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class NluResponseBodyMessages(DaraModel):
    def __init__(
        self,
        dialog_hub_nlu_info: main_models.NluResponseBodyMessagesDialogHubNluInfo = None,
        ds_nlu_info: main_models.NluResponseBodyMessagesDsNluInfo = None,
    ):
        self.dialog_hub_nlu_info = dialog_hub_nlu_info
        self.ds_nlu_info = ds_nlu_info

    def validate(self):
        if self.dialog_hub_nlu_info:
            self.dialog_hub_nlu_info.validate()
        if self.ds_nlu_info:
            self.ds_nlu_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dialog_hub_nlu_info is not None:
            result['DialogHubNluInfo'] = self.dialog_hub_nlu_info.to_map()

        if self.ds_nlu_info is not None:
            result['DsNluInfo'] = self.ds_nlu_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialogHubNluInfo') is not None:
            temp_model = main_models.NluResponseBodyMessagesDialogHubNluInfo()
            self.dialog_hub_nlu_info = temp_model.from_map(m.get('DialogHubNluInfo'))

        if m.get('DsNluInfo') is not None:
            temp_model = main_models.NluResponseBodyMessagesDsNluInfo()
            self.ds_nlu_info = temp_model.from_map(m.get('DsNluInfo'))

        return self

class NluResponseBodyMessagesDsNluInfo(DaraModel):
    def __init__(
        self,
        entity_list: List[main_models.NluResponseBodyMessagesDsNluInfoEntityList] = None,
        intent_list: List[main_models.NluResponseBodyMessagesDsNluInfoIntentList] = None,
    ):
        self.entity_list = entity_list
        self.intent_list = intent_list

    def validate(self):
        if self.entity_list:
            for v1 in self.entity_list:
                 if v1:
                    v1.validate()
        if self.intent_list:
            for v1 in self.intent_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EntityList'] = []
        if self.entity_list is not None:
            for k1 in self.entity_list:
                result['EntityList'].append(k1.to_map() if k1 else None)

        result['IntentList'] = []
        if self.intent_list is not None:
            for k1 in self.intent_list:
                result['IntentList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entity_list = []
        if m.get('EntityList') is not None:
            for k1 in m.get('EntityList'):
                temp_model = main_models.NluResponseBodyMessagesDsNluInfoEntityList()
                self.entity_list.append(temp_model.from_map(k1))

        self.intent_list = []
        if m.get('IntentList') is not None:
            for k1 in m.get('IntentList'):
                temp_model = main_models.NluResponseBodyMessagesDsNluInfoIntentList()
                self.intent_list.append(temp_model.from_map(k1))

        return self

class NluResponseBodyMessagesDsNluInfoIntentList(DaraModel):
    def __init__(
        self,
        intent_id: int = None,
        match_detail: str = None,
        match_type: str = None,
        name: str = None,
        score: float = None,
        slot_list: List[main_models.NluResponseBodyMessagesDsNluInfoIntentListSlotList] = None,
    ):
        self.intent_id = intent_id
        self.match_detail = match_detail
        self.match_type = match_type
        self.name = name
        self.score = score
        self.slot_list = slot_list

    def validate(self):
        if self.slot_list:
            for v1 in self.slot_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id

        if self.match_detail is not None:
            result['MatchDetail'] = self.match_detail

        if self.match_type is not None:
            result['MatchType'] = self.match_type

        if self.name is not None:
            result['Name'] = self.name

        if self.score is not None:
            result['Score'] = self.score

        result['SlotList'] = []
        if self.slot_list is not None:
            for k1 in self.slot_list:
                result['SlotList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')

        if m.get('MatchDetail') is not None:
            self.match_detail = m.get('MatchDetail')

        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        self.slot_list = []
        if m.get('SlotList') is not None:
            for k1 in m.get('SlotList'):
                temp_model = main_models.NluResponseBodyMessagesDsNluInfoIntentListSlotList()
                self.slot_list.append(temp_model.from_map(k1))

        return self

class NluResponseBodyMessagesDsNluInfoIntentListSlotList(DaraModel):
    def __init__(
        self,
        name: str = None,
        origin: str = None,
        type: str = None,
        value: str = None,
    ):
        self.name = name
        self.origin = origin
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class NluResponseBodyMessagesDsNluInfoEntityList(DaraModel):
    def __init__(
        self,
        name: str = None,
        origin: str = None,
        type: str = None,
        value: str = None,
    ):
        self.name = name
        self.origin = origin
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class NluResponseBodyMessagesDialogHubNluInfo(DaraModel):
    def __init__(
        self,
        global_dict_list: List[main_models.NluResponseBodyMessagesDialogHubNluInfoGlobalDictList] = None,
        global_sensitive_word_list: List[main_models.NluResponseBodyMessagesDialogHubNluInfoGlobalSensitiveWordList] = None,
    ):
        self.global_dict_list = global_dict_list
        self.global_sensitive_word_list = global_sensitive_word_list

    def validate(self):
        if self.global_dict_list:
            for v1 in self.global_dict_list:
                 if v1:
                    v1.validate()
        if self.global_sensitive_word_list:
            for v1 in self.global_sensitive_word_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GlobalDictList'] = []
        if self.global_dict_list is not None:
            for k1 in self.global_dict_list:
                result['GlobalDictList'].append(k1.to_map() if k1 else None)

        result['GlobalSensitiveWordList'] = []
        if self.global_sensitive_word_list is not None:
            for k1 in self.global_sensitive_word_list:
                result['GlobalSensitiveWordList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.global_dict_list = []
        if m.get('GlobalDictList') is not None:
            for k1 in m.get('GlobalDictList'):
                temp_model = main_models.NluResponseBodyMessagesDialogHubNluInfoGlobalDictList()
                self.global_dict_list.append(temp_model.from_map(k1))

        self.global_sensitive_word_list = []
        if m.get('GlobalSensitiveWordList') is not None:
            for k1 in m.get('GlobalSensitiveWordList'):
                temp_model = main_models.NluResponseBodyMessagesDialogHubNluInfoGlobalSensitiveWordList()
                self.global_sensitive_word_list.append(temp_model.from_map(k1))

        return self

class NluResponseBodyMessagesDialogHubNluInfoGlobalSensitiveWordList(DaraModel):
    def __init__(
        self,
        standard_word: str = None,
        word: str = None,
    ):
        self.standard_word = standard_word
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.standard_word is not None:
            result['StandardWord'] = self.standard_word

        if self.word is not None:
            result['Word'] = self.word

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StandardWord') is not None:
            self.standard_word = m.get('StandardWord')

        if m.get('Word') is not None:
            self.word = m.get('Word')

        return self

class NluResponseBodyMessagesDialogHubNluInfoGlobalDictList(DaraModel):
    def __init__(
        self,
        standard_word: str = None,
        word: str = None,
    ):
        self.standard_word = standard_word
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.standard_word is not None:
            result['StandardWord'] = self.standard_word

        if self.word is not None:
            result['Word'] = self.word

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StandardWord') is not None:
            self.standard_word = m.get('StandardWord')

        if m.get('Word') is not None:
            self.word = m.get('Word')

        return self

