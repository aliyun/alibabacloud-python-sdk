# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateWorkflowInstancesRequest(DaraModel):
    def __init__(
        self,
        auto_start_enabled: bool = None,
        comment: str = None,
        default_run_properties: main_models.CreateWorkflowInstancesRequestDefaultRunProperties = None,
        env_type: str = None,
        name: str = None,
        periods: main_models.CreateWorkflowInstancesRequestPeriods = None,
        project_id: int = None,
        tag_creation_policy: str = None,
        tags: List[main_models.CreateWorkflowInstancesRequestTags] = None,
        task_parameters: str = None,
        type: str = None,
        workflow_id: int = None,
        workflow_parameters: str = None,
    ):
        # The default value is true.
        self.auto_start_enabled = auto_start_enabled
        # The reason for the creation.
        self.comment = comment
        # The runtime configuration.
        self.default_run_properties = default_run_properties
        # The project environment. Valid values:
        # 
        # *   Prod
        # *   Dev
        self.env_type = env_type
        # The name.
        # 
        # This parameter is required.
        self.name = name
        # The configuration of the data backfilling period.
        self.periods = periods
        # The project ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The tag creation policy. Valid values:
        # 
        # *   Append: New tags are added on top of the existing tags of the manual workflow.
        # *   Overwrite: Existing tags of the manual workflow are not inherited. New tags are created directly.
        self.tag_creation_policy = tag_creation_policy
        # The task tag list.
        self.tags = tags
        # The task-specific parameters. The value is in the JSON format. The key specifies the task ID. You can call the GetTask operation to obtain the format of the value by querying the script parameters.
        self.task_parameters = task_parameters
        # The type of the workflow instance. Valid values:
        # 
        # *   SupplementData: Data backfill. The usage of RootTaskIds and IncludeTaskIds varies based on the backfill mode. See the description of the DefaultRunProperties.Mode parameter.
        # *   ManualWorkflow: Manually triggered workflow. WorkflowId is required for a manual workflow. RootTaskIds is optional. If not specified, the system uses the default root task list of the manual workflow.
        # *   Manual: Manual task. You only need to specify RootTaskIds. This is the list of manual tasks to run.
        # *   SmokeTest: Smoke test. You only need to specify RootTaskIds. This is the list of test tasks to run.
        # *   TriggerWorkflow: Triggered Workflow You must specify the WorkflowId of the triggered workflow. IncludeTaskIds is optional. If you do not specify IncludeTaskIds, the entire workflow runs.
        # 
        # This parameter is required.
        self.type = type
        # The ID of the workflow to which the instance belongs. This parameter is set to 1 for auto triggered tasks.
        # 
        # This parameter is required.
        self.workflow_id = workflow_id
        # The workflow parameters. This parameter takes effect when a specific workflow is specified (`WorkflowId != 1`). For scheduled workflows and triggered workflows, the format is key=value, and these parameters have lower priority than task parameters. For manual workflows, the format is JSON, and these parameters have higher priority than task parameters.
        self.workflow_parameters = workflow_parameters

    def validate(self):
        if self.default_run_properties:
            self.default_run_properties.validate()
        if self.periods:
            self.periods.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_start_enabled is not None:
            result['AutoStartEnabled'] = self.auto_start_enabled

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.default_run_properties is not None:
            result['DefaultRunProperties'] = self.default_run_properties.to_map()

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.name is not None:
            result['Name'] = self.name

        if self.periods is not None:
            result['Periods'] = self.periods.to_map()

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.tag_creation_policy is not None:
            result['TagCreationPolicy'] = self.tag_creation_policy

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.task_parameters is not None:
            result['TaskParameters'] = self.task_parameters

        if self.type is not None:
            result['Type'] = self.type

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        if self.workflow_parameters is not None:
            result['WorkflowParameters'] = self.workflow_parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoStartEnabled') is not None:
            self.auto_start_enabled = m.get('AutoStartEnabled')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('DefaultRunProperties') is not None:
            temp_model = main_models.CreateWorkflowInstancesRequestDefaultRunProperties()
            self.default_run_properties = temp_model.from_map(m.get('DefaultRunProperties'))

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Periods') is not None:
            temp_model = main_models.CreateWorkflowInstancesRequestPeriods()
            self.periods = temp_model.from_map(m.get('Periods'))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('TagCreationPolicy') is not None:
            self.tag_creation_policy = m.get('TagCreationPolicy')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateWorkflowInstancesRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TaskParameters') is not None:
            self.task_parameters = m.get('TaskParameters')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        if m.get('WorkflowParameters') is not None:
            self.workflow_parameters = m.get('WorkflowParameters')

        return self

class CreateWorkflowInstancesRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateWorkflowInstancesRequestPeriods(DaraModel):
    def __init__(
        self,
        biz_dates: List[main_models.CreateWorkflowInstancesRequestPeriodsBizDates] = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # The data timestamps. You can specify up to seven data timestamps.
        # 
        # This parameter is required.
        self.biz_dates = biz_dates
        # The end time of data backfill. Configure this parameter in the `hh:mm:ss` format. The time must be in the 24-hour clock. Default value: 23:59:59.
        # 
        # If you configure this parameter, you must also configure the StartTime parameter.
        self.end_time = end_time
        # The start time of data backfill. Configure this parameter in the `hh:mm:ss` format. The time must be in the 24-hour clock. Default value: 00:00:00.
        # 
        # If you configure this parameter, you must also configure the EndTime parameter.
        self.start_time = start_time

    def validate(self):
        if self.biz_dates:
            for v1 in self.biz_dates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BizDates'] = []
        if self.biz_dates is not None:
            for k1 in self.biz_dates:
                result['BizDates'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.biz_dates = []
        if m.get('BizDates') is not None:
            for k1 in m.get('BizDates'):
                temp_model = main_models.CreateWorkflowInstancesRequestPeriodsBizDates()
                self.biz_dates.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class CreateWorkflowInstancesRequestPeriodsBizDates(DaraModel):
    def __init__(
        self,
        end_biz_date: str = None,
        start_biz_date: str = None,
    ):
        # The data timestamp at which data is no longer backfilled. Configure this parameter in the `yyyy-mm-dd` format.
        # 
        # This parameter is required.
        self.end_biz_date = end_biz_date
        # The data timestamp at which the data starts to be backfilled. Configure this parameter in the `yyyy-mm-dd` format.
        # 
        # This parameter is required.
        self.start_biz_date = start_biz_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_biz_date is not None:
            result['EndBizDate'] = self.end_biz_date

        if self.start_biz_date is not None:
            result['StartBizDate'] = self.start_biz_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndBizDate') is not None:
            self.end_biz_date = m.get('EndBizDate')

        if m.get('StartBizDate') is not None:
            self.start_biz_date = m.get('StartBizDate')

        return self

class CreateWorkflowInstancesRequestDefaultRunProperties(DaraModel):
    def __init__(
        self,
        alert: main_models.CreateWorkflowInstancesRequestDefaultRunPropertiesAlert = None,
        analysis: main_models.CreateWorkflowInstancesRequestDefaultRunPropertiesAnalysis = None,
        exclude_project_ids: List[int] = None,
        exclude_task_ids: List[int] = None,
        include_project_ids: List[int] = None,
        include_task_ids: List[int] = None,
        mode: str = None,
        order: str = None,
        parallelism: int = None,
        priority: int = None,
        priority_weight_strategy: str = None,
        root_task_ids: List[int] = None,
        run_policy: main_models.CreateWorkflowInstancesRequestDefaultRunPropertiesRunPolicy = None,
        runtime_resource: str = None,
    ):
        # The alert settings.
        self.alert = alert
        # The analysis configuration. Required when Type = SupplementData.
        self.analysis = analysis
        # The IDs of the projects not to run.
        self.exclude_project_ids = exclude_project_ids
        # The IDs of the tasks not to run.
        self.exclude_task_ids = exclude_task_ids
        # The IDs of the projects to run.
        self.include_project_ids = include_project_ids
        # The IDs of the tasks to run.
        self.include_task_ids = include_task_ids
        # The data backfill mode. Default value: ManualSelection. Required when Type is set to SupplementData.
        # 
        # *   General: You can specify only one value for `RootTaskIds`. The `IncludeTaskIds` parameter is optional. If it\\"s not specified, it defaults to including `RootTaskIds`.
        # *   ManualSelection: You can specify multiple values for `RootTaskIds`. The `IncludeTaskIds` parameter is optional. If it is not specified, it defaults to including `RootTaskIds`.
        # *   Chain: If you set the Mode parameter to Chain, leave the `RootTaskIds` parameter empty and set the `IncludeTaskIds` parameter to the start task ID and the end task ID.
        # *   AllDownstream: Only one `RootTaskId` can be specified.
        self.mode = mode
        # The execution order. Default value: Asc.
        # 
        # *   Asc: ascending by business date.
        # *   Desc: descending by business date.
        self.order = order
        # The task concurrency. Values from 2 to 10 indicate concurrency. A value of 1 indicates sequential execution. Required when Type = SupplementData.
        self.parallelism = parallelism
        # The execution priority, range: 1–11. A higher value indicates higher priority.
        self.priority = priority
        # The priority weighting policy.
        # 
        # *   `Disable` (default): Do not enable.
        # *   `Upstream`: The priority is based on the total weight of upstream nodes. The deeper the hierarchy, the higher the weight.
        self.priority_weight_strategy = priority_weight_strategy
        # The list of root task IDs.
        # 
        # *   When Type is set to SupplementData, RootTaskIds is required unless Mode is set to Chain.
        # *   When Type is set to ManualWorkflow, RootTaskIds is optional. If it is not specified, the default root nodes of the manual workflow are used.
        # *   When Type is set to Manual, RootTaskIds is required and specifies the list of manual tasks to run.
        # *   When Type is set to SmokeTest, RootTaskIds is required and specifies the list of test tasks to run.
        self.root_task_ids = root_task_ids
        # The run policy. If the parameter is left empty, the task configuration is used.
        self.run_policy = run_policy
        # The custom scheduling resource group ID. If left empty, the task configuration is used.
        self.runtime_resource = runtime_resource

    def validate(self):
        if self.alert:
            self.alert.validate()
        if self.analysis:
            self.analysis.validate()
        if self.run_policy:
            self.run_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert is not None:
            result['Alert'] = self.alert.to_map()

        if self.analysis is not None:
            result['Analysis'] = self.analysis.to_map()

        if self.exclude_project_ids is not None:
            result['ExcludeProjectIds'] = self.exclude_project_ids

        if self.exclude_task_ids is not None:
            result['ExcludeTaskIds'] = self.exclude_task_ids

        if self.include_project_ids is not None:
            result['IncludeProjectIds'] = self.include_project_ids

        if self.include_task_ids is not None:
            result['IncludeTaskIds'] = self.include_task_ids

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.order is not None:
            result['Order'] = self.order

        if self.parallelism is not None:
            result['Parallelism'] = self.parallelism

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.priority_weight_strategy is not None:
            result['PriorityWeightStrategy'] = self.priority_weight_strategy

        if self.root_task_ids is not None:
            result['RootTaskIds'] = self.root_task_ids

        if self.run_policy is not None:
            result['RunPolicy'] = self.run_policy.to_map()

        if self.runtime_resource is not None:
            result['RuntimeResource'] = self.runtime_resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alert') is not None:
            temp_model = main_models.CreateWorkflowInstancesRequestDefaultRunPropertiesAlert()
            self.alert = temp_model.from_map(m.get('Alert'))

        if m.get('Analysis') is not None:
            temp_model = main_models.CreateWorkflowInstancesRequestDefaultRunPropertiesAnalysis()
            self.analysis = temp_model.from_map(m.get('Analysis'))

        if m.get('ExcludeProjectIds') is not None:
            self.exclude_project_ids = m.get('ExcludeProjectIds')

        if m.get('ExcludeTaskIds') is not None:
            self.exclude_task_ids = m.get('ExcludeTaskIds')

        if m.get('IncludeProjectIds') is not None:
            self.include_project_ids = m.get('IncludeProjectIds')

        if m.get('IncludeTaskIds') is not None:
            self.include_task_ids = m.get('IncludeTaskIds')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('PriorityWeightStrategy') is not None:
            self.priority_weight_strategy = m.get('PriorityWeightStrategy')

        if m.get('RootTaskIds') is not None:
            self.root_task_ids = m.get('RootTaskIds')

        if m.get('RunPolicy') is not None:
            temp_model = main_models.CreateWorkflowInstancesRequestDefaultRunPropertiesRunPolicy()
            self.run_policy = temp_model.from_map(m.get('RunPolicy'))

        if m.get('RuntimeResource') is not None:
            self.runtime_resource = m.get('RuntimeResource')

        return self

class CreateWorkflowInstancesRequestDefaultRunPropertiesRunPolicy(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        immediately: bool = None,
        start_time: str = None,
        type: str = None,
    ):
        # The end time of running. Configure this parameter in the `hh:mm:ss` format (24-hour clock). This parameter is required if you configure the RunPolicy parameter. Valid values:
        self.end_time = end_time
        # Specifies whether a task whose scheduled run time is in the future can be run immediately. Default value: false.
        self.immediately = immediately
        # The start time of running. Configure this parameter in the `hh:mm:ss` format (24-hour clock). This parameter is required if you configure the RunPolicy parameter.
        self.start_time = start_time
        # The time period type. This parameter is required if you configure the RunPolicy parameter. Valid values:
        # 
        # *   Daily
        # *   Weekend
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.immediately is not None:
            result['Immediately'] = self.immediately

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Immediately') is not None:
            self.immediately = m.get('Immediately')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateWorkflowInstancesRequestDefaultRunPropertiesAnalysis(DaraModel):
    def __init__(
        self,
        blocked: bool = None,
        enabled: bool = None,
    ):
        # Specifies whether to block execution if the analysis fails. Required when Type = SupplementData.
        self.blocked = blocked
        # Specifies whether to enable the analysis feature. Required when Type = SupplementData.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.blocked is not None:
            result['Blocked'] = self.blocked

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Blocked') is not None:
            self.blocked = m.get('Blocked')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        return self

class CreateWorkflowInstancesRequestDefaultRunPropertiesAlert(DaraModel):
    def __init__(
        self,
        notice_type: str = None,
        type: str = None,
    ):
        # The alert notification method. Valid values:
        # 
        # *   Sms: SMS only.
        # *   Mail: Mail only.
        # *   SmsMail: SMS and mail.
        self.notice_type = notice_type
        # The alerting policy. Valid values:
        # 
        # *   Success: Alerts on success.
        # *   Failure: Alerts on failure.
        # *   SuccessFailure: Alerts on both success and failure.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

