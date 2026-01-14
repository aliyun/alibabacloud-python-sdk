# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class GetJobResponseBody(DaraModel):
    def __init__(
        self,
        job: main_models.GetJobResponseBodyJob = None,
        request_id: str = None,
    ):
        self.job = job
        self.request_id = request_id

    def validate(self):
        if self.job:
            self.job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job is not None:
            result['job'] = self.job.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('job') is not None:
            temp_model = main_models.GetJobResponseBodyJob()
            self.job = temp_model.from_map(m.get('job'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetJobResponseBodyJob(DaraModel):
    def __init__(
        self,
        assert_check_detail: List[main_models.GetJobResponseBodyJobAssertCheckDetail] = None,
        config: main_models.GetJobResponseBodyJobConfig = None,
        create_time: str = None,
        description: str = None,
        download_url: Dict[str, Any] = None,
        elapsed_time: int = None,
        execute_type: str = None,
        is_pass_assert_check: bool = None,
        job_id: str = None,
        job_type: str = None,
        log_file: Dict[str, Any] = None,
        output: str = None,
        output_json_plan: Any = None,
        parameters: Dict[str, str] = None,
        status: str = None,
        status_detail: Dict[str, main_models.JobStatusDetailValue] = None,
        task_id: str = None,
        task_type: str = None,
        terraform_provider_version: str = None,
    ):
        self.assert_check_detail = assert_check_detail
        self.config = config
        self.create_time = create_time
        self.description = description
        self.download_url = download_url
        self.elapsed_time = elapsed_time
        self.execute_type = execute_type
        self.is_pass_assert_check = is_pass_assert_check
        self.job_id = job_id
        self.job_type = job_type
        self.log_file = log_file
        self.output = output
        self.output_json_plan = output_json_plan
        self.parameters = parameters
        self.status = status
        self.status_detail = status_detail
        self.task_id = task_id
        self.task_type = task_type
        self.terraform_provider_version = terraform_provider_version

    def validate(self):
        if self.assert_check_detail:
            for v1 in self.assert_check_detail:
                 if v1:
                    v1.validate()
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
        result['assertCheckDetail'] = []
        if self.assert_check_detail is not None:
            for k1 in self.assert_check_detail:
                result['assertCheckDetail'].append(k1.to_map() if k1 else None)

        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.download_url is not None:
            result['downloadUrl'] = self.download_url

        if self.elapsed_time is not None:
            result['elapsedTime'] = self.elapsed_time

        if self.execute_type is not None:
            result['executeType'] = self.execute_type

        if self.is_pass_assert_check is not None:
            result['isPassAssertCheck'] = self.is_pass_assert_check

        if self.job_id is not None:
            result['jobId'] = self.job_id

        if self.job_type is not None:
            result['jobType'] = self.job_type

        if self.log_file is not None:
            result['logFile'] = self.log_file

        if self.output is not None:
            result['output'] = self.output

        if self.output_json_plan is not None:
            result['outputJsonPlan'] = self.output_json_plan

        if self.parameters is not None:
            result['parameters'] = self.parameters

        if self.status is not None:
            result['status'] = self.status

        result['statusDetail'] = {}
        if self.status_detail is not None:
            for k1, v1 in self.status_detail.items():
                result['statusDetail'][k1] = v1.to_map() if v1 else None

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.task_type is not None:
            result['taskType'] = self.task_type

        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assert_check_detail = []
        if m.get('assertCheckDetail') is not None:
            for k1 in m.get('assertCheckDetail'):
                temp_model = main_models.GetJobResponseBodyJobAssertCheckDetail()
                self.assert_check_detail.append(temp_model.from_map(k1))

        if m.get('config') is not None:
            temp_model = main_models.GetJobResponseBodyJobConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('downloadUrl') is not None:
            self.download_url = m.get('downloadUrl')

        if m.get('elapsedTime') is not None:
            self.elapsed_time = m.get('elapsedTime')

        if m.get('executeType') is not None:
            self.execute_type = m.get('executeType')

        if m.get('isPassAssertCheck') is not None:
            self.is_pass_assert_check = m.get('isPassAssertCheck')

        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')

        if m.get('jobType') is not None:
            self.job_type = m.get('jobType')

        if m.get('logFile') is not None:
            self.log_file = m.get('logFile')

        if m.get('output') is not None:
            self.output = m.get('output')

        if m.get('outputJsonPlan') is not None:
            self.output_json_plan = m.get('outputJsonPlan')

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.status_detail = {}
        if m.get('statusDetail') is not None:
            for k1, v1 in m.get('statusDetail').items():
                temp_model = main_models.JobStatusDetailValue()
                self.status_detail[k1] = temp_model.from_map(v1)

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')

        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')

        return self

class GetJobResponseBodyJobConfig(DaraModel):
    def __init__(
        self,
        auto_apply: bool = None,
        has_config_proactive: str = None,
        is_destroy: bool = None,
        module_version: str = None,
        resources_changed: str = None,
        sub_command: str = None,
    ):
        self.auto_apply = auto_apply
        self.has_config_proactive = has_config_proactive
        self.is_destroy = is_destroy
        self.module_version = module_version
        self.resources_changed = resources_changed
        self.sub_command = sub_command

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_apply is not None:
            result['autoApply'] = self.auto_apply

        if self.has_config_proactive is not None:
            result['hasConfigProactive'] = self.has_config_proactive

        if self.is_destroy is not None:
            result['isDestroy'] = self.is_destroy

        if self.module_version is not None:
            result['moduleVersion'] = self.module_version

        if self.resources_changed is not None:
            result['resourcesChanged'] = self.resources_changed

        if self.sub_command is not None:
            result['subCommand'] = self.sub_command

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoApply') is not None:
            self.auto_apply = m.get('autoApply')

        if m.get('hasConfigProactive') is not None:
            self.has_config_proactive = m.get('hasConfigProactive')

        if m.get('isDestroy') is not None:
            self.is_destroy = m.get('isDestroy')

        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')

        if m.get('resourcesChanged') is not None:
            self.resources_changed = m.get('resourcesChanged')

        if m.get('subCommand') is not None:
            self.sub_command = m.get('subCommand')

        return self

class GetJobResponseBodyJobAssertCheckDetail(DaraModel):
    def __init__(
        self,
        comparison: str = None,
        expected_value: str = None,
        is_pass: bool = None,
        type: str = None,
    ):
        self.comparison = comparison
        self.expected_value = expected_value
        self.is_pass = is_pass
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comparison is not None:
            result['comparison'] = self.comparison

        if self.expected_value is not None:
            result['expectedValue'] = self.expected_value

        if self.is_pass is not None:
            result['isPass'] = self.is_pass

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comparison') is not None:
            self.comparison = m.get('comparison')

        if m.get('expectedValue') is not None:
            self.expected_value = m.get('expectedValue')

        if m.get('isPass') is not None:
            self.is_pass = m.get('isPass')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

