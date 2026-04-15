# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class UpdateFlowInput(DaraModel):
    def __init__(
        self,
        definition: str = None,
        description: str = None,
        environment_configuration: main_models.EnvironmentConfiguration = None,
        execution_role_arn: str = None,
        external_storage_location: str = None,
        flow_name: str = None,
        logging_configuration: main_models.LoggingConfiguration = None,
        resource_group_id: str = None,
        tracing_configuration: main_models.TracingConfiguration = None,
        workspace_id: str = None,
    ):
        # 工作流的定义内容，采用JSON或YAML格式
        self.definition = definition
        # 工作流的描述信息，用于说明该工作流的用途和功能
        self.description = description
        # 工作流的环境变量配置，包含一组命名变量列表
        self.environment_configuration = environment_configuration
        # 为工作流提供访问云服务权限的执行角色ARN
        self.execution_role_arn = execution_role_arn
        # 工作流的外部存储位置，如OSS路径
        self.external_storage_location = external_storage_location
        # 工作流的唯一标识名称，用于区分不同的工作流实例
        self.flow_name = flow_name
        # 工作流的日志配置
        self.logging_configuration = logging_configuration
        # 工作流所属的资源组标识符
        self.resource_group_id = resource_group_id
        # 工作流的链路追踪配置
        self.tracing_configuration = tracing_configuration
        # 工作流所属的工作空间标识符，用于资源隔离和权限管理
        self.workspace_id = workspace_id

    def validate(self):
        if self.environment_configuration:
            self.environment_configuration.validate()
        if self.logging_configuration:
            self.logging_configuration.validate()
        if self.tracing_configuration:
            self.tracing_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.definition is not None:
            result['definition'] = self.definition

        if self.description is not None:
            result['description'] = self.description

        if self.environment_configuration is not None:
            result['environmentConfiguration'] = self.environment_configuration.to_map()

        if self.execution_role_arn is not None:
            result['executionRoleArn'] = self.execution_role_arn

        if self.external_storage_location is not None:
            result['externalStorageLocation'] = self.external_storage_location

        if self.flow_name is not None:
            result['flowName'] = self.flow_name

        if self.logging_configuration is not None:
            result['loggingConfiguration'] = self.logging_configuration.to_map()

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.tracing_configuration is not None:
            result['tracingConfiguration'] = self.tracing_configuration.to_map()

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('definition') is not None:
            self.definition = m.get('definition')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('environmentConfiguration') is not None:
            temp_model = main_models.EnvironmentConfiguration()
            self.environment_configuration = temp_model.from_map(m.get('environmentConfiguration'))

        if m.get('executionRoleArn') is not None:
            self.execution_role_arn = m.get('executionRoleArn')

        if m.get('externalStorageLocation') is not None:
            self.external_storage_location = m.get('externalStorageLocation')

        if m.get('flowName') is not None:
            self.flow_name = m.get('flowName')

        if m.get('loggingConfiguration') is not None:
            temp_model = main_models.LoggingConfiguration()
            self.logging_configuration = temp_model.from_map(m.get('loggingConfiguration'))

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('tracingConfiguration') is not None:
            temp_model = main_models.TracingConfiguration()
            self.tracing_configuration = temp_model.from_map(m.get('tracingConfiguration'))

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

