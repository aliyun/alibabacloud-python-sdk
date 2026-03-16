# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fnf20190315 import models as main_models
from darabonba.model import DaraModel

class GetExecutionHistoryResponseBody(DaraModel):
    def __init__(
        self,
        events: List[main_models.GetExecutionHistoryResponseBodyEvents] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The events.
        self.events = events
        # You do not need to specify this parameter for the first request. The returned value of **ScheduleEventId** is used as the token for the next query. No value is returned for the last query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

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
        result['Events'] = []
        if self.events is not None:
            for k1 in self.events:
                result['Events'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k1 in m.get('Events'):
                temp_model = main_models.GetExecutionHistoryResponseBodyEvents()
                self.events.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetExecutionHistoryResponseBodyEvents(DaraModel):
    def __init__(
        self,
        event_detail: str = None,
        event_id: int = None,
        schedule_event_id: int = None,
        step_name: str = None,
        time: str = None,
        type: str = None,
    ):
        # The details about the execution step.
        self.event_detail = event_detail
        # The ID of the execution step.
        self.event_id = event_id
        # The ID of the scheduling step.
        self.schedule_event_id = schedule_event_id
        # The name of the execution step.
        self.step_name = step_name
        # The time when the event was updated.
        self.time = time
        # The type of the execution step. Valid values:
        # 
        # *   **StepEntered**
        # *   **StepStarted**
        # *   **StepSucceeded**
        # *   **StepFailed**
        # *   **StepExited**
        # *   **BranchEntered**
        # *   **BranchExited**
        # *   **IterationEntered**
        # *   **IterationExited**
        # *   **TaskScheduled**
        # *   **TaskStarted**
        # *   **TaskSubmitted**
        # *   **TaskSubmitFailed**
        # *   **TaskSucceeded**
        # *   **TaskFailed**
        # *   **TaskTimedOut**
        # *   **ExecutionStarted**
        # *   **ExecutionStopped**
        # *   **ExecutionSucceeded**
        # *   **ExecutionFailed**
        # *   **ExecutionTimedOut**
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_detail is not None:
            result['EventDetail'] = self.event_detail

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.schedule_event_id is not None:
            result['ScheduleEventId'] = self.schedule_event_id

        if self.step_name is not None:
            result['StepName'] = self.step_name

        if self.time is not None:
            result['Time'] = self.time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventDetail') is not None:
            self.event_detail = m.get('EventDetail')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('ScheduleEventId') is not None:
            self.schedule_event_id = m.get('ScheduleEventId')

        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

