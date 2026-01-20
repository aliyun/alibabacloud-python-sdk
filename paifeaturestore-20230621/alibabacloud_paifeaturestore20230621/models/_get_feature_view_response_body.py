# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class GetFeatureViewResponseBody(DaraModel):
    def __init__(
        self,
        config: str = None,
        feature_entity_id: str = None,
        feature_entity_name: str = None,
        fields: List[main_models.GetFeatureViewResponseBodyFields] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        gmt_sync_time: str = None,
        join_id: str = None,
        last_sync_config: str = None,
        mock_table_name: str = None,
        name: str = None,
        owner: str = None,
        project_id: str = None,
        project_name: str = None,
        publish_table_script: str = None,
        register_datasource_id: str = None,
        register_datasource_name: str = None,
        register_table: str = None,
        request_id: str = None,
        sync_online_table: bool = None,
        ttl: int = None,
        tags: List[str] = None,
        type: str = None,
        write_method: str = None,
        write_to_feature_db: bool = None,
    ):
        self.config = config
        self.feature_entity_id = feature_entity_id
        self.feature_entity_name = feature_entity_name
        self.fields = fields
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.gmt_sync_time = gmt_sync_time
        self.join_id = join_id
        self.last_sync_config = last_sync_config
        self.mock_table_name = mock_table_name
        self.name = name
        self.owner = owner
        self.project_id = project_id
        self.project_name = project_name
        self.publish_table_script = publish_table_script
        self.register_datasource_id = register_datasource_id
        self.register_datasource_name = register_datasource_name
        self.register_table = register_table
        self.request_id = request_id
        self.sync_online_table = sync_online_table
        self.ttl = ttl
        self.tags = tags
        self.type = type
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

        if self.feature_entity_name is not None:
            result['FeatureEntityName'] = self.feature_entity_name

        result['Fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['Fields'].append(k1.to_map() if k1 else None)

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.gmt_sync_time is not None:
            result['GmtSyncTime'] = self.gmt_sync_time

        if self.join_id is not None:
            result['JoinId'] = self.join_id

        if self.last_sync_config is not None:
            result['LastSyncConfig'] = self.last_sync_config

        if self.mock_table_name is not None:
            result['MockTableName'] = self.mock_table_name

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.publish_table_script is not None:
            result['PublishTableScript'] = self.publish_table_script

        if self.register_datasource_id is not None:
            result['RegisterDatasourceId'] = self.register_datasource_id

        if self.register_datasource_name is not None:
            result['RegisterDatasourceName'] = self.register_datasource_name

        if self.register_table is not None:
            result['RegisterTable'] = self.register_table

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('FeatureEntityName') is not None:
            self.feature_entity_name = m.get('FeatureEntityName')

        self.fields = []
        if m.get('Fields') is not None:
            for k1 in m.get('Fields'):
                temp_model = main_models.GetFeatureViewResponseBodyFields()
                self.fields.append(temp_model.from_map(k1))

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('GmtSyncTime') is not None:
            self.gmt_sync_time = m.get('GmtSyncTime')

        if m.get('JoinId') is not None:
            self.join_id = m.get('JoinId')

        if m.get('LastSyncConfig') is not None:
            self.last_sync_config = m.get('LastSyncConfig')

        if m.get('MockTableName') is not None:
            self.mock_table_name = m.get('MockTableName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('PublishTableScript') is not None:
            self.publish_table_script = m.get('PublishTableScript')

        if m.get('RegisterDatasourceId') is not None:
            self.register_datasource_id = m.get('RegisterDatasourceId')

        if m.get('RegisterDatasourceName') is not None:
            self.register_datasource_name = m.get('RegisterDatasourceName')

        if m.get('RegisterTable') is not None:
            self.register_table = m.get('RegisterTable')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

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

class GetFeatureViewResponseBodyFields(DaraModel):
    def __init__(
        self,
        attributes: List[str] = None,
        name: str = None,
        transform: List[main_models.GetFeatureViewResponseBodyFieldsTransform] = None,
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
                temp_model = main_models.GetFeatureViewResponseBodyFieldsTransform()
                self.transform.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetFeatureViewResponseBodyFieldsTransform(DaraModel):
    def __init__(
        self,
        input: List[main_models.GetFeatureViewResponseBodyFieldsTransformInput] = None,
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
                temp_model = main_models.GetFeatureViewResponseBodyFieldsTransformInput()
                self.input.append(temp_model.from_map(k1))

        if m.get('LLMConfigId') is not None:
            self.llmconfig_id = m.get('LLMConfigId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetFeatureViewResponseBodyFieldsTransformInput(DaraModel):
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

