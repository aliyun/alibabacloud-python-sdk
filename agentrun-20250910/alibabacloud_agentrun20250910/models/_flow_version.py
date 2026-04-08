# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class FlowVersion(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        definition: str = None,
        description: str = None,
        environment_configuration: main_models.EnvironmentConfiguration = None,
        external_storage_location: str = None,
        flow_id: str = None,
        flow_name: str = None,
        flow_version: str = None,
        logging_configuration: main_models.LoggingConfiguration = None,
        tracing_configuration: main_models.TracingConfiguration = None,
    ):
        # 工作流版本的创建时间，采用ISO 8601格式
        self.created_at = created_at
        # 工作流版本的定义内容（完整快照，仅在 GetFlowVersion 时返回）
        self.definition = definition
        # 工作流版本的描述信息
        self.description = description
        # 工作流版本的环境变量配置（完整快照，仅在 GetFlowVersion 时返回）
        self.environment_configuration = environment_configuration
        # 工作流版本的外部存储位置（完整快照，仅在 GetFlowVersion 时返回）
        self.external_storage_location = external_storage_location
        # 工作流的唯一标识符
        self.flow_id = flow_id
        self.flow_name = flow_name
        # 工作流版本号
        self.flow_version = flow_version
        # 工作流版本的日志配置（完整快照，仅在 GetFlowVersion 时返回）
        self.logging_configuration = logging_configuration
        # 工作流版本的链路追踪配置（完整快照，仅在 GetFlowVersion 时返回）
        self.tracing_configuration = tracing_configuration

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
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.definition is not None:
            result['definition'] = self.definition

        if self.description is not None:
            result['description'] = self.description

        if self.environment_configuration is not None:
            result['environmentConfiguration'] = self.environment_configuration.to_map()

        if self.external_storage_location is not None:
            result['externalStorageLocation'] = self.external_storage_location

        if self.flow_id is not None:
            result['flowId'] = self.flow_id

        if self.flow_name is not None:
            result['flowName'] = self.flow_name

        if self.flow_version is not None:
            result['flowVersion'] = self.flow_version

        if self.logging_configuration is not None:
            result['loggingConfiguration'] = self.logging_configuration.to_map()

        if self.tracing_configuration is not None:
            result['tracingConfiguration'] = self.tracing_configuration.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('definition') is not None:
            self.definition = m.get('definition')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('environmentConfiguration') is not None:
            temp_model = main_models.EnvironmentConfiguration()
            self.environment_configuration = temp_model.from_map(m.get('environmentConfiguration'))

        if m.get('externalStorageLocation') is not None:
            self.external_storage_location = m.get('externalStorageLocation')

        if m.get('flowId') is not None:
            self.flow_id = m.get('flowId')

        if m.get('flowName') is not None:
            self.flow_name = m.get('flowName')

        if m.get('flowVersion') is not None:
            self.flow_version = m.get('flowVersion')

        if m.get('loggingConfiguration') is not None:
            temp_model = main_models.LoggingConfiguration()
            self.logging_configuration = temp_model.from_map(m.get('loggingConfiguration'))

        if m.get('tracingConfiguration') is not None:
            temp_model = main_models.TracingConfiguration()
            self.tracing_configuration = temp_model.from_map(m.get('tracingConfiguration'))

        return self

