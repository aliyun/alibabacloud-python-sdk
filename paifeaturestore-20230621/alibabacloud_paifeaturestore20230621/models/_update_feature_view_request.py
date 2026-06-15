# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class UpdateFeatureViewRequest(DaraModel):
    def __init__(
        self,
        fields: List[main_models.UpdateFeatureViewRequestFields] = None,
    ):
        # A list of fields.
        # 
        # This parameter is required.
        self.fields = fields

    def validate(self):
        if self.fields:
            for v1 in self.fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['Fields'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fields = []
        if m.get('Fields') is not None:
            for k1 in m.get('Fields'):
                temp_model = main_models.UpdateFeatureViewRequestFields()
                self.fields.append(temp_model.from_map(k1))

        return self

class UpdateFeatureViewRequestFields(DaraModel):
    def __init__(
        self,
        attributes: List[str] = None,
        name: str = None,
        transform: List[main_models.UpdateFeatureViewRequestFieldsTransform] = None,
        type: str = None,
    ):
        # A list of field attributes. Valid values:
        # 
        # - `Partition`: Indicates that the field is a partition field.
        # 
        # - `PrimaryKey`: Indicates that the field is a primary key.
        # 
        # - `EventTime`: Indicates that the field is the event time.
        # 
        # This parameter is required.
        self.attributes = attributes
        # The name of the field.
        # 
        # This parameter is required.
        self.name = name
        # The feature generation configuration.
        self.transform = transform
        # The data type of the field.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.transform:
            for v1 in self.transform:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.name is not None:
            result['Name'] = self.name

        result['Transform'] = []
        if self.transform is not None:
            for k1 in self.transform:
                result['Transform'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.transform = []
        if m.get('Transform') is not None:
            for k1 in m.get('Transform'):
                temp_model = main_models.UpdateFeatureViewRequestFieldsTransform()
                self.transform.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateFeatureViewRequestFieldsTransform(DaraModel):
    def __init__(
        self,
        input: List[main_models.UpdateFeatureViewRequestFieldsTransformInput] = None,
        llmconfig_id: int = None,
        type: str = None,
    ):
        # The input fields.
        # 
        # This parameter is required.
        self.input = input
        # The ID of the LLM configuration.
        # 
        # This parameter is required.
        self.llmconfig_id = llmconfig_id
        # The type of feature generation.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.input:
            for v1 in self.input:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Input'] = []
        if self.input is not None:
            for k1 in self.input:
                result['Input'].append(k1.to_map() if k1 else None)

        if self.llmconfig_id is not None:
            result['LLMConfigId'] = self.llmconfig_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.input = []
        if m.get('Input') is not None:
            for k1 in m.get('Input'):
                temp_model = main_models.UpdateFeatureViewRequestFieldsTransformInput()
                self.input.append(temp_model.from_map(k1))

        if m.get('LLMConfigId') is not None:
            self.llmconfig_id = m.get('LLMConfigId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateFeatureViewRequestFieldsTransformInput(DaraModel):
    def __init__(
        self,
        modality: str = None,
        name: str = None,
        type: str = None,
    ):
        # The modality of the input, such as text or image.
        self.modality = modality
        # The name of the input field.
        # 
        # This parameter is required.
        self.name = name
        # The data type of the input field.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.modality is not None:
            result['Modality'] = self.modality

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Modality') is not None:
            self.modality = m.get('Modality')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

