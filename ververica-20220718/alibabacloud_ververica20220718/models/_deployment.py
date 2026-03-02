# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class Deployment(DaraModel):
    def __init__(
        self,
        artifact: main_models.Artifact = None,
        batch_resource_setting: main_models.BatchResourceSetting = None,
        created_at: str = None,
        creator: str = None,
        creator_name: str = None,
        deployment_has_changed: bool = None,
        deployment_id: str = None,
        deployment_target: main_models.BriefDeploymentTarget = None,
        description: str = None,
        engine_version: str = None,
        execution_mode: str = None,
        flink_conf: Dict[str, Any] = None,
        job_summary: main_models.JobSummary = None,
        labels: Dict[str, Any] = None,
        local_variables: List[main_models.LocalVariable] = None,
        logging: main_models.Logging = None,
        modified_at: str = None,
        modifier: str = None,
        modifier_name: str = None,
        name: str = None,
        namespace: str = None,
        referenced_deployment_draft_id: str = None,
        streaming_resource_setting: main_models.StreamingResourceSetting = None,
        workspace: str = None,
    ):
        # The parameters that are required for starting a deployment.
        self.artifact = artifact
        # The resource configuration of the batch deployment.
        self.batch_resource_setting = batch_resource_setting
        # The time at which the deployment was created.
        self.created_at = created_at
        # The ID of the account that is used to create the deployment.
        self.creator = creator
        # The name of the account that is used to create the deployment.
        self.creator_name = creator_name
        # Specifies whether the deployment is modified after the deployment is started.
        self.deployment_has_changed = deployment_has_changed
        # The ID of the deployment.
        self.deployment_id = deployment_id
        # The cluster on which the deployment is deployed.
        self.deployment_target = deployment_target
        # The description of the deployment.
        self.description = description
        # The engine version of the deployment.
        self.engine_version = engine_version
        # The execution mode of the deployment. Valid values:
        # 
        # *   STREAMING
        # *   BATCH
        self.execution_mode = execution_mode
        # The Realtime Compute for Apache Flink configuration.
        self.flink_conf = flink_conf
        # The summary of jobs in the deployment.
        self.job_summary = job_summary
        self.labels = labels
        # The variables of the deployment.
        self.local_variables = local_variables
        # The logging configuration.
        self.logging = logging
        # The time at which the deployment was modified.
        self.modified_at = modified_at
        # The ID of the account that is used to modify the deployment.
        self.modifier = modifier
        # The name of the account that is used to modify the deployment.
        self.modifier_name = modifier_name
        # The name of the deployment.
        self.name = name
        # The name of the namespace.
        self.namespace = namespace
        self.referenced_deployment_draft_id = referenced_deployment_draft_id
        # The resource configuration of the streaming deployment.
        self.streaming_resource_setting = streaming_resource_setting
        # The workspace to which the deployment belongs.
        self.workspace = workspace

    def validate(self):
        if self.artifact:
            self.artifact.validate()
        if self.batch_resource_setting:
            self.batch_resource_setting.validate()
        if self.deployment_target:
            self.deployment_target.validate()
        if self.job_summary:
            self.job_summary.validate()
        if self.local_variables:
            for v1 in self.local_variables:
                 if v1:
                    v1.validate()
        if self.logging:
            self.logging.validate()
        if self.streaming_resource_setting:
            self.streaming_resource_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact is not None:
            result['artifact'] = self.artifact.to_map()

        if self.batch_resource_setting is not None:
            result['batchResourceSetting'] = self.batch_resource_setting.to_map()

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.creator is not None:
            result['creator'] = self.creator

        if self.creator_name is not None:
            result['creatorName'] = self.creator_name

        if self.deployment_has_changed is not None:
            result['deploymentHasChanged'] = self.deployment_has_changed

        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id

        if self.deployment_target is not None:
            result['deploymentTarget'] = self.deployment_target.to_map()

        if self.description is not None:
            result['description'] = self.description

        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version

        if self.execution_mode is not None:
            result['executionMode'] = self.execution_mode

        if self.flink_conf is not None:
            result['flinkConf'] = self.flink_conf

        if self.job_summary is not None:
            result['jobSummary'] = self.job_summary.to_map()

        if self.labels is not None:
            result['labels'] = self.labels

        result['localVariables'] = []
        if self.local_variables is not None:
            for k1 in self.local_variables:
                result['localVariables'].append(k1.to_map() if k1 else None)

        if self.logging is not None:
            result['logging'] = self.logging.to_map()

        if self.modified_at is not None:
            result['modifiedAt'] = self.modified_at

        if self.modifier is not None:
            result['modifier'] = self.modifier

        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name

        if self.name is not None:
            result['name'] = self.name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.referenced_deployment_draft_id is not None:
            result['referencedDeploymentDraftId'] = self.referenced_deployment_draft_id

        if self.streaming_resource_setting is not None:
            result['streamingResourceSetting'] = self.streaming_resource_setting.to_map()

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('artifact') is not None:
            temp_model = main_models.Artifact()
            self.artifact = temp_model.from_map(m.get('artifact'))

        if m.get('batchResourceSetting') is not None:
            temp_model = main_models.BatchResourceSetting()
            self.batch_resource_setting = temp_model.from_map(m.get('batchResourceSetting'))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')

        if m.get('deploymentHasChanged') is not None:
            self.deployment_has_changed = m.get('deploymentHasChanged')

        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')

        if m.get('deploymentTarget') is not None:
            temp_model = main_models.BriefDeploymentTarget()
            self.deployment_target = temp_model.from_map(m.get('deploymentTarget'))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')

        if m.get('executionMode') is not None:
            self.execution_mode = m.get('executionMode')

        if m.get('flinkConf') is not None:
            self.flink_conf = m.get('flinkConf')

        if m.get('jobSummary') is not None:
            temp_model = main_models.JobSummary()
            self.job_summary = temp_model.from_map(m.get('jobSummary'))

        if m.get('labels') is not None:
            self.labels = m.get('labels')

        self.local_variables = []
        if m.get('localVariables') is not None:
            for k1 in m.get('localVariables'):
                temp_model = main_models.LocalVariable()
                self.local_variables.append(temp_model.from_map(k1))

        if m.get('logging') is not None:
            temp_model = main_models.Logging()
            self.logging = temp_model.from_map(m.get('logging'))

        if m.get('modifiedAt') is not None:
            self.modified_at = m.get('modifiedAt')

        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')

        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('referencedDeploymentDraftId') is not None:
            self.referenced_deployment_draft_id = m.get('referencedDeploymentDraftId')

        if m.get('streamingResourceSetting') is not None:
            temp_model = main_models.StreamingResourceSetting()
            self.streaming_resource_setting = temp_model.from_map(m.get('streamingResourceSetting'))

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

