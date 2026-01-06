# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class GetConnectionResponseBody(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        configs: Dict[str, str] = None,
        connection_id: str = None,
        connection_name: str = None,
        connection_type: str = None,
        creator: str = None,
        description: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        models: List[main_models.GetConnectionResponseBodyModels] = None,
        request_id: str = None,
        resource_meta: main_models.GetConnectionResponseBodyResourceMeta = None,
        secrets: Dict[str, str] = None,
        workspace_id: str = None,
    ):
        # The resource accessibility. Valid values:
        # 
        # *   PUBLIC: All members in the workspace can access the workspace.
        # *   PRIVATE: Only the creator can access the workspace.
        self.accessibility = accessibility
        # The connection configuration.
        self.configs = configs
        # The connection ID.
        self.connection_id = connection_id
        # The connection name.
        self.connection_name = connection_name
        # The type of the connection. Valid values:
        # 
        # *   DashScopeConnection: Alibaba Cloud Model Studio connection.
        # *   OpenLLMConnection: Open source model connection.
        # *   MilvusConnection: Milvus connection.
        # *   OpenSearchConnection: OpenSearch connection.
        # *   LindormConnection: Lindorm connection.
        # *   ElasticsearchConnection: Elasticsearch connection.
        # *   HologresConnection: Hologres connection.
        # *   RDSConnection: RDS connection.
        # *   CustomConnection: Custom connection.
        self.connection_type = connection_type
        # The creator of the connection.
        self.creator = creator
        # The connection description.
        self.description = description
        # The time when the connection is created, in UTC. The time follows the ISO 8601 standard.
        self.gmt_create_time = gmt_create_time
        # The time when the connection is modified, in UTC. The time follows the ISO 8601 standard.
        self.gmt_modified_time = gmt_modified_time
        # The models, which apply to model service connections.
        self.models = models
        # The request ID.
        self.request_id = request_id
        # The instance resource information of the connection, which applies to database connections.
        self.resource_meta = resource_meta
        # The encrypted configuration, in key-value pairs. Examples: the database logon password and the key of the model connection.
        self.secrets = secrets
        # The workspace ID.
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

        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id

        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name

        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        result['Models'] = []
        if self.models is not None:
            for k1 in self.models:
                result['Models'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')

        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')

        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        self.models = []
        if m.get('Models') is not None:
            for k1 in m.get('Models'):
                temp_model = main_models.GetConnectionResponseBodyModels()
                self.models.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceMeta') is not None:
            temp_model = main_models.GetConnectionResponseBodyResourceMeta()
            self.resource_meta = temp_model.from_map(m.get('ResourceMeta'))

        if m.get('Secrets') is not None:
            self.secrets = m.get('Secrets')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class GetConnectionResponseBodyResourceMeta(DaraModel):
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

class GetConnectionResponseBodyModels(DaraModel):
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
        # Indicates whether a tool can be called by using ToolCall. Valid values:
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

