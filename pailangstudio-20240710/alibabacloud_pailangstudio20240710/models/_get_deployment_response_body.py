# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pailangstudio20240710 import models as main_models
from darabonba.model import DaraModel

class GetDeploymentResponseBody(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        auto_approval: bool = None,
        chat_history_config: main_models.GetDeploymentResponseBodyChatHistoryConfig = None,
        content_moderation_config: main_models.GetDeploymentResponseBodyContentModerationConfig = None,
        creator: str = None,
        deployment_config: str = None,
        deployment_id: str = None,
        deployment_stages: List[main_models.GetDeploymentResponseBodyDeploymentStages] = None,
        deployment_status: str = None,
        description: str = None,
        enable_trace: bool = None,
        error_message: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        operation_type: str = None,
        request_id: str = None,
        resource_id: str = None,
        resource_snapshot_id: str = None,
        resource_type: str = None,
        service_name: str = None,
        work_dir: str = None,
        workspace_id: str = None,
    ):
        # The workspace visibility. Valid values:  
        # - PRIVATE: The resource is visible only to you and administrators in this workspace.  
        # - PUBLIC: The resource is visible to all users in this workspace.
        self.accessibility = accessibility
        # Indicates whether deployment confirmation is automatically skipped.
        self.auto_approval = auto_approval
        # Chat history configuration.
        self.chat_history_config = chat_history_config
        # Content moderation configuration.
        self.content_moderation_config = content_moderation_config
        # Creator ID.
        self.creator = creator
        # Deployment configuration. For details, see [Deployment Configuration](https://help.aliyun.com/zh/pai/user-guide/parameters-of-model-services) in PAI-EAS documentation.
        self.deployment_config = deployment_config
        # The ID of the deployment job.
        self.deployment_id = deployment_id
        # Stage information of the deployment.
        self.deployment_stages = deployment_stages
        # Task Status. Valid values:  
        # * Creating: Creating.  
        # * Failed: Deployment failed.  
        # * Stopping: Stopping.  
        # * Waiting: Waiting.  
        # * Starting: Starting.  
        # * Running: Running.  
        # * Pending: Pending.  
        # * WaitForConfirm: Waiting for confirmation.  
        # * Canceled: Canceled.  
        # * Succeed: Succeeded.
        self.deployment_status = deployment_status
        # The service description.
        self.description = description
        # Indicates whether Tracing Analysis is enabled.
        self.enable_trace = enable_trace
        # Error message.
        self.error_message = error_message
        # Creation Time.
        self.gmt_create_time = gmt_create_time
        # Updated At.
        self.gmt_modified_time = gmt_modified_time
        # Operation Type. Valid values:  
        # * Create: Create a new service.  
        # * Update: Update an existing service.
        self.operation_type = operation_type
        # The request ID.
        self.request_id = request_id
        # The ID of the resource to be deployed.
        self.resource_id = resource_id
        # The snapshot ID of the resource to be deployed. If this parameter is provided, the system deploys directly based on this snapshot. If not provided, the system creates a new snapshot of the resource before deployment.
        self.resource_snapshot_id = resource_snapshot_id
        # The resource type to be deployed. Valid values:  
        # * Flow: A pipeline project  
        # * Code: A Code project
        self.resource_type = resource_type
        # Service Name. Format requirements:  
        # * Supports lowercase letters, digits, and underscores.  
        # * Must start with a letter.  
        # * Length must be 1–45 characters.
        self.service_name = service_name
        # The OSS working directory for the service. It stores runtime logs, conversation history, and other data.
        self.work_dir = work_dir
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.chat_history_config:
            self.chat_history_config.validate()
        if self.content_moderation_config:
            self.content_moderation_config.validate()
        if self.deployment_stages:
            for v1 in self.deployment_stages:
                 if v1:
                    v1.validate()

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

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.deployment_config is not None:
            result['DeploymentConfig'] = self.deployment_config

        if self.deployment_id is not None:
            result['DeploymentId'] = self.deployment_id

        result['DeploymentStages'] = []
        if self.deployment_stages is not None:
            for k1 in self.deployment_stages:
                result['DeploymentStages'].append(k1.to_map() if k1 else None)

        if self.deployment_status is not None:
            result['DeploymentStatus'] = self.deployment_status

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_trace is not None:
            result['EnableTrace'] = self.enable_trace

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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
            temp_model = main_models.GetDeploymentResponseBodyChatHistoryConfig()
            self.chat_history_config = temp_model.from_map(m.get('ChatHistoryConfig'))

        if m.get('ContentModerationConfig') is not None:
            temp_model = main_models.GetDeploymentResponseBodyContentModerationConfig()
            self.content_moderation_config = temp_model.from_map(m.get('ContentModerationConfig'))

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DeploymentConfig') is not None:
            self.deployment_config = m.get('DeploymentConfig')

        if m.get('DeploymentId') is not None:
            self.deployment_id = m.get('DeploymentId')

        self.deployment_stages = []
        if m.get('DeploymentStages') is not None:
            for k1 in m.get('DeploymentStages'):
                temp_model = main_models.GetDeploymentResponseBodyDeploymentStages()
                self.deployment_stages.append(temp_model.from_map(k1))

        if m.get('DeploymentStatus') is not None:
            self.deployment_status = m.get('DeploymentStatus')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableTrace') is not None:
            self.enable_trace = m.get('EnableTrace')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

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

class GetDeploymentResponseBodyDeploymentStages(DaraModel):
    def __init__(
        self,
        description: str = None,
        error_message: str = None,
        gmt_end_time: str = None,
        gmt_start_time: str = None,
        stage: int = None,
        stage_info: str = None,
        stage_name: str = None,
        stage_status: str = None,
    ):
        # Deployment stage description.
        self.description = description
        # Error message.
        self.error_message = error_message
        # End time.
        self.gmt_end_time = gmt_end_time
        # Start Time.
        self.gmt_start_time = gmt_start_time
        # Deployment stage.
        self.stage = stage
        # Deployment stage information.
        self.stage_info = stage_info
        # Deployment stage name.
        self.stage_name = stage_name
        # Deployment stage status. Valid values:  
        # * NotStarted: Not started.  
        # * WaitForConfirm: Waiting for confirmation.  
        # * Waiting: Waiting.  
        # * Creating: Creating.  
        # * Running: Running.  
        # * Succeed: Succeeded.  
        # * Failed: Failed.  
        # * Canceled: Canceled.
        self.stage_status = stage_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.gmt_end_time is not None:
            result['GmtEndTime'] = self.gmt_end_time

        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time

        if self.stage is not None:
            result['Stage'] = self.stage

        if self.stage_info is not None:
            result['StageInfo'] = self.stage_info

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        if self.stage_status is not None:
            result['StageStatus'] = self.stage_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('GmtEndTime') is not None:
            self.gmt_end_time = m.get('GmtEndTime')

        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')

        if m.get('Stage') is not None:
            self.stage = m.get('Stage')

        if m.get('StageInfo') is not None:
            self.stage_info = m.get('StageInfo')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        if m.get('StageStatus') is not None:
            self.stage_status = m.get('StageStatus')

        return self

class GetDeploymentResponseBodyContentModerationConfig(DaraModel):
    def __init__(
        self,
        enable_input_moderation: bool = None,
        enable_output_moderation: bool = None,
        streaming_moderation_threshold: int = None,
    ):
        # Indicates whether to enable security review for input.
        self.enable_input_moderation = enable_input_moderation
        # Indicates whether to enable content moderation for output.
        self.enable_output_moderation = enable_output_moderation
        # Cache size for streaming output content submitted for moderation. The default value is 5.
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

class GetDeploymentResponseBodyChatHistoryConfig(DaraModel):
    def __init__(
        self,
        connection_name: str = None,
        storage_type: str = None,
    ):
        # The connection name. This parameter is required when the chat history storage type is RDS.
        self.connection_name = connection_name
        # The storage class. Valid values:  
        # * LOCAL: Chat history is stored in a local SQLite file. This option does not support multi-instance deployment.  
        # * OSS: Chat history is stored in a specific path under the service OSS workspace path.  
        # * RDS: Chat history is stored in an RDS Table, and an RDS connection must be specified.
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

