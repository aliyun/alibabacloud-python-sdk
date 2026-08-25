# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class ListJobsResponseBody(DaraModel):
    def __init__(
        self,
        jobs: List[main_models.ListJobsResponseBodyJobs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of job information.
        self.jobs = jobs
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of results returned per page. Default value: 20. Minimum value: 1. Maximum value: 100.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.jobs:
            for v1 in self.jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['jobs'] = []
        if self.jobs is not None:
            for k1 in self.jobs:
                result['jobs'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.jobs = []
        if m.get('jobs') is not None:
            for k1 in m.get('jobs'):
                temp_model = main_models.ListJobsResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListJobsResponseBodyJobs(DaraModel):
    def __init__(
        self,
        config: main_models.ListJobsResponseBodyJobsConfig = None,
        create_time: str = None,
        description: str = None,
        elapsed_time: int = None,
        execute_type: str = None,
        is_pass_assert_check: bool = None,
        job_id: str = None,
        status: str = None,
        status_detail: Dict[str, main_models.JobsStatusDetailValue] = None,
        task_id: str = None,
        terraform_provider_version: str = None,
    ):
        # The job configuration.
        self.config = config
        # The time when the job was created, in UTC in the ISO 8601 format of YYYY-MM-DDTHH:mm:ssZ.
        self.create_time = create_time
        # The job description.
        self.description = description
        # The execution duration.
        self.elapsed_time = elapsed_time
        # The execution type. Valid values:
        # 
        # - Manual: Manual execution (default).
        # - Auto: Automatic execution.
        self.execute_type = execute_type
        # Indicates whether the assertion check passed.
        self.is_pass_assert_check = is_pass_assert_check
        # The job ID.
        self.job_id = job_id
        # The job status. Valid values:
        # 
        # - Pending: The initial status after the job is created.
        # - PlanQueued: After the job is created, if no workflow is available, the job is queued.
        # - Planning: The resource job is in the Plan execution phase.
        # - ConfigProactiveInProgress: Compliance pre-check is in progress. The account must have the compliance pre-check feature enabled.
        # - ConfigProactiveSuccess: Compliance pre-check succeeded. The account must have the compliance pre-check feature enabled.
        # - Planned: The resource job has completed Plan execution.
        # - PlannedAndFinished: After Plan execution is completed, no diff is found. This is a final status.
        # - Confirmed: The resource job is waiting for confirmation after Plan execution is completed.
        # - ApplyQueued: During job execution, if no workflow is available, the job is queued.
        # - Applying: The resource job is in the Apply execution phase.
        # - Applied: The resource job has completed Apply execution. This is a final status.
        # - Errored: The job execution encountered an error. This is a final status.
        # - Canceled: The job execution was canceled. This is a final status.
        # - Discarded: The plan of the resource job was discarded. This is a final status.
        # - ConfigProactiveFailure: Compliance pre-check failed. The account must have the compliance pre-check feature enabled.
        self.status = status
        # The status details.
        self.status_detail = status_detail
        # The task ID.
        self.task_id = task_id
        # The Terraform provider version.
        self.terraform_provider_version = terraform_provider_version

    def validate(self):
        if self.config:
            self.config.validate()
        if self.status_detail:
            for v1 in self.status_detail.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.elapsed_time is not None:
            result['elapsedTime'] = self.elapsed_time

        if self.execute_type is not None:
            result['executeType'] = self.execute_type

        if self.is_pass_assert_check is not None:
            result['isPassAssertCheck'] = self.is_pass_assert_check

        if self.job_id is not None:
            result['jobId'] = self.job_id

        if self.status is not None:
            result['status'] = self.status

        result['statusDetail'] = {}
        if self.status_detail is not None:
            for k1, v1 in self.status_detail.items():
                result['statusDetail'][k1] = v1.to_map() if v1 else None

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.ListJobsResponseBodyJobsConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('elapsedTime') is not None:
            self.elapsed_time = m.get('elapsedTime')

        if m.get('executeType') is not None:
            self.execute_type = m.get('executeType')

        if m.get('isPassAssertCheck') is not None:
            self.is_pass_assert_check = m.get('isPassAssertCheck')

        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.status_detail = {}
        if m.get('statusDetail') is not None:
            for k1, v1 in m.get('statusDetail').items():
                temp_model = main_models.JobsStatusDetailValue()
                self.status_detail[k1] = temp_model.from_map(v1)

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')

        return self

class ListJobsResponseBodyJobsConfig(DaraModel):
    def __init__(
        self,
        is_destroy: bool = None,
        module_description: str = None,
        module_version: str = None,
        resources_changed: str = None,
        sub_command: str = None,
    ):
        # Indicates whether the job is a destroy job.
        self.is_destroy = is_destroy
        # The template description.
        self.module_description = module_description
        # The template version.
        self.module_version = module_version
        # The resource change content.
        self.resources_changed = resources_changed
        # The operation command.
        self.sub_command = sub_command

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_destroy is not None:
            result['isDestroy'] = self.is_destroy

        if self.module_description is not None:
            result['moduleDescription'] = self.module_description

        if self.module_version is not None:
            result['moduleVersion'] = self.module_version

        if self.resources_changed is not None:
            result['resourcesChanged'] = self.resources_changed

        if self.sub_command is not None:
            result['subCommand'] = self.sub_command

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isDestroy') is not None:
            self.is_destroy = m.get('isDestroy')

        if m.get('moduleDescription') is not None:
            self.module_description = m.get('moduleDescription')

        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')

        if m.get('resourcesChanged') is not None:
            self.resources_changed = m.get('resourcesChanged')

        if m.get('subCommand') is not None:
            self.sub_command = m.get('subCommand')

        return self

