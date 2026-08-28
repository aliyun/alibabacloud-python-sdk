# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class GetPatrolReportDetailResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetPatrolReportDetailResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The inspection report details.
        self.data = data
        # The business error code. This value is not empty when success is false. This value is empty when success is true.
        self.error_code = error_code
        # The business error message. This value is not empty when success is false. This value is empty when success is true.
        self.error_message = error_message
        # The business status code, which is always 200. Use success to determine whether the business request was successful.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the business request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetPatrolReportDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetPatrolReportDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        completed_at: str = None,
        created_at: str = None,
        namespace: str = None,
        overview: main_models.GetPatrolReportDetailResponseBodyDataOverview = None,
        report_id: str = None,
        scope_config: main_models.GetPatrolReportDetailResponseBodyDataScopeConfig = None,
        scope_type: str = None,
        trigger_type: str = None,
        unhealthy_jobs: List[main_models.GetPatrolReportDetailResponseBodyDataUnhealthyJobs] = None,
        updated_at: str = None,
        workspace: str = None,
    ):
        # The completion time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.completed_at = completed_at
        # The creation time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.created_at = created_at
        # The namespace.
        self.namespace = namespace
        # The inspection overview.
        self.overview = overview
        # The report ID.
        self.report_id = report_id
        # The inspection scope configuration.
        self.scope_config = scope_config
        # The inspection scope type.
        self.scope_type = scope_type
        # The trigger type.
        self.trigger_type = trigger_type
        # The list of unhealthy jobs.
        self.unhealthy_jobs = unhealthy_jobs
        # The update time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.updated_at = updated_at
        # The workspace ID.
        self.workspace = workspace

    def validate(self):
        if self.overview:
            self.overview.validate()
        if self.scope_config:
            self.scope_config.validate()
        if self.unhealthy_jobs:
            for v1 in self.unhealthy_jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completed_at is not None:
            result['completedAt'] = self.completed_at

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.overview is not None:
            result['overview'] = self.overview.to_map()

        if self.report_id is not None:
            result['reportId'] = self.report_id

        if self.scope_config is not None:
            result['scopeConfig'] = self.scope_config.to_map()

        if self.scope_type is not None:
            result['scopeType'] = self.scope_type

        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type

        result['unhealthyJobs'] = []
        if self.unhealthy_jobs is not None:
            for k1 in self.unhealthy_jobs:
                result['unhealthyJobs'].append(k1.to_map() if k1 else None)

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('completedAt') is not None:
            self.completed_at = m.get('completedAt')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('overview') is not None:
            temp_model = main_models.GetPatrolReportDetailResponseBodyDataOverview()
            self.overview = temp_model.from_map(m.get('overview'))

        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')

        if m.get('scopeConfig') is not None:
            temp_model = main_models.GetPatrolReportDetailResponseBodyDataScopeConfig()
            self.scope_config = temp_model.from_map(m.get('scopeConfig'))

        if m.get('scopeType') is not None:
            self.scope_type = m.get('scopeType')

        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')

        self.unhealthy_jobs = []
        if m.get('unhealthyJobs') is not None:
            for k1 in m.get('unhealthyJobs'):
                temp_model = main_models.GetPatrolReportDetailResponseBodyDataUnhealthyJobs()
                self.unhealthy_jobs.append(temp_model.from_map(k1))

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class GetPatrolReportDetailResponseBodyDataUnhealthyJobs(DaraModel):
    def __init__(
        self,
        analysis: str = None,
        deployment_id: str = None,
        deployment_name: str = None,
        description: str = None,
        job_id: str = None,
        recommendation: str = None,
        risk_level: str = None,
        tags: List[str] = None,
    ):
        # The analysis.
        self.analysis = analysis
        # The deployment ID.
        self.deployment_id = deployment_id
        # The deployment name.
        self.deployment_name = deployment_name
        # The problem description.
        self.description = description
        # The job ID.
        self.job_id = job_id
        # The recommendation.
        self.recommendation = recommendation
        # The risk level.
        self.risk_level = risk_level
        # The list of tags diagnosed by AI for the job.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis is not None:
            result['analysis'] = self.analysis

        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id

        if self.deployment_name is not None:
            result['deploymentName'] = self.deployment_name

        if self.description is not None:
            result['description'] = self.description

        if self.job_id is not None:
            result['jobId'] = self.job_id

        if self.recommendation is not None:
            result['recommendation'] = self.recommendation

        if self.risk_level is not None:
            result['riskLevel'] = self.risk_level

        if self.tags is not None:
            result['tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysis') is not None:
            self.analysis = m.get('analysis')

        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')

        if m.get('deploymentName') is not None:
            self.deployment_name = m.get('deploymentName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')

        if m.get('recommendation') is not None:
            self.recommendation = m.get('recommendation')

        if m.get('riskLevel') is not None:
            self.risk_level = m.get('riskLevel')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        return self

class GetPatrolReportDetailResponseBodyDataScopeConfig(DaraModel):
    def __init__(
        self,
        deployment_ids: List[str] = None,
        tags: Dict[str, List[str]] = None,
    ):
        # The list of deployment IDs. This parameter is valid only when scopeType is set to DEPLOYMENTS.
        self.deployment_ids = deployment_ids
        # The tag mapping. This parameter is valid only when scopeType is set to TAGS. The key is the tag name, and the value is the list of tag values.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_ids is not None:
            result['deploymentIds'] = self.deployment_ids

        if self.tags is not None:
            result['tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentIds') is not None:
            self.deployment_ids = m.get('deploymentIds')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        return self

class GetPatrolReportDetailResponseBodyDataOverview(DaraModel):
    def __init__(
        self,
        problem_summary: main_models.GetPatrolReportDetailResponseBodyDataOverviewProblemSummary = None,
        risk_summary: main_models.GetPatrolReportDetailResponseBodyDataOverviewRiskSummary = None,
        total: int = None,
    ):
        # The problem summary.
        self.problem_summary = problem_summary
        # The risk summary.
        self.risk_summary = risk_summary
        # The total number of jobs.
        self.total = total

    def validate(self):
        if self.problem_summary:
            self.problem_summary.validate()
        if self.risk_summary:
            self.risk_summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.problem_summary is not None:
            result['problemSummary'] = self.problem_summary.to_map()

        if self.risk_summary is not None:
            result['riskSummary'] = self.risk_summary.to_map()

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('problemSummary') is not None:
            temp_model = main_models.GetPatrolReportDetailResponseBodyDataOverviewProblemSummary()
            self.problem_summary = temp_model.from_map(m.get('problemSummary'))

        if m.get('riskSummary') is not None:
            temp_model = main_models.GetPatrolReportDetailResponseBodyDataOverviewRiskSummary()
            self.risk_summary = temp_model.from_map(m.get('riskSummary'))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class GetPatrolReportDetailResponseBodyDataOverviewRiskSummary(DaraModel):
    def __init__(
        self,
        critical: int = None,
        info: int = None,
        warning: int = None,
    ):
        # The number of critical-level jobs.
        self.critical = critical
        # The number of info-level jobs.
        self.info = info
        # The number of warning-level jobs.
        self.warning = warning

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.critical is not None:
            result['critical'] = self.critical

        if self.info is not None:
            result['info'] = self.info

        if self.warning is not None:
            result['warning'] = self.warning

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('critical') is not None:
            self.critical = m.get('critical')

        if m.get('info') is not None:
            self.info = m.get('info')

        if m.get('warning') is not None:
            self.warning = m.get('warning')

        return self

class GetPatrolReportDetailResponseBodyDataOverviewProblemSummary(DaraModel):
    def __init__(
        self,
        delay_and_backpressure: int = None,
        unhealthy: int = None,
        unhealthy_checkpoints: int = None,
    ):
        # The number of jobs with delay and backpressure.
        self.delay_and_backpressure = delay_and_backpressure
        # The number of unhealthy jobs.
        self.unhealthy = unhealthy
        # The number of jobs with unhealthy checkpoints.
        self.unhealthy_checkpoints = unhealthy_checkpoints

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delay_and_backpressure is not None:
            result['delayAndBackpressure'] = self.delay_and_backpressure

        if self.unhealthy is not None:
            result['unhealthy'] = self.unhealthy

        if self.unhealthy_checkpoints is not None:
            result['unhealthyCheckpoints'] = self.unhealthy_checkpoints

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('delayAndBackpressure') is not None:
            self.delay_and_backpressure = m.get('delayAndBackpressure')

        if m.get('unhealthy') is not None:
            self.unhealthy = m.get('unhealthy')

        if m.get('unhealthyCheckpoints') is not None:
            self.unhealthy_checkpoints = m.get('unhealthyCheckpoints')

        return self

