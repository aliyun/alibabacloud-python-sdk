# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartAIWorkflowRequest(DaraModel):
    def __init__(
        self,
        dispatch_tag: str = None,
        inputs: str = None,
        user_data: str = None,
        workflow_id: str = None,
    ):
        # The tag for the task.
        self.dispatch_tag = dispatch_tag
        # A JSON string containing the specific input parameters, such as information about the media assets, standard live streams, or RTC streams.
        self.inputs = inputs
        # A user-defined parameter for passing custom metadata.
        self.user_data = user_data
        # The ID of the workflow template.
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dispatch_tag is not None:
            result['DispatchTag'] = self.dispatch_tag

        if self.inputs is not None:
            result['Inputs'] = self.inputs

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DispatchTag') is not None:
            self.dispatch_tag = m.get('DispatchTag')

        if m.get('Inputs') is not None:
            self.inputs = m.get('Inputs')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

