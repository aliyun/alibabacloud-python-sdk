# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class GetTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task: main_models.GetTaskResponseBodyTask = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The task information.
        self.task = task

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.task is not None:
            result['task'] = self.task.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('task') is not None:
            temp_model = main_models.GetTaskResponseBodyTask()
            self.task = temp_model.from_map(m.get('task'))

        return self

class GetTaskResponseBodyTask(DaraModel):
    def __init__(
        self,
        auto_apply: bool = None,
        auto_destroy: bool = None,
        create_time: str = None,
        current_job_id: str = None,
        current_job_status: str = None,
        deletion_protection: bool = None,
        description: str = None,
        group_info: main_models.GetTaskResponseBodyTaskGroupInfo = None,
        init_module_state: bool = None,
        latest_module_version: str = None,
        module_id: str = None,
        module_name: str = None,
        module_version: str = None,
        name: str = None,
        protection_strategy: List[str] = None,
        ram_role: str = None,
        skip_property_validation: bool = None,
        skip_region_validation: bool = None,
        status: str = None,
        tags: List[main_models.GetTaskResponseBodyTaskTags] = None,
        task_backend: main_models.GetTaskResponseBodyTaskTaskBackend = None,
        task_id: str = None,
        task_output_path: str = None,
        terraform_version: str = None,
        trigger_strategy: str = None,
    ):
        # Indicates whether the task is automatically executed.
        self.auto_apply = auto_apply
        # Indicates whether automatic deletion is enabled. When enabled, resources are automatically destroyed after the task is completed.
        self.auto_destroy = auto_destroy
        # The time when the task was created.
        self.create_time = create_time
        # The job ID of the current task.
        self.current_job_id = current_job_id
        # The current job status.
        self.current_job_status = current_job_status
        # Indicates whether deletion protection is enabled.
        self.deletion_protection = deletion_protection
        # The description of the task.
        self.description = description
        # The group information.
        self.group_info = group_info
        # Specifies whether to use a state file. Default value: false. This parameter is applicable to templates that originate from resource export. Only one task can use this parameter at a time.
        self.init_module_state = init_module_state
        # The latest version number of the template.
        self.latest_module_version = latest_module_version
        # The template ID.
        self.module_id = module_id
        # The template name.
        self.module_name = module_name
        # The template version.
        self.module_version = module_version
        # The task name.
        self.name = name
        # The list of resource protection strategies.
        self.protection_strategy = protection_strategy
        # The RAM role.
        self.ram_role = ram_role
        # Specifies whether to skip enumeration value validation. Default value: false.
        self.skip_property_validation = skip_property_validation
        self.skip_region_validation = skip_region_validation
        # The task status. Valid values:
        # 
        # - Available: the task is available and no job is running.
        # - Running: a job is currently running.
        self.status = status
        # The list of task tags.
        self.tags = tags
        # The task backend configuration. After this parameter is configured, runtime log information is saved to the specified OSS bucket.
        self.task_backend = task_backend
        # The task ID.
        self.task_id = task_id
        # The task output path.
        self.task_output_path = task_output_path
        # The Terraform version.
        self.terraform_version = terraform_version
        # The job trigger method. Valid values:
        # 
        # - Manual: manually triggered (default).
        # - NewVersion: triggered when a new template version is published.
        # - ParameterSetUpdated: triggered when the parameter set content changes or the parameter set attach relationship changes.
        # - Auto: automatically triggered when the task properties change, such as task creation, execution version change, or job trigger policy change (when changed from another value to Auto).
        self.trigger_strategy = trigger_strategy

    def validate(self):
        if self.group_info:
            self.group_info.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.task_backend:
            self.task_backend.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_apply is not None:
            result['autoApply'] = self.auto_apply

        if self.auto_destroy is not None:
            result['autoDestroy'] = self.auto_destroy

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.current_job_id is not None:
            result['currentJobId'] = self.current_job_id

        if self.current_job_status is not None:
            result['currentJobStatus'] = self.current_job_status

        if self.deletion_protection is not None:
            result['deletionProtection'] = self.deletion_protection

        if self.description is not None:
            result['description'] = self.description

        if self.group_info is not None:
            result['groupInfo'] = self.group_info.to_map()

        if self.init_module_state is not None:
            result['initModuleState'] = self.init_module_state

        if self.latest_module_version is not None:
            result['latestModuleVersion'] = self.latest_module_version

        if self.module_id is not None:
            result['moduleId'] = self.module_id

        if self.module_name is not None:
            result['moduleName'] = self.module_name

        if self.module_version is not None:
            result['moduleVersion'] = self.module_version

        if self.name is not None:
            result['name'] = self.name

        if self.protection_strategy is not None:
            result['protectionStrategy'] = self.protection_strategy

        if self.ram_role is not None:
            result['ramRole'] = self.ram_role

        if self.skip_property_validation is not None:
            result['skipPropertyValidation'] = self.skip_property_validation

        if self.skip_region_validation is not None:
            result['skipRegionValidation'] = self.skip_region_validation

        if self.status is not None:
            result['status'] = self.status

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.task_backend is not None:
            result['taskBackend'] = self.task_backend.to_map()

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.task_output_path is not None:
            result['taskOutputPath'] = self.task_output_path

        if self.terraform_version is not None:
            result['terraformVersion'] = self.terraform_version

        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoApply') is not None:
            self.auto_apply = m.get('autoApply')

        if m.get('autoDestroy') is not None:
            self.auto_destroy = m.get('autoDestroy')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('currentJobId') is not None:
            self.current_job_id = m.get('currentJobId')

        if m.get('currentJobStatus') is not None:
            self.current_job_status = m.get('currentJobStatus')

        if m.get('deletionProtection') is not None:
            self.deletion_protection = m.get('deletionProtection')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('groupInfo') is not None:
            temp_model = main_models.GetTaskResponseBodyTaskGroupInfo()
            self.group_info = temp_model.from_map(m.get('groupInfo'))

        if m.get('initModuleState') is not None:
            self.init_module_state = m.get('initModuleState')

        if m.get('latestModuleVersion') is not None:
            self.latest_module_version = m.get('latestModuleVersion')

        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')

        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')

        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('protectionStrategy') is not None:
            self.protection_strategy = m.get('protectionStrategy')

        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')

        if m.get('skipPropertyValidation') is not None:
            self.skip_property_validation = m.get('skipPropertyValidation')

        if m.get('skipRegionValidation') is not None:
            self.skip_region_validation = m.get('skipRegionValidation')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.GetTaskResponseBodyTaskTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('taskBackend') is not None:
            temp_model = main_models.GetTaskResponseBodyTaskTaskBackend()
            self.task_backend = temp_model.from_map(m.get('taskBackend'))

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('taskOutputPath') is not None:
            self.task_output_path = m.get('taskOutputPath')

        if m.get('terraformVersion') is not None:
            self.terraform_version = m.get('terraformVersion')

        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')

        return self

class GetTaskResponseBodyTaskTaskBackend(DaraModel):
    def __init__(
        self,
        bucket_endpoint: str = None,
        bucket_name: str = None,
        object_path: str = None,
    ):
        # The endpoint information.
        self.bucket_endpoint = bucket_endpoint
        # The bucket name.
        self.bucket_name = bucket_name
        # The object path.
        self.object_path = object_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_endpoint is not None:
            result['bucketEndpoint'] = self.bucket_endpoint

        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name

        if self.object_path is not None:
            result['objectPath'] = self.object_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketEndpoint') is not None:
            self.bucket_endpoint = m.get('bucketEndpoint')

        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')

        if m.get('objectPath') is not None:
            self.object_path = m.get('objectPath')

        return self

class GetTaskResponseBodyTaskTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key of the task.
        self.tag_key = tag_key
        # The tag value of the task.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key

        if self.tag_value is not None:
            result['tagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')

        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')

        return self

class GetTaskResponseBodyTaskGroupInfo(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        group_name: str = None,
        project_id: str = None,
        project_name: str = None,
    ):
        # The group ID.
        self.group_id = group_id
        # The group name.
        self.group_name = group_name
        # The project ID.
        self.project_id = project_id
        # The project name.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.project_id is not None:
            result['projectId'] = self.project_id

        if self.project_name is not None:
            result['projectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')

        return self

