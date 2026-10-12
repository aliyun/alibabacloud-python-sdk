# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWorkflowInstancesShrinkRequest(DaraModel):
    def __init__(
        self,
        auto_start_enabled: bool = None,
        comment: str = None,
        default_run_properties_shrink: str = None,
        env_type: str = None,
        name: str = None,
        periods_shrink: str = None,
        project_id: int = None,
        tag_creation_policy: str = None,
        tags_shrink: str = None,
        task_parameters: str = None,
        type: str = None,
        workflow_id: int = None,
        workflow_parameters: str = None,
    ):
        # Specifies whether to run the instance immediately after it is created. Default value: true.
        self.auto_start_enabled = auto_start_enabled
        # The reason for creation.
        self.comment = comment
        # The runtime configurations.
        self.default_run_properties_shrink = default_run_properties_shrink
        # The project environment. Valid values:
        # - Prod: production.
        # - Dev: development.
        self.env_type = env_type
        # The name.
        # 
        # This parameter is required.
        self.name = name
        # The data backfill period settings.
        self.periods_shrink = periods_shrink
        # The project ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The tag creation policy.
        # - Append: Append mode. Inherits existing tags from the manual business process and appends new tags.
        # - Overwrite: Overwrite mode. Does not inherit existing tags from the manual business process and directly creates tags.
        self.tag_creation_policy = tag_creation_policy
        # The list of task tags.
        self.tags_shrink = tags_shrink
        # The task parameters. You can use this parameter to set parameters for specific tasks. The value is in JSON format. The key is the task ID. For the format of the value, refer to the task script parameters (Task.Script.Parameter in the response of the GetTask operation).
        self.task_parameters = task_parameters
        # The type of the workflow instance. Valid values:
        # - SupplementData: data backfill. The methods for specifying RootTaskIds and IncludeTaskIds vary based on the data backfill pattern. For more information, see the parameter description of DefaultRunProperties.Mode.
        # - ManualWorkflow: manual workflow. You must set WorkflowId to the ID of the manual workflow. RootTaskIds is optional. If you do not specify RootTaskIds, the default root node list of the manual workflow is used.
        # - Manual: manual task. You only need to specify RootTaskIds, which is the list of manual tasks to be run.
        # - SmokeTest: smoke test. You only need to specify RootTaskIds, which is the list of test tasks to be run.
        # - TriggerWorkflow: trigger-based workflow. You must set WorkflowId to the ID of the trigger-based workflow. IncludeTaskIds is optional. If you do not specify IncludeTaskIds, the entire workflow is run.
        # 
        # This parameter is required.
        self.type = type
        # The ID of the workflow to which the task belongs. The WorkflowId of a periodic task is always 1.
        # 
        # This parameter is required.
        self.workflow_id = workflow_id
        # The workflow parameters. This parameter takes effect only when a specific workflow is specified (WorkflowId != 1). For a periodic workflow or a trigger-based workflow, the format is key=value, and the priority is lower than that of task parameters. For a manual workflow, the format is JSON, and the priority is higher than that of task parameters.
        self.workflow_parameters = workflow_parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_start_enabled is not None:
            result['AutoStartEnabled'] = self.auto_start_enabled

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.default_run_properties_shrink is not None:
            result['DefaultRunProperties'] = self.default_run_properties_shrink

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.name is not None:
            result['Name'] = self.name

        if self.periods_shrink is not None:
            result['Periods'] = self.periods_shrink

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.tag_creation_policy is not None:
            result['TagCreationPolicy'] = self.tag_creation_policy

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

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
            self.default_run_properties_shrink = m.get('DefaultRunProperties')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Periods') is not None:
            self.periods_shrink = m.get('Periods')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('TagCreationPolicy') is not None:
            self.tag_creation_policy = m.get('TagCreationPolicy')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        if m.get('TaskParameters') is not None:
            self.task_parameters = m.get('TaskParameters')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        if m.get('WorkflowParameters') is not None:
            self.workflow_parameters = m.get('WorkflowParameters')

        return self

