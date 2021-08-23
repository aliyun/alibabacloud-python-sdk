# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


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


class PaasResponseNodeContentDTO(TeaModel):
    def __init__(
        self,
        type: str = None,
        text: str = None,
        image: str = None,
        button_list: PaasButtonListDTO = None,
    ):
        # Type
        self.type = type
        # Text
        self.text = text
        # Image
        self.image = image
        # ButtonList
        self.button_list = button_list

    def validate(self):
        if self.button_list:
            self.button_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.text is not None:
            result['Text'] = self.text
        if self.image is not None:
            result['Image'] = self.image
        if self.button_list is not None:
            result['ButtonList'] = self.button_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ButtonList') is not None:
            temp_model = PaasButtonListDTO()
            self.button_list = temp_model.from_map(m['ButtonList'])
        return self


class PaasResponsePluginFieldDataDTO(TeaModel):
    def __init__(
        self,
        name: str = None,
        content_response: PaasResponseNodeContentDTO = None,
    ):
        # Name
        self.name = name
        # ContentResponse
        self.content_response = content_response

    def validate(self):
        if self.content_response:
            self.content_response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.content_response is not None:
            result['ContentResponse'] = self.content_response.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ContentResponse') is not None:
            temp_model = PaasResponseNodeContentDTO()
            self.content_response = temp_model.from_map(m['ContentResponse'])
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


class PaasConditionEntryDTO(TeaModel):
    def __init__(
        self,
        id: str = None,
        term: str = None,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        # id
        self.id = id
        # Term
        self.term = term
        # Name
        self.name = name
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
            result['id'] = self.id
        if self.term is not None:
            result['Term'] = self.term
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('Term') is not None:
            self.term = m.get('Term')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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


class PaasFunctionPluginFieldDataDTO(TeaModel):
    def __init__(
        self,
        function: str = None,
        aliyun_function: str = None,
        type: str = None,
        description: str = None,
        end_point: str = None,
        code: str = None,
        name: str = None,
        aliyun_service: str = None,
        switch: List[PaasSwitchCaseDTO] = None,
        params: Dict[str, Any] = None,
    ):
        # Function
        self.function = function
        # AliyunFunction
        self.aliyun_function = aliyun_function
        # Type
        self.type = type
        # Description
        self.description = description
        # EndPoint
        self.end_point = end_point
        # Code
        self.code = code
        # Name
        self.name = name
        # AliyunService
        self.aliyun_service = aliyun_service
        # Switch
        self.switch = switch
        # Params
        self.params = params

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
        if self.function is not None:
            result['Function'] = self.function
        if self.aliyun_function is not None:
            result['AliyunFunction'] = self.aliyun_function
        if self.type is not None:
            result['Type'] = self.type
        if self.description is not None:
            result['Description'] = self.description
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        if self.aliyun_service is not None:
            result['AliyunService'] = self.aliyun_service
        result['Switch'] = []
        if self.switch is not None:
            for k in self.switch:
                result['Switch'].append(k.to_map() if k else None)
        if self.params is not None:
            result['Params'] = self.params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Function') is not None:
            self.function = m.get('Function')
        if m.get('AliyunFunction') is not None:
            self.aliyun_function = m.get('AliyunFunction')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AliyunService') is not None:
            self.aliyun_service = m.get('AliyunService')
        self.switch = []
        if m.get('Switch') is not None:
            for k in m.get('Switch'):
                temp_model = PaasSwitchCaseDTO()
                self.switch.append(temp_model.from_map(k))
        if m.get('Params') is not None:
            self.params = m.get('Params')
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


class PaasSlotConfigDTO(TeaModel):
    def __init__(
        self,
        is_array: bool = None,
        is_necessary: bool = None,
        value: str = None,
        life_span: int = None,
        name: str = None,
        question: List[str] = None,
    ):
        # IsArray
        self.is_array = is_array
        # IsNecessary
        self.is_necessary = is_necessary
        # Value
        self.value = value
        # LifeSpan
        self.life_span = life_span
        # Name
        self.name = name
        # Question
        self.question = question

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
        if self.value is not None:
            result['Value'] = self.value
        if self.life_span is not None:
            result['LifeSpan'] = self.life_span
        if self.name is not None:
            result['Name'] = self.name
        if self.question is not None:
            result['Question'] = self.question
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsArray') is not None:
            self.is_array = m.get('IsArray')
        if m.get('IsNecessary') is not None:
            self.is_necessary = m.get('IsNecessary')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('LifeSpan') is not None:
            self.life_span = m.get('LifeSpan')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        return self


class PaasSlotPluginFieldDataDTO(TeaModel):
    def __init__(
        self,
        intent_name: str = None,
        intent_id: str = None,
        name: str = None,
        is_sys_intent: bool = None,
        content_slot: List[PaasSlotConfigDTO] = None,
    ):
        # IntentName
        self.intent_name = intent_name
        # IntentId
        self.intent_id = intent_id
        # Name
        self.name = name
        # IsSysIntent
        self.is_sys_intent = is_sys_intent
        # ContentSlot
        self.content_slot = content_slot

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
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.name is not None:
            result['Name'] = self.name
        if self.is_sys_intent is not None:
            result['IsSysIntent'] = self.is_sys_intent
        result['ContentSlot'] = []
        if self.content_slot is not None:
            for k in self.content_slot:
                result['ContentSlot'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('IsSysIntent') is not None:
            self.is_sys_intent = m.get('IsSysIntent')
        self.content_slot = []
        if m.get('ContentSlot') is not None:
            for k in m.get('ContentSlot'):
                temp_model = PaasSlotConfigDTO()
                self.content_slot.append(temp_model.from_map(k))
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
        slot: PaasSlotDTO = None,
        response: PaasResponseDTO = None,
        function: PaasFunctionDTO = None,
    ):
        self.entry = entry
        self.slot = slot
        self.response = response
        self.function = function

    def validate(self):
        if self.entry:
            self.entry.validate()
        if self.slot:
            self.slot.validate()
        if self.response:
            self.response.validate()
        if self.function:
            self.function.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry is not None:
            result['Entry'] = self.entry.to_map()
        if self.slot is not None:
            result['Slot'] = self.slot.to_map()
        if self.response is not None:
            result['Response'] = self.response.to_map()
        if self.function is not None:
            result['Function'] = self.function.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Entry') is not None:
            temp_model = PaasEntryDTO()
            self.entry = temp_model.from_map(m['Entry'])
        if m.get('Slot') is not None:
            temp_model = PaasSlotDTO()
            self.slot = temp_model.from_map(m['Slot'])
        if m.get('Response') is not None:
            temp_model = PaasResponseDTO()
            self.response = temp_model.from_map(m['Response'])
        if m.get('Function') is not None:
            temp_model = PaasFunctionDTO()
            self.function = temp_model.from_map(m['Function'])
        return self


class PaasNodeDTO(TeaModel):
    def __init__(
        self,
        code: str = None,
        id: str = None,
        label: str = None,
        xx: float = None,
        yy: float = None,
        plugin_data: PaasPluginDataDTO = None,
    ):
        # Code
        self.code = code
        # Id
        self.id = id
        # Label
        self.label = label
        # Xx
        self.xx = xx
        # Yy
        self.yy = yy
        # PluginData
        self.plugin_data = plugin_data

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
        if self.xx is not None:
            result['Xx'] = self.xx
        if self.yy is not None:
            result['Yy'] = self.yy
        if self.plugin_data is not None:
            result['PluginData'] = self.plugin_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Xx') is not None:
            self.xx = m.get('Xx')
        if m.get('Yy') is not None:
            self.yy = m.get('Yy')
        if m.get('PluginData') is not None:
            temp_model = PaasPluginDataDTO()
            self.plugin_data = temp_model.from_map(m['PluginData'])
        return self


class PaasEdgeDTO(TeaModel):
    def __init__(
        self,
        target: str = None,
        id: str = None,
        source: str = None,
        label: str = None,
    ):
        # Target
        self.target = target
        # Id
        self.id = id
        # Source
        self.source = source
        # Label
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target is not None:
            result['Target'] = self.target
        if self.id is not None:
            result['Id'] = self.id
        if self.source is not None:
            result['Source'] = self.source
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class UpdateDialogFlowModuleDefinition(TeaModel):
    def __init__(
        self,
        nodes: List[PaasNodeDTO] = None,
        edges: List[PaasEdgeDTO] = None,
    ):
        # Nodes
        self.nodes = nodes
        # Edges
        self.edges = edges

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()
        if self.edges:
            for k in self.edges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        result['Edges'] = []
        if self.edges is not None:
            for k in self.edges:
                result['Edges'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = PaasNodeDTO()
                self.nodes.append(temp_model.from_map(k))
        self.edges = []
        if m.get('Edges') is not None:
            for k in m.get('Edges'):
                temp_model = PaasEdgeDTO()
                self.edges.append(temp_model.from_map(k))
        return self


class Children(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        parent_category_id: int = None,
        area_code: str = None,
        name: str = None,
        childrens: List['Children'] = None,
    ):
        # 分类Id
        self.category_id = category_id
        # 父分类Id
        self.parent_category_id = parent_category_id
        # 地区代号
        self.area_code = area_code
        # 名称
        self.name = name
        # 子元素
        self.childrens = childrens

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
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        if self.area_code is not None:
            result['AreaCode'] = self.area_code
        if self.name is not None:
            result['Name'] = self.name
        result['Childrens'] = []
        if self.childrens is not None:
            for k in self.childrens:
                result['Childrens'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        if m.get('AreaCode') is not None:
            self.area_code = m.get('AreaCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.childrens = []
        if m.get('Childrens') is not None:
            for k in m.get('Childrens'):
                temp_model = Children()
                self.childrens.append(temp_model.from_map(k))
        return self


class UsersayMtopDTO(TeaModel):
    def __init__(
        self,
        id: str = None,
        data: List[SectionMtopDTO] = None,
        strict: bool = None,
    ):
        # Id
        self.id = id
        # Data
        self.data = data
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
        if self.id is not None:
            result['Id'] = self.id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.strict is not None:
            result['Strict'] = self.strict
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = SectionMtopDTO()
                self.data.append(temp_model.from_map(k))
        if m.get('Strict') is not None:
            self.strict = m.get('Strict')
        return self


class RuleMtopDTO(TeaModel):
    def __init__(
        self,
        strict: bool = None,
        text: str = None,
        warning: List[str] = None,
        error: List[str] = None,
    ):
        # Strict
        self.strict = strict
        # Text
        self.text = text
        # Warning
        self.warning = warning
        # Error
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.strict is not None:
            result['Strict'] = self.strict
        if self.text is not None:
            result['Text'] = self.text
        if self.warning is not None:
            result['Warning'] = self.warning
        if self.error is not None:
            result['Error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Strict') is not None:
            self.strict = m.get('Strict')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Warning') is not None:
            self.warning = m.get('Warning')
        if m.get('Error') is not None:
            self.error = m.get('Error')
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
        question: List[str] = None,
        life_span: int = None,
        name: str = None,
        is_array: bool = None,
        value: str = None,
        is_necessary: bool = None,
        tags: List[TagMtopDTO] = None,
    ):
        # Id
        self.id = id
        # Question
        self.question = question
        # LifeSpan
        self.life_span = life_span
        # Name
        self.name = name
        # IsArray
        self.is_array = is_array
        # Value
        self.value = value
        # IsNecessary
        self.is_necessary = is_necessary
        # Tags
        self.tags = tags

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
        if self.question is not None:
            result['Question'] = self.question
        if self.life_span is not None:
            result['LifeSpan'] = self.life_span
        if self.name is not None:
            result['Name'] = self.name
        if self.is_array is not None:
            result['IsArray'] = self.is_array
        if self.value is not None:
            result['Value'] = self.value
        if self.is_necessary is not None:
            result['IsNecessary'] = self.is_necessary
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('LifeSpan') is not None:
            self.life_span = m.get('LifeSpan')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('IsArray') is not None:
            self.is_array = m.get('IsArray')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('IsNecessary') is not None:
            self.is_necessary = m.get('IsNecessary')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = TagMtopDTO()
                self.tags.append(temp_model.from_map(k))
        return self


class IntentCreateDTO(TeaModel):
    def __init__(
        self,
        intent_id: int = None,
        name: str = None,
        user_say: List[UsersayMtopDTO] = None,
        rule_check: List[RuleMtopDTO] = None,
        slot: List[SlotrecordMtopDTO] = None,
    ):
        # IntentId
        self.intent_id = intent_id
        # Name
        self.name = name
        # UserSay
        self.user_say = user_say
        # RuleCheck
        self.rule_check = rule_check
        self.slot = slot

    def validate(self):
        if self.user_say:
            for k in self.user_say:
                if k:
                    k.validate()
        if self.rule_check:
            for k in self.rule_check:
                if k:
                    k.validate()
        if self.slot:
            for k in self.slot:
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
        result['UserSay'] = []
        if self.user_say is not None:
            for k in self.user_say:
                result['UserSay'].append(k.to_map() if k else None)
        result['RuleCheck'] = []
        if self.rule_check is not None:
            for k in self.rule_check:
                result['RuleCheck'].append(k.to_map() if k else None)
        result['Slot'] = []
        if self.slot is not None:
            for k in self.slot:
                result['Slot'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.user_say = []
        if m.get('UserSay') is not None:
            for k in m.get('UserSay'):
                temp_model = UsersayMtopDTO()
                self.user_say.append(temp_model.from_map(k))
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
        return self


class PaasFunctionPluginParams(TeaModel):
    def __init__(
        self,
        method: str = None,
        query: Dict[str, str] = None,
        header: Dict[str, str] = None,
        body: str = None,
        url: str = None,
    ):
        # Method
        self.method = method
        # Query
        self.query = query
        # Header
        self.header = header
        # Body
        self.body = body
        # Url
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method is not None:
            result['Method'] = self.method
        if self.query is not None:
            result['Query'] = self.query
        if self.header is not None:
            result['Header'] = self.header
        if self.body is not None:
            result['Body'] = self.body
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('Header') is not None:
            self.header = m.get('Header')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class PaasProcessData(TeaModel):
    def __init__(
        self,
        nodes: List[PaasNodeDTO] = None,
        edges: List[PaasEdgeDTO] = None,
    ):
        # Nodes
        self.nodes = nodes
        # Edges
        self.edges = edges

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()
        if self.edges:
            for k in self.edges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        result['Edges'] = []
        if self.edges is not None:
            for k in self.edges:
                result['Edges'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = PaasNodeDTO()
                self.nodes.append(temp_model.from_map(k))
        self.edges = []
        if m.get('Edges') is not None:
            for k in m.get('Edges'):
                temp_model = PaasEdgeDTO()
                self.edges.append(temp_model.from_map(k))
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
        dialog_id: int = None,
        entity_name: str = None,
        entity_type: str = None,
        regex: str = None,
        members: List[CreateEntityRequestMembers] = None,
    ):
        self.dialog_id = dialog_id
        self.entity_name = entity_name
        self.entity_type = entity_type
        self.regex = regex
        self.members = members

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
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.regex is not None:
            result['Regex'] = self.regex
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = CreateEntityRequestMembers()
                self.members.append(temp_model.from_map(k))
        return self


class CreateEntityShrinkRequest(TeaModel):
    def __init__(
        self,
        dialog_id: int = None,
        entity_name: str = None,
        entity_type: str = None,
        regex: str = None,
        members_shrink: str = None,
    ):
        self.dialog_id = dialog_id
        self.entity_name = entity_name
        self.entity_type = entity_type
        self.regex = regex
        self.members_shrink = members_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.regex is not None:
            result['Regex'] = self.regex
        if self.members_shrink is not None:
            result['Members'] = self.members_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        if m.get('Members') is not None:
            self.members_shrink = m.get('Members')
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
        body: CreateEntityResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSynonymRequest(TeaModel):
    def __init__(
        self,
        core_word_name: str = None,
        synonym: str = None,
    ):
        self.core_word_name = core_word_name
        self.synonym = synonym

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        if self.synonym is not None:
            result['Synonym'] = self.synonym
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        body: AddSynonymResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddSynonymResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCategoryRequest(TeaModel):
    def __init__(
        self,
        category_id: int = None,
    ):
        self.category_id = category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        body: DeleteCategoryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishKnowledgeRequest(TeaModel):
    def __init__(
        self,
        knowledge_id: int = None,
        async_: bool = None,
    ):
        self.knowledge_id = knowledge_id
        self.async_ = async_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.async_ is not None:
            result['Async'] = self.async_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
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
        body: PublishKnowledgeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PublishKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotKnowledgeDetailsRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
        limit: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class ListBotKnowledgeDetailsResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        request_id: str = None,
        datas: List[Dict[str, Any]] = None,
    ):
        self.cost_time = cost_time
        self.request_id = request_id
        self.datas = datas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.datas is not None:
            result['Datas'] = self.datas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        return self


class ListBotKnowledgeDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListBotKnowledgeDetailsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListBotKnowledgeDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryIntentsRequest(TeaModel):
    def __init__(
        self,
        intent_name: str = None,
        dialog_id: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.intent_name = intent_name
        self.dialog_id = dialog_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryIntentsResponseBodyIntentsSlotTags(TeaModel):
    def __init__(
        self,
        value: str = None,
        user_say_id: str = None,
    ):
        self.value = value
        self.user_say_id = user_say_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')
        return self


class QueryIntentsResponseBodyIntentsSlot(TeaModel):
    def __init__(
        self,
        value: str = None,
        life_span: int = None,
        slot_id: str = None,
        is_necessary: bool = None,
        is_array: bool = None,
        tags: List[QueryIntentsResponseBodyIntentsSlotTags] = None,
        question: List[str] = None,
        name: str = None,
    ):
        self.value = value
        self.life_span = life_span
        self.slot_id = slot_id
        self.is_necessary = is_necessary
        self.is_array = is_array
        self.tags = tags
        self.question = question
        self.name = name

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
        if self.value is not None:
            result['Value'] = self.value
        if self.life_span is not None:
            result['LifeSpan'] = self.life_span
        if self.slot_id is not None:
            result['SlotId'] = self.slot_id
        if self.is_necessary is not None:
            result['IsNecessary'] = self.is_necessary
        if self.is_array is not None:
            result['IsArray'] = self.is_array
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.question is not None:
            result['Question'] = self.question
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('LifeSpan') is not None:
            self.life_span = m.get('LifeSpan')
        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')
        if m.get('IsNecessary') is not None:
            self.is_necessary = m.get('IsNecessary')
        if m.get('IsArray') is not None:
            self.is_array = m.get('IsArray')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = QueryIntentsResponseBodyIntentsSlotTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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
        user_say_id: str = None,
        strict: bool = None,
    ):
        self.data = data
        self.user_say_id = user_say_id
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
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id
        if self.strict is not None:
            result['Strict'] = self.strict
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryIntentsResponseBodyIntentsUserSayData()
                self.data.append(temp_model.from_map(k))
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')
        if m.get('Strict') is not None:
            self.strict = m.get('Strict')
        return self


class QueryIntentsResponseBodyIntentsRuleCheck(TeaModel):
    def __init__(
        self,
        error: List[str] = None,
        warning: List[str] = None,
        text: str = None,
        strict: bool = None,
    ):
        self.error = error
        self.warning = warning
        self.text = text
        self.strict = strict

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.warning is not None:
            result['Warning'] = self.warning
        if self.text is not None:
            result['Text'] = self.text
        if self.strict is not None:
            result['Strict'] = self.strict
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Warning') is not None:
            self.warning = m.get('Warning')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Strict') is not None:
            self.strict = m.get('Strict')
        return self


class QueryIntentsResponseBodyIntents(TeaModel):
    def __init__(
        self,
        modify_user_id: str = None,
        modify_user_name: str = None,
        create_time: str = None,
        create_user_name: str = None,
        slot: List[QueryIntentsResponseBodyIntentsSlot] = None,
        user_say: List[QueryIntentsResponseBodyIntentsUserSay] = None,
        name: str = None,
        rule_check: List[QueryIntentsResponseBodyIntentsRuleCheck] = None,
        create_user_id: str = None,
        intent_id: int = None,
        modify_time: str = None,
    ):
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.create_time = create_time
        self.create_user_name = create_user_name
        self.slot = slot
        self.user_say = user_say
        self.name = name
        self.rule_check = rule_check
        self.create_user_id = create_user_id
        self.intent_id = intent_id
        self.modify_time = modify_time

    def validate(self):
        if self.slot:
            for k in self.slot:
                if k:
                    k.validate()
        if self.user_say:
            for k in self.user_say:
                if k:
                    k.validate()
        if self.rule_check:
            for k in self.rule_check:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        result['Slot'] = []
        if self.slot is not None:
            for k in self.slot:
                result['Slot'].append(k.to_map() if k else None)
        result['UserSay'] = []
        if self.user_say is not None:
            for k in self.user_say:
                result['UserSay'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        result['RuleCheck'] = []
        if self.rule_check is not None:
            for k in self.rule_check:
                result['RuleCheck'].append(k.to_map() if k else None)
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
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
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.rule_check = []
        if m.get('RuleCheck') is not None:
            for k in m.get('RuleCheck'):
                temp_model = QueryIntentsResponseBodyIntentsRuleCheck()
                self.rule_check.append(temp_model.from_map(k))
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class QueryIntentsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        intents: List[QueryIntentsResponseBodyIntents] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.intents = intents

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Intents'] = []
        if self.intents is not None:
            for k in self.intents:
                result['Intents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.intents = []
        if m.get('Intents') is not None:
            for k in m.get('Intents'):
                temp_model = QueryIntentsResponseBodyIntents()
                self.intents.append(temp_model.from_map(k))
        return self


class QueryIntentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryIntentsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryIntentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCategoryRequest(TeaModel):
    def __init__(
        self,
        category_id: int = None,
    ):
        self.category_id = category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        return self


class DescribeCategoryResponseBody(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        request_id: str = None,
        parent_category_id: int = None,
        name: str = None,
    ):
        self.category_id = category_id
        self.request_id = request_id
        self.parent_category_id = parent_category_id
        self.name = name

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
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCategoryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotReceptionDetailDatasRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        return self


class ListBotReceptionDetailDatasResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        request_id: str = None,
        datas: List[Dict[str, Any]] = None,
    ):
        self.cost_time = cost_time
        self.request_id = request_id
        self.datas = datas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.datas is not None:
            result['Datas'] = self.datas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        return self


class ListBotReceptionDetailDatasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListBotReceptionDetailDatasResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListBotReceptionDetailDatasResponseBody()
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
        entity_id: int = None,
        apply_type: str = None,
        member: AppendEntityMemberRequestMember = None,
    ):
        self.entity_id = entity_id
        self.apply_type = apply_type
        self.member = member

    def validate(self):
        if self.member:
            self.member.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.apply_type is not None:
            result['ApplyType'] = self.apply_type
        if self.member is not None:
            result['Member'] = self.member.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('ApplyType') is not None:
            self.apply_type = m.get('ApplyType')
        if m.get('Member') is not None:
            temp_model = AppendEntityMemberRequestMember()
            self.member = temp_model.from_map(m['Member'])
        return self


class AppendEntityMemberShrinkRequest(TeaModel):
    def __init__(
        self,
        entity_id: int = None,
        apply_type: str = None,
        member_shrink: str = None,
    ):
        self.entity_id = entity_id
        self.apply_type = apply_type
        self.member_shrink = member_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.apply_type is not None:
            result['ApplyType'] = self.apply_type
        if self.member_shrink is not None:
            result['Member'] = self.member_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('ApplyType') is not None:
            self.apply_type = m.get('ApplyType')
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
        body: AppendEntityMemberResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AppendEntityMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBotRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        language_code: str = None,
        time_zone: str = None,
        request_id: str = None,
        introduction: str = None,
        instance_id: str = None,
        categories: List[DescribeBotResponseBodyCategories] = None,
        create_time: str = None,
        avatar: str = None,
        logo: str = None,
        name: str = None,
    ):
        self.language_code = language_code
        self.time_zone = time_zone
        self.request_id = request_id
        self.introduction = introduction
        self.instance_id = instance_id
        self.categories = categories
        self.create_time = create_time
        self.avatar = avatar
        self.logo = logo
        self.name = name

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
        if self.language_code is not None:
            result['LanguageCode'] = self.language_code
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['Categories'] = []
        if self.categories is not None:
            for k in self.categories:
                result['Categories'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.logo is not None:
            result['Logo'] = self.logo
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.categories = []
        if m.get('Categories') is not None:
            for k in m.get('Categories'):
                temp_model = DescribeBotResponseBodyCategories()
                self.categories.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('Logo') is not None:
            self.logo = m.get('Logo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotColdDsDatasRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
        limit: int = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class ListBotColdDsDatasResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        request_id: str = None,
        datas: List[Dict[str, Any]] = None,
    ):
        self.cost_time = cost_time
        self.request_id = request_id
        self.datas = datas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.datas is not None:
            result['Datas'] = self.datas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        return self


class ListBotColdDsDatasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListBotColdDsDatasResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListBotColdDsDatasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePerspectiveRequest(TeaModel):
    def __init__(
        self,
        perspective_id: str = None,
    ):
        self.perspective_id = perspective_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        return self


class DescribePerspectiveResponseBody(TeaModel):
    def __init__(
        self,
        status: int = None,
        perspective_code: str = None,
        modify_time: str = None,
        request_id: str = None,
        self_define: bool = None,
        create_time: str = None,
        modify_user_name: str = None,
        perspective_id: str = None,
        create_user_name: str = None,
        name: str = None,
    ):
        self.status = status
        self.perspective_code = perspective_code
        self.modify_time = modify_time
        self.request_id = request_id
        self.self_define = self_define
        self.create_time = create_time
        self.modify_user_name = modify_user_name
        self.perspective_id = perspective_id
        self.create_user_name = create_user_name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.perspective_code is not None:
            result['PerspectiveCode'] = self.perspective_code
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.self_define is not None:
            result['SelfDefine'] = self.self_define
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PerspectiveCode') is not None:
            self.perspective_code = m.get('PerspectiveCode')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SelfDefine') is not None:
            self.self_define = m.get('SelfDefine')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribePerspectiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePerspectiveResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePerspectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDialogRequest(TeaModel):
    def __init__(
        self,
        dialog_id: int = None,
        dialog_name: str = None,
        description: str = None,
    ):
        self.dialog_id = dialog_id
        self.dialog_name = dialog_name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
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
        body: UpdateDialogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDialogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBotRequest(TeaModel):
    def __init__(
        self,
        language_code: str = None,
        name: str = None,
        avatar: str = None,
        introduction: str = None,
        robot_type: str = None,
    ):
        self.language_code = language_code
        self.name = name
        self.avatar = avatar
        self.introduction = introduction
        self.robot_type = robot_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language_code is not None:
            result['LanguageCode'] = self.language_code
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.robot_type is not None:
            result['RobotType'] = self.robot_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('RobotType') is not None:
            self.robot_type = m.get('RobotType')
        return self


class CreateBotResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_id: str = None,
    ):
        self.request_id = request_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateBotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateBotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateBotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIntentRequest(TeaModel):
    def __init__(
        self,
        intent_id: int = None,
    ):
        self.intent_id = intent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
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
        user_say_id: str = None,
        strict: bool = None,
    ):
        self.data = data
        self.user_say_id = user_say_id
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
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id
        if self.strict is not None:
            result['Strict'] = self.strict
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeIntentResponseBodyUserSayData()
                self.data.append(temp_model.from_map(k))
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')
        if m.get('Strict') is not None:
            self.strict = m.get('Strict')
        return self


class DescribeIntentResponseBodySlotTags(TeaModel):
    def __init__(
        self,
        value: str = None,
        user_say_id: str = None,
    ):
        self.value = value
        self.user_say_id = user_say_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')
        return self


class DescribeIntentResponseBodySlot(TeaModel):
    def __init__(
        self,
        value: str = None,
        life_span: int = None,
        slot_id: str = None,
        is_necessary: bool = None,
        is_array: bool = None,
        tags: List[DescribeIntentResponseBodySlotTags] = None,
        question: List[str] = None,
        name: str = None,
    ):
        self.value = value
        self.life_span = life_span
        self.slot_id = slot_id
        self.is_necessary = is_necessary
        self.is_array = is_array
        self.tags = tags
        self.question = question
        self.name = name

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
        if self.value is not None:
            result['Value'] = self.value
        if self.life_span is not None:
            result['LifeSpan'] = self.life_span
        if self.slot_id is not None:
            result['SlotId'] = self.slot_id
        if self.is_necessary is not None:
            result['IsNecessary'] = self.is_necessary
        if self.is_array is not None:
            result['IsArray'] = self.is_array
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.question is not None:
            result['Question'] = self.question
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('LifeSpan') is not None:
            self.life_span = m.get('LifeSpan')
        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')
        if m.get('IsNecessary') is not None:
            self.is_necessary = m.get('IsNecessary')
        if m.get('IsArray') is not None:
            self.is_array = m.get('IsArray')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeIntentResponseBodySlotTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeIntentResponseBodyRuleCheck(TeaModel):
    def __init__(
        self,
        error: List[str] = None,
        warning: List[str] = None,
        text: str = None,
        strict: bool = None,
    ):
        self.error = error
        self.warning = warning
        self.text = text
        self.strict = strict

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.warning is not None:
            result['Warning'] = self.warning
        if self.text is not None:
            result['Text'] = self.text
        if self.strict is not None:
            result['Strict'] = self.strict
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Warning') is not None:
            self.warning = m.get('Warning')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Strict') is not None:
            self.strict = m.get('Strict')
        return self


class DescribeIntentResponseBody(TeaModel):
    def __init__(
        self,
        modify_time: str = None,
        request_id: str = None,
        create_time: str = None,
        dialog_id: int = None,
        create_user_id: str = None,
        create_user_name: str = None,
        name: str = None,
        intent_id: int = None,
        type: str = None,
        modify_user_id: str = None,
        user_say: List[DescribeIntentResponseBodyUserSay] = None,
        modify_user_name: str = None,
        slot: List[DescribeIntentResponseBodySlot] = None,
        rule_check: List[DescribeIntentResponseBodyRuleCheck] = None,
    ):
        self.modify_time = modify_time
        self.request_id = request_id
        self.create_time = create_time
        self.dialog_id = dialog_id
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.name = name
        self.intent_id = intent_id
        self.type = type
        self.modify_user_id = modify_user_id
        self.user_say = user_say
        self.modify_user_name = modify_user_name
        self.slot = slot
        self.rule_check = rule_check

    def validate(self):
        if self.user_say:
            for k in self.user_say:
                if k:
                    k.validate()
        if self.slot:
            for k in self.slot:
                if k:
                    k.validate()
        if self.rule_check:
            for k in self.rule_check:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.name is not None:
            result['Name'] = self.name
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.type is not None:
            result['Type'] = self.type
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        result['UserSay'] = []
        if self.user_say is not None:
            for k in self.user_say:
                result['UserSay'].append(k.to_map() if k else None)
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        result['Slot'] = []
        if self.slot is not None:
            for k in self.slot:
                result['Slot'].append(k.to_map() if k else None)
        result['RuleCheck'] = []
        if self.rule_check is not None:
            for k in self.rule_check:
                result['RuleCheck'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        self.user_say = []
        if m.get('UserSay') is not None:
            for k in m.get('UserSay'):
                temp_model = DescribeIntentResponseBodyUserSay()
                self.user_say.append(temp_model.from_map(k))
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        self.slot = []
        if m.get('Slot') is not None:
            for k in m.get('Slot'):
                temp_model = DescribeIntentResponseBodySlot()
                self.slot.append(temp_model.from_map(k))
        self.rule_check = []
        if m.get('RuleCheck') is not None:
            for k in m.get('RuleCheck'):
                temp_model = DescribeIntentResponseBodyRuleCheck()
                self.rule_check.append(temp_model.from_map(k))
        return self


class DescribeIntentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeIntentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDialogsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        dialog_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.dialog_name = dialog_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryDialogsResponseBodyDialogs(TeaModel):
    def __init__(
        self,
        status: int = None,
        dialog_name: str = None,
        modify_user_id: str = None,
        is_online: bool = None,
        create_user_name: str = None,
        create_time: str = None,
        create_user_id: str = None,
        modify_user_name: str = None,
        description: str = None,
        dialog_id: int = None,
        is_sample_dialog: bool = None,
        modify_time: str = None,
    ):
        self.status = status
        self.dialog_name = dialog_name
        self.modify_user_id = modify_user_id
        self.is_online = is_online
        self.create_user_name = create_user_name
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.modify_user_name = modify_user_name
        self.description = description
        self.dialog_id = dialog_id
        self.is_sample_dialog = is_sample_dialog
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.is_online is not None:
            result['IsOnline'] = self.is_online
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.description is not None:
            result['Description'] = self.description
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.is_sample_dialog is not None:
            result['IsSampleDialog'] = self.is_sample_dialog
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('IsOnline') is not None:
            self.is_online = m.get('IsOnline')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('IsSampleDialog') is not None:
            self.is_sample_dialog = m.get('IsSampleDialog')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class QueryDialogsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        dialogs: List[QueryDialogsResponseBodyDialogs] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.dialogs = dialogs

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Dialogs'] = []
        if self.dialogs is not None:
            for k in self.dialogs:
                result['Dialogs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.dialogs = []
        if m.get('Dialogs') is not None:
            for k in m.get('Dialogs'):
                temp_model = QueryDialogsResponseBodyDialogs()
                self.dialogs.append(temp_model.from_map(k))
        return self


class QueryDialogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDialogsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDialogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDialogRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        dialog_name: str = None,
        description: str = None,
    ):
        self.instance_id = instance_id
        self.dialog_name = dialog_name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class CreateDialogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        dialog_id: int = None,
    ):
        self.request_id = request_id
        self.dialog_id = dialog_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        return self


class CreateDialogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDialogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDialogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCoreWordsRequest(TeaModel):
    def __init__(
        self,
        core_word_name: str = None,
        page_number: int = None,
        page_size: int = None,
        synonym: str = None,
    ):
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
        synonyms: List[str] = None,
        create_time: str = None,
        modify_time: str = None,
    ):
        self.core_word_code = core_word_code
        self.core_word_name = core_word_name
        self.synonyms = synonyms
        self.create_time = create_time
        self.modify_time = modify_time

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
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoreWordCode') is not None:
            self.core_word_code = m.get('CoreWordCode')
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class QueryCoreWordsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        core_words: List[QueryCoreWordsResponseBodyCoreWords] = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.total_count = total_count
        self.core_words = core_words
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['CoreWords'] = []
        if self.core_words is not None:
            for k in self.core_words:
                result['CoreWords'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.core_words = []
        if m.get('CoreWords') is not None:
            for k in m.get('CoreWords'):
                temp_model = QueryCoreWordsResponseBodyCoreWords()
                self.core_words.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class QueryCoreWordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryCoreWordsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryCoreWordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCoreWordRequest(TeaModel):
    def __init__(
        self,
        core_word_name: str = None,
        core_word_code: str = None,
    ):
        self.core_word_name = core_word_name
        self.core_word_code = core_word_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        if self.core_word_code is not None:
            result['CoreWordCode'] = self.core_word_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        if m.get('CoreWordCode') is not None:
            self.core_word_code = m.get('CoreWordCode')
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
        body: UpdateCoreWordResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateCoreWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCategoryRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        category_id: int = None,
    ):
        self.name = name
        self.category_id = category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
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
        body: UpdateCategoryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConversationListRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        session_id: str = None,
        sender_id: str = None,
        start_date: str = None,
        end_date: str = None,
        page_number: str = None,
        page_size: str = None,
    ):
        self.instance_id = instance_id
        self.session_id = session_id
        self.sender_id = sender_id
        self.start_date = start_date
        self.end_date = end_date
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetConversationListResponseBody(TeaModel):
    def __init__(
        self,
        messages: List[Dict[str, Any]] = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        total_counts: int = None,
    ):
        self.messages = messages
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Messages') is not None:
            self.messages = m.get('Messages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')
        return self


class GetConversationListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetConversationListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetConversationListResponseBody()
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
        entity_id: int = None,
        entity_name: str = None,
        entity_type: str = None,
        regex: str = None,
        members: List[UpdateEntityRequestMembers] = None,
    ):
        self.entity_id = entity_id
        self.entity_name = entity_name
        self.entity_type = entity_type
        self.regex = regex
        self.members = members

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
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.regex is not None:
            result['Regex'] = self.regex
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = UpdateEntityRequestMembers()
                self.members.append(temp_model.from_map(k))
        return self


class UpdateEntityShrinkRequest(TeaModel):
    def __init__(
        self,
        entity_id: int = None,
        entity_name: str = None,
        entity_type: str = None,
        regex: str = None,
        members_shrink: str = None,
    ):
        self.entity_id = entity_id
        self.entity_name = entity_name
        self.entity_type = entity_type
        self.regex = regex
        self.members_shrink = members_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.regex is not None:
            result['Regex'] = self.regex
        if self.members_shrink is not None:
            result['Members'] = self.members_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        if m.get('Members') is not None:
            self.members_shrink = m.get('Members')
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
        body: UpdateEntityResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCoreWordRequest(TeaModel):
    def __init__(
        self,
        core_word_name: str = None,
    ):
        self.core_word_name = core_word_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        body: DeleteCoreWordResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteCoreWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveKnowledgeCategoryRequest(TeaModel):
    def __init__(
        self,
        knowledge_id: int = None,
        category_id: int = None,
    ):
        self.knowledge_id = knowledge_id
        self.category_id = category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
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
        body: MoveKnowledgeCategoryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = MoveKnowledgeCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIntentRequest(TeaModel):
    def __init__(
        self,
        intent_definition: IntentCreateDTO = None,
        dialog_id: int = None,
    ):
        self.intent_definition = intent_definition
        self.dialog_id = dialog_id

    def validate(self):
        if self.intent_definition:
            self.intent_definition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_definition is not None:
            result['IntentDefinition'] = self.intent_definition.to_map()
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentDefinition') is not None:
            temp_model = IntentCreateDTO()
            self.intent_definition = temp_model.from_map(m['IntentDefinition'])
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        return self


class CreateIntentShrinkRequest(TeaModel):
    def __init__(
        self,
        intent_definition_shrink: str = None,
        dialog_id: int = None,
    ):
        self.intent_definition_shrink = intent_definition_shrink
        self.dialog_id = dialog_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_definition_shrink is not None:
            result['IntentDefinition'] = self.intent_definition_shrink
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentDefinition') is not None:
            self.intent_definition_shrink = m.get('IntentDefinition')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        return self


class CreateIntentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        intent_id: int = None,
    ):
        self.request_id = request_id
        self.intent_id = intent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class CreateIntentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateIntentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePerspectiveRequest(TeaModel):
    def __init__(
        self,
        perspective_id: str = None,
        name: str = None,
    ):
        self.perspective_id = perspective_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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
        body: UpdatePerspectiveResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdatePerspectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCategoriesRequest(TeaModel):
    def __init__(
        self,
        parent_category_id: int = None,
        show_childrens: bool = None,
        knowledge_type: int = None,
    ):
        self.parent_category_id = parent_category_id
        self.show_childrens = show_childrens
        self.knowledge_type = knowledge_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        if self.show_childrens is not None:
            result['ShowChildrens'] = self.show_childrens
        if self.knowledge_type is not None:
            result['KnowledgeType'] = self.knowledge_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        if m.get('ShowChildrens') is not None:
            self.show_childrens = m.get('ShowChildrens')
        if m.get('KnowledgeType') is not None:
            self.knowledge_type = m.get('KnowledgeType')
        return self


class QueryCategoriesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        categories: List[Children] = None,
    ):
        self.request_id = request_id
        self.categories = categories

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Categories'] = []
        if self.categories is not None:
            for k in self.categories:
                result['Categories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.categories = []
        if m.get('Categories') is not None:
            for k in m.get('Categories'):
                temp_model = Children()
                self.categories.append(temp_model.from_map(k))
        return self


class QueryCategoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryCategoriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryCategoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDialogRequest(TeaModel):
    def __init__(
        self,
        dialog_id: int = None,
    ):
        self.dialog_id = dialog_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        body: DeleteDialogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDialogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryKnowledgesRequest(TeaModel):
    def __init__(
        self,
        knowledge_title: str = None,
        core_word_name: str = None,
        page_number: int = None,
        page_size: int = None,
        category_id: int = None,
    ):
        self.knowledge_title = knowledge_title
        self.core_word_name = core_word_name
        self.page_number = page_number
        self.page_size = page_size
        self.category_id = category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_title is not None:
            result['KnowledgeTitle'] = self.knowledge_title
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeTitle') is not None:
            self.knowledge_title = m.get('KnowledgeTitle')
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        return self


class QueryKnowledgesResponseBodyKnowledges(TeaModel):
    def __init__(
        self,
        knowledge_status: int = None,
        end_date: str = None,
        knowledge_id: int = None,
        create_user_name: str = None,
        create_time: str = None,
        start_date: str = None,
        knowledge_title: str = None,
        modify_user_name: str = None,
        core_words: List[str] = None,
        version: str = None,
        category_id: int = None,
        modify_time: str = None,
    ):
        self.knowledge_status = knowledge_status
        self.end_date = end_date
        self.knowledge_id = knowledge_id
        self.create_user_name = create_user_name
        self.create_time = create_time
        self.start_date = start_date
        self.knowledge_title = knowledge_title
        self.modify_user_name = modify_user_name
        self.core_words = core_words
        self.version = version
        self.category_id = category_id
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_status is not None:
            result['KnowledgeStatus'] = self.knowledge_status
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.knowledge_title is not None:
            result['KnowledgeTitle'] = self.knowledge_title
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.core_words is not None:
            result['CoreWords'] = self.core_words
        if self.version is not None:
            result['Version'] = self.version
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeStatus') is not None:
            self.knowledge_status = m.get('KnowledgeStatus')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('KnowledgeTitle') is not None:
            self.knowledge_title = m.get('KnowledgeTitle')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('CoreWords') is not None:
            self.core_words = m.get('CoreWords')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class QueryKnowledgesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        knowledges: List[QueryKnowledgesResponseBodyKnowledges] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.knowledges = knowledges

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Knowledges'] = []
        if self.knowledges is not None:
            for k in self.knowledges:
                result['Knowledges'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.knowledges = []
        if m.get('Knowledges') is not None:
            for k in m.get('Knowledges'):
                temp_model = QueryKnowledgesResponseBodyKnowledges()
                self.knowledges.append(temp_model.from_map(k))
        return self


class QueryKnowledgesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryKnowledgesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryKnowledgesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncResultRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetAsyncResultResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAsyncResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAsyncResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAsyncResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDialogRequest(TeaModel):
    def __init__(
        self,
        dialog_id: int = None,
    ):
        self.dialog_id = dialog_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        return self


class DescribeDialogResponseBody(TeaModel):
    def __init__(
        self,
        status: int = None,
        modify_time: str = None,
        description: str = None,
        request_id: str = None,
        create_time: str = None,
        create_user_id: str = None,
        dialog_id: int = None,
        create_user_name: str = None,
        is_online: bool = None,
        dialog_name: str = None,
        modify_user_id: str = None,
        modify_user_name: str = None,
        is_sample_dialog: bool = None,
    ):
        self.status = status
        self.modify_time = modify_time
        self.description = description
        self.request_id = request_id
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.dialog_id = dialog_id
        self.create_user_name = create_user_name
        self.is_online = is_online
        self.dialog_name = dialog_name
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.is_sample_dialog = is_sample_dialog

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.description is not None:
            result['Description'] = self.description
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.is_online is not None:
            result['IsOnline'] = self.is_online
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.is_sample_dialog is not None:
            result['IsSampleDialog'] = self.is_sample_dialog
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('IsOnline') is not None:
            self.is_online = m.get('IsOnline')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('IsSampleDialog') is not None:
            self.is_sample_dialog = m.get('IsSampleDialog')
        return self


class DescribeDialogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDialogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDialogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIntentRequest(TeaModel):
    def __init__(
        self,
        intent_definition: IntentCreateDTO = None,
        intent_id: int = None,
    ):
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
        if self.intent_definition is not None:
            result['IntentDefinition'] = self.intent_definition.to_map()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentDefinition') is not None:
            temp_model = IntentCreateDTO()
            self.intent_definition = temp_model.from_map(m['IntentDefinition'])
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class UpdateIntentShrinkRequest(TeaModel):
    def __init__(
        self,
        intent_definition_shrink: str = None,
        intent_id: int = None,
    ):
        self.intent_definition_shrink = intent_definition_shrink
        self.intent_id = intent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_definition_shrink is not None:
            result['IntentDefinition'] = self.intent_definition_shrink
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentDefinition') is not None:
            self.intent_definition_shrink = m.get('IntentDefinition')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class UpdateIntentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        intent_id: int = None,
    ):
        self.request_id = request_id
        self.intent_id = intent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class UpdateIntentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateIntentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveSynonymRequest(TeaModel):
    def __init__(
        self,
        core_word_name: str = None,
        synonym: str = None,
    ):
        self.core_word_name = core_word_name
        self.synonym = synonym

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        if self.synonym is not None:
            result['Synonym'] = self.synonym
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        body: RemoveSynonymResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveSynonymResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDialogFlowRequest(TeaModel):
    def __init__(
        self,
        dialog_id: int = None,
    ):
        self.dialog_id = dialog_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        return self


class DescribeDialogFlowResponseBody(TeaModel):
    def __init__(
        self,
        status: int = None,
        modify_time: str = None,
        account_id: str = None,
        request_id: str = None,
        instance_id: str = None,
        module_name: str = None,
        create_time: str = None,
        create_user_id: str = None,
        templates: str = None,
        dialog_id: int = None,
        global_vars: Dict[str, Any] = None,
        create_user_name: str = None,
        module_id: int = None,
        module_definition: PaasProcessData = None,
        dialog_name: str = None,
        modify_user_id: str = None,
        modify_user_name: str = None,
        tags: str = None,
    ):
        self.status = status
        self.modify_time = modify_time
        self.account_id = account_id
        self.request_id = request_id
        self.instance_id = instance_id
        self.module_name = module_name
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.templates = templates
        self.dialog_id = dialog_id
        self.global_vars = global_vars
        self.create_user_name = create_user_name
        self.module_id = module_id
        self.module_definition = module_definition
        self.dialog_name = dialog_name
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.tags = tags

    def validate(self):
        if self.module_definition:
            self.module_definition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.templates is not None:
            result['Templates'] = self.templates
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.global_vars is not None:
            result['GlobalVars'] = self.global_vars
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_definition is not None:
            result['ModuleDefinition'] = self.module_definition.to_map()
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('Templates') is not None:
            self.templates = m.get('Templates')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('GlobalVars') is not None:
            self.global_vars = m.get('GlobalVars')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleDefinition') is not None:
            temp_model = PaasProcessData()
            self.module_definition = temp_model.from_map(m['ModuleDefinition'])
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class DescribeDialogFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDialogFlowResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDialogFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ActivatePerspectiveRequest(TeaModel):
    def __init__(
        self,
        perspective_id: str = None,
    ):
        self.perspective_id = perspective_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        body: ActivatePerspectiveResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ActivatePerspectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeKnowledgeRequest(TeaModel):
    def __init__(
        self,
        knowledge_id: int = None,
    ):
        self.knowledge_id = knowledge_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class DescribeKnowledgeResponseBodySimQuestions(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        sim_question_id: int = None,
        title: str = None,
        modify_time: str = None,
    ):
        self.create_time = create_time
        self.sim_question_id = sim_question_id
        self.title = title
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.sim_question_id is not None:
            result['SimQuestionId'] = self.sim_question_id
        if self.title is not None:
            result['Title'] = self.title
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SimQuestionId') is not None:
            self.sim_question_id = m.get('SimQuestionId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class DescribeKnowledgeResponseBodySolutions(TeaModel):
    def __init__(
        self,
        perspective_ids: List[str] = None,
        summary: str = None,
        create_time: str = None,
        plain_text: str = None,
        solution_id: int = None,
        content: str = None,
        modify_time: str = None,
    ):
        self.perspective_ids = perspective_ids
        self.summary = summary
        self.create_time = create_time
        self.plain_text = plain_text
        self.solution_id = solution_id
        self.content = content
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.perspective_ids is not None:
            result['PerspectiveIds'] = self.perspective_ids
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.plain_text is not None:
            result['PlainText'] = self.plain_text
        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id
        if self.content is not None:
            result['Content'] = self.content
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PerspectiveIds') is not None:
            self.perspective_ids = m.get('PerspectiveIds')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PlainText') is not None:
            self.plain_text = m.get('PlainText')
        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
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


class DescribeKnowledgeResponseBody(TeaModel):
    def __init__(
        self,
        knowledge_title: str = None,
        category_id: int = None,
        modify_time: str = None,
        core_words: List[str] = None,
        request_id: str = None,
        create_time: str = None,
        knowledge_id: int = None,
        key_words: List[str] = None,
        end_date: str = None,
        create_user_name: str = None,
        start_date: str = None,
        sim_questions: List[DescribeKnowledgeResponseBodySimQuestions] = None,
        solutions: List[DescribeKnowledgeResponseBodySolutions] = None,
        version: int = None,
        modify_user_name: str = None,
        knowledge_status: int = None,
        outlines: List[DescribeKnowledgeResponseBodyOutlines] = None,
        knowledge_type: int = None,
    ):
        self.knowledge_title = knowledge_title
        self.category_id = category_id
        self.modify_time = modify_time
        self.core_words = core_words
        self.request_id = request_id
        self.create_time = create_time
        self.knowledge_id = knowledge_id
        self.key_words = key_words
        self.end_date = end_date
        self.create_user_name = create_user_name
        self.start_date = start_date
        self.sim_questions = sim_questions
        self.solutions = solutions
        self.version = version
        self.modify_user_name = modify_user_name
        self.knowledge_status = knowledge_status
        self.outlines = outlines
        self.knowledge_type = knowledge_type

    def validate(self):
        if self.sim_questions:
            for k in self.sim_questions:
                if k:
                    k.validate()
        if self.solutions:
            for k in self.solutions:
                if k:
                    k.validate()
        if self.outlines:
            for k in self.outlines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_title is not None:
            result['KnowledgeTitle'] = self.knowledge_title
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.core_words is not None:
            result['CoreWords'] = self.core_words
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.key_words is not None:
            result['KeyWords'] = self.key_words
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        result['SimQuestions'] = []
        if self.sim_questions is not None:
            for k in self.sim_questions:
                result['SimQuestions'].append(k.to_map() if k else None)
        result['Solutions'] = []
        if self.solutions is not None:
            for k in self.solutions:
                result['Solutions'].append(k.to_map() if k else None)
        if self.version is not None:
            result['Version'] = self.version
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.knowledge_status is not None:
            result['KnowledgeStatus'] = self.knowledge_status
        result['Outlines'] = []
        if self.outlines is not None:
            for k in self.outlines:
                result['Outlines'].append(k.to_map() if k else None)
        if self.knowledge_type is not None:
            result['KnowledgeType'] = self.knowledge_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeTitle') is not None:
            self.knowledge_title = m.get('KnowledgeTitle')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('CoreWords') is not None:
            self.core_words = m.get('CoreWords')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
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
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('KnowledgeStatus') is not None:
            self.knowledge_status = m.get('KnowledgeStatus')
        self.outlines = []
        if m.get('Outlines') is not None:
            for k in m.get('Outlines'):
                temp_model = DescribeKnowledgeResponseBodyOutlines()
                self.outlines.append(temp_model.from_map(k))
        if m.get('KnowledgeType') is not None:
            self.knowledge_type = m.get('KnowledgeType')
        return self


class DescribeKnowledgeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeKnowledgeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPerspectivesResponseBodyPerspectives(TeaModel):
    def __init__(
        self,
        status: int = None,
        modify_user_name: str = None,
        create_user_name: str = None,
        create_time: str = None,
        perspective_id: str = None,
        self_define: bool = None,
        name: str = None,
        perspective_code: str = None,
        modify_time: str = None,
    ):
        self.status = status
        self.modify_user_name = modify_user_name
        self.create_user_name = create_user_name
        self.create_time = create_time
        self.perspective_id = perspective_id
        self.self_define = self_define
        self.name = name
        self.perspective_code = perspective_code
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        if self.self_define is not None:
            result['SelfDefine'] = self.self_define
        if self.name is not None:
            result['Name'] = self.name
        if self.perspective_code is not None:
            result['PerspectiveCode'] = self.perspective_code
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        if m.get('SelfDefine') is not None:
            self.self_define = m.get('SelfDefine')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PerspectiveCode') is not None:
            self.perspective_code = m.get('PerspectiveCode')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class QueryPerspectivesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        perspectives: List[QueryPerspectivesResponseBodyPerspectives] = None,
    ):
        self.request_id = request_id
        self.perspectives = perspectives

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Perspectives'] = []
        if self.perspectives is not None:
            for k in self.perspectives:
                result['Perspectives'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.perspectives = []
        if m.get('Perspectives') is not None:
            for k in m.get('Perspectives'):
                temp_model = QueryPerspectivesResponseBodyPerspectives()
                self.perspectives.append(temp_model.from_map(k))
        return self


class QueryPerspectivesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryPerspectivesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryPerspectivesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePerspectiveRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreatePerspectiveResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        perspective_id: str = None,
    ):
        self.request_id = request_id
        self.perspective_id = perspective_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')
        return self


class CreatePerspectiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePerspectiveResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreatePerspectiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEntityRequest(TeaModel):
    def __init__(
        self,
        entity_id: int = None,
    ):
        self.entity_id = entity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        body: DeleteEntityResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteEntityResponseBody()
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
        entity_id: int = None,
        remove_type: str = None,
        member: RemoveEntityMemberRequestMember = None,
    ):
        self.entity_id = entity_id
        self.remove_type = remove_type
        self.member = member

    def validate(self):
        if self.member:
            self.member.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.remove_type is not None:
            result['RemoveType'] = self.remove_type
        if self.member is not None:
            result['Member'] = self.member.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('RemoveType') is not None:
            self.remove_type = m.get('RemoveType')
        if m.get('Member') is not None:
            temp_model = RemoveEntityMemberRequestMember()
            self.member = temp_model.from_map(m['Member'])
        return self


class RemoveEntityMemberShrinkRequest(TeaModel):
    def __init__(
        self,
        entity_id: int = None,
        remove_type: str = None,
        member_shrink: str = None,
    ):
        self.entity_id = entity_id
        self.remove_type = remove_type
        self.member_shrink = member_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.remove_type is not None:
            result['RemoveType'] = self.remove_type
        if self.member_shrink is not None:
            result['Member'] = self.member_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('RemoveType') is not None:
            self.remove_type = m.get('RemoveType')
        if m.get('Member') is not None:
            self.member_shrink = m.get('Member')
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
        body: RemoveEntityMemberResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveEntityMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TestDialogFlowRequest(TeaModel):
    def __init__(
        self,
        dialog_id: int = None,
    ):
        self.dialog_id = dialog_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        body: TestDialogFlowResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TestDialogFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBotDsStatDataRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        return self


class GetBotDsStatDataResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        request_id: str = None,
        datas: List[Dict[str, Any]] = None,
    ):
        self.cost_time = cost_time
        self.request_id = request_id
        self.datas = datas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.datas is not None:
            result['Datas'] = self.datas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        return self


class GetBotDsStatDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetBotDsStatDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetBotDsStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FeedbackRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        session_id: str = None,
        message_id: str = None,
        feedback: str = None,
    ):
        self.instance_id = instance_id
        self.session_id = session_id
        self.message_id = message_id
        self.feedback = feedback

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        return self


class FeedbackResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        feedback: str = None,
        message_id: str = None,
    ):
        self.request_id = request_id
        self.feedback = feedback
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class FeedbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FeedbackResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = FeedbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        session_id: str = None,
        knowledge_id: str = None,
        sender_id: str = None,
        sender_nick: str = None,
        tag: str = None,
        utterance: str = None,
        recommend: bool = None,
        recommend_num: int = None,
        intent_name: str = None,
        vendor_param: str = None,
        perspective: List[str] = None,
    ):
        self.instance_id = instance_id
        self.session_id = session_id
        self.knowledge_id = knowledge_id
        self.sender_id = sender_id
        self.sender_nick = sender_nick
        self.tag = tag
        self.utterance = utterance
        self.recommend = recommend
        self.recommend_num = recommend_num
        self.intent_name = intent_name
        self.vendor_param = vendor_param
        self.perspective = perspective

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.sender_nick is not None:
            result['SenderNick'] = self.sender_nick
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        if self.recommend is not None:
            result['Recommend'] = self.recommend
        if self.recommend_num is not None:
            result['RecommendNum'] = self.recommend_num
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.vendor_param is not None:
            result['VendorParam'] = self.vendor_param
        if self.perspective is not None:
            result['Perspective'] = self.perspective
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SenderNick') is not None:
            self.sender_nick = m.get('SenderNick')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        if m.get('Recommend') is not None:
            self.recommend = m.get('Recommend')
        if m.get('RecommendNum') is not None:
            self.recommend_num = m.get('RecommendNum')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('VendorParam') is not None:
            self.vendor_param = m.get('VendorParam')
        if m.get('Perspective') is not None:
            self.perspective = m.get('Perspective')
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
        hit_statement: str = None,
        summary: str = None,
        related_knowledges: List[ChatResponseBodyMessagesKnowledgeRelatedKnowledges] = None,
        category: str = None,
        title: str = None,
        content: str = None,
        answer_source: str = None,
        id: str = None,
    ):
        self.hit_statement = hit_statement
        self.summary = summary
        self.related_knowledges = related_knowledges
        self.category = category
        self.title = title
        self.content = content
        self.answer_source = answer_source
        self.id = id

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
        if self.hit_statement is not None:
            result['HitStatement'] = self.hit_statement
        if self.summary is not None:
            result['Summary'] = self.summary
        result['RelatedKnowledges'] = []
        if self.related_knowledges is not None:
            for k in self.related_knowledges:
                result['RelatedKnowledges'].append(k.to_map() if k else None)
        if self.category is not None:
            result['Category'] = self.category
        if self.title is not None:
            result['Title'] = self.title
        if self.content is not None:
            result['Content'] = self.content
        if self.answer_source is not None:
            result['AnswerSource'] = self.answer_source
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HitStatement') is not None:
            self.hit_statement = m.get('HitStatement')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        self.related_knowledges = []
        if m.get('RelatedKnowledges') is not None:
            for k in m.get('RelatedKnowledges'):
                temp_model = ChatResponseBodyMessagesKnowledgeRelatedKnowledges()
                self.related_knowledges.append(temp_model.from_map(k))
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ChatResponseBodyMessagesTextSlots(TeaModel):
    def __init__(
        self,
        value: str = None,
        origin: str = None,
        name: str = None,
        is_hit: bool = None,
    ):
        self.value = value
        self.origin = origin
        self.name = name
        self.is_hit = is_hit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.name is not None:
            result['Name'] = self.name
        if self.is_hit is not None:
            result['IsHit'] = self.is_hit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('IsHit') is not None:
            self.is_hit = m.get('IsHit')
        return self


class ChatResponseBodyMessagesText(TeaModel):
    def __init__(
        self,
        hit_statement: str = None,
        dialog_name: str = None,
        article_title: str = None,
        answer_source: str = None,
        slots: List[ChatResponseBodyMessagesTextSlots] = None,
        intent_name: str = None,
        meta_data: str = None,
        node_name: str = None,
        external_flags: Dict[str, Any] = None,
        ext: Dict[str, Any] = None,
        user_defined_chat_title: str = None,
        content: str = None,
        node_id: str = None,
    ):
        self.hit_statement = hit_statement
        self.dialog_name = dialog_name
        self.article_title = article_title
        self.answer_source = answer_source
        self.slots = slots
        self.intent_name = intent_name
        self.meta_data = meta_data
        self.node_name = node_name
        self.external_flags = external_flags
        self.ext = ext
        self.user_defined_chat_title = user_defined_chat_title
        self.content = content
        self.node_id = node_id

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
        if self.hit_statement is not None:
            result['HitStatement'] = self.hit_statement
        if self.dialog_name is not None:
            result['DialogName'] = self.dialog_name
        if self.article_title is not None:
            result['ArticleTitle'] = self.article_title
        if self.answer_source is not None:
            result['AnswerSource'] = self.answer_source
        result['Slots'] = []
        if self.slots is not None:
            for k in self.slots:
                result['Slots'].append(k.to_map() if k else None)
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.meta_data is not None:
            result['MetaData'] = self.meta_data
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.external_flags is not None:
            result['ExternalFlags'] = self.external_flags
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.user_defined_chat_title is not None:
            result['UserDefinedChatTitle'] = self.user_defined_chat_title
        if self.content is not None:
            result['Content'] = self.content
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HitStatement') is not None:
            self.hit_statement = m.get('HitStatement')
        if m.get('DialogName') is not None:
            self.dialog_name = m.get('DialogName')
        if m.get('ArticleTitle') is not None:
            self.article_title = m.get('ArticleTitle')
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        self.slots = []
        if m.get('Slots') is not None:
            for k in m.get('Slots'):
                temp_model = ChatResponseBodyMessagesTextSlots()
                self.slots.append(temp_model.from_map(k))
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('MetaData') is not None:
            self.meta_data = m.get('MetaData')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('ExternalFlags') is not None:
            self.external_flags = m.get('ExternalFlags')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('UserDefinedChatTitle') is not None:
            self.user_defined_chat_title = m.get('UserDefinedChatTitle')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class ChatResponseBodyMessagesRecommends(TeaModel):
    def __init__(
        self,
        summary: str = None,
        knowledge_id: str = None,
        category: str = None,
        title: str = None,
        answer_source: str = None,
        content: str = None,
    ):
        self.summary = summary
        self.knowledge_id = knowledge_id
        self.category = category
        self.title = title
        self.answer_source = answer_source
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        if self.category is not None:
            result['Category'] = self.category
        if self.title is not None:
            result['Title'] = self.title
        if self.answer_source is not None:
            result['AnswerSource'] = self.answer_source
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('AnswerSource') is not None:
            self.answer_source = m.get('AnswerSource')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class ChatResponseBodyMessages(TeaModel):
    def __init__(
        self,
        type: str = None,
        knowledge: ChatResponseBodyMessagesKnowledge = None,
        text: ChatResponseBodyMessagesText = None,
        recommends: List[ChatResponseBodyMessagesRecommends] = None,
    ):
        self.type = type
        self.knowledge = knowledge
        self.text = text
        self.recommends = recommends

    def validate(self):
        if self.knowledge:
            self.knowledge.validate()
        if self.text:
            self.text.validate()
        if self.recommends:
            for k in self.recommends:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.knowledge is not None:
            result['Knowledge'] = self.knowledge.to_map()
        if self.text is not None:
            result['Text'] = self.text.to_map()
        result['Recommends'] = []
        if self.recommends is not None:
            for k in self.recommends:
                result['Recommends'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Knowledge') is not None:
            temp_model = ChatResponseBodyMessagesKnowledge()
            self.knowledge = temp_model.from_map(m['Knowledge'])
        if m.get('Text') is not None:
            temp_model = ChatResponseBodyMessagesText()
            self.text = temp_model.from_map(m['Text'])
        self.recommends = []
        if m.get('Recommends') is not None:
            for k in m.get('Recommends'):
                temp_model = ChatResponseBodyMessagesRecommends()
                self.recommends.append(temp_model.from_map(k))
        return self


class ChatResponseBody(TeaModel):
    def __init__(
        self,
        messages: List[ChatResponseBodyMessages] = None,
        request_id: str = None,
        tag: str = None,
        session_id: str = None,
        message_id: str = None,
    ):
        self.messages = messages
        self.request_id = request_id
        self.tag = tag
        self.session_id = session_id
        self.message_id = message_id

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
        result['Messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['Messages'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('Messages') is not None:
            for k in m.get('Messages'):
                temp_model = ChatResponseBodyMessages()
                self.messages.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class ChatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ChatResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ChatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableKnowledgeRequest(TeaModel):
    def __init__(
        self,
        knowledge_id: int = None,
    ):
        self.knowledge_id = knowledge_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        body: DisableKnowledgeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotHotDsDatasRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
        limit: int = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class ListBotHotDsDatasResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        request_id: str = None,
        datas: List[Dict[str, Any]] = None,
    ):
        self.cost_time = cost_time
        self.request_id = request_id
        self.datas = datas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.datas is not None:
            result['Datas'] = self.datas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        return self


class ListBotHotDsDatasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListBotHotDsDatasResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListBotHotDsDatasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBotKnowledgeStatDataRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        return self


class GetBotKnowledgeStatDataResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        request_id: str = None,
        datas: List[Dict[str, Any]] = None,
    ):
        self.cost_time = cost_time
        self.request_id = request_id
        self.datas = datas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.datas is not None:
            result['Datas'] = self.datas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        return self


class GetBotKnowledgeStatDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetBotKnowledgeStatDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetBotKnowledgeStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateKnowledgeRequestKnowledgeSolutions(TeaModel):
    def __init__(
        self,
        content: str = None,
        plain_text: str = None,
        solution_id: int = None,
        perspective_ids: List[str] = None,
        action: str = None,
    ):
        self.content = content
        self.plain_text = plain_text
        self.solution_id = solution_id
        self.perspective_ids = perspective_ids
        self.action = action

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.plain_text is not None:
            result['PlainText'] = self.plain_text
        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id
        if self.perspective_ids is not None:
            result['PerspectiveIds'] = self.perspective_ids
        if self.action is not None:
            result['Action'] = self.action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('PlainText') is not None:
            self.plain_text = m.get('PlainText')
        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')
        if m.get('PerspectiveIds') is not None:
            self.perspective_ids = m.get('PerspectiveIds')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        return self


class UpdateKnowledgeRequestKnowledgeOutlines(TeaModel):
    def __init__(
        self,
        knowledge_id: int = None,
        title: str = None,
        outline_id: int = None,
        action: str = None,
    ):
        self.knowledge_id = knowledge_id
        self.title = title
        self.outline_id = outline_id
        self.action = action

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
        if self.outline_id is not None:
            result['OutlineId'] = self.outline_id
        if self.action is not None:
            result['Action'] = self.action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('OutlineId') is not None:
            self.outline_id = m.get('OutlineId')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        return self


class UpdateKnowledgeRequestKnowledgeSimQuestions(TeaModel):
    def __init__(
        self,
        title: str = None,
        sim_question_id: int = None,
        action: str = None,
    ):
        self.title = title
        self.sim_question_id = sim_question_id
        self.action = action

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        if self.sim_question_id is not None:
            result['SimQuestionId'] = self.sim_question_id
        if self.action is not None:
            result['Action'] = self.action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('SimQuestionId') is not None:
            self.sim_question_id = m.get('SimQuestionId')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        return self


class UpdateKnowledgeRequestKnowledge(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        knowledge_title: str = None,
        knowledge_type: int = None,
        solutions: List[UpdateKnowledgeRequestKnowledgeSolutions] = None,
        start_date: str = None,
        end_date: str = None,
        outlines: List[UpdateKnowledgeRequestKnowledgeOutlines] = None,
        sim_questions: List[UpdateKnowledgeRequestKnowledgeSimQuestions] = None,
        knowledge_id: int = None,
    ):
        self.category_id = category_id
        self.knowledge_title = knowledge_title
        self.knowledge_type = knowledge_type
        self.solutions = solutions
        self.start_date = start_date
        self.end_date = end_date
        self.outlines = outlines
        self.sim_questions = sim_questions
        self.knowledge_id = knowledge_id

    def validate(self):
        if self.solutions:
            for k in self.solutions:
                if k:
                    k.validate()
        if self.outlines:
            for k in self.outlines:
                if k:
                    k.validate()
        if self.sim_questions:
            for k in self.sim_questions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.knowledge_title is not None:
            result['KnowledgeTitle'] = self.knowledge_title
        if self.knowledge_type is not None:
            result['KnowledgeType'] = self.knowledge_type
        result['Solutions'] = []
        if self.solutions is not None:
            for k in self.solutions:
                result['Solutions'].append(k.to_map() if k else None)
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        result['Outlines'] = []
        if self.outlines is not None:
            for k in self.outlines:
                result['Outlines'].append(k.to_map() if k else None)
        result['SimQuestions'] = []
        if self.sim_questions is not None:
            for k in self.sim_questions:
                result['SimQuestions'].append(k.to_map() if k else None)
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('KnowledgeTitle') is not None:
            self.knowledge_title = m.get('KnowledgeTitle')
        if m.get('KnowledgeType') is not None:
            self.knowledge_type = m.get('KnowledgeType')
        self.solutions = []
        if m.get('Solutions') is not None:
            for k in m.get('Solutions'):
                temp_model = UpdateKnowledgeRequestKnowledgeSolutions()
                self.solutions.append(temp_model.from_map(k))
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
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
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class UpdateKnowledgeRequest(TeaModel):
    def __init__(
        self,
        knowledge: UpdateKnowledgeRequestKnowledge = None,
    ):
        self.knowledge = knowledge

    def validate(self):
        if self.knowledge:
            self.knowledge.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge is not None:
            result['Knowledge'] = self.knowledge.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Knowledge') is not None:
            temp_model = UpdateKnowledgeRequestKnowledge()
            self.knowledge = temp_model.from_map(m['Knowledge'])
        return self


class UpdateKnowledgeShrinkRequest(TeaModel):
    def __init__(
        self,
        knowledge_shrink: str = None,
    ):
        self.knowledge_shrink = knowledge_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_shrink is not None:
            result['Knowledge'] = self.knowledge_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Knowledge') is not None:
            self.knowledge_shrink = m.get('Knowledge')
        return self


class UpdateKnowledgeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        knowledge_id: int = None,
    ):
        self.request_id = request_id
        self.knowledge_id = knowledge_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class UpdateKnowledgeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateKnowledgeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateKnowledgeRequestKnowledgeSolutions(TeaModel):
    def __init__(
        self,
        content: str = None,
        plain_text: str = None,
        perspective_ids: List[str] = None,
    ):
        self.content = content
        self.plain_text = plain_text
        self.perspective_ids = perspective_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.plain_text is not None:
            result['PlainText'] = self.plain_text
        if self.perspective_ids is not None:
            result['PerspectiveIds'] = self.perspective_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('PlainText') is not None:
            self.plain_text = m.get('PlainText')
        if m.get('PerspectiveIds') is not None:
            self.perspective_ids = m.get('PerspectiveIds')
        return self


class CreateKnowledgeRequestKnowledgeOutlines(TeaModel):
    def __init__(
        self,
        knowledge_id: int = None,
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


class CreateKnowledgeRequestKnowledge(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        knowledge_title: str = None,
        knowledge_type: int = None,
        solutions: List[CreateKnowledgeRequestKnowledgeSolutions] = None,
        start_date: str = None,
        end_date: str = None,
        outlines: List[CreateKnowledgeRequestKnowledgeOutlines] = None,
        sim_questions: List[CreateKnowledgeRequestKnowledgeSimQuestions] = None,
    ):
        self.category_id = category_id
        self.knowledge_title = knowledge_title
        self.knowledge_type = knowledge_type
        self.solutions = solutions
        self.start_date = start_date
        self.end_date = end_date
        self.outlines = outlines
        self.sim_questions = sim_questions

    def validate(self):
        if self.solutions:
            for k in self.solutions:
                if k:
                    k.validate()
        if self.outlines:
            for k in self.outlines:
                if k:
                    k.validate()
        if self.sim_questions:
            for k in self.sim_questions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.knowledge_title is not None:
            result['KnowledgeTitle'] = self.knowledge_title
        if self.knowledge_type is not None:
            result['KnowledgeType'] = self.knowledge_type
        result['Solutions'] = []
        if self.solutions is not None:
            for k in self.solutions:
                result['Solutions'].append(k.to_map() if k else None)
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        result['Outlines'] = []
        if self.outlines is not None:
            for k in self.outlines:
                result['Outlines'].append(k.to_map() if k else None)
        result['SimQuestions'] = []
        if self.sim_questions is not None:
            for k in self.sim_questions:
                result['SimQuestions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('KnowledgeTitle') is not None:
            self.knowledge_title = m.get('KnowledgeTitle')
        if m.get('KnowledgeType') is not None:
            self.knowledge_type = m.get('KnowledgeType')
        self.solutions = []
        if m.get('Solutions') is not None:
            for k in m.get('Solutions'):
                temp_model = CreateKnowledgeRequestKnowledgeSolutions()
                self.solutions.append(temp_model.from_map(k))
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
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
        return self


class CreateKnowledgeRequest(TeaModel):
    def __init__(
        self,
        knowledge: CreateKnowledgeRequestKnowledge = None,
    ):
        self.knowledge = knowledge

    def validate(self):
        if self.knowledge:
            self.knowledge.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge is not None:
            result['Knowledge'] = self.knowledge.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Knowledge') is not None:
            temp_model = CreateKnowledgeRequestKnowledge()
            self.knowledge = temp_model.from_map(m['Knowledge'])
        return self


class CreateKnowledgeShrinkRequest(TeaModel):
    def __init__(
        self,
        knowledge_shrink: str = None,
    ):
        self.knowledge_shrink = knowledge_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_shrink is not None:
            result['Knowledge'] = self.knowledge_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Knowledge') is not None:
            self.knowledge_shrink = m.get('Knowledge')
        return self


class CreateKnowledgeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        knowledge_id: int = None,
    ):
        self.request_id = request_id
        self.knowledge_id = knowledge_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')
        return self


class CreateKnowledgeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateKnowledgeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIntentRequest(TeaModel):
    def __init__(
        self,
        intent_id: int = None,
    ):
        self.intent_id = intent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class DeleteIntentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        intent_id: int = None,
    ):
        self.request_id = request_id
        self.intent_id = intent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class DeleteIntentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteIntentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteKnowledgeRequest(TeaModel):
    def __init__(
        self,
        knowledge_id: int = None,
    ):
        self.knowledge_id = knowledge_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        body: DeleteKnowledgeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteKnowledgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotChatHistorysRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
        limit: int = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class ListBotChatHistorysResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        request_id: str = None,
        datas: List[Dict[str, Any]] = None,
    ):
        self.cost_time = cost_time
        self.request_id = request_id
        self.datas = datas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.datas is not None:
            result['Datas'] = self.datas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        return self


class ListBotChatHistorysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListBotChatHistorysResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListBotChatHistorysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableDialogFlowRequest(TeaModel):
    def __init__(
        self,
        dialog_id: int = None,
    ):
        self.dialog_id = dialog_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        body: DisableDialogFlowResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableDialogFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBotsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryBotsResponseBodyBots(TeaModel):
    def __init__(
        self,
        introduction: str = None,
        avatar: str = None,
        time_zone: str = None,
        create_time: str = None,
        language_code: str = None,
        instance_id: str = None,
        name: str = None,
    ):
        self.introduction = introduction
        self.avatar = avatar
        self.time_zone = time_zone
        self.create_time = create_time
        self.language_code = language_code
        self.instance_id = instance_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.language_code is not None:
            result['LanguageCode'] = self.language_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class QueryBotsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        bots: List[QueryBotsResponseBodyBots] = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.total_count = total_count
        self.bots = bots
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Bots'] = []
        if self.bots is not None:
            for k in self.bots:
                result['Bots'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.bots = []
        if m.get('Bots') is not None:
            for k in m.get('Bots'):
                temp_model = QueryBotsResponseBodyBots()
                self.bots.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class QueryBotsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryBotsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryBotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishDialogFlowRequest(TeaModel):
    def __init__(
        self,
        dialog_id: int = None,
    ):
        self.dialog_id = dialog_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        body: PublishDialogFlowResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PublishDialogFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotColdKnowledgesRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
        limit: int = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class ListBotColdKnowledgesResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        request_id: str = None,
        datas: List[Dict[str, Any]] = None,
    ):
        self.cost_time = cost_time
        self.request_id = request_id
        self.datas = datas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.datas is not None:
            result['Datas'] = self.datas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        return self


class ListBotColdKnowledgesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListBotColdKnowledgesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListBotColdKnowledgesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCoreWordRequest(TeaModel):
    def __init__(
        self,
        core_word_name: str = None,
    ):
        self.core_word_name = core_word_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        return self


class CreateCoreWordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        core_word_code: str = None,
    ):
        self.request_id = request_id
        self.core_word_code = core_word_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.core_word_code is not None:
            result['CoreWordCode'] = self.core_word_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CoreWordCode') is not None:
            self.core_word_code = m.get('CoreWordCode')
        return self


class CreateCoreWordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCoreWordResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateCoreWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBotRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        body: DeleteBotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteBotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySystemEntitiesRequest(TeaModel):
    def __init__(
        self,
        entity_name: str = None,
    ):
        self.entity_name = entity_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        system_entities: List[QuerySystemEntitiesResponseBodySystemEntities] = None,
        request_id: str = None,
    ):
        self.system_entities = system_entities
        self.request_id = request_id

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
        result['SystemEntities'] = []
        if self.system_entities is not None:
            for k in self.system_entities:
                result['SystemEntities'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.system_entities = []
        if m.get('SystemEntities') is not None:
            for k in m.get('SystemEntities'):
                temp_model = QuerySystemEntitiesResponseBodySystemEntities()
                self.system_entities.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QuerySystemEntitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySystemEntitiesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QuerySystemEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConversationLogsRequest(TeaModel):
    def __init__(
        self,
        session_id: str = None,
    ):
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class ListConversationLogsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        chat_logs: List[Dict[str, Any]] = None,
        rounds: int = None,
    ):
        self.request_id = request_id
        self.chat_logs = chat_logs
        self.rounds = rounds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.chat_logs is not None:
            result['ChatLogs'] = self.chat_logs
        if self.rounds is not None:
            result['Rounds'] = self.rounds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ChatLogs') is not None:
            self.chat_logs = m.get('ChatLogs')
        if m.get('Rounds') is not None:
            self.rounds = m.get('Rounds')
        return self


class ListConversationLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListConversationLogsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListConversationLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBotChatDataRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        return self


class GetBotChatDataResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        request_id: str = None,
        datas: List[Dict[str, Any]] = None,
    ):
        self.cost_time = cost_time
        self.request_id = request_id
        self.datas = datas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.datas is not None:
            result['Datas'] = self.datas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        return self


class GetBotChatDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetBotChatDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetBotChatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCoreWordRequest(TeaModel):
    def __init__(
        self,
        core_word_name: str = None,
    ):
        self.core_word_name = core_word_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        return self


class DescribeCoreWordResponseBody(TeaModel):
    def __init__(
        self,
        core_word_name: str = None,
        synonyms: List[str] = None,
        modify_time: str = None,
        request_id: str = None,
        create_time: str = None,
        core_word_code: str = None,
    ):
        self.core_word_name = core_word_name
        self.synonyms = synonyms
        self.modify_time = modify_time
        self.request_id = request_id
        self.create_time = create_time
        self.core_word_code = core_word_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.core_word_name is not None:
            result['CoreWordName'] = self.core_word_name
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.core_word_code is not None:
            result['CoreWordCode'] = self.core_word_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoreWordName') is not None:
            self.core_word_name = m.get('CoreWordName')
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CoreWordCode') is not None:
            self.core_word_code = m.get('CoreWordCode')
        return self


class DescribeCoreWordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCoreWordResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCoreWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBotSessionDataRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        return self


class GetBotSessionDataResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        request_id: str = None,
        datas: List[Dict[str, Any]] = None,
    ):
        self.cost_time = cost_time
        self.request_id = request_id
        self.datas = datas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.datas is not None:
            result['Datas'] = self.datas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        return self


class GetBotSessionDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetBotSessionDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetBotSessionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotHotKnowledgesRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
        limit: int = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class ListBotHotKnowledgesResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        request_id: str = None,
        datas: List[Dict[str, Any]] = None,
    ):
        self.cost_time = cost_time
        self.request_id = request_id
        self.datas = datas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.datas is not None:
            result['Datas'] = self.datas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        return self


class ListBotHotKnowledgesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListBotHotKnowledgesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListBotHotKnowledgesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEntitiesRequest(TeaModel):
    def __init__(
        self,
        entity_name: str = None,
        dialog_id: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.entity_name = entity_name
        self.dialog_id = dialog_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryEntitiesResponseBodyEntitiesMembers(TeaModel):
    def __init__(
        self,
        synonyms: List[str] = None,
        member_name: str = None,
    ):
        self.synonyms = synonyms
        self.member_name = member_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        return self


class QueryEntitiesResponseBodyEntities(TeaModel):
    def __init__(
        self,
        members: List[QueryEntitiesResponseBodyEntitiesMembers] = None,
        modify_user_id: str = None,
        modify_user_name: str = None,
        entity_id: int = None,
        create_user_name: str = None,
        create_time: str = None,
        regex: str = None,
        entity_type: str = None,
        create_user_id: str = None,
        entity_name: str = None,
        modify_time: str = None,
    ):
        self.members = members
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.entity_id = entity_id
        self.create_user_name = create_user_name
        self.create_time = create_time
        self.regex = regex
        self.entity_type = entity_type
        self.create_user_id = create_user_id
        self.entity_name = entity_name
        self.modify_time = modify_time

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
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.regex is not None:
            result['Regex'] = self.regex
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = QueryEntitiesResponseBodyEntitiesMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class QueryEntitiesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        entities: List[QueryEntitiesResponseBodyEntities] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.entities = entities

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Entities'] = []
        if self.entities is not None:
            for k in self.entities:
                result['Entities'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.entities = []
        if m.get('Entities') is not None:
            for k in m.get('Entities'):
                temp_model = QueryEntitiesResponseBodyEntities()
                self.entities.append(temp_model.from_map(k))
        return self


class QueryEntitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryEntitiesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryEntitiesResponseBody()
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
        dialog_id: int = None,
        module_definition: UpdateDialogFlowRequestModuleDefinition = None,
    ):
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
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.module_definition is not None:
            result['ModuleDefinition'] = self.module_definition.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('ModuleDefinition') is not None:
            temp_model = UpdateDialogFlowRequestModuleDefinition()
            self.module_definition = temp_model.from_map(m['ModuleDefinition'])
        return self


class UpdateDialogFlowShrinkRequest(TeaModel):
    def __init__(
        self,
        dialog_id: int = None,
        module_definition_shrink: str = None,
    ):
        self.dialog_id = dialog_id
        self.module_definition_shrink = module_definition_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.module_definition_shrink is not None:
            result['ModuleDefinition'] = self.module_definition_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        body: UpdateDialogFlowResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDialogFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBotDsDetailsRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        robot_instance_id: str = None,
        limit: int = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.robot_instance_id = robot_instance_id
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.robot_instance_id is not None:
            result['RobotInstanceId'] = self.robot_instance_id
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RobotInstanceId') is not None:
            self.robot_instance_id = m.get('RobotInstanceId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class ListBotDsDetailsResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: str = None,
        request_id: str = None,
        datas: List[Dict[str, Any]] = None,
    ):
        self.cost_time = cost_time
        self.request_id = request_id
        self.datas = datas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.datas is not None:
            result['Datas'] = self.datas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Datas') is not None:
            self.datas = m.get('Datas')
        return self


class ListBotDsDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListBotDsDetailsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListBotDsDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        utterance: str = None,
        session_id: str = None,
        recommend_num: int = None,
        perspective: List[str] = None,
    ):
        self.instance_id = instance_id
        self.utterance = utterance
        self.session_id = session_id
        self.recommend_num = recommend_num
        self.perspective = perspective

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.recommend_num is not None:
            result['RecommendNum'] = self.recommend_num
        if self.perspective is not None:
            result['Perspective'] = self.perspective
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('RecommendNum') is not None:
            self.recommend_num = m.get('RecommendNum')
        if m.get('Perspective') is not None:
            self.perspective = m.get('Perspective')
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
        request_id: str = None,
        associate: List[AssociateResponseBodyAssociate] = None,
        session_id: str = None,
        message_id: str = None,
    ):
        self.request_id = request_id
        self.associate = associate
        self.session_id = session_id
        self.message_id = message_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Associate'] = []
        if self.associate is not None:
            for k in self.associate:
                result['Associate'].append(k.to_map() if k else None)
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.associate = []
        if m.get('Associate') is not None:
            for k in m.get('Associate'):
                temp_model = AssociateResponseBodyAssociate()
                self.associate.append(temp_model.from_map(k))
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class AssociateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssociateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AssociateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCategoryRequest(TeaModel):
    def __init__(
        self,
        parent_category_id: int = None,
        name: str = None,
        knowledge_type: int = None,
        biz_code: str = None,
    ):
        self.parent_category_id = parent_category_id
        self.name = name
        self.knowledge_type = knowledge_type
        self.biz_code = biz_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id
        if self.name is not None:
            result['Name'] = self.name
        if self.knowledge_type is not None:
            result['KnowledgeType'] = self.knowledge_type
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('KnowledgeType') is not None:
            self.knowledge_type = m.get('KnowledgeType')
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
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
        body: CreateCategoryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEntitiesRequest(TeaModel):
    def __init__(
        self,
        entity_id: int = None,
    ):
        self.entity_id = entity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        return self


class DescribeEntitiesResponseBodyMembers(TeaModel):
    def __init__(
        self,
        synonyms: List[str] = None,
        member_name: str = None,
    ):
        self.synonyms = synonyms
        self.member_name = member_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        return self


class DescribeEntitiesResponseBody(TeaModel):
    def __init__(
        self,
        entity_id: int = None,
        entity_type: str = None,
        modify_time: str = None,
        modify_user_id: str = None,
        request_id: str = None,
        regex: str = None,
        entity_name: str = None,
        create_time: str = None,
        modify_user_name: str = None,
        create_user_id: str = None,
        create_user_name: str = None,
        members: List[DescribeEntitiesResponseBodyMembers] = None,
    ):
        self.entity_id = entity_id
        self.entity_type = entity_type
        self.modify_time = modify_time
        self.modify_user_id = modify_user_id
        self.request_id = request_id
        self.regex = regex
        self.entity_name = entity_name
        self.create_time = create_time
        self.modify_user_name = modify_user_name
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.members = members

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
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.regex is not None:
            result['Regex'] = self.regex
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = DescribeEntitiesResponseBodyMembers()
                self.members.append(temp_model.from_map(k))
        return self


class DescribeEntitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEntitiesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


