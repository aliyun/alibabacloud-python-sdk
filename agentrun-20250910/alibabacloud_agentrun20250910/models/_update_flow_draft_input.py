# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class UpdateFlowDraftInput(DaraModel):
    def __init__(
        self,
        definition: str = None,
        description: str = None,
        environment_configuration: main_models.EnvironmentConfiguration = None,
        execution_role_arn: str = None,
        external_storage_location: str = None,
    ):
        # 工作流的 FDL 定义
        self.definition = definition
        # 工作流的描述信息
        self.description = description
        # 工作流执行期间可以访问的环境变量配置，包含一组命名变量列表
        self.environment_configuration = environment_configuration
        # 工作流执行时使用的 RAM 角色 ARN
        self.execution_role_arn = execution_role_arn
        # 工作流执行历史的外部存储位置
        self.external_storage_location = external_storage_location

    def validate(self):
        if self.environment_configuration:
            self.environment_configuration.validate()

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

        return self

