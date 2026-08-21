# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetWorkflowTaskResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        finish_time_utc: str = None,
        gmt_create_utc: str = None,
        node_results: str = None,
        outputs: str = None,
        request_id: str = None,
        status: str = None,
        task_id: str = None,
        user_data: str = None,
        workflow_id: str = None,
    ):
        # The error code returned when transcoding fails.
        self.error_code = error_code
        # The error message returned when transcoding fails.
        self.error_message = error_message
        # The time when the task was completed. The time is in the yyyy-MM-ddTHH:mm:ssZ format.
        self.finish_time_utc = finish_time_utc
        # The time when the task was created. The time is in the yyyy-MM-ddTHH:mm:ssZ format.
        self.gmt_create_utc = gmt_create_utc
        # The node results of the workflow task. The value is in JSON format and varies based on the workflow configuration.
        self.node_results = node_results
        # The output information.
        self.outputs = outputs
        # Id of the request
        self.request_id = request_id
        # The result of this review. This indicates the current manual review result. Valid values:
        # - **running**: Running.
        # - **stopped**: Stopped.
        # - **failed**: Failed.
        # - **partial-succeeded**: Partially succeeded.
        # - **succeeded**: Succeeded.
        self.status = status
        # The task ID used to query the refresh status.
        self.task_id = task_id
        # The custom information.
        self.user_data = user_data
        # The workflow ID. You can log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Configuration Management** > **Media Processing** > **Workflow Management** to view the ID.
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.finish_time_utc is not None:
            result['FinishTimeUtc'] = self.finish_time_utc

        if self.gmt_create_utc is not None:
            result['GmtCreateUtc'] = self.gmt_create_utc

        if self.node_results is not None:
            result['NodeResults'] = self.node_results

        if self.outputs is not None:
            result['Outputs'] = self.outputs

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('FinishTimeUtc') is not None:
            self.finish_time_utc = m.get('FinishTimeUtc')

        if m.get('GmtCreateUtc') is not None:
            self.gmt_create_utc = m.get('GmtCreateUtc')

        if m.get('NodeResults') is not None:
            self.node_results = m.get('NodeResults')

        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

