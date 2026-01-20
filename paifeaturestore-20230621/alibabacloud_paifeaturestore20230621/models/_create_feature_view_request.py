# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class CreateFeatureViewRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        feature_entity_id: str = None,
        fields: List[main_models.CreateFeatureViewRequestFields] = None,
        name: str = None,
        project_id: str = None,
        register_datasource_id: str = None,
        register_table: str = None,
        sync_online_table: bool = None,
        ttl: int = None,
        tags: List[str] = None,
        type: str = None,
        write_method: str = None,
        write_to_feature_db: bool = None,
    ):
        self.config = config
        self.feature_entity_id = feature_entity_id
        self.fields = fields
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.project_id = project_id
        self.register_datasource_id = register_datasource_id
        self.register_table = register_table
        # This parameter is required.
        self.sync_online_table = sync_online_table
        self.ttl = ttl
        self.tags = tags
        # This parameter is required.
        self.type = type
        # This parameter is required.
        self.write_method = write_method
        self.write_to_feature_db = write_to_feature_db

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
        if self.config is not None:
            result['Config'] = self.config

        if self.feature_entity_id is not None:
            result['FeatureEntityId'] = self.feature_entity_id

        result['Fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['Fields'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.register_datasource_id is not None:
            result['RegisterDatasourceId'] = self.register_datasource_id

        if self.register_table is not None:
            result['RegisterTable'] = self.register_table

        if self.sync_online_table is not None:
            result['SyncOnlineTable'] = self.sync_online_table

        if self.ttl is not None:
            result['TTL'] = self.ttl

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.type is not None:
            result['Type'] = self.type

        if self.write_method is not None:
            result['WriteMethod'] = self.write_method

        if self.write_to_feature_db is not None:
            result['WriteToFeatureDB'] = self.write_to_feature_db

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('FeatureEntityId') is not None:
            self.feature_entity_id = m.get('FeatureEntityId')

        self.fields = []
        if m.get('Fields') is not None:
            for k1 in m.get('Fields'):
                temp_model = main_models.CreateFeatureViewRequestFields()
                self.fields.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegisterDatasourceId') is not None:
            self.register_datasource_id = m.get('RegisterDatasourceId')

        if m.get('RegisterTable') is not None:
            self.register_table = m.get('RegisterTable')

        if m.get('SyncOnlineTable') is not None:
            self.sync_online_table = m.get('SyncOnlineTable')

        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WriteMethod') is not None:
            self.write_method = m.get('WriteMethod')

        if m.get('WriteToFeatureDB') is not None:
            self.write_to_feature_db = m.get('WriteToFeatureDB')

        return self

class CreateFeatureViewRequestFields(DaraModel):
    def __init__(
        self,
        attributes: List[str] = None,
        name: str = None,
        transform: List[main_models.CreateFeatureViewRequestFieldsTransform] = None,
        type: str = None,
    ):
        self.attributes = attributes
        self.name = name
        self.transform = transform
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
                temp_model = main_models.CreateFeatureViewRequestFieldsTransform()
                self.transform.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateFeatureViewRequestFieldsTransform(DaraModel):
    def __init__(
        self,
        input: List[main_models.CreateFeatureViewRequestFieldsTransformInput] = None,
        llmconfig_id: int = None,
        type: str = None,
    ):
        self.input = input
        self.llmconfig_id = llmconfig_id
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
                temp_model = main_models.CreateFeatureViewRequestFieldsTransformInput()
                self.input.append(temp_model.from_map(k1))

        if m.get('LLMConfigId') is not None:
            self.llmconfig_id = m.get('LLMConfigId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateFeatureViewRequestFieldsTransformInput(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        self.name = name
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

