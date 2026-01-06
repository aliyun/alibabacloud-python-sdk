# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class CreateConnectionRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        configs: Dict[str, str] = None,
        connection_name: str = None,
        connection_type: str = None,
        description: str = None,
        models: List[main_models.CreateConnectionRequestModels] = None,
        resource_meta: main_models.CreateConnectionRequestResourceMeta = None,
        secrets: Dict[str, str] = None,
        workspace_id: str = None,
    ):
        # The accessibility of the workspace. Valid values:
        # 
        # *   PRIVATE: The workspace is accessible only to you and the administrator of the workspace. This is the default value.
        # *   PUBLIC: The workspace is accessible to all users in the workspace.
        self.accessibility = accessibility
        # The connection configurations, in key-value pairs. The key varies based on the connection type. For more information, see the supplementary notes below the request parameters.
        # 
        # This parameter is required.
        self.configs = configs
        # The connection name.
        # 
        # This parameter is required.
        self.connection_name = connection_name
        # The connection type. Valid values:
        # 
        # *   DashScopeConnection: Alibaba Cloud Model Studio connection
        # *   OpenLLMConnection: open source model connection
        # *   MilvusConnection: Milvus connection
        # *   OpenSearchConnection: OpenSearch connection
        # *   LindormConnection: Lindorm connection
        # *   ElasticsearchConnection: Elasticsearch connection
        # *   HologresConnection: Hologres connection
        # *   RDSConnection: RDS connection
        # *   CustomConnection: custom connection
        self.connection_type = connection_type
        # The connection description.
        self.description = description
        # The models, which apply to model service connections.
        self.models = models
        # The instance resource information of the connection, which applies to database connections.
        self.resource_meta = resource_meta
        # The configuration to be encrypted. Examples: the database logon account and password and the key of the model service.
        self.secrets = secrets
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.models:
            for v1 in self.models:
                 if v1:
                    v1.validate()
        if self.resource_meta:
            self.resource_meta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.configs is not None:
            result['Configs'] = self.configs

        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name

        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type

        if self.description is not None:
            result['Description'] = self.description

        result['Models'] = []
        if self.models is not None:
            for k1 in self.models:
                result['Models'].append(k1.to_map() if k1 else None)

        if self.resource_meta is not None:
            result['ResourceMeta'] = self.resource_meta.to_map()

        if self.secrets is not None:
            result['Secrets'] = self.secrets

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('Configs') is not None:
            self.configs = m.get('Configs')

        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')

        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.models = []
        if m.get('Models') is not None:
            for k1 in m.get('Models'):
                temp_model = main_models.CreateConnectionRequestModels()
                self.models.append(temp_model.from_map(k1))

        if m.get('ResourceMeta') is not None:
            temp_model = main_models.CreateConnectionRequestResourceMeta()
            self.resource_meta = temp_model.from_map(m.get('ResourceMeta'))

        if m.get('Secrets') is not None:
            self.secrets = m.get('Secrets')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class CreateConnectionRequestResourceMeta(DaraModel):
    def __init__(
        self,
        extra: str = None,
        instance_id: str = None,
        instance_name: str = None,
    ):
        self.extra = extra
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extra is not None:
            result['Extra'] = self.extra

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        return self

class CreateConnectionRequestModels(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        model: str = None,
        model_type: str = None,
        tool_call: bool = None,
    ):
        # The display name of the model.
        self.display_name = display_name
        # The model identifier.
        self.model = model
        # The model type. Valid values:
        # 
        # *   LLM
        # *   Embedding
        # *   ReRank
        self.model_type = model_type
        # Specifies whether a tool can be called by using ToolCall. Valid values:
        # 
        # *   true
        # *   false
        self.tool_call = tool_call

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.model is not None:
            result['Model'] = self.model

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.tool_call is not None:
            result['ToolCall'] = self.tool_call

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('ToolCall') is not None:
            self.tool_call = m.get('ToolCall')

        return self

