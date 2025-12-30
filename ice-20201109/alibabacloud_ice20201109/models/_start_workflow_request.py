# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartWorkflowRequest(DaraModel):
    def __init__(
        self,
        skip_input_verification: bool = None,
        task_input: str = None,
        user_data: str = None,
        workflow_id: str = None,
    ):
        self.skip_input_verification = skip_input_verification
        # The workflow input. Only media assets are supported.
        self.task_input = task_input
        # The user-defined data in the JSON format, which cannot be up to 512 bytes in length. You can specify a custom callback URL. For more information, see [Configure a callback upon editing completion](https://help.aliyun.com/document_detail/451631.html).
        self.user_data = user_data
        # The ID of the workflow template. To view the template ID, log on to the [IMS console](https://ims.console.aliyun.com/settings/workflow/list) and choose Configurations > Workflow Template.
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.skip_input_verification is not None:
            result['SkipInputVerification'] = self.skip_input_verification

        if self.task_input is not None:
            result['TaskInput'] = self.task_input

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkipInputVerification') is not None:
            self.skip_input_verification = m.get('SkipInputVerification')

        if m.get('TaskInput') is not None:
            self.task_input = m.get('TaskInput')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

