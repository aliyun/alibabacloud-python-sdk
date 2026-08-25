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
        # Specifies whether to run the workflow instance immediately after creation. Default value: true.
        self.auto_start_enabled = auto_start_enabled
        # The reason for creating the workflow instance.
        self.comment = comment
        # The runtime configurations.
        self.default_run_properties_shrink = default_run_properties_shrink
        # The project environment. Valid values:
        # - Prod: production
        # - Dev: development
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
        # The tag creation policy. Valid values:
        # - Append: append mode. New tags are appended to the existing tags inherited from the manual workflow.
        # - Overwrite: overwrite mode. Existing tags of the manual workflow are not inherited. Tags are created directly.
        self.tag_creation_policy = tag_creation_policy
        # The list of node labels.
        self.tags_shrink = tags_shrink
        # The node parameters used to set parameters for specific nodes. The value is in JSON format. The key is the node ID, and the value format refers to the node script parameter (the Task.Script.Parameter field in the GetTask response).
        self.task_parameters = task_parameters
        # The type of the workflow instance. Valid values:
        # 
        # - SupplementData: data backfill. The method for specifying RootTaskIds and IncludeTaskIds varies based on the data backfill pattern. For more information, see the DefaultRunProperties.Mode parameter description.
        # - ManualWorkflow: manual workflow. Set WorkflowId to the ID of the manual workflow. RootTaskIds is optional. If you do not specify RootTaskIds, the default root node list of the manual workflow is used.
        # - Manual: manual node. Only RootTaskIds is required, which specifies the list of manual nodes to run.
        # - SmokeTest: smoke test. Only RootTaskIds is required, which specifies the list of test nodes to run.
        # - TriggerWorkflow: trigger-based workflow. Set WorkflowId to the ID of the trigger-based workflow. IncludeTaskIds is optional. If you do not specify IncludeTaskIds, the entire workflow is run.
        # 
        # This parameter is required.
        self.type = type
        # The ID of the workflow to which the instance belongs. The WorkflowId for periodic nodes is 1.
        # 
        # This parameter is required.
        self.workflow_id = workflow_id
        # The workflow parameters. This parameter takes effect when a unique workflow is specified (`WorkflowId != 1`). For periodic workflows and trigger-based workflows, the format is key=value, and the priority is lower than node parameters. For manual workflows, the format is JSON, and the priority is higher than node parameters.
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

