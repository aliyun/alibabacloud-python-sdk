# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class Job(DaraModel):
    def __init__(
        self,
        artifact: main_models.Artifact = None,
        batch_resource_setting: main_models.BatchResourceSetting = None,
        created_at: str = None,
        creator: str = None,
        creator_name: str = None,
        deployment_id: str = None,
        deployment_name: str = None,
        end_time: int = None,
        engine_version: str = None,
        execution_mode: str = None,
        flink_conf: Dict[str, Any] = None,
        job_id: str = None,
        local_variables: List[main_models.LocalVariable] = None,
        logging: main_models.Logging = None,
        metric: main_models.JobMetric = None,
        modified_at: str = None,
        modifier: str = None,
        modifier_name: str = None,
        namespace: str = None,
        restore_strategy: main_models.DeploymentRestoreStrategy = None,
        session_cluster_name: str = None,
        start_time: int = None,
        status: main_models.JobStatus = None,
        streaming_resource_setting: main_models.StreamingResourceSetting = None,
        user_flink_conf: Dict[str, Any] = None,
        workspace: str = None,
    ):
        # The content template of the job.
        self.artifact = artifact
        # The resource configuration of the job in batch mode.
        self.batch_resource_setting = batch_resource_setting
        # The time when the job was created.
        self.created_at = created_at
        # The ID of the account that is used to create the job.
        self.creator = creator
        # The name of the account that is used to create the job.
        self.creator_name = creator_name
        # The deployment ID.
        self.deployment_id = deployment_id
        # The name of the deployment.
        self.deployment_name = deployment_name
        # The end time of the job.
        self.end_time = end_time
        # The engine version of the deployment.
        self.engine_version = engine_version
        # The execution mode of the job. Valid values:
        # 
        # *   STREAM
        # *   BATCH
        self.execution_mode = execution_mode
        # The configuration of the job.
        self.flink_conf = flink_conf
        # The job ID.
        self.job_id = job_id
        # The variables.
        self.local_variables = local_variables
        # The logging configuration of the job.
        self.logging = logging
        # The resource information of the job.
        self.metric = metric
        # The time when the job was modified.
        self.modified_at = modified_at
        # The ID of the account that is used to modify the job.
        self.modifier = modifier
        # The name of the account that is used to modify the job.
        self.modifier_name = modifier_name
        # The name of the namespace.
        self.namespace = namespace
        # The startup strategy of the job.
        self.restore_strategy = restore_strategy
        # If the job runs in a session cluster, the value of this parameter is the name of the session cluster. Otherwise, the value of this parameter is null.
        self.session_cluster_name = session_cluster_name
        # The start time of the job.
        self.start_time = start_time
        # The status of the job.
        self.status = status
        # The resource configuration of the job in streaming mode.
        self.streaming_resource_setting = streaming_resource_setting
        # The Flink configuration.
        self.user_flink_conf = user_flink_conf
        # The workspace.
        self.workspace = workspace

    def validate(self):
        if self.artifact:
            self.artifact.validate()
        if self.batch_resource_setting:
            self.batch_resource_setting.validate()
        if self.local_variables:
            for v1 in self.local_variables:
                 if v1:
                    v1.validate()
        if self.logging:
            self.logging.validate()
        if self.metric:
            self.metric.validate()
        if self.restore_strategy:
            self.restore_strategy.validate()
        if self.status:
            self.status.validate()
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

        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id

        if self.deployment_name is not None:
            result['deploymentName'] = self.deployment_name

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version

        if self.execution_mode is not None:
            result['executionMode'] = self.execution_mode

        if self.flink_conf is not None:
            result['flinkConf'] = self.flink_conf

        if self.job_id is not None:
            result['jobId'] = self.job_id

        result['localVariables'] = []
        if self.local_variables is not None:
            for k1 in self.local_variables:
                result['localVariables'].append(k1.to_map() if k1 else None)

        if self.logging is not None:
            result['logging'] = self.logging.to_map()

        if self.metric is not None:
            result['metric'] = self.metric.to_map()

        if self.modified_at is not None:
            result['modifiedAt'] = self.modified_at

        if self.modifier is not None:
            result['modifier'] = self.modifier

        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.restore_strategy is not None:
            result['restoreStrategy'] = self.restore_strategy.to_map()

        if self.session_cluster_name is not None:
            result['sessionClusterName'] = self.session_cluster_name

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.status is not None:
            result['status'] = self.status.to_map()

        if self.streaming_resource_setting is not None:
            result['streamingResourceSetting'] = self.streaming_resource_setting.to_map()

        if self.user_flink_conf is not None:
            result['userFlinkConf'] = self.user_flink_conf

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

        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')

        if m.get('deploymentName') is not None:
            self.deployment_name = m.get('deploymentName')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')

        if m.get('executionMode') is not None:
            self.execution_mode = m.get('executionMode')

        if m.get('flinkConf') is not None:
            self.flink_conf = m.get('flinkConf')

        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')

        self.local_variables = []
        if m.get('localVariables') is not None:
            for k1 in m.get('localVariables'):
                temp_model = main_models.LocalVariable()
                self.local_variables.append(temp_model.from_map(k1))

        if m.get('logging') is not None:
            temp_model = main_models.Logging()
            self.logging = temp_model.from_map(m.get('logging'))

        if m.get('metric') is not None:
            temp_model = main_models.JobMetric()
            self.metric = temp_model.from_map(m.get('metric'))

        if m.get('modifiedAt') is not None:
            self.modified_at = m.get('modifiedAt')

        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')

        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('restoreStrategy') is not None:
            temp_model = main_models.DeploymentRestoreStrategy()
            self.restore_strategy = temp_model.from_map(m.get('restoreStrategy'))

        if m.get('sessionClusterName') is not None:
            self.session_cluster_name = m.get('sessionClusterName')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('status') is not None:
            temp_model = main_models.JobStatus()
            self.status = temp_model.from_map(m.get('status'))

        if m.get('streamingResourceSetting') is not None:
            temp_model = main_models.StreamingResourceSetting()
            self.streaming_resource_setting = temp_model.from_map(m.get('streamingResourceSetting'))

        if m.get('userFlinkConf') is not None:
            self.user_flink_conf = m.get('userFlinkConf')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

