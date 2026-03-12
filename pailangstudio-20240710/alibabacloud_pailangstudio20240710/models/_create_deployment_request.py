# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pailangstudio20240710 import models as main_models
from darabonba.model import DaraModel

class CreateDeploymentRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        auto_approval: bool = None,
        chat_history_config: main_models.CreateDeploymentRequestChatHistoryConfig = None,
        content_moderation_config: main_models.CreateDeploymentRequestContentModerationConfig = None,
        deployment_config: str = None,
        description: str = None,
        enable_trace: bool = None,
        resource_id: str = None,
        resource_snapshot_id: str = None,
        resource_type: str = None,
        service_name: str = None,
        work_dir: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.auto_approval = auto_approval
        self.chat_history_config = chat_history_config
        self.content_moderation_config = content_moderation_config
        self.deployment_config = deployment_config
        self.description = description
        self.enable_trace = enable_trace
        self.resource_id = resource_id
        self.resource_snapshot_id = resource_snapshot_id
        self.resource_type = resource_type
        self.service_name = service_name
        self.work_dir = work_dir
        self.workspace_id = workspace_id

    def validate(self):
        if self.chat_history_config:
            self.chat_history_config.validate()
        if self.content_moderation_config:
            self.content_moderation_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.auto_approval is not None:
            result['AutoApproval'] = self.auto_approval

        if self.chat_history_config is not None:
            result['ChatHistoryConfig'] = self.chat_history_config.to_map()

        if self.content_moderation_config is not None:
            result['ContentModerationConfig'] = self.content_moderation_config.to_map()

        if self.deployment_config is not None:
            result['DeploymentConfig'] = self.deployment_config

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_trace is not None:
            result['EnableTrace'] = self.enable_trace

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_snapshot_id is not None:
            result['ResourceSnapshotId'] = self.resource_snapshot_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.work_dir is not None:
            result['WorkDir'] = self.work_dir

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('AutoApproval') is not None:
            self.auto_approval = m.get('AutoApproval')

        if m.get('ChatHistoryConfig') is not None:
            temp_model = main_models.CreateDeploymentRequestChatHistoryConfig()
            self.chat_history_config = temp_model.from_map(m.get('ChatHistoryConfig'))

        if m.get('ContentModerationConfig') is not None:
            temp_model = main_models.CreateDeploymentRequestContentModerationConfig()
            self.content_moderation_config = temp_model.from_map(m.get('ContentModerationConfig'))

        if m.get('DeploymentConfig') is not None:
            self.deployment_config = m.get('DeploymentConfig')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableTrace') is not None:
            self.enable_trace = m.get('EnableTrace')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceSnapshotId') is not None:
            self.resource_snapshot_id = m.get('ResourceSnapshotId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('WorkDir') is not None:
            self.work_dir = m.get('WorkDir')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class CreateDeploymentRequestContentModerationConfig(DaraModel):
    def __init__(
        self,
        enable_input_moderation: bool = None,
        enable_output_moderation: bool = None,
        streaming_moderation_threshold: int = None,
    ):
        # 启用输入内容审查
        self.enable_input_moderation = enable_input_moderation
        # 启用输出内容审查
        self.enable_output_moderation = enable_output_moderation
        # 流式输出内容送审缓存大小
        self.streaming_moderation_threshold = streaming_moderation_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_input_moderation is not None:
            result['EnableInputModeration'] = self.enable_input_moderation

        if self.enable_output_moderation is not None:
            result['EnableOutputModeration'] = self.enable_output_moderation

        if self.streaming_moderation_threshold is not None:
            result['StreamingModerationThreshold'] = self.streaming_moderation_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableInputModeration') is not None:
            self.enable_input_moderation = m.get('EnableInputModeration')

        if m.get('EnableOutputModeration') is not None:
            self.enable_output_moderation = m.get('EnableOutputModeration')

        if m.get('StreamingModerationThreshold') is not None:
            self.streaming_moderation_threshold = m.get('StreamingModerationThreshold')

        return self

class CreateDeploymentRequestChatHistoryConfig(DaraModel):
    def __init__(
        self,
        connection_name: str = None,
        storage_type: str = None,
    ):
        # 连接名称
        self.connection_name = connection_name
        # 存储类型
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

