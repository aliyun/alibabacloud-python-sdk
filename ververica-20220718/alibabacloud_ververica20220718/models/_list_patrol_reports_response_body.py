# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class ListPatrolReportsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListPatrolReportsResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The paginated data of inspection reports.
        self.data = data
        # The business error code. This value is not empty when success is false. This value is empty when success is true.
        self.error_code = error_code
        # The business error message. This value is not empty when success is false. This value is empty when success is true.
        self.error_message = error_message
        # The business status code, which is always 200. Use the success field to determine whether the business request was successful.
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
            temp_model = main_models.ListPatrolReportsResponseBodyData()
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

class ListPatrolReportsResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListPatrolReportsResponseBodyDataItems] = None,
        page: int = None,
        size: int = None,
        total: int = None,
    ):
        # The list of inspection reports.
        self.items = items
        # The current page number.
        self.page = page
        # The number of records per page.
        self.size = size
        # The total number of records.
        self.total = total

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['page'] = self.page

        if self.size is not None:
            result['size'] = self.size

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListPatrolReportsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListPatrolReportsResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        completed_at: str = None,
        created_at: str = None,
        error_message: str = None,
        inspected_jobs: int = None,
        namespace: str = None,
        problem_delay_backpressure_count: int = None,
        problem_unhealthy_checkpoint_count: int = None,
        problem_unhealthy_count: int = None,
        report_id: str = None,
        risk_critical_count: int = None,
        risk_info_count: int = None,
        risk_warning_count: int = None,
        scope_config: main_models.ListPatrolReportsResponseBodyDataItemsScopeConfig = None,
        scope_type: str = None,
        started_at: str = None,
        status: str = None,
        total_jobs: int = None,
        trigger_type: str = None,
        updated_at: str = None,
        workspace: str = None,
    ):
        # The inspection completion time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.completed_at = completed_at
        # The creation time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.created_at = created_at
        # The error message.
        self.error_message = error_message
        # The number of inspected jobs.
        self.inspected_jobs = inspected_jobs
        # The namespace.
        self.namespace = namespace
        # The number of jobs with delay and backpressure.
        self.problem_delay_backpressure_count = problem_delay_backpressure_count
        # The number of jobs with unhealthy checkpoints.
        self.problem_unhealthy_checkpoint_count = problem_unhealthy_checkpoint_count
        # The number of unhealthy jobs.
        self.problem_unhealthy_count = problem_unhealthy_count
        # The report ID.
        self.report_id = report_id
        # The number of jobs with a Critical risk level.
        self.risk_critical_count = risk_critical_count
        # The number of jobs with an Info risk level.
        self.risk_info_count = risk_info_count
        # The number of jobs with a Warning risk level.
        self.risk_warning_count = risk_warning_count
        # The inspection scope configuration.
        self.scope_config = scope_config
        # The inspection scope type.
        self.scope_type = scope_type
        # The inspection start time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.started_at = started_at
        # The report status.
        self.status = status
        # The total number of jobs.
        self.total_jobs = total_jobs
        # The trigger type.
        self.trigger_type = trigger_type
        # The update time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.updated_at = updated_at
        # The workspace ID.
        self.workspace = workspace

    def validate(self):
        if self.scope_config:
            self.scope_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completed_at is not None:
            result['completedAt'] = self.completed_at

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.inspected_jobs is not None:
            result['inspectedJobs'] = self.inspected_jobs

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.problem_delay_backpressure_count is not None:
            result['problemDelayBackpressureCount'] = self.problem_delay_backpressure_count

        if self.problem_unhealthy_checkpoint_count is not None:
            result['problemUnhealthyCheckpointCount'] = self.problem_unhealthy_checkpoint_count

        if self.problem_unhealthy_count is not None:
            result['problemUnhealthyCount'] = self.problem_unhealthy_count

        if self.report_id is not None:
            result['reportId'] = self.report_id

        if self.risk_critical_count is not None:
            result['riskCriticalCount'] = self.risk_critical_count

        if self.risk_info_count is not None:
            result['riskInfoCount'] = self.risk_info_count

        if self.risk_warning_count is not None:
            result['riskWarningCount'] = self.risk_warning_count

        if self.scope_config is not None:
            result['scopeConfig'] = self.scope_config.to_map()

        if self.scope_type is not None:
            result['scopeType'] = self.scope_type

        if self.started_at is not None:
            result['startedAt'] = self.started_at

        if self.status is not None:
            result['status'] = self.status

        if self.total_jobs is not None:
            result['totalJobs'] = self.total_jobs

        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type

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

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('inspectedJobs') is not None:
            self.inspected_jobs = m.get('inspectedJobs')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('problemDelayBackpressureCount') is not None:
            self.problem_delay_backpressure_count = m.get('problemDelayBackpressureCount')

        if m.get('problemUnhealthyCheckpointCount') is not None:
            self.problem_unhealthy_checkpoint_count = m.get('problemUnhealthyCheckpointCount')

        if m.get('problemUnhealthyCount') is not None:
            self.problem_unhealthy_count = m.get('problemUnhealthyCount')

        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')

        if m.get('riskCriticalCount') is not None:
            self.risk_critical_count = m.get('riskCriticalCount')

        if m.get('riskInfoCount') is not None:
            self.risk_info_count = m.get('riskInfoCount')

        if m.get('riskWarningCount') is not None:
            self.risk_warning_count = m.get('riskWarningCount')

        if m.get('scopeConfig') is not None:
            temp_model = main_models.ListPatrolReportsResponseBodyDataItemsScopeConfig()
            self.scope_config = temp_model.from_map(m.get('scopeConfig'))

        if m.get('scopeType') is not None:
            self.scope_type = m.get('scopeType')

        if m.get('startedAt') is not None:
            self.started_at = m.get('startedAt')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('totalJobs') is not None:
            self.total_jobs = m.get('totalJobs')

        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class ListPatrolReportsResponseBodyDataItemsScopeConfig(DaraModel):
    def __init__(
        self,
        deployment_ids: List[str] = None,
        tags: Dict[str, List[str]] = None,
    ):
        # The list of deployment IDs. This field is valid only when scopeType is set to DEPLOYMENTS.
        self.deployment_ids = deployment_ids
        # The tag mapping. This field is valid only when scopeType is set to TAGS. The key is the tag name, and the value is a list of tag values.
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

