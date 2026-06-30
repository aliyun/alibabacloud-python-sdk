# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class AgentInfo(DaraModel):
    def __init__(
        self,
        agent_description: str = None,
        agent_name: str = None,
        id: int = None,
        input_type: str = None,
        instruction_type: str = None,
        instruction_type_param: main_models.AgentInfoInstructionTypeParam = None,
        model_type: str = None,
    ):
        self.agent_description = agent_description
        self.agent_name = agent_name
        self.id = id
        self.input_type = input_type
        self.instruction_type = instruction_type
        self.instruction_type_param = instruction_type_param
        self.model_type = model_type

    def validate(self):
        if self.instruction_type_param:
            self.instruction_type_param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_description is not None:
            result['AgentDescription'] = self.agent_description

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.id is not None:
            result['Id'] = self.id

        if self.input_type is not None:
            result['InputType'] = self.input_type

        if self.instruction_type is not None:
            result['InstructionType'] = self.instruction_type

        if self.instruction_type_param is not None:
            result['InstructionTypeParam'] = self.instruction_type_param.to_map()

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentDescription') is not None:
            self.agent_description = m.get('AgentDescription')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InputType') is not None:
            self.input_type = m.get('InputType')

        if m.get('InstructionType') is not None:
            self.instruction_type = m.get('InstructionType')

        if m.get('InstructionTypeParam') is not None:
            temp_model = main_models.AgentInfoInstructionTypeParam()
            self.instruction_type_param = temp_model.from_map(m.get('InstructionTypeParam'))

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        return self

class AgentInfoInstructionTypeParam(DaraModel):
    def __init__(
        self,
        custom_prompt_param: main_models.AgentInfoInstructionTypeParamCustomPromptParam = None,
        fields_param: main_models.AgentInfoInstructionTypeParamFieldsParam = None,
        service_inspection_param: main_models.AgentInfoInstructionTypeParamServiceInspectionParam = None,
        tag_category_param: main_models.AgentInfoInstructionTypeParamTagCategoryParam = None,
    ):
        self.custom_prompt_param = custom_prompt_param
        self.fields_param = fields_param
        self.service_inspection_param = service_inspection_param
        self.tag_category_param = tag_category_param

    def validate(self):
        if self.custom_prompt_param:
            self.custom_prompt_param.validate()
        if self.fields_param:
            self.fields_param.validate()
        if self.service_inspection_param:
            self.service_inspection_param.validate()
        if self.tag_category_param:
            self.tag_category_param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_prompt_param is not None:
            result['CustomPromptParam'] = self.custom_prompt_param.to_map()

        if self.fields_param is not None:
            result['FieldsParam'] = self.fields_param.to_map()

        if self.service_inspection_param is not None:
            result['ServiceInspectionParam'] = self.service_inspection_param.to_map()

        if self.tag_category_param is not None:
            result['TagCategoryParam'] = self.tag_category_param.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomPromptParam') is not None:
            temp_model = main_models.AgentInfoInstructionTypeParamCustomPromptParam()
            self.custom_prompt_param = temp_model.from_map(m.get('CustomPromptParam'))

        if m.get('FieldsParam') is not None:
            temp_model = main_models.AgentInfoInstructionTypeParamFieldsParam()
            self.fields_param = temp_model.from_map(m.get('FieldsParam'))

        if m.get('ServiceInspectionParam') is not None:
            temp_model = main_models.AgentInfoInstructionTypeParamServiceInspectionParam()
            self.service_inspection_param = temp_model.from_map(m.get('ServiceInspectionParam'))

        if m.get('TagCategoryParam') is not None:
            temp_model = main_models.AgentInfoInstructionTypeParamTagCategoryParam()
            self.tag_category_param = temp_model.from_map(m.get('TagCategoryParam'))

        return self

class AgentInfoInstructionTypeParamTagCategoryParam(DaraModel):
    def __init__(
        self,
        name_desc_pair_list: List[main_models.AgentInfoInstructionTypeParamTagCategoryParamNameDescPairList] = None,
    ):
        self.name_desc_pair_list = name_desc_pair_list

    def validate(self):
        if self.name_desc_pair_list:
            for v1 in self.name_desc_pair_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NameDescPairList'] = []
        if self.name_desc_pair_list is not None:
            for k1 in self.name_desc_pair_list:
                result['NameDescPairList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.name_desc_pair_list = []
        if m.get('NameDescPairList') is not None:
            for k1 in m.get('NameDescPairList'):
                temp_model = main_models.AgentInfoInstructionTypeParamTagCategoryParamNameDescPairList()
                self.name_desc_pair_list.append(temp_model.from_map(k1))

        return self

class AgentInfoInstructionTypeParamTagCategoryParamNameDescPairList(DaraModel):
    def __init__(
        self,
        desc: str = None,
        name: str = None,
        value_list: List[str] = None,
    ):
        self.desc = desc
        self.name = name
        self.value_list = value_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['Desc'] = self.desc

        if self.name is not None:
            result['Name'] = self.name

        if self.value_list is not None:
            result['ValueList'] = self.value_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ValueList') is not None:
            self.value_list = m.get('ValueList')

        return self

class AgentInfoInstructionTypeParamServiceInspectionParam(DaraModel):
    def __init__(
        self,
        dimensions: List[main_models.AgentInfoInstructionTypeParamServiceInspectionParamDimensions] = None,
        scene_description: str = None,
        scene_name: str = None,
    ):
        self.dimensions = dimensions
        self.scene_description = scene_description
        self.scene_name = scene_name

    def validate(self):
        if self.dimensions:
            for v1 in self.dimensions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k1 in self.dimensions:
                result['Dimensions'].append(k1.to_map() if k1 else None)

        if self.scene_description is not None:
            result['SceneDescription'] = self.scene_description

        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k1 in m.get('Dimensions'):
                temp_model = main_models.AgentInfoInstructionTypeParamServiceInspectionParamDimensions()
                self.dimensions.append(temp_model.from_map(k1))

        if m.get('SceneDescription') is not None:
            self.scene_description = m.get('SceneDescription')

        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        return self

class AgentInfoInstructionTypeParamServiceInspectionParamDimensions(DaraModel):
    def __init__(
        self,
        desc: str = None,
        dimension: str = None,
    ):
        self.desc = desc
        self.dimension = dimension

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['Desc'] = self.desc

        if self.dimension is not None:
            result['Dimension'] = self.dimension

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        return self

class AgentInfoInstructionTypeParamFieldsParam(DaraModel):
    def __init__(
        self,
        name_desc_pair_list: List[main_models.AgentInfoInstructionTypeParamFieldsParamNameDescPairList] = None,
    ):
        self.name_desc_pair_list = name_desc_pair_list

    def validate(self):
        if self.name_desc_pair_list:
            for v1 in self.name_desc_pair_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NameDescPairList'] = []
        if self.name_desc_pair_list is not None:
            for k1 in self.name_desc_pair_list:
                result['NameDescPairList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.name_desc_pair_list = []
        if m.get('NameDescPairList') is not None:
            for k1 in m.get('NameDescPairList'):
                temp_model = main_models.AgentInfoInstructionTypeParamFieldsParamNameDescPairList()
                self.name_desc_pair_list.append(temp_model.from_map(k1))

        return self

class AgentInfoInstructionTypeParamFieldsParamNameDescPairList(DaraModel):
    def __init__(
        self,
        desc: str = None,
        name: str = None,
        value: str = None,
    ):
        self.desc = desc
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['Desc'] = self.desc

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class AgentInfoInstructionTypeParamCustomPromptParam(DaraModel):
    def __init__(
        self,
        custom_prompt: str = None,
        name_desc_pair_list: List[main_models.AgentInfoInstructionTypeParamCustomPromptParamNameDescPairList] = None,
    ):
        self.custom_prompt = custom_prompt
        self.name_desc_pair_list = name_desc_pair_list

    def validate(self):
        if self.name_desc_pair_list:
            for v1 in self.name_desc_pair_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_prompt is not None:
            result['CustomPrompt'] = self.custom_prompt

        result['NameDescPairList'] = []
        if self.name_desc_pair_list is not None:
            for k1 in self.name_desc_pair_list:
                result['NameDescPairList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomPrompt') is not None:
            self.custom_prompt = m.get('CustomPrompt')

        self.name_desc_pair_list = []
        if m.get('NameDescPairList') is not None:
            for k1 in m.get('NameDescPairList'):
                temp_model = main_models.AgentInfoInstructionTypeParamCustomPromptParamNameDescPairList()
                self.name_desc_pair_list.append(temp_model.from_map(k1))

        return self



class AgentInfoInstructionTypeParamCustomPromptParamNameDescPairList(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
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

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

