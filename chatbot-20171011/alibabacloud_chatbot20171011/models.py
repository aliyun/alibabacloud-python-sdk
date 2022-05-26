# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class Children(TeaModel):
    def __init__(
        self,
        area_code: str = None,
        category_id: int = None,
        childrens: List['Children'] = None,
        name: str = None,
        parent_category_id: int = None,
    ):
        # 地区代号
        self.area_code = area_code
        # 分类Id
        self.category_id = category_id
        # 子元素
        self.childrens = childrens
        # 名称
        self.name = name
        # 父分类Id
        self.parent_category_id = parent_category_id

    def validate(self):
        if self.childrens:
            for k in self.childrens:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_code is not None:
            result['AreaCode'] = self.area_code
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        result['Childrens'] = []
        if self.childrens is not None:
            for k in self.childrens:
                result['Childrens'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaCode') is not None:
            self.area_code = m.get('AreaCode')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        self.childrens = []
        if m.get('Childrens') is not None:
            for k in m.get('Childrens'):
                temp_model = Children()
                self.childrens.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        return self


class RuleMtopDTO(TeaModel):
    def __init__(
        self,
        error: List[str] = None,
        strict: bool = None,
        text: str = None,
        warning: List[str] = None,
    ):
        # Error
        self.error = error
        # Strict
        self.strict = strict
        # Text
        self.text = text
        # Warning
        self.warning = warning

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class TagMtopDTO(TeaModel):
    def __init__(
        self,
        user_say_id: str = None,
        value: str = None,
    ):
        # UserSayId
        self.user_say_id = user_say_id
        # Value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class SlotrecordMtopDTO(TeaModel):
    def __init__(
        self,
        id: str = None,
        is_array: bool = None,
        is_necessary: bool = None,
        life_span: int = None,
        name: str = None,
        question: List[str] = None,
        tags: List[TagMtopDTO] = None,
        value: str = None,
    ):
        # Id
        self.id = id
        # IsArray
        self.is_array = is_array
        # IsNecessary
        self.is_necessary = is_necessary
        # LifeSpan
        self.life_span = life_span
        # Name
        self.name = name
        # Question
        self.question = question
        # Tags
        self.tags = tags
        # Value
        self.value = value

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.is_array is not None:
            result['IsArray'] = self.is_array
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
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsArray') is not None:
            self.is_array = m.get('IsArray')
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
            for k in m.get('Tags'):
                temp_model = TagMtopDTO()
                self.tags.append(temp_model.from_map(k))
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SectionMtopDTO(TeaModel):
    def __init__(
        self,
        slot_id: str = None,
        text: str = None,
    ):
        # SlotId
        self.slot_id = slot_id
        # Text
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UsersayMtopDTO(TeaModel):
    def __init__(
        self,
        data: List[SectionMtopDTO] = None,
        id: str = None,
        strict: bool = None,
    ):
        # Data
        self.data = data
        # Id
        self.id = id
        # Strict
        self.strict = strict

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.strict is not None:
            result['Strict'] = self.strict
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = SectionMtopDTO()
                self.data.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Strict') is not None:
            self.strict = m.get('Strict')
        return self


class IntentCreateDTO(TeaModel):
    def __init__(
        self,
        intent_id: int = None,
        name: str = None,
        rule_check: List[RuleMtopDTO] = None,
        slot: List[SlotrecordMtopDTO] = None,
        user_say: List[UsersayMtopDTO] = None,
    ):
        # IntentId
        self.intent_id = intent_id
        # Name
        self.name = name
        # RuleCheck
        self.rule_check = rule_check
        self.slot = slot
        # UserSay
        self.user_say = user_say

    def validate(self):
        if self.rule_check:
            for k in self.rule_check:
                if k:
                    k.validate()
        if self.slot:
            for k in self.slot:
                if k:
                    k.validate()
        if self.user_say:
            for k in self.user_say:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.name is not None:
            result['Name'] = self.name
        result['RuleCheck'] = []
        if self.rule_check is not None:
            for k in self.rule_check:
                result['RuleCheck'].append(k.to_map() if k else None)
        result['Slot'] = []
        if self.slot is not None:
            for k in self.slot:
                result['Slot'].append(k.to_map() if k else None)
        result['UserSay'] = []
        if self.user_say is not None:
            for k in self.user_say:
                result['UserSay'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.rule_check = []
        if m.get('RuleCheck') is not None:
            for k in m.get('RuleCheck'):
                temp_model = RuleMtopDTO()
                self.rule_check.append(temp_model.from_map(k))
        self.slot = []
        if m.get('Slot') is not None:
            for k in m.get('Slot'):
                temp_model = SlotrecordMtopDTO()
                self.slot.append(temp_model.from_map(k))
        self.user_say = []
        if m.get('UserSay') is not None:
            for k in m.get('UserSay'):
                temp_model = UsersayMtopDTO()
                self.user_say.append(temp_model.from_map(k))
        return self


class PaasButtonDTO(TeaModel):
    def __init__(
        self,
        name: str = None,
        text: str = None,
        type: str = None,
    ):
        # Name
        self.name = name
        # Text
        self.text = text
        # Type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PaasButtonListDTO(TeaModel):
    def __init__(
        self,
        button: List[PaasButtonDTO] = None,
        intro: str = None,
    ):
        # Button
        self.button = button
        # Intro
        self.intro = intro

    def validate(self):
        if self.button:
            for k in self.button:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Button'] = []
        if self.button is not None:
            for k in self.button:
                result['Button'].append(k.to_map() if k else None)
        if self.intro is not None:
            result['Intro'] = self.intro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.button = []
        if m.get('Button') is not None:
            for k in m.get('Button'):
                temp_model = PaasButtonDTO()
                self.button.append(temp_model.from_map(k))
        if m.get('Intro') is not None:
            self.intro = m.get('Intro')
        return self


class PaasConditionEntryDTO(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        term: str = None,
        type: str = None,
        value: str = None,
    ):
        # Id
        self.id = id
        # Name
        self.name = name
        # Term
        self.term = term
        # Type
        self.type = type
        # Value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.term is not None:
            result['Term'] = self.term
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Term') is not None:
            self.term = m.get('Term')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class PaasConditionSetDTO(TeaModel):
    def __init__(
        self,
        condition_entries: List[PaasConditionEntryDTO] = None,
    ):
        # ConditionEntries
        self.condition_entries = condition_entries

    def validate(self):
        if self.condition_entries:
            for k in self.condition_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConditionEntries'] = []
        if self.condition_entries is not None:
            for k in self.condition_entries:
                result['ConditionEntries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.condition_entries = []
        if m.get('ConditionEntries') is not None:
            for k in m.get('ConditionEntries'):
                temp_model = PaasConditionEntryDTO()
                self.condition_entries.append(temp_model.from_map(k))
        return self


class PaasEdgeDTO(TeaModel):
    def __init__(
        self,
        id: str = None,
        label: str = None,
        source: str = None,
        target: str = None,
    ):
        # Id
        self.id = id
        # Label
        self.label = label
        # Source
        self.source = source
        # Target
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.label is not None:
            result['Label'] = self.label
        if self.source is not None:
            result['Source'] = self.source
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class PaasEntryPluginFieldDataDTO(TeaModel):
    def __init__(
        self,
        content_entry: List[PaasConditionSetDTO] = None,
        life_span: int = None,
        name: str = None,
    ):
        # ContentEntry
        self.content_entry = content_entry
        # LifeSpan
        self.life_span = life_span
        # Name
        self.name = name

    def validate(self):
        if self.content_entry:
            for k in self.content_entry:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContentEntry'] = []
        if self.content_entry is not None:
            for k in self.content_entry:
                result['ContentEntry'].append(k.to_map() if k else None)
        if self.life_span is not None:
            result['LifeSpan'] = self.life_span
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content_entry = []
        if m.get('ContentEntry') is not None:
            for k in m.get('ContentEntry'):
                temp_model = PaasConditionSetDTO()
                self.content_entry.append(temp_model.from_map(k))
        if m.get('LifeSpan') is not None:
            self.life_span = m.get('LifeSpan')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class PaasEntryDTO(TeaModel):
    def __init__(
        self,
        plugin_field_data_entry: PaasEntryPluginFieldDataDTO = None,
    ):
        # PluginFieldDataEntry
        self.plugin_field_data_entry = plugin_field_data_entry

    def validate(self):
        if self.plugin_field_data_entry:
            self.plugin_field_data_entry.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plugin_field_data_entry is not None:
            result['PluginFieldDataEntry'] = self.plugin_field_data_entry.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PluginFieldDataEntry') is not None:
            temp_model = PaasEntryPluginFieldDataDTO()
            self.plugin_field_data_entry = temp_model.from_map(m['PluginFieldDataEntry'])
        return self


class PaasSwitchCaseDTO(TeaModel):
    def __init__(
        self,
        id: str = None,
        label: str = None,
        type: str = None,
        value: str = None,
        variable_name: str = None,
    ):
        # Id
        self.id = id
        # Label
        self.label = label
        # Type
        self.type = type
        # Value
        self.value = value
        # VariableName
        self.variable_name = variable_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.label is not None:
            result['Label'] = self.label
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        return self


class PaasFunctionPluginFieldDataDTO(TeaModel):
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
        switch: List[PaasSwitchCaseDTO] = None,
        type: str = None,
    ):
        # AliyunFunction
        self.aliyun_function = aliyun_function
        # AliyunService
        self.aliyun_service = aliyun_service
        # Code
        self.code = code
        # Description
        self.description = description
        # EndPoint
        self.end_point = end_point
        # Function
        self.function = function
        # Name
        self.name = name
        # Params
        self.params = params
        # Switch
        self.switch = switch
        # Type
        self.type = type

    def validate(self):
        if self.switch:
            for k in self.switch:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.switch:
                result['Switch'].append(k.to_map() if k else None)
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
            for k in m.get('Switch'):
                temp_model = PaasSwitchCaseDTO()
                self.switch.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PaasFunctionDTO(TeaModel):
    def __init__(
        self,
        plugin_field_data_function: PaasFunctionPluginFieldDataDTO = None,
    ):
        # PluginFieldDataFunction
        self.plugin_field_data_function = plugin_field_data_function

    def validate(self):
        if self.plugin_field_data_function:
            self.plugin_field_data_function.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plugin_field_data_function is not None:
            result['PluginFieldDataFunction'] = self.plugin_field_data_function.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PluginFieldDataFunction') is not None:
            temp_model = PaasFunctionPluginFieldDataDTO()
            self.plugin_field_data_function = temp_model.from_map(m['PluginFieldDataFunction'])
        return self


class PaasFunctionPluginParams(TeaModel):
    def __init__(
        self,
        body: str = None,
        header: Dict[str, str] = None,
        method: str = None,
        query: Dict[str, str] = None,
        url: str = None,
    ):
        # Body
        self.body = body
        # Header
        self.header = header
        # Method
        self.method = method
        # Query
        self.query = query
        # Url
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.header is not None:
            result['Header'] = self.header
        if self.method is not None:
            result['Method'] = self.method
        if self.query is not None:
            result['Query'] = self.query
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('Header') is not None:
            self.header = m.get('Header')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class PaasResponseNodeContentDTO(TeaModel):
    def __init__(
        self,
        button_list: PaasButtonListDTO = None,
        image: str = None,
        text: str = None,
        type: str = None,
    ):
        # ButtonList
        self.button_list = button_list
        # Image
        self.image = image
        # Text
        self.text = text
        # Type
        self.type = type

    def validate(self):
        if self.button_list:
            self.button_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.button_list is not None:
            result['ButtonList'] = self.button_list.to_map()
        if self.image is not None:
            result['Image'] = self.image
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ButtonList') is not None:
            temp_model = PaasButtonListDTO()
            self.button_list = temp_model.from_map(m['ButtonList'])
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PaasResponsePluginFieldDataDTO(TeaModel):
    def __init__(
        self,
        content_response: PaasResponseNodeContentDTO = None,
        name: str = None,
    ):
        # ContentResponse
        self.content_response = content_response
        # Name
        self.name = name

    def validate(self):
        if self.content_response:
            self.content_response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_response is not None:
            result['ContentResponse'] = self.content_response.to_map()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentResponse') is not None:
            temp_model = PaasResponseNodeContentDTO()
            self.content_response = temp_model.from_map(m['ContentResponse'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class PaasResponseDTO(TeaModel):
    def __init__(
        self,
        plugin_field_data_response: PaasResponsePluginFieldDataDTO = None,
    ):
        self.plugin_field_data_response = plugin_field_data_response

    def validate(self):
        if self.plugin_field_data_response:
            self.plugin_field_data_response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plugin_field_data_response is not None:
            result['PluginFieldDataResponse'] = self.plugin_field_data_response.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PluginFieldDataResponse') is not None:
            temp_model = PaasResponsePluginFieldDataDTO()
            self.plugin_field_data_response = temp_model.from_map(m['PluginFieldDataResponse'])
        return self


class PaasSlotConfigDTO(TeaModel):
    def __init__(
        self,
        is_array: bool = None,
        is_necessary: bool = None,
        life_span: int = None,
        name: str = None,
        question: List[str] = None,
        value: str = None,
    ):
        # IsArray
        self.is_array = is_array
        # IsNecessary
        self.is_necessary = is_necessary
        # LifeSpan
        self.life_span = life_span
        # Name
        self.name = name
        # Question
        self.question = question
        # Value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_array is not None:
            result['IsArray'] = self.is_array
        if self.is_necessary is not None:
            result['IsNecessary'] = self.is_necessary
        if self.life_span is not None:
            result['LifeSpan'] = self.life_span
        if self.name is not None:
            result['Name'] = self.name
        if self.question is not None:
            result['Question'] = self.question
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsArray') is not None:
            self.is_array = m.get('IsArray')
        if m.get('IsNecessary') is not None:
            self.is_necessary = m.get('IsNecessary')
        if m.get('LifeSpan') is not None:
            self.life_span = m.get('LifeSpan')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class PaasSlotPluginFieldDataDTO(TeaModel):
    def __init__(
        self,
        content_slot: List[PaasSlotConfigDTO] = None,
        intent_id: str = None,
        intent_name: str = None,
        is_sys_intent: bool = None,
        name: str = None,
    ):
        # ContentSlot
        self.content_slot = content_slot
        # IntentId
        self.intent_id = intent_id
        # IntentName
        self.intent_name = intent_name
        # IsSysIntent
        self.is_sys_intent = is_sys_intent
        # Name
        self.name = name

    def validate(self):
        if self.content_slot:
            for k in self.content_slot:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContentSlot'] = []
        if self.content_slot is not None:
            for k in self.content_slot:
                result['ContentSlot'].append(k.to_map() if k else None)
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.is_sys_intent is not None:
            result['IsSysIntent'] = self.is_sys_intent
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content_slot = []
        if m.get('ContentSlot') is not None:
            for k in m.get('ContentSlot'):
                temp_model = PaasSlotConfigDTO()
                self.content_slot.append(temp_model.from_map(k))
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('IsSysIntent') is not None:
            self.is_sys_intent = m.get('IsSysIntent')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class PaasSlotDTO(TeaModel):
    def __init__(
        self,
        plugin_field_data_slot: PaasSlotPluginFieldDataDTO = None,
    ):
        self.plugin_field_data_slot = plugin_field_data_slot

    def validate(self):
        if self.plugin_field_data_slot:
            self.plugin_field_data_slot.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plugin_field_data_slot is not None:
            result['PluginFieldDataSlot'] = self.plugin_field_data_slot.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PluginFieldDataSlot') is not None:
            temp_model = PaasSlotPluginFieldDataDTO()
            self.plugin_field_data_slot = temp_model.from_map(m['PluginFieldDataSlot'])
        return self


class PaasPluginDataDTO(TeaModel):
    def __init__(
        self,
        entry: PaasEntryDTO = None,
        function: PaasFunctionDTO = None,
        response: PaasResponseDTO = None,
        slot: PaasSlotDTO = None,
    ):
        self.entry = entry
        self.function = function
        self.response = response
        self.slot = slot

    def validate(self):
        if self.entry:
            self.entry.validate()
        if self.function:
            self.function.validate()
        if self.response:
            self.response.validate()
        if self.slot:
            self.slot.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry is not None:
            result['Entry'] = self.entry.to_map()
        if self.function is not None:
            result['Function'] = self.function.to_map()
        if self.response is not None:
            result['Response'] = self.response.to_map()
        if self.slot is not None:
            result['Slot'] = self.slot.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Entry') is not None:
            temp_model = PaasEntryDTO()
            self.entry = temp_model.from_map(m['Entry'])
        if m.get('Function') is not None:
            temp_model = PaasFunctionDTO()
            self.function = temp_model.from_map(m['Function'])
        if m.get('Response') is not None:
            temp_model = PaasResponseDTO()
            self.response = temp_model.from_map(m['Response'])
        if m.get('Slot') is not None:
            temp_model = PaasSlotDTO()
            self.slot = temp_model.from_map(m['Slot'])
        return self


class PaasNodeDTO(TeaModel):
    def __init__(
        self,
        code: str = None,
        id: str = None,
        label: str = None,
        plugin_data: PaasPluginDataDTO = None,
        xx: float = None,
        yy: float = None,
    ):
        # Code
        self.code = code
        # Id
        self.id = id
        # Label
        self.label = label
        # PluginData
        self.plugin_data = plugin_data
        # Xx
        self.xx = xx
        # Yy
        self.yy = yy

    def validate(self):
        if self.plugin_data:
            self.plugin_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.id is not None:
            result['Id'] = self.id
        if self.label is not None:
            result['Label'] = self.label
        if self.plugin_data is not None:
            result['PluginData'] = self.plugin_data.to_map()
        if self.xx is not None:
            result['Xx'] = self.xx
        if self.yy is not None:
            result['Yy'] = self.yy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('PluginData') is not None:
            temp_model = PaasPluginDataDTO()
            self.plugin_data = temp_model.from_map(m['PluginData'])
        if m.get('Xx') is not None:
            self.xx = m.get('Xx')
        if m.get('Yy') is not None:
            self.yy = m.get('Yy')
        return self


class PaasProcessData(TeaModel):
    def __init__(
        self,
        edges: List[PaasEdgeDTO] = None,
        nodes: List[PaasNodeDTO] = None,
    ):
        # Edges
        self.edges = edges
        # Nodes
        self.nodes = nodes

    def validate(self):
        if self.edges:
            for k in self.edges:
                if k:
                    k.validate()
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Edges'] = []
        if self.edges is not None:
            for k in self.edges:
                result['Edges'].append(k.to_map() if k else None)
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.edges = []
        if m.get('Edges') is not None:
            for k in m.get('Edges'):
                temp_model = PaasEdgeDTO()
                self.edges.append(temp_model.from_map(k))
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = PaasNodeDTO()
                self.nodes.append(temp_model.from_map(k))
        return self


class UpdateDialogFlowModuleDefinition(TeaModel):
    def __init__(
        self,
        edges: List[PaasEdgeDTO] = None,
        nodes: List[PaasNodeDTO] = None,
    ):
        # Edges
        self.edges = edges
        # Nodes
        self.nodes = nodes

    def validate(self):
        if self.edges:
            for k in self.edges:
                if k:
                    k.validate()
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Edges'] = []
        if self.edges is not None:
            for k in self.edges:
                result['Edges'].append(k.to_map() if k else None)
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.edges = []
        if m.get('Edges') is not None:
            for k in m.get('Edges'):
                temp_model = PaasEdgeDTO()
                self.edges.append(temp_model.from_map(k))
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = PaasNodeDTO()
                self.nodes.append(temp_model.from_map(k))
        return self


class ActivatePerspectiveRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        perspective_id: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.perspective_id = perspective_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        return self


class ActivatePerspectiveResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ActivatePerspectiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ActivatePerspectiveResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ActivatePerspectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSynonymRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        core_word_name: str = None,
        synonym: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.core_word_name = core_word_name
        self.synonym = synonym

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        if self.synonym is not None:
            result['Synonym'] = self.synonym
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        if m.get('Synonym') is not None:
            self.synonym = m.get('Synonym')
        return self


class AddSynonymResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddSynonymResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddSynonymResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddSynonymResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppendEntityMemberRequestMember(TeaModel):
    def __init__(
        self,
        member_name: str = None,
        synonyms: List[str] = None,
    ):
        self.member_name = member_name
        self.synonyms = synonyms

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        return self


class AppendEntityMemberRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        apply_type: str = None,
        entity_id: int = None,
        member: AppendEntityMemberRequestMember = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.apply_type = apply_type
        self.entity_id = entity_id
        self.member = member

    def validate(self):
        if self.member:
            self.member.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.apply_type is not None:
            result['ApplyType'] = self.apply_type
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.member is not None:
            result['Member'] = self.member.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ApplyType') is not None:
            self.apply_type = m.get('ApplyType')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('Member') is not None:
            temp_model = AppendEntityMemberRequestMember()
            self.member = temp_model.from_map(m['Member'])
        return self


class AppendEntityMemberShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        apply_type: str = None,
        entity_id: int = None,
        member_shrink: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.apply_type = apply_type
        self.entity_id = entity_id
        self.member_shrink = member_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.apply_type is not None:
            result['ApplyType'] = self.apply_type
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.member_shrink is not None:
            result['Member'] = self.member_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ApplyType') is not None:
            self.apply_type = m.get('ApplyType')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('Member') is not None:
            self.member_shrink = m.get('Member')
        return self


class AppendEntityMemberResponseBody(TeaModel):
    def __init__(
        self,
        entity_id: int = None,
        request_id: str = None,
    ):
        self.entity_id = entity_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppendEntityMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AppendEntityMemberResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AppendEntityMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        perspective: List[str] = None,
        recommend_num: int = None,
        session_id: str = None,
        utterance: str = None,
    ):
        self.agent_key = agent_key
        self.instance_id = instance_id
        self.perspective = perspective
        self.recommend_num = recommend_num
        self.session_id = session_id
        self.utterance = utterance

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.perspective is not None:
            result['Perspective'] = self.perspective
        if self.recommend_num is not None:
            result['RecommendNum'] = self.recommend_num
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Perspective') is not None:
            self.perspective = m.get('Perspective')
        if m.get('RecommendNum') is not None:
            self.recommend_num = m.get('RecommendNum')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        return self


class AssociateResponseBodyAssociate(TeaModel):
    def __init__(
        self,
        title: str = None,
    ):
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class AssociateResponseBody(TeaModel):
    def __init__(
        self,
        associate: List[AssociateResponseBodyAssociate] = None,
        message_id: str = None,
        request_id: str = None,
        session_id: str = None,
    ):
        self.associate = associate
        self.message_id = message_id
        self.request_id = request_id
        self.session_id = session_id

    def validate(self):
        if self.associate:
            for k in self.associate:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Associate'] = []
        if self.associate is not None:
            for k in self.associate:
                result['Associate'].append(k.to_map() if k else None)
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.associate = []
        if m.get('Associate') is not None:
            for k in m.get('Associate'):
                temp_model = AssociateResponseBodyAssociate()
                self.associate.append(temp_model.from_map(k))
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class AssociateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssociateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        intent_name: str = None,
        knowledge_id: str = None,
        perspective: List[str] = None,
        sender_id: str = None,
        sender_nick: str = None,
        session_id: str = None,
        tag: str = None,
        utterance: str = None,
        vendor_param: str = None,
    ):
        self.agent_key = agent_key
        self.instance_id = instance_id
        self.intent_name = intent_name
        self.knowledge_id = knowledge_id
        self.perspective = perspective
        self.sender_id = sender_id
        self.sender_nick = sender_nick
        self.session_id = session_id
        self.tag = tag
        self.utterance = utterance
        self.vendor_param = vendor_param

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.perspective is not None:
            result['Perspective'] = self.perspective
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.sender_nick is not None:
            result['SenderNick'] = self.sender_nick
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        if self.vendor_param is not None:
            result['VendorParam'] = self.vendor_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Perspective') is not None:
            self.perspective = m.get('Perspective')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SenderNick') is not None:
            self.sender_nick = m.get('SenderNick')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        if m.get('VendorParam') is not None:
            self.vendor_param = m.get('VendorParam')
        return self


class ChatResponseBodyMessagesKnowledgeRelatedKnowledges(TeaModel):
    def __init__(
        self,
        knowledge_id: str = None,
        title: str = None,
    ):
        self.knowledge_id = knowledge_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ChatResponseBodyMessagesKnowledge(TeaModel):
    def __init__(
        self,
        answer_source: str = None,
        category: str = None,
        content: str = None,
        content_type: str = None,
        hit_statement: str = None,
        id: str = None,
        related_knowledges: List[ChatResponseBodyMessagesKnowledgeRelatedKnowledges] = None,
        score: float = None,
        summary: str = None,
        title: str = None,
    ):
        self.answer_source = answer_source
        self.category = category
        self.content = content
        self.content_type = content_type
        self.hit_statement = hit_statement
        self.id = id
        self.related_knowledges = related_knowledges
        self.score = score
        self.summary = summary
        self.title = title

    def validate(self):
        if self.related_knowledges:
            for k in self.related_knowledges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_source is not None:
            result['AnswerSource'] = self.answer_source
        if self.category is not None:
            result['Category'] = self.category
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.hit_statement is not None:
            result['HitStatement'] = self.hit_statement
        if self.id is not None:
            result['Id'] = self.id
        result['RelatedKnowledges'] = []
        if self.related_knowledges is not None:
            for k in self.related_knowledges:
                result['RelatedKnowledges'].append(k.to_map() if k else None)
        if self.score is not None:
            result['Score'] = self.score
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('HitStatement') is not None:
            self.hit_statement = m.get('HitStatement')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.related_knowledges = []
        if m.get('RelatedKnowledges') is not None:
            for k in m.get('RelatedKnowledges'):
                temp_model = ChatResponseBodyMessagesKnowledgeRelatedKnowledges()
                self.related_knowledges.append(temp_model.from_map(k))
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ChatResponseBodyMessagesRecommends(TeaModel):
    def __init__(
        self,
        answer_source: str = None,
        knowledge_id: str = None,
        score: float = None,
        title: str = None,
    ):
        self.answer_source = answer_source
        self.knowledge_id = knowledge_id
        self.score = score
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_source is not None:
            result['AnswerSource'] = self.answer_source
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.score is not None:
            result['Score'] = self.score
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ChatResponseBodyMessagesTextSlots(TeaModel):
    def __init__(
        self,
        is_hit: bool = None,
        name: str = None,
        origin: str = None,
        value: str = None,
    ):
        self.is_hit = is_hit
        self.name = name
        self.origin = origin
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_hit is not None:
            result['IsHit'] = self.is_hit
        if self.name is not None:
            result['Name'] = self.name
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsHit') is not None:
            self.is_hit = m.get('IsHit')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ChatResponseBodyMessagesText(TeaModel):
    def __init__(
        self,
        answer_source: str = None,
        article_title: str = None,
        commands: Dict[str, Any] = None,
        content: str = None,
        content_type: str = None,
        dialog_name: str = None,
        ext: Dict[str, Any] = None,
        external_flags: Dict[str, Any] = None,
        hit_statement: str = None,
        intent_name: str = None,
        meta_data: str = None,
        node_id: str = None,
        node_name: str = None,
        score: float = None,
        slots: List[ChatResponseBodyMessagesTextSlots] = None,
        user_defined_chat_title: str = None,
    ):
        self.answer_source = answer_source
        self.article_title = article_title
        self.commands = commands
        self.content = content
        self.content_type = content_type
        self.dialog_name = dialog_name
        self.ext = ext
        self.external_flags = external_flags
        self.hit_statement = hit_statement
        self.intent_name = intent_name
        self.meta_data = meta_data
        self.node_id = node_id
        self.node_name = node_name
        self.score = score
        self.slots = slots
        self.user_defined_chat_title = user_defined_chat_title

    def validate(self):
        if self.slots:
            for k in self.slots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_source is not None:
            result['AnswerSource'] = self.answer_source
        if self.article_title is not None:
            result['ArticleTitle'] = self.article_title
        if self.commands is not None:
            result['Commands'] = self.commands
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.external_flags is not None:
            result['ExternalFlags'] = self.external_flags
        if self.hit_statement is not None:
            result['HitStatement'] = self.hit_statement
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.meta_data is not None:
            result['MetaData'] = self.meta_data
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.score is not None:
            result['Score'] = self.score
        result['Slots'] = []
        if self.slots is not None:
            for k in self.slots:
                result['Slots'].append(k.to_map() if k else None)
        if self.user_defined_chat_title is not None:
            result['UserDefinedChatTitle'] = self.user_defined_chat_title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        if m.get('ArticleTitle') is not None:
            self.article_title = m.get('ArticleTitle')
        if m.get('Commands') is not None:
            self.commands = m.get('Commands')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('ExternalFlags') is not None:
            self.external_flags = m.get('ExternalFlags')
        if m.get('HitStatement') is not None:
            self.hit_statement = m.get('HitStatement')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('MetaData') is not None:
            self.meta_data = m.get('MetaData')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        self.slots = []
        if m.get('Slots') is not None:
            for k in m.get('Slots'):
                temp_model = ChatResponseBodyMessagesTextSlots()
                self.slots.append(temp_model.from_map(k))
        if m.get('UserDefinedChatTitle') is not None:
            self.user_defined_chat_title = m.get('UserDefinedChatTitle')
        return self


class ChatResponseBodyMessages(TeaModel):
    def __init__(
        self,
        answer_source: str = None,
        answer_type: str = None,
        knowledge: ChatResponseBodyMessagesKnowledge = None,
        recommends: List[ChatResponseBodyMessagesRecommends] = None,
        text: ChatResponseBodyMessagesText = None,
        title: str = None,
        type: str = None,
        voice_title: str = None,
    ):
        self.answer_source = answer_source
        self.answer_type = answer_type
        self.knowledge = knowledge
        self.recommends = recommends
        self.text = text
        # 在线场景，反问标题
        self.title = title
        self.type = type
        # 语音场景，澄清内容
        self.voice_title = voice_title

    def validate(self):
        if self.knowledge:
            self.knowledge.validate()
        if self.recommends:
            for k in self.recommends:
                if k:
                    k.validate()
        if self.text:
            self.text.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_source is not None:
            result['AnswerSource'] = self.answer_source
        if self.answer_type is not None:
            result['AnswerType'] = self.answer_type
        if self.knowledge is not None:
            result['Knowledge'] = self.knowledge.to_map()
        result['Recommends'] = []
        if self.recommends is not None:
            for k in self.recommends:
                result['Recommends'].append(k.to_map() if k else None)
        if self.text is not None:
            result['Text'] = self.text.to_map()
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.voice_title is not None:
            result['VoiceTitle'] = self.voice_title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        if m.get('AnswerType') is not None:
            self.answer_type = m.get('AnswerType')
        if m.get('Knowledge') is not None:
            temp_model = ChatResponseBodyMessagesKnowledge()
            self.knowledge = temp_model.from_map(m['Knowledge'])
        self.recommends = []
        if m.get('Recommends') is not None:
            for k in m.get('Recommends'):
                temp_model = ChatResponseBodyMessagesRecommends()
                self.recommends.append(temp_model.from_map(k))
        if m.get('Text') is not None:
            temp_model = ChatResponseBodyMessagesText()
            self.text = temp_model.from_map(m['Text'])
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VoiceTitle') is not None:
            self.voice_title = m.get('VoiceTitle')
        return self


class ChatResponseBody(TeaModel):
    def __init__(
        self,
        message_id: str = None,
        messages: List[ChatResponseBodyMessages] = None,
        request_id: str = None,
        session_id: str = None,
        tag: str = None,
    ):
        self.message_id = message_id
        self.messages = messages
        self.request_id = request_id
        self.session_id = session_id
        self.tag = tag

    def validate(self):
        if self.messages:
            for k in self.messages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        result['Messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['Messages'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        self.messages = []
        if m.get('Messages') is not None:
            for k in m.get('Messages'):
                temp_model = ChatResponseBodyMessages()
                self.messages.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class ChatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChatResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBotRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        avatar: str = None,
        introduction: str = None,
        language_code: str = None,
        name: str = None,
        robot_type: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.avatar = avatar
        self.introduction = introduction
        self.language_code = language_code
        self.name = name
        self.robot_type = robot_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.language_code is not None:
            result['LanguageCode'] = self.language_code
        if self.name is not None:
            result['Name'] = self.name
        if self.robot_type is not None:
            result['RobotType'] = self.robot_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RobotType') is not None:
            self.robot_type = m.get('RobotType')
        return self


class CreateBotResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
    ):
        self.instance_id = instance_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateBotResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateBotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCategoryRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        biz_code: str = None,
        knowledge_type: int = None,
        name: str = None,
        parent_category_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.biz_code = biz_code
        self.knowledge_type = knowledge_type
        self.name = name
        self.parent_category_id = parent_category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.knowledge_type is not None:
            result['KnowledgeType'] = self.knowledge_type
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('KnowledgeType') is not None:
            self.knowledge_type = m.get('KnowledgeType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        return self


class CreateCategoryResponseBody(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.category_id = category_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCategoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCoreWordRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        core_word_name: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.core_word_name = core_word_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        return self


class CreateCoreWordResponseBody(TeaModel):
    def __init__(
        self,
        core_word_code: str = None,
        request_id: str = None,
    ):
        self.core_word_code = core_word_code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.core_word_code is not None:
            result['CoreWordCode'] = self.core_word_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoreWordCode') is not None:
            self.core_word_code = m.get('CoreWordCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCoreWordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCoreWordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCoreWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDialogRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        description: str = None,
        dialog_name: str = None,
        instance_id: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.description = description
        self.dialog_name = dialog_name
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.description is not None:
            result['Description'] = self.description
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateDialogResponseBody(TeaModel):
    def __init__(
        self,
        dialog_id: int = None,
        request_id: str = None,
    ):
        self.dialog_id = dialog_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDialogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDialogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDialogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEntityRequestMembers(TeaModel):
    def __init__(
        self,
        member_name: str = None,
        synonyms: List[str] = None,
    ):
        self.member_name = member_name
        self.synonyms = synonyms

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        return self


class CreateEntityRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        dialog_id: int = None,
        entity_name: str = None,
        entity_type: str = None,
        members: List[CreateEntityRequestMembers] = None,
        regex: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.dialog_id = dialog_id
        self.entity_name = entity_name
        self.entity_type = entity_type
        self.members = members
        self.regex = regex

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.regex is not None:
            result['Regex'] = self.regex
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = CreateEntityRequestMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        return self


class CreateEntityShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        dialog_id: int = None,
        entity_name: str = None,
        entity_type: str = None,
        members_shrink: str = None,
        regex: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.dialog_id = dialog_id
        self.entity_name = entity_name
        self.entity_type = entity_type
        self.members_shrink = members_shrink
        self.regex = regex

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.members_shrink is not None:
            result['Members'] = self.members_shrink
        if self.regex is not None:
            result['Regex'] = self.regex
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Members') is not None:
            self.members_shrink = m.get('Members')
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        return self


class CreateEntityResponseBody(TeaModel):
    def __init__(
        self,
        entity_id: int = None,
        request_id: str = None,
    ):
        self.entity_id = entity_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateEntityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIntentRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        dialog_id: int = None,
        intent_definition: IntentCreateDTO = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.dialog_id = dialog_id
        self.intent_definition = intent_definition

    def validate(self):
        if self.intent_definition:
            self.intent_definition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.intent_definition is not None:
            result['IntentDefinition'] = self.intent_definition.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('IntentDefinition') is not None:
            temp_model = IntentCreateDTO()
            self.intent_definition = temp_model.from_map(m['IntentDefinition'])
        return self


class CreateIntentShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        dialog_id: int = None,
        intent_definition_shrink: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.dialog_id = dialog_id
        self.intent_definition_shrink = intent_definition_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.intent_definition_shrink is not None:
            result['IntentDefinition'] = self.intent_definition_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('IntentDefinition') is not None:
            self.intent_definition_shrink = m.get('IntentDefinition')
        return self


class CreateIntentResponseBody(TeaModel):
    def __init__(
        self,
        intent_id: int = None,
        request_id: str = None,
    ):
        self.intent_id = intent_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateIntentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateIntentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateKnowledgeRequestKnowledgeOutlines(TeaModel):
    def __init__(
        self,
        knowledge_id: int = None,
        outline_id: int = None,
        title: str = None,
    ):
        self.knowledge_id = knowledge_id
        self.outline_id = outline_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.outline_id is not None:
            result['OutlineId'] = self.outline_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('OutlineId') is not None:
            self.outline_id = m.get('OutlineId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateKnowledgeRequestKnowledgeSimQuestions(TeaModel):
    def __init__(
        self,
        title: str = None,
    ):
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateKnowledgeRequestKnowledgeSolutions(TeaModel):
    def __init__(
        self,
        content: str = None,
        perspective_ids: List[str] = None,
        plain_text: str = None,
    ):
        self.content = content
        self.perspective_ids = perspective_ids
        self.plain_text = plain_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.perspective_ids is not None:
            result['PerspectiveIds'] = self.perspective_ids
        if self.plain_text is not None:
            result['PlainText'] = self.plain_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('PerspectiveIds') is not None:
            self.perspective_ids = m.get('PerspectiveIds')
        if m.get('PlainText') is not None:
            self.plain_text = m.get('PlainText')
        return self


class CreateKnowledgeRequestKnowledge(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        end_date: str = None,
        knowledge_title: str = None,
        knowledge_type: int = None,
        outlines: List[CreateKnowledgeRequestKnowledgeOutlines] = None,
        sim_questions: List[CreateKnowledgeRequestKnowledgeSimQuestions] = None,
        solutions: List[CreateKnowledgeRequestKnowledgeSolutions] = None,
        start_date: str = None,
    ):
        self.category_id = category_id
        self.end_date = end_date
        self.knowledge_title = knowledge_title
        self.knowledge_type = knowledge_type
        self.outlines = outlines
        self.sim_questions = sim_questions
        self.solutions = solutions
        self.start_date = start_date

    def validate(self):
        if self.outlines:
            for k in self.outlines:
                if k:
                    k.validate()
        if self.sim_questions:
            for k in self.sim_questions:
                if k:
                    k.validate()
        if self.solutions:
            for k in self.solutions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.knowledge_title is not None:
            result['KnowledgeTitle'] = self.knowledge_title
        if self.knowledge_type is not None:
            result['KnowledgeType'] = self.knowledge_type
        result['Outlines'] = []
        if self.outlines is not None:
            for k in self.outlines:
                result['Outlines'].append(k.to_map() if k else None)
        result['SimQuestions'] = []
        if self.sim_questions is not None:
            for k in self.sim_questions:
                result['SimQuestions'].append(k.to_map() if k else None)
        result['Solutions'] = []
        if self.solutions is not None:
            for k in self.solutions:
                result['Solutions'].append(k.to_map() if k else None)
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('KnowledgeTitle') is not None:
            self.knowledge_title = m.get('KnowledgeTitle')
        if m.get('KnowledgeType') is not None:
            self.knowledge_type = m.get('KnowledgeType')
        self.outlines = []
        if m.get('Outlines') is not None:
            for k in m.get('Outlines'):
                temp_model = CreateKnowledgeRequestKnowledgeOutlines()
                self.outlines.append(temp_model.from_map(k))
        self.sim_questions = []
        if m.get('SimQuestions') is not None:
            for k in m.get('SimQuestions'):
                temp_model = CreateKnowledgeRequestKnowledgeSimQuestions()
                self.sim_questions.append(temp_model.from_map(k))
        self.solutions = []
        if m.get('Solutions') is not None:
            for k in m.get('Solutions'):
                temp_model = CreateKnowledgeRequestKnowledgeSolutions()
                self.solutions.append(temp_model.from_map(k))
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class CreateKnowledgeRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge: CreateKnowledgeRequestKnowledge = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.knowledge = knowledge

    def validate(self):
        if self.knowledge:
            self.knowledge.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge is not None:
            result['Knowledge'] = self.knowledge.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Knowledge') is not None:
            temp_model = CreateKnowledgeRequestKnowledge()
            self.knowledge = temp_model.from_map(m['Knowledge'])
        return self


class CreateKnowledgeShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge_shrink: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.knowledge_shrink = knowledge_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_shrink is not None:
            result['Knowledge'] = self.knowledge_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Knowledge') is not None:
            self.knowledge_shrink = m.get('Knowledge')
        return self


class CreateKnowledgeResponseBody(TeaModel):
    def __init__(
        self,
        knowledge_id: int = None,
        request_id: str = None,
    ):
        self.knowledge_id = knowledge_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateKnowledgeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateKnowledgeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePerspectiveRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        name: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreatePerspectiveResponseBody(TeaModel):
    def __init__(
        self,
        perspective_id: str = None,
        request_id: str = None,
    ):
        self.perspective_id = perspective_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePerspectiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePerspectiveResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePerspectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBotRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteBotResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteBotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteBotResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteBotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCategoryRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        category_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.category_id = category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        return self


class DeleteCategoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCategoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCoreWordRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        core_word_name: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.core_word_name = core_word_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        return self


class DeleteCoreWordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteCoreWordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCoreWordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCoreWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDialogRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        dialog_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.dialog_id = dialog_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        return self


class DeleteDialogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDialogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDialogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDialogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEntityRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        entity_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.entity_id = entity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        return self


class DeleteEntityResponseBody(TeaModel):
    def __init__(
        self,
        entity_id: int = None,
        request_id: str = None,
    ):
        self.entity_id = entity_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEntityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIntentRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        intent_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.intent_id = intent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class DeleteIntentResponseBody(TeaModel):
    def __init__(
        self,
        intent_id: int = None,
        request_id: str = None,
    ):
        self.intent_id = intent_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteIntentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteIntentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteKnowledgeRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.knowledge_id = knowledge_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class DeleteKnowledgeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteKnowledgeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteKnowledgeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePerspectiveRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        perspective_id: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.perspective_id = perspective_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        return self


class DeletePerspectiveResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeletePerspectiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePerspectiveResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePerspectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBotRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeBotResponseBodyCategories(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        name: str = None,
        parent_category_id: int = None,
    ):
        self.category_id = category_id
        self.name = name
        self.parent_category_id = parent_category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        return self


class DescribeBotResponseBody(TeaModel):
    def __init__(
        self,
        avatar: str = None,
        categories: List[DescribeBotResponseBodyCategories] = None,
        create_time: str = None,
        instance_id: str = None,
        introduction: str = None,
        language_code: str = None,
        logo: str = None,
        name: str = None,
        request_id: str = None,
        time_zone: str = None,
    ):
        self.avatar = avatar
        self.categories = categories
        self.create_time = create_time
        self.instance_id = instance_id
        self.introduction = introduction
        self.language_code = language_code
        self.logo = logo
        self.name = name
        self.request_id = request_id
        self.time_zone = time_zone

    def validate(self):
        if self.categories:
            for k in self.categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        result['Categories'] = []
        if self.categories is not None:
            for k in self.categories:
                result['Categories'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.language_code is not None:
            result['LanguageCode'] = self.language_code
        if self.logo is not None:
            result['Logo'] = self.logo
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        self.categories = []
        if m.get('Categories') is not None:
            for k in m.get('Categories'):
                temp_model = DescribeBotResponseBodyCategories()
                self.categories.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')
        if m.get('Logo') is not None:
            self.logo = m.get('Logo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        return self


class DescribeBotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBotResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeBotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCategoryRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        category_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.category_id = category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        return self


class DescribeCategoryResponseBody(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        name: str = None,
        parent_category_id: int = None,
        request_id: str = None,
    ):
        self.category_id = category_id
        self.name = name
        self.parent_category_id = parent_category_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCategoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCoreWordRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        core_word_name: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.core_word_name = core_word_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        return self


class DescribeCoreWordResponseBody(TeaModel):
    def __init__(
        self,
        core_word_code: str = None,
        core_word_name: str = None,
        create_time: str = None,
        modify_time: str = None,
        request_id: str = None,
        synonyms: List[str] = None,
    ):
        self.core_word_code = core_word_code
        self.core_word_name = core_word_name
        self.create_time = create_time
        self.modify_time = modify_time
        self.request_id = request_id
        self.synonyms = synonyms

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.core_word_code is not None:
            result['CoreWordCode'] = self.core_word_code
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoreWordCode') is not None:
            self.core_word_code = m.get('CoreWordCode')
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        return self


class DescribeCoreWordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCoreWordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCoreWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDialogRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        dialog_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.dialog_id = dialog_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        return self


class DescribeDialogResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_user_id: str = None,
        create_user_name: str = None,
        description: str = None,
        dialog_id: int = None,
        dialog_name: str = None,
        is_online: bool = None,
        is_sample_dialog: bool = None,
        modify_time: str = None,
        modify_user_id: str = None,
        modify_user_name: str = None,
        request_id: str = None,
        status: int = None,
    ):
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.description = description
        self.dialog_id = dialog_id
        self.dialog_name = dialog_name
        self.is_online = is_online
        self.is_sample_dialog = is_sample_dialog
        self.modify_time = modify_time
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.description is not None:
            result['Description'] = self.description
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.is_online is not None:
            result['IsOnline'] = self.is_online
        if self.is_sample_dialog is not None:
            result['IsSampleDialog'] = self.is_sample_dialog
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('IsOnline') is not None:
            self.is_online = m.get('IsOnline')
        if m.get('IsSampleDialog') is not None:
            self.is_sample_dialog = m.get('IsSampleDialog')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDialogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDialogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDialogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDialogFlowRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        dialog_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.dialog_id = dialog_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        return self


class DescribeDialogFlowResponseBody(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        create_time: str = None,
        create_user_id: str = None,
        create_user_name: str = None,
        dialog_id: int = None,
        dialog_name: str = None,
        global_vars: Dict[str, Any] = None,
        instance_id: str = None,
        modify_time: str = None,
        modify_user_id: str = None,
        modify_user_name: str = None,
        module_definition: PaasProcessData = None,
        module_id: int = None,
        module_name: str = None,
        request_id: str = None,
        status: int = None,
        tags: str = None,
        templates: str = None,
    ):
        self.account_id = account_id
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.dialog_id = dialog_id
        self.dialog_name = dialog_name
        self.global_vars = global_vars
        self.instance_id = instance_id
        self.modify_time = modify_time
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.module_definition = module_definition
        self.module_id = module_id
        self.module_name = module_name
        self.request_id = request_id
        self.status = status
        self.tags = tags
        self.templates = templates

    def validate(self):
        if self.module_definition:
            self.module_definition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.global_vars is not None:
            result['GlobalVars'] = self.global_vars
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.module_definition is not None:
            result['ModuleDefinition'] = self.module_definition.to_map()
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.templates is not None:
            result['Templates'] = self.templates
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('GlobalVars') is not None:
            self.global_vars = m.get('GlobalVars')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('ModuleDefinition') is not None:
            temp_model = PaasProcessData()
            self.module_definition = temp_model.from_map(m['ModuleDefinition'])
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Templates') is not None:
            self.templates = m.get('Templates')
        return self


class DescribeDialogFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDialogFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDialogFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEntitiesRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        entity_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.entity_id = entity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        return self


class DescribeEntitiesResponseBodyMembers(TeaModel):
    def __init__(
        self,
        member_name: str = None,
        synonyms: List[str] = None,
    ):
        self.member_name = member_name
        self.synonyms = synonyms

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        return self


class DescribeEntitiesResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_user_id: str = None,
        create_user_name: str = None,
        entity_id: int = None,
        entity_name: str = None,
        entity_type: str = None,
        members: List[DescribeEntitiesResponseBodyMembers] = None,
        modify_time: str = None,
        modify_user_id: str = None,
        modify_user_name: str = None,
        regex: str = None,
        request_id: str = None,
    ):
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.entity_id = entity_id
        self.entity_name = entity_name
        self.entity_type = entity_type
        self.members = members
        self.modify_time = modify_time
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.regex = regex
        self.request_id = request_id

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.regex is not None:
            result['Regex'] = self.regex
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = DescribeEntitiesResponseBodyMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEntitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEntitiesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIntentRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        intent_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.intent_id = intent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class DescribeIntentResponseBodyRuleCheck(TeaModel):
    def __init__(
        self,
        error: List[str] = None,
        strict: bool = None,
        text: str = None,
        warning: List[str] = None,
    ):
        self.error = error
        self.strict = strict
        self.text = text
        self.warning = warning

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeIntentResponseBodySlotTags(TeaModel):
    def __init__(
        self,
        user_say_id: str = None,
        value: str = None,
    ):
        self.user_say_id = user_say_id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeIntentResponseBodySlot(TeaModel):
    def __init__(
        self,
        is_array: bool = None,
        is_necessary: bool = None,
        life_span: int = None,
        name: str = None,
        question: List[str] = None,
        slot_id: str = None,
        tags: List[DescribeIntentResponseBodySlotTags] = None,
        value: str = None,
    ):
        self.is_array = is_array
        self.is_necessary = is_necessary
        self.life_span = life_span
        self.name = name
        self.question = question
        self.slot_id = slot_id
        self.tags = tags
        self.value = value

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_array is not None:
            result['IsArray'] = self.is_array
        if self.is_necessary is not None:
            result['IsNecessary'] = self.is_necessary
        if self.life_span is not None:
            result['LifeSpan'] = self.life_span
        if self.name is not None:
            result['Name'] = self.name
        if self.question is not None:
            result['Question'] = self.question
        if self.slot_id is not None:
            result['SlotId'] = self.slot_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsArray') is not None:
            self.is_array = m.get('IsArray')
        if m.get('IsNecessary') is not None:
            self.is_necessary = m.get('IsNecessary')
        if m.get('LifeSpan') is not None:
            self.life_span = m.get('LifeSpan')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeIntentResponseBodySlotTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeIntentResponseBodyUserSayData(TeaModel):
    def __init__(
        self,
        slot_id: str = None,
        text: str = None,
    ):
        self.slot_id = slot_id
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeIntentResponseBodyUserSay(TeaModel):
    def __init__(
        self,
        data: List[DescribeIntentResponseBodyUserSayData] = None,
        strict: bool = None,
        user_say_id: str = None,
    ):
        self.data = data
        self.strict = strict
        self.user_say_id = user_say_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.strict is not None:
            result['Strict'] = self.strict
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeIntentResponseBodyUserSayData()
                self.data.append(temp_model.from_map(k))
        if m.get('Strict') is not None:
            self.strict = m.get('Strict')
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')
        return self


class DescribeIntentResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_user_id: str = None,
        create_user_name: str = None,
        dialog_id: int = None,
        intent_id: int = None,
        modify_time: str = None,
        modify_user_id: str = None,
        modify_user_name: str = None,
        name: str = None,
        request_id: str = None,
        rule_check: List[DescribeIntentResponseBodyRuleCheck] = None,
        slot: List[DescribeIntentResponseBodySlot] = None,
        type: str = None,
        user_say: List[DescribeIntentResponseBodyUserSay] = None,
    ):
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.dialog_id = dialog_id
        self.intent_id = intent_id
        self.modify_time = modify_time
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.name = name
        self.request_id = request_id
        self.rule_check = rule_check
        self.slot = slot
        self.type = type
        self.user_say = user_say

    def validate(self):
        if self.rule_check:
            for k in self.rule_check:
                if k:
                    k.validate()
        if self.slot:
            for k in self.slot:
                if k:
                    k.validate()
        if self.user_say:
            for k in self.user_say:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RuleCheck'] = []
        if self.rule_check is not None:
            for k in self.rule_check:
                result['RuleCheck'].append(k.to_map() if k else None)
        result['Slot'] = []
        if self.slot is not None:
            for k in self.slot:
                result['Slot'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        result['UserSay'] = []
        if self.user_say is not None:
            for k in self.user_say:
                result['UserSay'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rule_check = []
        if m.get('RuleCheck') is not None:
            for k in m.get('RuleCheck'):
                temp_model = DescribeIntentResponseBodyRuleCheck()
                self.rule_check.append(temp_model.from_map(k))
        self.slot = []
        if m.get('Slot') is not None:
            for k in m.get('Slot'):
                temp_model = DescribeIntentResponseBodySlot()
                self.slot.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        self.user_say = []
        if m.get('UserSay') is not None:
            for k in m.get('UserSay'):
                temp_model = DescribeIntentResponseBodyUserSay()
                self.user_say.append(temp_model.from_map(k))
        return self


class DescribeIntentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeIntentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeKnowledgeRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.knowledge_id = knowledge_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class DescribeKnowledgeResponseBodyOutlines(TeaModel):
    def __init__(
        self,
        knowledge_id: int = None,
        outline_id: int = None,
        title: str = None,
    ):
        self.knowledge_id = knowledge_id
        self.outline_id = outline_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.outline_id is not None:
            result['OutlineId'] = self.outline_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('OutlineId') is not None:
            self.outline_id = m.get('OutlineId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeKnowledgeResponseBodySimQuestions(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        modify_time: str = None,
        sim_question_id: int = None,
        title: str = None,
    ):
        self.create_time = create_time
        self.modify_time = modify_time
        self.sim_question_id = sim_question_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.sim_question_id is not None:
            result['SimQuestionId'] = self.sim_question_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('SimQuestionId') is not None:
            self.sim_question_id = m.get('SimQuestionId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeKnowledgeResponseBodySolutions(TeaModel):
    def __init__(
        self,
        content: str = None,
        create_time: str = None,
        modify_time: str = None,
        perspective_ids: List[str] = None,
        plain_text: str = None,
        solution_id: int = None,
        summary: str = None,
    ):
        self.content = content
        self.create_time = create_time
        self.modify_time = modify_time
        self.perspective_ids = perspective_ids
        self.plain_text = plain_text
        self.solution_id = solution_id
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.perspective_ids is not None:
            result['PerspectiveIds'] = self.perspective_ids
        if self.plain_text is not None:
            result['PlainText'] = self.plain_text
        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('PerspectiveIds') is not None:
            self.perspective_ids = m.get('PerspectiveIds')
        if m.get('PlainText') is not None:
            self.plain_text = m.get('PlainText')
        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class DescribeKnowledgeResponseBody(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        core_words: List[str] = None,
        create_time: str = None,
        create_user_name: str = None,
        end_date: str = None,
        key_words: List[str] = None,
        knowledge_id: int = None,
        knowledge_status: int = None,
        knowledge_title: str = None,
        knowledge_type: int = None,
        modify_time: str = None,
        modify_user_name: str = None,
        outlines: List[DescribeKnowledgeResponseBodyOutlines] = None,
        request_id: str = None,
        sim_questions: List[DescribeKnowledgeResponseBodySimQuestions] = None,
        solutions: List[DescribeKnowledgeResponseBodySolutions] = None,
        start_date: str = None,
        version: int = None,
    ):
        self.category_id = category_id
        self.core_words = core_words
        self.create_time = create_time
        self.create_user_name = create_user_name
        self.end_date = end_date
        self.key_words = key_words
        self.knowledge_id = knowledge_id
        self.knowledge_status = knowledge_status
        self.knowledge_title = knowledge_title
        self.knowledge_type = knowledge_type
        self.modify_time = modify_time
        self.modify_user_name = modify_user_name
        self.outlines = outlines
        self.request_id = request_id
        self.sim_questions = sim_questions
        self.solutions = solutions
        self.start_date = start_date
        self.version = version

    def validate(self):
        if self.outlines:
            for k in self.outlines:
                if k:
                    k.validate()
        if self.sim_questions:
            for k in self.sim_questions:
                if k:
                    k.validate()
        if self.solutions:
            for k in self.solutions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.core_words is not None:
            result['CoreWords'] = self.core_words
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.key_words is not None:
            result['KeyWords'] = self.key_words
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.knowledge_status is not None:
            result['KnowledgeStatus'] = self.knowledge_status
        if self.knowledge_title is not None:
            result['KnowledgeTitle'] = self.knowledge_title
        if self.knowledge_type is not None:
            result['KnowledgeType'] = self.knowledge_type
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        result['Outlines'] = []
        if self.outlines is not None:
            for k in self.outlines:
                result['Outlines'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SimQuestions'] = []
        if self.sim_questions is not None:
            for k in self.sim_questions:
                result['SimQuestions'].append(k.to_map() if k else None)
        result['Solutions'] = []
        if self.solutions is not None:
            for k in self.solutions:
                result['Solutions'].append(k.to_map() if k else None)
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CoreWords') is not None:
            self.core_words = m.get('CoreWords')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('KnowledgeStatus') is not None:
            self.knowledge_status = m.get('KnowledgeStatus')
        if m.get('KnowledgeTitle') is not None:
            self.knowledge_title = m.get('KnowledgeTitle')
        if m.get('KnowledgeType') is not None:
            self.knowledge_type = m.get('KnowledgeType')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        self.outlines = []
        if m.get('Outlines') is not None:
            for k in m.get('Outlines'):
                temp_model = DescribeKnowledgeResponseBodyOutlines()
                self.outlines.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sim_questions = []
        if m.get('SimQuestions') is not None:
            for k in m.get('SimQuestions'):
                temp_model = DescribeKnowledgeResponseBodySimQuestions()
                self.sim_questions.append(temp_model.from_map(k))
        self.solutions = []
        if m.get('Solutions') is not None:
            for k in m.get('Solutions'):
                temp_model = DescribeKnowledgeResponseBodySolutions()
                self.solutions.append(temp_model.from_map(k))
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeKnowledgeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeKnowledgeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePerspectiveRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        perspective_id: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.perspective_id = perspective_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        return self


class DescribePerspectiveResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_user_name: str = None,
        modify_time: str = None,
        modify_user_name: str = None,
        name: str = None,
        perspective_code: str = None,
        perspective_id: str = None,
        request_id: str = None,
        self_define: bool = None,
        status: int = None,
    ):
        self.create_time = create_time
        self.create_user_name = create_user_name
        self.modify_time = modify_time
        self.modify_user_name = modify_user_name
        self.name = name
        self.perspective_code = perspective_code
        self.perspective_id = perspective_id
        self.request_id = request_id
        self.self_define = self_define
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.name is not None:
            result['Name'] = self.name
        if self.perspective_code is not None:
            result['PerspectiveCode'] = self.perspective_code
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.self_define is not None:
            result['SelfDefine'] = self.self_define
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PerspectiveCode') is not None:
            self.perspective_code = m.get('PerspectiveCode')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SelfDefine') is not None:
            self.self_define = m.get('SelfDefine')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribePerspectiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePerspectiveResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePerspectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableDialogFlowRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        dialog_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.dialog_id = dialog_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        return self


class DisableDialogFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableDialogFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableDialogFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableDialogFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableKnowledgeRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.knowledge_id = knowledge_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class DisableKnowledgeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableKnowledgeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableKnowledgeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FeedbackRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        feedback: str = None,
        instance_id: str = None,
        message_id: str = None,
        session_id: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.feedback = feedback
        self.instance_id = instance_id
        self.message_id = message_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class FeedbackResponseBody(TeaModel):
    def __init__(
        self,
        feedback: str = None,
        http_status: int = None,
        message_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.feedback = feedback
        self.http_status = http_status
        self.message_id = message_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.http_status is not None:
            result['HttpStatus'] = self.http_status
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('HttpStatus') is not None:
            self.http_status = m.get('HttpStatus')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FeedbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FeedbackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FeedbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncResultRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        task_id: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetAsyncResultResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAsyncResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAsyncResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAsyncResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBotChatDataRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
        start_time: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetBotChatDataResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        datas: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.cost_time = cost_time
        self.datas = datas
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBotChatDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBotChatDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetBotChatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBotDsStatDataRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
        start_time: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetBotDsStatDataResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        datas: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.cost_time = cost_time
        self.datas = datas
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBotDsStatDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBotDsStatDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetBotDsStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBotKnowledgeStatDataRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
        start_time: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetBotKnowledgeStatDataResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        datas: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.cost_time = cost_time
        self.datas = datas
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBotKnowledgeStatDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBotKnowledgeStatDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetBotKnowledgeStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBotSessionDataRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
        start_time: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetBotSessionDataResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        datas: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.cost_time = cost_time
        self.datas = datas
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBotSessionDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBotSessionDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetBotSessionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConversationListRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        end_date: str = None,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        sender_id: str = None,
        session_id: str = None,
        start_date: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.end_date = end_date
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.sender_id = sender_id
        self.session_id = session_id
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class GetConversationListResponseBody(TeaModel):
    def __init__(
        self,
        messages: List[Dict[str, Any]] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_counts: int = None,
    ):
        self.messages = messages
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_counts = total_counts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.messages is not None:
            result['Messages'] = self.messages
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Messages') is not None:
            self.messages = m.get('Messages')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')
        return self


class GetConversationListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConversationListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetConversationListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotChatHistorysRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        end_time: str = None,
        limit: int = None,
        robot_instance_id: str = None,
        start_time: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.end_time = end_time
        self.limit = limit
        self.robot_instance_id = robot_instance_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListBotChatHistorysResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        datas: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.cost_time = cost_time
        self.datas = datas
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBotChatHistorysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBotChatHistorysResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListBotChatHistorysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotColdDsDatasRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        end_time: str = None,
        limit: int = None,
        robot_instance_id: str = None,
        start_time: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.end_time = end_time
        self.limit = limit
        self.robot_instance_id = robot_instance_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListBotColdDsDatasResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        datas: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.cost_time = cost_time
        self.datas = datas
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBotColdDsDatasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBotColdDsDatasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListBotColdDsDatasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotColdKnowledgesRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        end_time: str = None,
        limit: int = None,
        robot_instance_id: str = None,
        start_time: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.end_time = end_time
        self.limit = limit
        self.robot_instance_id = robot_instance_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListBotColdKnowledgesResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        datas: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.cost_time = cost_time
        self.datas = datas
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBotColdKnowledgesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBotColdKnowledgesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListBotColdKnowledgesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotDsDetailsRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        end_time: str = None,
        limit: int = None,
        robot_instance_id: str = None,
        start_time: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.end_time = end_time
        self.limit = limit
        self.robot_instance_id = robot_instance_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListBotDsDetailsResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        datas: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.cost_time = cost_time
        self.datas = datas
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBotDsDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBotDsDetailsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListBotDsDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotHotDsDatasRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        end_time: str = None,
        limit: int = None,
        robot_instance_id: str = None,
        start_time: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.end_time = end_time
        self.limit = limit
        self.robot_instance_id = robot_instance_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListBotHotDsDatasResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        datas: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.cost_time = cost_time
        self.datas = datas
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBotHotDsDatasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBotHotDsDatasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListBotHotDsDatasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotHotKnowledgesRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        end_time: str = None,
        limit: int = None,
        robot_instance_id: str = None,
        start_time: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.end_time = end_time
        self.limit = limit
        self.robot_instance_id = robot_instance_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListBotHotKnowledgesResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        datas: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.cost_time = cost_time
        self.datas = datas
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBotHotKnowledgesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBotHotKnowledgesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListBotHotKnowledgesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotKnowledgeDetailsRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        end_time: str = None,
        limit: str = None,
        robot_instance_id: str = None,
        start_time: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.end_time = end_time
        self.limit = limit
        self.robot_instance_id = robot_instance_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListBotKnowledgeDetailsResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        datas: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.cost_time = cost_time
        self.datas = datas
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBotKnowledgeDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBotKnowledgeDetailsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListBotKnowledgeDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotReceptionDetailDatasRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
        start_time: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListBotReceptionDetailDatasResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        datas: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.cost_time = cost_time
        self.datas = datas
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.datas is not None:
            result['Datas'] = self.datas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBotReceptionDetailDatasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBotReceptionDetailDatasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListBotReceptionDetailDatasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConversationLogsRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        session_id: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class ListConversationLogsResponseBody(TeaModel):
    def __init__(
        self,
        chat_logs: List[Dict[str, Any]] = None,
        request_id: str = None,
        rounds: int = None,
    ):
        self.chat_logs = chat_logs
        self.request_id = request_id
        self.rounds = rounds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chat_logs is not None:
            result['ChatLogs'] = self.chat_logs
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rounds is not None:
            result['Rounds'] = self.rounds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChatLogs') is not None:
            self.chat_logs = m.get('ChatLogs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rounds') is not None:
            self.rounds = m.get('Rounds')
        return self


class ListConversationLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListConversationLogsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListConversationLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveKnowledgeCategoryRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        category_id: int = None,
        knowledge_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.category_id = category_id
        self.knowledge_id = knowledge_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class MoveKnowledgeCategoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MoveKnowledgeCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MoveKnowledgeCategoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MoveKnowledgeCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishDialogFlowRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        dialog_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.dialog_id = dialog_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        return self


class PublishDialogFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PublishDialogFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishDialogFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PublishDialogFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishKnowledgeRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        async_: bool = None,
        knowledge_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.async_ = async_
        self.knowledge_id = knowledge_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class PublishKnowledgeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PublishKnowledgeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishKnowledgeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PublishKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBotsRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryBotsResponseBodyBots(TeaModel):
    def __init__(
        self,
        avatar: str = None,
        create_time: str = None,
        instance_id: str = None,
        introduction: str = None,
        language_code: str = None,
        name: str = None,
        time_zone: str = None,
    ):
        self.avatar = avatar
        self.create_time = create_time
        self.instance_id = instance_id
        self.introduction = introduction
        self.language_code = language_code
        self.name = name
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.language_code is not None:
            result['LanguageCode'] = self.language_code
        if self.name is not None:
            result['Name'] = self.name
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        return self


class QueryBotsResponseBody(TeaModel):
    def __init__(
        self,
        bots: List[QueryBotsResponseBodyBots] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.bots = bots
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.bots:
            for k in self.bots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bots'] = []
        if self.bots is not None:
            for k in self.bots:
                result['Bots'].append(k.to_map() if k else None)
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
        self.bots = []
        if m.get('Bots') is not None:
            for k in m.get('Bots'):
                temp_model = QueryBotsResponseBodyBots()
                self.bots.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryBotsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryBotsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryBotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCategoriesRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge_type: int = None,
        parent_category_id: int = None,
        show_childrens: bool = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.knowledge_type = knowledge_type
        self.parent_category_id = parent_category_id
        self.show_childrens = show_childrens

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_type is not None:
            result['KnowledgeType'] = self.knowledge_type
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        if self.show_childrens is not None:
            result['ShowChildrens'] = self.show_childrens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('KnowledgeType') is not None:
            self.knowledge_type = m.get('KnowledgeType')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        if m.get('ShowChildrens') is not None:
            self.show_childrens = m.get('ShowChildrens')
        return self


class QueryCategoriesResponseBody(TeaModel):
    def __init__(
        self,
        categories: List[Children] = None,
        request_id: str = None,
    ):
        self.categories = categories
        self.request_id = request_id

    def validate(self):
        if self.categories:
            for k in self.categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Categories'] = []
        if self.categories is not None:
            for k in self.categories:
                result['Categories'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.categories = []
        if m.get('Categories') is not None:
            for k in m.get('Categories'):
                temp_model = Children()
                self.categories.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryCategoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCategoriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryCategoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCoreWordsRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        core_word_name: str = None,
        page_number: int = None,
        page_size: int = None,
        synonym: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.core_word_name = core_word_name
        self.page_number = page_number
        self.page_size = page_size
        self.synonym = synonym

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.synonym is not None:
            result['Synonym'] = self.synonym
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Synonym') is not None:
            self.synonym = m.get('Synonym')
        return self


class QueryCoreWordsResponseBodyCoreWords(TeaModel):
    def __init__(
        self,
        core_word_code: str = None,
        core_word_name: str = None,
        create_time: str = None,
        modify_time: str = None,
        synonyms: List[str] = None,
    ):
        self.core_word_code = core_word_code
        self.core_word_name = core_word_name
        self.create_time = create_time
        self.modify_time = modify_time
        self.synonyms = synonyms

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.core_word_code is not None:
            result['CoreWordCode'] = self.core_word_code
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoreWordCode') is not None:
            self.core_word_code = m.get('CoreWordCode')
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        return self


class QueryCoreWordsResponseBody(TeaModel):
    def __init__(
        self,
        core_words: List[QueryCoreWordsResponseBodyCoreWords] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.core_words = core_words
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.core_words:
            for k in self.core_words:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CoreWords'] = []
        if self.core_words is not None:
            for k in self.core_words:
                result['CoreWords'].append(k.to_map() if k else None)
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
        self.core_words = []
        if m.get('CoreWords') is not None:
            for k in m.get('CoreWords'):
                temp_model = QueryCoreWordsResponseBodyCoreWords()
                self.core_words.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryCoreWordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCoreWordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryCoreWordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDialogsRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        dialog_name: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.dialog_name = dialog_name
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryDialogsResponseBodyDialogs(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_user_id: str = None,
        create_user_name: str = None,
        description: str = None,
        dialog_id: int = None,
        dialog_name: str = None,
        is_online: bool = None,
        is_sample_dialog: bool = None,
        modify_time: str = None,
        modify_user_id: str = None,
        modify_user_name: str = None,
        status: int = None,
    ):
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.description = description
        self.dialog_id = dialog_id
        self.dialog_name = dialog_name
        self.is_online = is_online
        self.is_sample_dialog = is_sample_dialog
        self.modify_time = modify_time
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.description is not None:
            result['Description'] = self.description
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.is_online is not None:
            result['IsOnline'] = self.is_online
        if self.is_sample_dialog is not None:
            result['IsSampleDialog'] = self.is_sample_dialog
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('IsOnline') is not None:
            self.is_online = m.get('IsOnline')
        if m.get('IsSampleDialog') is not None:
            self.is_sample_dialog = m.get('IsSampleDialog')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryDialogsResponseBody(TeaModel):
    def __init__(
        self,
        dialogs: List[QueryDialogsResponseBodyDialogs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.dialogs = dialogs
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.dialogs:
            for k in self.dialogs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Dialogs'] = []
        if self.dialogs is not None:
            for k in self.dialogs:
                result['Dialogs'].append(k.to_map() if k else None)
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
        self.dialogs = []
        if m.get('Dialogs') is not None:
            for k in m.get('Dialogs'):
                temp_model = QueryDialogsResponseBodyDialogs()
                self.dialogs.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryDialogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDialogsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryDialogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEntitiesRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        dialog_id: int = None,
        entity_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.dialog_id = dialog_id
        self.entity_name = entity_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryEntitiesResponseBodyEntitiesMembers(TeaModel):
    def __init__(
        self,
        member_name: str = None,
        synonyms: List[str] = None,
    ):
        self.member_name = member_name
        self.synonyms = synonyms

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        return self


class QueryEntitiesResponseBodyEntities(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_user_id: str = None,
        create_user_name: str = None,
        entity_id: int = None,
        entity_name: str = None,
        entity_type: str = None,
        members: List[QueryEntitiesResponseBodyEntitiesMembers] = None,
        modify_time: str = None,
        modify_user_id: str = None,
        modify_user_name: str = None,
        regex: str = None,
    ):
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.entity_id = entity_id
        self.entity_name = entity_name
        self.entity_type = entity_type
        self.members = members
        self.modify_time = modify_time
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.regex = regex

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.regex is not None:
            result['Regex'] = self.regex
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = QueryEntitiesResponseBodyEntitiesMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        return self


class QueryEntitiesResponseBody(TeaModel):
    def __init__(
        self,
        entities: List[QueryEntitiesResponseBodyEntities] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.entities = entities
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.entities:
            for k in self.entities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Entities'] = []
        if self.entities is not None:
            for k in self.entities:
                result['Entities'].append(k.to_map() if k else None)
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
        self.entities = []
        if m.get('Entities') is not None:
            for k in m.get('Entities'):
                temp_model = QueryEntitiesResponseBodyEntities()
                self.entities.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryEntitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryEntitiesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryIntentsRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        dialog_id: int = None,
        instance_id: str = None,
        intent_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.dialog_id = dialog_id
        # 机器人实例 ID
        self.instance_id = instance_id
        self.intent_name = intent_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryIntentsResponseBodyIntentsRuleCheck(TeaModel):
    def __init__(
        self,
        error: List[str] = None,
        strict: bool = None,
        text: str = None,
        warning: List[str] = None,
    ):
        self.error = error
        self.strict = strict
        self.text = text
        self.warning = warning

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class QueryIntentsResponseBodyIntentsSlotTags(TeaModel):
    def __init__(
        self,
        user_say_id: str = None,
        value: str = None,
    ):
        self.user_say_id = user_say_id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class QueryIntentsResponseBodyIntentsSlot(TeaModel):
    def __init__(
        self,
        is_array: bool = None,
        is_necessary: bool = None,
        life_span: int = None,
        name: str = None,
        question: List[str] = None,
        slot_id: str = None,
        tags: List[QueryIntentsResponseBodyIntentsSlotTags] = None,
        value: str = None,
    ):
        self.is_array = is_array
        self.is_necessary = is_necessary
        self.life_span = life_span
        self.name = name
        self.question = question
        self.slot_id = slot_id
        self.tags = tags
        self.value = value

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_array is not None:
            result['IsArray'] = self.is_array
        if self.is_necessary is not None:
            result['IsNecessary'] = self.is_necessary
        if self.life_span is not None:
            result['LifeSpan'] = self.life_span
        if self.name is not None:
            result['Name'] = self.name
        if self.question is not None:
            result['Question'] = self.question
        if self.slot_id is not None:
            result['SlotId'] = self.slot_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsArray') is not None:
            self.is_array = m.get('IsArray')
        if m.get('IsNecessary') is not None:
            self.is_necessary = m.get('IsNecessary')
        if m.get('LifeSpan') is not None:
            self.life_span = m.get('LifeSpan')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = QueryIntentsResponseBodyIntentsSlotTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryIntentsResponseBodyIntentsUserSayData(TeaModel):
    def __init__(
        self,
        slot_id: str = None,
        text: str = None,
    ):
        self.slot_id = slot_id
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class QueryIntentsResponseBodyIntentsUserSay(TeaModel):
    def __init__(
        self,
        data: List[QueryIntentsResponseBodyIntentsUserSayData] = None,
        strict: bool = None,
        user_say_id: str = None,
    ):
        self.data = data
        self.strict = strict
        self.user_say_id = user_say_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.strict is not None:
            result['Strict'] = self.strict
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryIntentsResponseBodyIntentsUserSayData()
                self.data.append(temp_model.from_map(k))
        if m.get('Strict') is not None:
            self.strict = m.get('Strict')
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')
        return self


class QueryIntentsResponseBodyIntents(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_user_id: str = None,
        create_user_name: str = None,
        intent_id: int = None,
        modify_time: str = None,
        modify_user_id: str = None,
        modify_user_name: str = None,
        name: str = None,
        rule_check: List[QueryIntentsResponseBodyIntentsRuleCheck] = None,
        slot: List[QueryIntentsResponseBodyIntentsSlot] = None,
        user_say: List[QueryIntentsResponseBodyIntentsUserSay] = None,
    ):
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.intent_id = intent_id
        self.modify_time = modify_time
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.name = name
        self.rule_check = rule_check
        self.slot = slot
        self.user_say = user_say

    def validate(self):
        if self.rule_check:
            for k in self.rule_check:
                if k:
                    k.validate()
        if self.slot:
            for k in self.slot:
                if k:
                    k.validate()
        if self.user_say:
            for k in self.user_say:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.name is not None:
            result['Name'] = self.name
        result['RuleCheck'] = []
        if self.rule_check is not None:
            for k in self.rule_check:
                result['RuleCheck'].append(k.to_map() if k else None)
        result['Slot'] = []
        if self.slot is not None:
            for k in self.slot:
                result['Slot'].append(k.to_map() if k else None)
        result['UserSay'] = []
        if self.user_say is not None:
            for k in self.user_say:
                result['UserSay'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.rule_check = []
        if m.get('RuleCheck') is not None:
            for k in m.get('RuleCheck'):
                temp_model = QueryIntentsResponseBodyIntentsRuleCheck()
                self.rule_check.append(temp_model.from_map(k))
        self.slot = []
        if m.get('Slot') is not None:
            for k in m.get('Slot'):
                temp_model = QueryIntentsResponseBodyIntentsSlot()
                self.slot.append(temp_model.from_map(k))
        self.user_say = []
        if m.get('UserSay') is not None:
            for k in m.get('UserSay'):
                temp_model = QueryIntentsResponseBodyIntentsUserSay()
                self.user_say.append(temp_model.from_map(k))
        return self


class QueryIntentsResponseBody(TeaModel):
    def __init__(
        self,
        intents: List[QueryIntentsResponseBodyIntents] = None,
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
            for k in self.intents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Intents'] = []
        if self.intents is not None:
            for k in self.intents:
                result['Intents'].append(k.to_map() if k else None)
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
            for k in m.get('Intents'):
                temp_model = QueryIntentsResponseBodyIntents()
                self.intents.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryIntentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryIntentsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryIntentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryKnowledgesRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        category_id: int = None,
        core_word_name: str = None,
        knowledge_title: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.category_id = category_id
        self.core_word_name = core_word_name
        self.knowledge_title = knowledge_title
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        if self.knowledge_title is not None:
            result['KnowledgeTitle'] = self.knowledge_title
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        if m.get('KnowledgeTitle') is not None:
            self.knowledge_title = m.get('KnowledgeTitle')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryKnowledgesResponseBodyKnowledges(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        core_words: List[str] = None,
        create_time: str = None,
        create_user_name: str = None,
        end_date: str = None,
        knowledge_id: int = None,
        knowledge_status: int = None,
        knowledge_title: str = None,
        modify_time: str = None,
        modify_user_name: str = None,
        start_date: str = None,
        version: str = None,
    ):
        self.category_id = category_id
        self.core_words = core_words
        self.create_time = create_time
        self.create_user_name = create_user_name
        self.end_date = end_date
        self.knowledge_id = knowledge_id
        self.knowledge_status = knowledge_status
        self.knowledge_title = knowledge_title
        self.modify_time = modify_time
        self.modify_user_name = modify_user_name
        self.start_date = start_date
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.core_words is not None:
            result['CoreWords'] = self.core_words
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.knowledge_status is not None:
            result['KnowledgeStatus'] = self.knowledge_status
        if self.knowledge_title is not None:
            result['KnowledgeTitle'] = self.knowledge_title
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CoreWords') is not None:
            self.core_words = m.get('CoreWords')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('KnowledgeStatus') is not None:
            self.knowledge_status = m.get('KnowledgeStatus')
        if m.get('KnowledgeTitle') is not None:
            self.knowledge_title = m.get('KnowledgeTitle')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class QueryKnowledgesResponseBody(TeaModel):
    def __init__(
        self,
        knowledges: List[QueryKnowledgesResponseBodyKnowledges] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.knowledges = knowledges
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.knowledges:
            for k in self.knowledges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Knowledges'] = []
        if self.knowledges is not None:
            for k in self.knowledges:
                result['Knowledges'].append(k.to_map() if k else None)
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
        self.knowledges = []
        if m.get('Knowledges') is not None:
            for k in m.get('Knowledges'):
                temp_model = QueryKnowledgesResponseBodyKnowledges()
                self.knowledges.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryKnowledgesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryKnowledgesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryKnowledgesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPerspectivesRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        return self


class QueryPerspectivesResponseBodyPerspectives(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_user_name: str = None,
        modify_time: str = None,
        modify_user_name: str = None,
        name: str = None,
        perspective_code: str = None,
        perspective_id: str = None,
        self_define: bool = None,
        status: int = None,
    ):
        self.create_time = create_time
        self.create_user_name = create_user_name
        self.modify_time = modify_time
        self.modify_user_name = modify_user_name
        self.name = name
        self.perspective_code = perspective_code
        self.perspective_id = perspective_id
        self.self_define = self_define
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.name is not None:
            result['Name'] = self.name
        if self.perspective_code is not None:
            result['PerspectiveCode'] = self.perspective_code
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        if self.self_define is not None:
            result['SelfDefine'] = self.self_define
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PerspectiveCode') is not None:
            self.perspective_code = m.get('PerspectiveCode')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        if m.get('SelfDefine') is not None:
            self.self_define = m.get('SelfDefine')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryPerspectivesResponseBody(TeaModel):
    def __init__(
        self,
        perspectives: List[QueryPerspectivesResponseBodyPerspectives] = None,
        request_id: str = None,
    ):
        self.perspectives = perspectives
        self.request_id = request_id

    def validate(self):
        if self.perspectives:
            for k in self.perspectives:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Perspectives'] = []
        if self.perspectives is not None:
            for k in self.perspectives:
                result['Perspectives'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.perspectives = []
        if m.get('Perspectives') is not None:
            for k in m.get('Perspectives'):
                temp_model = QueryPerspectivesResponseBodyPerspectives()
                self.perspectives.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryPerspectivesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPerspectivesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPerspectivesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySystemEntitiesRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        entity_name: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.entity_name = entity_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        return self


class QuerySystemEntitiesResponseBodySystemEntities(TeaModel):
    def __init__(
        self,
        default_question: str = None,
        entity_code: str = None,
        entity_name: str = None,
    ):
        self.default_question = default_question
        self.entity_code = entity_code
        self.entity_name = entity_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_question is not None:
            result['DefaultQuestion'] = self.default_question
        if self.entity_code is not None:
            result['EntityCode'] = self.entity_code
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultQuestion') is not None:
            self.default_question = m.get('DefaultQuestion')
        if m.get('EntityCode') is not None:
            self.entity_code = m.get('EntityCode')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        return self


class QuerySystemEntitiesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        system_entities: List[QuerySystemEntitiesResponseBodySystemEntities] = None,
    ):
        self.request_id = request_id
        self.system_entities = system_entities

    def validate(self):
        if self.system_entities:
            for k in self.system_entities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SystemEntities'] = []
        if self.system_entities is not None:
            for k in self.system_entities:
                result['SystemEntities'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.system_entities = []
        if m.get('SystemEntities') is not None:
            for k in m.get('SystemEntities'):
                temp_model = QuerySystemEntitiesResponseBodySystemEntities()
                self.system_entities.append(temp_model.from_map(k))
        return self


class QuerySystemEntitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySystemEntitiesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QuerySystemEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveEntityMemberRequestMember(TeaModel):
    def __init__(
        self,
        member_name: str = None,
        synonyms: List[str] = None,
    ):
        self.member_name = member_name
        self.synonyms = synonyms

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        return self


class RemoveEntityMemberRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        entity_id: int = None,
        member: RemoveEntityMemberRequestMember = None,
        remove_type: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.entity_id = entity_id
        self.member = member
        self.remove_type = remove_type

    def validate(self):
        if self.member:
            self.member.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.member is not None:
            result['Member'] = self.member.to_map()
        if self.remove_type is not None:
            result['RemoveType'] = self.remove_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('Member') is not None:
            temp_model = RemoveEntityMemberRequestMember()
            self.member = temp_model.from_map(m['Member'])
        if m.get('RemoveType') is not None:
            self.remove_type = m.get('RemoveType')
        return self


class RemoveEntityMemberShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        entity_id: int = None,
        member_shrink: str = None,
        remove_type: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.entity_id = entity_id
        self.member_shrink = member_shrink
        self.remove_type = remove_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.member_shrink is not None:
            result['Member'] = self.member_shrink
        if self.remove_type is not None:
            result['RemoveType'] = self.remove_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('Member') is not None:
            self.member_shrink = m.get('Member')
        if m.get('RemoveType') is not None:
            self.remove_type = m.get('RemoveType')
        return self


class RemoveEntityMemberResponseBody(TeaModel):
    def __init__(
        self,
        entity_id: int = None,
        request_id: str = None,
    ):
        self.entity_id = entity_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveEntityMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveEntityMemberResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveEntityMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveSynonymRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        core_word_name: str = None,
        synonym: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.core_word_name = core_word_name
        self.synonym = synonym

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        if self.synonym is not None:
            result['Synonym'] = self.synonym
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        if m.get('Synonym') is not None:
            self.synonym = m.get('Synonym')
        return self


class RemoveSynonymResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveSynonymResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveSynonymResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveSynonymResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TestDialogFlowRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        dialog_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.dialog_id = dialog_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        return self


class TestDialogFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TestDialogFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TestDialogFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TestDialogFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCategoryRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        category_id: int = None,
        name: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.category_id = category_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateCategoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCategoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCoreWordRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        core_word_code: str = None,
        core_word_name: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.core_word_code = core_word_code
        self.core_word_name = core_word_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.core_word_code is not None:
            result['CoreWordCode'] = self.core_word_code
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CoreWordCode') is not None:
            self.core_word_code = m.get('CoreWordCode')
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        return self


class UpdateCoreWordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateCoreWordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCoreWordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateCoreWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDialogRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        description: str = None,
        dialog_id: int = None,
        dialog_name: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.description = description
        self.dialog_id = dialog_id
        self.dialog_name = dialog_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.description is not None:
            result['Description'] = self.description
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        return self


class UpdateDialogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDialogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDialogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateDialogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDialogFlowRequestModuleDefinition(TeaModel):
    def __init__(
        self,
        global_vars: Dict[str, Any] = None,
        module_definition: PaasProcessData = None,
    ):
        self.global_vars = global_vars
        self.module_definition = module_definition

    def validate(self):
        if self.module_definition:
            self.module_definition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.global_vars is not None:
            result['GlobalVars'] = self.global_vars
        if self.module_definition is not None:
            result['ModuleDefinition'] = self.module_definition.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlobalVars') is not None:
            self.global_vars = m.get('GlobalVars')
        if m.get('ModuleDefinition') is not None:
            temp_model = PaasProcessData()
            self.module_definition = temp_model.from_map(m['ModuleDefinition'])
        return self


class UpdateDialogFlowRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        dialog_id: int = None,
        module_definition: UpdateDialogFlowRequestModuleDefinition = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.dialog_id = dialog_id
        self.module_definition = module_definition

    def validate(self):
        if self.module_definition:
            self.module_definition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.module_definition is not None:
            result['ModuleDefinition'] = self.module_definition.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('ModuleDefinition') is not None:
            temp_model = UpdateDialogFlowRequestModuleDefinition()
            self.module_definition = temp_model.from_map(m['ModuleDefinition'])
        return self


class UpdateDialogFlowShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        dialog_id: int = None,
        module_definition_shrink: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.dialog_id = dialog_id
        self.module_definition_shrink = module_definition_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.module_definition_shrink is not None:
            result['ModuleDefinition'] = self.module_definition_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('ModuleDefinition') is not None:
            self.module_definition_shrink = m.get('ModuleDefinition')
        return self


class UpdateDialogFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDialogFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDialogFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateDialogFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEntityRequestMembers(TeaModel):
    def __init__(
        self,
        member_name: str = None,
        synonyms: List[str] = None,
    ):
        self.member_name = member_name
        self.synonyms = synonyms

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        return self


class UpdateEntityRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        entity_id: int = None,
        entity_name: str = None,
        entity_type: str = None,
        members: List[UpdateEntityRequestMembers] = None,
        regex: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.entity_id = entity_id
        self.entity_name = entity_name
        self.entity_type = entity_type
        self.members = members
        self.regex = regex

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.regex is not None:
            result['Regex'] = self.regex
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = UpdateEntityRequestMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        return self


class UpdateEntityShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        entity_id: int = None,
        entity_name: str = None,
        entity_type: str = None,
        members_shrink: str = None,
        regex: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.entity_id = entity_id
        self.entity_name = entity_name
        self.entity_type = entity_type
        self.members_shrink = members_shrink
        self.regex = regex

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.members_shrink is not None:
            result['Members'] = self.members_shrink
        if self.regex is not None:
            result['Regex'] = self.regex
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Members') is not None:
            self.members_shrink = m.get('Members')
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        return self


class UpdateEntityResponseBody(TeaModel):
    def __init__(
        self,
        entity_id: int = None,
        request_id: str = None,
    ):
        self.entity_id = entity_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateEntityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEntityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIntentRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        intent_definition: IntentCreateDTO = None,
        intent_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.intent_definition = intent_definition
        self.intent_id = intent_id

    def validate(self):
        if self.intent_definition:
            self.intent_definition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.intent_definition is not None:
            result['IntentDefinition'] = self.intent_definition.to_map()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('IntentDefinition') is not None:
            temp_model = IntentCreateDTO()
            self.intent_definition = temp_model.from_map(m['IntentDefinition'])
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class UpdateIntentShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        intent_definition_shrink: str = None,
        intent_id: int = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.intent_definition_shrink = intent_definition_shrink
        self.intent_id = intent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.intent_definition_shrink is not None:
            result['IntentDefinition'] = self.intent_definition_shrink
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('IntentDefinition') is not None:
            self.intent_definition_shrink = m.get('IntentDefinition')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class UpdateIntentResponseBody(TeaModel):
    def __init__(
        self,
        intent_id: int = None,
        request_id: str = None,
    ):
        self.intent_id = intent_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateIntentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateIntentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateKnowledgeRequestKnowledgeOutlines(TeaModel):
    def __init__(
        self,
        action: str = None,
        knowledge_id: int = None,
        outline_id: int = None,
        title: str = None,
    ):
        self.action = action
        self.knowledge_id = knowledge_id
        self.outline_id = outline_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.outline_id is not None:
            result['OutlineId'] = self.outline_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('OutlineId') is not None:
            self.outline_id = m.get('OutlineId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateKnowledgeRequestKnowledgeSimQuestions(TeaModel):
    def __init__(
        self,
        action: str = None,
        sim_question_id: int = None,
        title: str = None,
    ):
        self.action = action
        self.sim_question_id = sim_question_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.sim_question_id is not None:
            result['SimQuestionId'] = self.sim_question_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('SimQuestionId') is not None:
            self.sim_question_id = m.get('SimQuestionId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateKnowledgeRequestKnowledgeSolutions(TeaModel):
    def __init__(
        self,
        action: str = None,
        content: str = None,
        perspective_ids: List[str] = None,
        plain_text: str = None,
        solution_id: int = None,
    ):
        self.action = action
        self.content = content
        self.perspective_ids = perspective_ids
        self.plain_text = plain_text
        self.solution_id = solution_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.content is not None:
            result['Content'] = self.content
        if self.perspective_ids is not None:
            result['PerspectiveIds'] = self.perspective_ids
        if self.plain_text is not None:
            result['PlainText'] = self.plain_text
        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('PerspectiveIds') is not None:
            self.perspective_ids = m.get('PerspectiveIds')
        if m.get('PlainText') is not None:
            self.plain_text = m.get('PlainText')
        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')
        return self


class UpdateKnowledgeRequestKnowledge(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        end_date: str = None,
        knowledge_id: int = None,
        knowledge_title: str = None,
        knowledge_type: int = None,
        outlines: List[UpdateKnowledgeRequestKnowledgeOutlines] = None,
        sim_questions: List[UpdateKnowledgeRequestKnowledgeSimQuestions] = None,
        solutions: List[UpdateKnowledgeRequestKnowledgeSolutions] = None,
        start_date: str = None,
    ):
        self.category_id = category_id
        self.end_date = end_date
        self.knowledge_id = knowledge_id
        self.knowledge_title = knowledge_title
        self.knowledge_type = knowledge_type
        self.outlines = outlines
        self.sim_questions = sim_questions
        self.solutions = solutions
        self.start_date = start_date

    def validate(self):
        if self.outlines:
            for k in self.outlines:
                if k:
                    k.validate()
        if self.sim_questions:
            for k in self.sim_questions:
                if k:
                    k.validate()
        if self.solutions:
            for k in self.solutions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.knowledge_title is not None:
            result['KnowledgeTitle'] = self.knowledge_title
        if self.knowledge_type is not None:
            result['KnowledgeType'] = self.knowledge_type
        result['Outlines'] = []
        if self.outlines is not None:
            for k in self.outlines:
                result['Outlines'].append(k.to_map() if k else None)
        result['SimQuestions'] = []
        if self.sim_questions is not None:
            for k in self.sim_questions:
                result['SimQuestions'].append(k.to_map() if k else None)
        result['Solutions'] = []
        if self.solutions is not None:
            for k in self.solutions:
                result['Solutions'].append(k.to_map() if k else None)
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('KnowledgeTitle') is not None:
            self.knowledge_title = m.get('KnowledgeTitle')
        if m.get('KnowledgeType') is not None:
            self.knowledge_type = m.get('KnowledgeType')
        self.outlines = []
        if m.get('Outlines') is not None:
            for k in m.get('Outlines'):
                temp_model = UpdateKnowledgeRequestKnowledgeOutlines()
                self.outlines.append(temp_model.from_map(k))
        self.sim_questions = []
        if m.get('SimQuestions') is not None:
            for k in m.get('SimQuestions'):
                temp_model = UpdateKnowledgeRequestKnowledgeSimQuestions()
                self.sim_questions.append(temp_model.from_map(k))
        self.solutions = []
        if m.get('Solutions') is not None:
            for k in m.get('Solutions'):
                temp_model = UpdateKnowledgeRequestKnowledgeSolutions()
                self.solutions.append(temp_model.from_map(k))
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class UpdateKnowledgeRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge: UpdateKnowledgeRequestKnowledge = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.knowledge = knowledge

    def validate(self):
        if self.knowledge:
            self.knowledge.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge is not None:
            result['Knowledge'] = self.knowledge.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Knowledge') is not None:
            temp_model = UpdateKnowledgeRequestKnowledge()
            self.knowledge = temp_model.from_map(m['Knowledge'])
        return self


class UpdateKnowledgeShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge_shrink: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.knowledge_shrink = knowledge_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.knowledge_shrink is not None:
            result['Knowledge'] = self.knowledge_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Knowledge') is not None:
            self.knowledge_shrink = m.get('Knowledge')
        return self


class UpdateKnowledgeResponseBody(TeaModel):
    def __init__(
        self,
        knowledge_id: int = None,
        request_id: str = None,
    ):
        self.knowledge_id = knowledge_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateKnowledgeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateKnowledgeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePerspectiveRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        name: str = None,
        perspective_id: str = None,
    ):
        # 业务空间key,不设置则访问默认业务空间，key值在主账号业务管理页面获取
        self.agent_key = agent_key
        self.name = name
        self.perspective_id = perspective_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.name is not None:
            result['Name'] = self.name
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        return self


class UpdatePerspectiveResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePerspectiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePerspectiveResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdatePerspectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


