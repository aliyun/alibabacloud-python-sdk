# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class ListIntentionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListIntentionsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # API Status Code
        self.code = code
        # Returned Data
        self.data = data
        # HTTP Status Code
        self.http_status_code = http_status_code
        # API Message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Is Success
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListIntentionsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListIntentionsResponseBodyData(DaraModel):
    def __init__(
        self,
        bot_id: str = None,
        intent_list: List[main_models.ListIntentionsResponseBodyDataIntentList] = None,
        message: str = None,
        success: bool = None,
    ):
        # Bot ID
        self.bot_id = bot_id
        # Intent List
        self.intent_list = intent_list
        # API Message
        self.message = message
        # Indicates whether the operation was successful.
        self.success = success

    def validate(self):
        if self.intent_list:
            for v1 in self.intent_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bot_id is not None:
            result['BotId'] = self.bot_id

        result['IntentList'] = []
        if self.intent_list is not None:
            for k1 in self.intent_list:
                result['IntentList'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BotId') is not None:
            self.bot_id = m.get('BotId')

        self.intent_list = []
        if m.get('IntentList') is not None:
            for k1 in m.get('IntentList'):
                temp_model = main_models.ListIntentionsResponseBodyDataIntentList()
                self.intent_list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListIntentionsResponseBodyDataIntentList(DaraModel):
    def __init__(
        self,
        alias: List[str] = None,
        bot_id: int = None,
        bot_name: str = None,
        dialog_id: str = None,
        id: int = None,
        language: str = None,
        name: str = None,
        rule_check: List[main_models.ListIntentionsResponseBodyDataIntentListRuleCheck] = None,
        slot: List[main_models.ListIntentionsResponseBodyDataIntentListSlot] = None,
        table_id: int = None,
        type: int = None,
        user_say: List[main_models.ListIntentionsResponseBodyDataIntentListUserSay] = None,
    ):
        # Intent Alias
        self.alias = alias
        # Bot ID (Deprecated)
        self.bot_id = bot_id
        # Bot Name
        self.bot_name = bot_name
        # Conversation Flow ID
        self.dialog_id = dialog_id
        # Intent ID
        self.id = id
        # Language
        # 
        # - English (en-us)
        # 
        # - Chinese (zh-cn)
        self.language = language
        # Intent Name
        self.name = name
        # LGF Intent Expression
        self.rule_check = rule_check
        # Intent Slot Information
        self.slot = slot
        # Table ID
        self.table_id = table_id
        # Intent Type:
        # 
        # - 0: Normal intent;
        # 
        # - 1: UNKNOWN;
        # 
        # - 2: TableQA intent;
        # 
        # - 3: Generated from standard intent
        self.type = type
        # User Say List
        self.user_say = user_say

    def validate(self):
        if self.rule_check:
            for v1 in self.rule_check:
                 if v1:
                    v1.validate()
        if self.slot:
            for v1 in self.slot:
                 if v1:
                    v1.validate()
        if self.user_say:
            for v1 in self.user_say:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.bot_id is not None:
            result['BotId'] = self.bot_id

        if self.bot_name is not None:
            result['BotName'] = self.bot_name

        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id

        if self.id is not None:
            result['Id'] = self.id

        if self.language is not None:
            result['Language'] = self.language

        if self.name is not None:
            result['Name'] = self.name

        result['RuleCheck'] = []
        if self.rule_check is not None:
            for k1 in self.rule_check:
                result['RuleCheck'].append(k1.to_map() if k1 else None)

        result['Slot'] = []
        if self.slot is not None:
            for k1 in self.slot:
                result['Slot'].append(k1.to_map() if k1 else None)

        if self.table_id is not None:
            result['TableId'] = self.table_id

        if self.type is not None:
            result['Type'] = self.type

        result['UserSay'] = []
        if self.user_say is not None:
            for k1 in self.user_say:
                result['UserSay'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('BotId') is not None:
            self.bot_id = m.get('BotId')

        if m.get('BotName') is not None:
            self.bot_name = m.get('BotName')

        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.rule_check = []
        if m.get('RuleCheck') is not None:
            for k1 in m.get('RuleCheck'):
                temp_model = main_models.ListIntentionsResponseBodyDataIntentListRuleCheck()
                self.rule_check.append(temp_model.from_map(k1))

        self.slot = []
        if m.get('Slot') is not None:
            for k1 in m.get('Slot'):
                temp_model = main_models.ListIntentionsResponseBodyDataIntentListSlot()
                self.slot.append(temp_model.from_map(k1))

        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        self.user_say = []
        if m.get('UserSay') is not None:
            for k1 in m.get('UserSay'):
                temp_model = main_models.ListIntentionsResponseBodyDataIntentListUserSay()
                self.user_say.append(temp_model.from_map(k1))

        return self

class ListIntentionsResponseBodyDataIntentListUserSay(DaraModel):
    def __init__(
        self,
        from_id: str = None,
        id: str = None,
        strict: bool = None,
        user_say_data: List[main_models.ListIntentionsResponseBodyDataIntentListUserSayUserSayData] = None,
    ):
        # Source ID
        # >Notice: Invalid content
        self.from_id = from_id
        # The ID of the user utterance.
        self.id = id
        # Is Strict Match
        self.strict = strict
        # User Say List
        self.user_say_data = user_say_data

    def validate(self):
        if self.user_say_data:
            for v1 in self.user_say_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_id is not None:
            result['FromId'] = self.from_id

        if self.id is not None:
            result['Id'] = self.id

        if self.strict is not None:
            result['Strict'] = self.strict

        result['UserSayData'] = []
        if self.user_say_data is not None:
            for k1 in self.user_say_data:
                result['UserSayData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromId') is not None:
            self.from_id = m.get('FromId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Strict') is not None:
            self.strict = m.get('Strict')

        self.user_say_data = []
        if m.get('UserSayData') is not None:
            for k1 in m.get('UserSayData'):
                temp_model = main_models.ListIntentionsResponseBodyDataIntentListUserSayUserSayData()
                self.user_say_data.append(temp_model.from_map(k1))

        return self

class ListIntentionsResponseBodyDataIntentListUserSayUserSayData(DaraModel):
    def __init__(
        self,
        slot_id: str = None,
        text: str = None,
    ):
        # Slot Unique Identifier
        self.slot_id = slot_id
        # Expression
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.slot_id is not None:
            result['SlotId'] = self.slot_id

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

class ListIntentionsResponseBodyDataIntentListSlot(DaraModel):
    def __init__(
        self,
        feedback_functions: List[main_models.ListIntentionsResponseBodyDataIntentListSlotFeedbackFunctions] = None,
        feedback_type: str = None,
        id: str = None,
        is_array: bool = None,
        is_encrypt: bool = None,
        is_interactive: bool = None,
        is_necessary: bool = None,
        life_span: int = None,
        name: str = None,
        question: List[str] = None,
        tags: List[main_models.ListIntentionsResponseBodyDataIntentListSlotTags] = None,
        value: str = None,
    ):
        # The follow-up question function.
        # >Notice: This parameter is invalid.
        self.feedback_functions = feedback_functions
        # Feedback Type
        # >Notice: Invalid content
        self.feedback_type = feedback_type
        # Slot Unique Identifier
        self.id = id
        # Is Array:
        # 
        # - true: Yes
        # 
        # - false: No
        self.is_array = is_array
        # Is Encrypted
        # >Notice: Invalid content
        self.is_encrypt = is_encrypt
        # Is Interactive
        # >Notice: Invalid content
        self.is_interactive = is_interactive
        # Is Required Slot:
        # 
        # - true: Yes
        # 
        # - false: No
        self.is_necessary = is_necessary
        # Slot Lifecycle
        self.life_span = life_span
        # Slot Name
        self.name = name
        # Slot Follow-up Question
        self.question = question
        # Slot Tagging Labels
        self.tags = tags
        # Slot Tagging Result
        self.value = value

    def validate(self):
        if self.feedback_functions:
            for v1 in self.feedback_functions:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FeedbackFunctions'] = []
        if self.feedback_functions is not None:
            for k1 in self.feedback_functions:
                result['FeedbackFunctions'].append(k1.to_map() if k1 else None)

        if self.feedback_type is not None:
            result['FeedbackType'] = self.feedback_type

        if self.id is not None:
            result['Id'] = self.id

        if self.is_array is not None:
            result['IsArray'] = self.is_array

        if self.is_encrypt is not None:
            result['IsEncrypt'] = self.is_encrypt

        if self.is_interactive is not None:
            result['IsInteractive'] = self.is_interactive

        if self.is_necessary is not None:
            result['IsNecessary'] = self.is_necessary

        if self.life_span is not None:
            result['LifeSpan'] = self.life_span

        if self.name is not None:
            result['Name'] = self.name

        if self.question is not None:
            result['Question'] = self.question

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.feedback_functions = []
        if m.get('FeedbackFunctions') is not None:
            for k1 in m.get('FeedbackFunctions'):
                temp_model = main_models.ListIntentionsResponseBodyDataIntentListSlotFeedbackFunctions()
                self.feedback_functions.append(temp_model.from_map(k1))

        if m.get('FeedbackType') is not None:
            self.feedback_type = m.get('FeedbackType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsArray') is not None:
            self.is_array = m.get('IsArray')

        if m.get('IsEncrypt') is not None:
            self.is_encrypt = m.get('IsEncrypt')

        if m.get('IsInteractive') is not None:
            self.is_interactive = m.get('IsInteractive')

        if m.get('IsNecessary') is not None:
            self.is_necessary = m.get('IsNecessary')

        if m.get('LifeSpan') is not None:
            self.life_span = m.get('LifeSpan')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Question') is not None:
            self.question = m.get('Question')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListIntentionsResponseBodyDataIntentListSlotTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListIntentionsResponseBodyDataIntentListSlotTags(DaraModel):
    def __init__(
        self,
        user_say_id: str = None,
        value: str = None,
    ):
        # User Say Unique Identifier for the Label
        self.user_say_id = user_say_id
        # The value of the tag is the result of tagging an intent expression.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListIntentionsResponseBodyDataIntentListSlotFeedbackFunctions(DaraModel):
    def __init__(
        self,
        aliyun_function: str = None,
        aliyun_service: str = None,
        code: str = None,
        description: str = None,
        end_point: str = None,
        function: str = None,
        name: str = None,
        params: Dict[str, Any] = None,
        switch: List[main_models.ListIntentionsResponseBodyDataIntentListSlotFeedbackFunctionsSwitch] = None,
        type: str = None,
    ):
        # Alibaba Cloud Function Name
        self.aliyun_function = aliyun_function
        # Alibaba Cloud Service
        self.aliyun_service = aliyun_service
        # API Status Code
        self.code = code
        # Follow-up Question Description
        self.description = description
        # Endpoint
        self.end_point = end_point
        # Follow-up Question Function
        self.function = function
        # Function Name
        self.name = name
        # Parameters
        self.params = params
        # Feature Switch. Values:
        # 
        # - **on**: Enabled
        # 
        # - **off**: Disabled
        self.switch = switch
        # Follow-up Question Type
        self.type = type

    def validate(self):
        if self.switch:
            for v1 in self.switch:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_function is not None:
            result['AliyunFunction'] = self.aliyun_function

        if self.aliyun_service is not None:
            result['AliyunService'] = self.aliyun_service

        if self.code is not None:
            result['Code'] = self.code

        if self.description is not None:
            result['Description'] = self.description

        if self.end_point is not None:
            result['EndPoint'] = self.end_point

        if self.function is not None:
            result['Function'] = self.function

        if self.name is not None:
            result['Name'] = self.name

        if self.params is not None:
            result['Params'] = self.params

        result['Switch'] = []
        if self.switch is not None:
            for k1 in self.switch:
                result['Switch'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunFunction') is not None:
            self.aliyun_function = m.get('AliyunFunction')

        if m.get('AliyunService') is not None:
            self.aliyun_service = m.get('AliyunService')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')

        if m.get('Function') is not None:
            self.function = m.get('Function')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        self.switch = []
        if m.get('Switch') is not None:
            for k1 in m.get('Switch'):
                temp_model = main_models.ListIntentionsResponseBodyDataIntentListSlotFeedbackFunctionsSwitch()
                self.switch.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListIntentionsResponseBodyDataIntentListSlotFeedbackFunctionsSwitch(DaraModel):
    def __init__(
        self,
        id: str = None,
        label: str = None,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        # Condition ID
        self.id = id
        # Follow-up Question Label
        self.label = label
        # Condition Name
        self.name = name
        # Type
        self.type = type
        # Condition Value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.label is not None:
            result['Label'] = self.label

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListIntentionsResponseBodyDataIntentListRuleCheck(DaraModel):
    def __init__(
        self,
        error: List[str] = None,
        strict: bool = None,
        text: str = None,
        warning: List[str] = None,
    ):
        # Error Message
        self.error = error
        # Is Strict Match
        self.strict = strict
        # Expression Value
        self.text = text
        # Warning Message
        self.warning = warning

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error is not None:
            result['Error'] = self.error

        if self.strict is not None:
            result['Strict'] = self.strict

        if self.text is not None:
            result['Text'] = self.text

        if self.warning is not None:
            result['Warning'] = self.warning

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('Strict') is not None:
            self.strict = m.get('Strict')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Warning') is not None:
            self.warning = m.get('Warning')

        return self

