# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        completed_time: int = None,
        created_time: int = None,
        description: str = None,
        message: str = None,
        name: str = None,
        progress: int = None,
        request_id: str = None,
        result: str = None,
        success: bool = None,
        updated_time: int = None,
    ):
        # HttpCode
        self.code = code
        # The time when the task was complete. The time is a UNIX timestamp. Unit: seconds.
        self.completed_time = completed_time
        # The time when the job was created. This value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time
        # The status of the job. Valid values:
        # 
        # *   **created**: The job is created.
        # *   **expired**: The job expires.
        # *   **completed**: The job is completed.
        # *   **cancelled**: The job is canceled.
        self.description = description
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The name of the job.
        self.name = name
        # The progress of the job. Valid values: 0 to 100. Unit: percentage (%). If the job fails, the value -1 is returned.
        self.progress = progress
        # The ID of the request.
        self.request_id = request_id
        # The result of the job.
        self.result = result
        # Indicates whether the call is successful.
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success
        # The time when the job was updated. This value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.completed_time is not None:
            result['CompletedTime'] = self.completed_time

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.message is not None:
            result['Message'] = self.message

        if self.name is not None:
            result['Name'] = self.name

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result

        if self.success is not None:
            result['Success'] = self.success

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        return self

