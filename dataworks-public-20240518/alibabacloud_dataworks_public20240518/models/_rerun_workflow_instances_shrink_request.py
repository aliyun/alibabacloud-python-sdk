# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RerunWorkflowInstancesShrinkRequest(DaraModel):
    def __init__(
        self,
        bizdate: int = None,
        end_trigger_time: int = None,
        env_type: str = None,
        filter_shrink: str = None,
        ids_shrink: str = None,
        name: str = None,
        project_id: int = None,
        start_trigger_time: int = None,
        status: str = None,
        type: str = None,
        workflow_id: int = None,
    ):
        # The data timestamp specified for the manual workflow instance run, used for matching.
        # 
        # The value is a 13-digit number, such as `1710239005403`.
        self.bizdate = bizdate
        # The end trigger time (creation time) of the manual workflow instance used for matching. This parameter must be used together with StartTriggerTime.
        # 
        # The value is a 13-digit number, such as `1710239005403`.
        self.end_trigger_time = end_trigger_time
        # The project environment. Valid values:
        # 
        # - Prod: Production.
        # - Dev: Development.
        self.env_type = env_type
        # The matching conditions for the internal instances of the manual workflow instance.
        self.filter_shrink = filter_shrink
        # The list of manual workflow instance IDs used for matching.
        self.ids_shrink = ids_shrink
        # The name of the manual workflow used for fuzzy matching.
        self.name = name
        # The project ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The start trigger time (creation time) of the manual workflow instance used for matching. This parameter must be used together with EndTriggerTime.
        # 
        # The value is a 13-digit number, such as `1710239005403`.
        self.start_trigger_time = start_trigger_time
        # The running status of the manual workflow instance used for matching.
        self.status = status
        # The type of the workflow instance. Valid values:
        # 
        # - ManualWorkflow: Manual workflow.
        # 
        # This parameter is required.
        self.type = type
        # The ID of the workflow.
        # 
        # This parameter is required.
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate

        if self.end_trigger_time is not None:
            result['EndTriggerTime'] = self.end_trigger_time

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.filter_shrink is not None:
            result['Filter'] = self.filter_shrink

        if self.ids_shrink is not None:
            result['Ids'] = self.ids_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.start_trigger_time is not None:
            result['StartTriggerTime'] = self.start_trigger_time

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')

        if m.get('EndTriggerTime') is not None:
            self.end_trigger_time = m.get('EndTriggerTime')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Filter') is not None:
            self.filter_shrink = m.get('Filter')

        if m.get('Ids') is not None:
            self.ids_shrink = m.get('Ids')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('StartTriggerTime') is not None:
            self.start_trigger_time = m.get('StartTriggerTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

