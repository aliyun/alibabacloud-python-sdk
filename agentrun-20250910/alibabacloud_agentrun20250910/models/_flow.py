# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class Flow(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        definition: str = None,
        description: str = None,
        disable_public_network_access: bool = None,
        environment_configuration: main_models.EnvironmentConfiguration = None,
        execution_role_arn: str = None,
        external_storage_location: str = None,
        flow_arn: str = None,
        flow_id: str = None,
        flow_name: str = None,
        last_updated_at: str = None,
        logging_configuration: main_models.LoggingConfiguration = None,
        resource_group_id: str = None,
        tracing_configuration: main_models.TracingConfiguration = None,
        workspace_id: str = None,
    ):
        # The time when the workflow was created, in ISO 8601 format.
        self.created_at = created_at
        # The definition of the workflow.
        self.definition = definition
        # The description of the workflow, which explains the purpose and functionality of the workflow.
        self.description = description
        # Specifies whether to disable public network access for the workflow. This setting serves as the default policy at the workflow level.
        self.disable_public_network_access = disable_public_network_access
        # The environment variable configuration of the workflow, which contains a list of named variables.
        self.environment_configuration = environment_configuration
        # The ARN of the execution role that grants the workflow permissions to access cloud services.
        self.execution_role_arn = execution_role_arn
        # The external storage location of the workflow.
        self.external_storage_location = external_storage_location
        # The globally unique Alibaba Cloud Resource Name (ARN) of the workflow.
        self.flow_arn = flow_arn
        # The unique identifier of the workflow.
        self.flow_id = flow_id
        # The name of the workflow, which is used to identify and distinguish different workflow instances.
        self.flow_name = flow_name
        # The time when the workflow was last updated, in ISO 8601 format.
        self.last_updated_at = last_updated_at
        # The logging configuration of the workflow.
        self.logging_configuration = logging_configuration
        # The ID of the resource group to which the workflow belongs.
        self.resource_group_id = resource_group_id
        # The Tracing Analysis configuration of the workflow.
        self.tracing_configuration = tracing_configuration
        # The ID of the workspace to which the workflow belongs.
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
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.definition is not None:
            result['definition'] = self.definition

        if self.description is not None:
            result['description'] = self.description

        if self.disable_public_network_access is not None:
            result['disablePublicNetworkAccess'] = self.disable_public_network_access

        if self.environment_configuration is not None:
            result['environmentConfiguration'] = self.environment_configuration.to_map()

        if self.execution_role_arn is not None:
            result['executionRoleArn'] = self.execution_role_arn

        if self.external_storage_location is not None:
            result['externalStorageLocation'] = self.external_storage_location

        if self.flow_arn is not None:
            result['flowArn'] = self.flow_arn

        if self.flow_id is not None:
            result['flowId'] = self.flow_id

        if self.flow_name is not None:
            result['flowName'] = self.flow_name

        if self.last_updated_at is not None:
            result['lastUpdatedAt'] = self.last_updated_at

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
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('definition') is not None:
            self.definition = m.get('definition')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('disablePublicNetworkAccess') is not None:
            self.disable_public_network_access = m.get('disablePublicNetworkAccess')

        if m.get('environmentConfiguration') is not None:
            temp_model = main_models.EnvironmentConfiguration()
            self.environment_configuration = temp_model.from_map(m.get('environmentConfiguration'))

        if m.get('executionRoleArn') is not None:
            self.execution_role_arn = m.get('executionRoleArn')

        if m.get('externalStorageLocation') is not None:
            self.external_storage_location = m.get('externalStorageLocation')

        if m.get('flowArn') is not None:
            self.flow_arn = m.get('flowArn')

        if m.get('flowId') is not None:
            self.flow_id = m.get('flowId')

        if m.get('flowName') is not None:
            self.flow_name = m.get('flowName')

        if m.get('lastUpdatedAt') is not None:
            self.last_updated_at = m.get('lastUpdatedAt')

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

