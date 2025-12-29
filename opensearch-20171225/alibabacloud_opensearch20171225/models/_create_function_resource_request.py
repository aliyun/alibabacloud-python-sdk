# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class CreateFunctionResourceRequest(DaraModel):
    def __init__(
        self,
        data: main_models.CreateFunctionResourceRequestData = None,
        description: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # The resource data. The data structure varies with the resource type.
        self.data = data
        # The description of the resource.
        self.description = description
        # The name of the resource.
        self.resource_name = resource_name
        # The resource type.
        # 
        # Valid values:
        # 
        # *   feature_generator
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   raw_file
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.resource_type = resource_type

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.CreateFunctionResourceRequestData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class CreateFunctionResourceRequestData(DaraModel):
    def __init__(
        self,
        content: str = None,
        generators: List[main_models.CreateFunctionResourceRequestDataGenerators] = None,
    ):
        # The content of the file that corresponds to a resource of the raw_file type.
        self.content = content
        # The feature generators that correspond to resources of the feature_generator type.
        self.generators = generators

    def validate(self):
        if self.generators:
            for v1 in self.generators:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        result['Generators'] = []
        if self.generators is not None:
            for k1 in self.generators:
                result['Generators'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        self.generators = []
        if m.get('Generators') is not None:
            for k1 in m.get('Generators'):
                temp_model = main_models.CreateFunctionResourceRequestDataGenerators()
                self.generators.append(temp_model.from_map(k1))

        return self

class CreateFunctionResourceRequestDataGenerators(DaraModel):
    def __init__(
        self,
        generator: str = None,
        input: main_models.CreateFunctionResourceRequestDataGeneratorsInput = None,
        output: str = None,
    ):
        # The type of the feature generator.
        # 
        # Valid values:
        # 
        # *   lookup
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   sequence
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   overlap
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   raw
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   combo
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   id
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.generator = generator
        # The input.
        self.input = input
        # The name of the output feature.
        self.output = output

    def validate(self):
        if self.input:
            self.input.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.generator is not None:
            result['Generator'] = self.generator

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.output is not None:
            result['Output'] = self.output

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Generator') is not None:
            self.generator = m.get('Generator')

        if m.get('Input') is not None:
            temp_model = main_models.CreateFunctionResourceRequestDataGeneratorsInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('Output') is not None:
            self.output = m.get('Output')

        return self

class CreateFunctionResourceRequestDataGeneratorsInput(DaraModel):
    def __init__(
        self,
        features: List[main_models.CreateFunctionResourceRequestDataGeneratorsInputFeatures] = None,
    ):
        # The input features.
        self.features = features

    def validate(self):
        if self.features:
            for v1 in self.features:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Features'] = []
        if self.features is not None:
            for k1 in self.features:
                result['Features'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.features = []
        if m.get('Features') is not None:
            for k1 in m.get('Features'):
                temp_model = main_models.CreateFunctionResourceRequestDataGeneratorsInputFeatures()
                self.features.append(temp_model.from_map(k1))

        return self

class CreateFunctionResourceRequestDataGeneratorsInputFeatures(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The name of the feature.
        self.name = name
        # The type of the feature.
        # 
        # Valid values:
        # 
        # *   item
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   user
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

