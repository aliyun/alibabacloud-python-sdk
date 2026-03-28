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
        # Workspace visibility. Valid values:  
        # - PRIVATE: The service is visible only to you and administrators within this workspace.  
        # - PUBLIC: The service is visible to all users within this workspace.
        self.accessibility = accessibility
        # Indicates whether to automatically skip the deployment confirmation step.
        self.auto_approval = auto_approval
        # Chat history configuration.
        self.chat_history_config = chat_history_config
        # Content moderation configuration.
        self.content_moderation_config = content_moderation_config
        # Deployment configuration. For details, see [Deployment Configuration](https://help.aliyun.com/zh/pai/user-guide/parameters-of-model-services) in PAI-EAS.
        self.deployment_config = deployment_config
        # Service description.
        self.description = description
        # Indicates whether to enable Tracing Analysis.
        self.enable_trace = enable_trace
        # The ID of the resource to deploy.
        self.resource_id = resource_id
        # The snapshot ID of the resource to deploy. If this parameter is provided, the system deploys directly based on this snapshot. If this parameter is not provided, the system creates a new snapshot of the resource and then executes the deployment.
        self.resource_snapshot_id = resource_snapshot_id
        # The resource type to deploy. Valid values:
        # * Flow: A pipeline project
        # * Code: A code project
        self.resource_type = resource_type
        # Service name. Format requirements:
        # * Supports lowercase letters, digits, and underscores
        # * Must start with a letter
        # * Length must be 1 to 45 characters
        self.service_name = service_name
        # The OSS working directory for the service. It is used to store the service\\"s runtime logs, conversation history, and other data.
        self.work_dir = work_dir
        # Workspace ID. For information about how to obtain a workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
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
        # Whether to enable security review for input.
        self.enable_input_moderation = enable_input_moderation
        # Whether to enable content moderation for output.
        self.enable_output_moderation = enable_output_moderation
        # The cache size for streaming output content submitted for moderation. Default value: 5.
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
        # Connection name. This parameter is required when the chat history storage type is RDS.
        self.connection_name = connection_name
        # Storage class. Valid values:  
        # * LOCAL: Chat history is stored in a local SQLite file. This option does not support multi-instance deployment.  
        # * OSS: Chat history is stored under a specific path within the service\\"s OSS workspace path.  
        # * RDS: Chat history is stored in an RDS table, and an RDS connection must be specified.
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

