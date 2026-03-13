# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class AsyncTask(DaraModel):
    def __init__(
        self,
        already_retried_times: int = None,
        destination_status: str = None,
        duration_ms: int = None,
        end_time: int = None,
        events: List[main_models.AsyncTaskEvent] = None,
        function_arn: str = None,
        instance_id: str = None,
        qualifier: str = None,
        request_id: str = None,
        return_payload: str = None,
        started_time: int = None,
        status: str = None,
        task_error_message: str = None,
        task_id: str = None,
        task_payload: str = None,
    ):
        # The number of retries after the asynchronous task fails.
        self.already_retried_times = already_retried_times
        # The final state of the asynchronous task.
        self.destination_status = destination_status
        # The execution duration of the asynchronous task.
        self.duration_ms = duration_ms
        # The end time of the asynchronous task. Unit: milliseconds.
        self.end_time = end_time
        # The events of the asynchronous task.
        self.events = events
        # The Alibaba Cloud Resource Name (ARN) of the function.
        self.function_arn = function_arn
        # The ID of the instance that corresponds to the asynchronous task.
        self.instance_id = instance_id
        # The version or alias of the function.
        self.qualifier = qualifier
        # The ID of the request corresponding to this asynchronous task.
        self.request_id = request_id
        # The content of the response after the asynchronous task is executed. The maximum size is 1 MB. This parameter is in public preview. If you want to use this parameter, [contact us](https://help.aliyun.com/document_detail/2513733.html).
        self.return_payload = return_payload
        # The start time of the asynchronous task. Unit: milliseconds.
        self.started_time = started_time
        # The state of the asynchronous task.
        # 
        # *   Enqueued: The asynchronous invocation is enqueued and waiting to be executed.
        # *   Succeeded: The invocation is successful.
        # *   Failed: The invocation fails.
        # *   Running: The invocation is being executed.
        # *   Stopped: The invocation is terminated.
        # *   Stopping: The invocation is being terminated.
        # *   Invalid: The invocation is invalid and not executed due to specific reasons. For example, the function is deleted.
        # *   Expired: The maximum validity period of messages is specified for asynchronous invocation. The invocation is discarded and not executed because the specified maximum validity period of messages expires.
        # *   Retrying: The asynchronous invocation is being retried due to an execution error.
        self.status = status
        # The error message for an asynchronous task failure.
        self.task_error_message = task_error_message
        # The ID of the asynchronous task.
        self.task_id = task_id
        # The content of the input parameter during asynchronous task execution.
        self.task_payload = task_payload

    def validate(self):
        if self.events:
            for v1 in self.events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.already_retried_times is not None:
            result['alreadyRetriedTimes'] = self.already_retried_times

        if self.destination_status is not None:
            result['destinationStatus'] = self.destination_status

        if self.duration_ms is not None:
            result['durationMs'] = self.duration_ms

        if self.end_time is not None:
            result['endTime'] = self.end_time

        result['events'] = []
        if self.events is not None:
            for k1 in self.events:
                result['events'].append(k1.to_map() if k1 else None)

        if self.function_arn is not None:
            result['functionArn'] = self.function_arn

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.qualifier is not None:
            result['qualifier'] = self.qualifier

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.return_payload is not None:
            result['returnPayload'] = self.return_payload

        if self.started_time is not None:
            result['startedTime'] = self.started_time

        if self.status is not None:
            result['status'] = self.status

        if self.task_error_message is not None:
            result['taskErrorMessage'] = self.task_error_message

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.task_payload is not None:
            result['taskPayload'] = self.task_payload

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alreadyRetriedTimes') is not None:
            self.already_retried_times = m.get('alreadyRetriedTimes')

        if m.get('destinationStatus') is not None:
            self.destination_status = m.get('destinationStatus')

        if m.get('durationMs') is not None:
            self.duration_ms = m.get('durationMs')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        self.events = []
        if m.get('events') is not None:
            for k1 in m.get('events'):
                temp_model = main_models.AsyncTaskEvent()
                self.events.append(temp_model.from_map(k1))

        if m.get('functionArn') is not None:
            self.function_arn = m.get('functionArn')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('returnPayload') is not None:
            self.return_payload = m.get('returnPayload')

        if m.get('startedTime') is not None:
            self.started_time = m.get('startedTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskErrorMessage') is not None:
            self.task_error_message = m.get('taskErrorMessage')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('taskPayload') is not None:
            self.task_payload = m.get('taskPayload')

        return self

