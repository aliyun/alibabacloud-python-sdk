# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class GetCopilotSessionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetCopilotSessionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        # - If `code == Success`, this field is empty.
        # - Otherwise, this field contains the request error message.
        self.message = message
        # The request ID. You can use it for end-to-end diagnostics.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetCopilotSessionResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetCopilotSessionResponseBodyData(DaraModel):
    def __init__(
        self,
        active_turn: main_models.GetCopilotSessionResponseBodyDataActiveTurn = None,
        created_at: str = None,
        cursor: str = None,
        last_turn: main_models.GetCopilotSessionResponseBodyDataLastTurn = None,
        name: str = None,
        scheduled_task: main_models.GetCopilotSessionResponseBodyDataScheduledTask = None,
        session_id: str = None,
        session_type: str = None,
        status: str = None,
        updated_at: str = None,
    ):
        # The execution information of the turn that currently occupies the session.
        self.active_turn = active_turn
        # The time when the session was created, in ISO 8601 format.
        self.created_at = created_at
        # The cursor of the latest persisted event in the current session.
        self.cursor = cursor
        # The information about the most recent execution turn.
        self.last_turn = last_turn
        # The session title.
        self.name = name
        # The snapshot information captured when the scheduled task was triggered.
        self.scheduled_task = scheduled_task
        # The session ID.
        self.session_id = session_id
        # The session source. Valid values:
        # - openapi: API call.
        # - cron: Scheduled task.
        # - im_dingtalk: DingTalk.
        # - im_feishu: Lark.
        # - alert: Alert.
        self.session_type = session_type
        # The session status. Valid values:
        # - active: The session is not archived.
        # - archived: The session is archived.
        self.status = status
        # The time when the session was last updated, in ISO 8601 format.
        self.updated_at = updated_at

    def validate(self):
        if self.active_turn:
            self.active_turn.validate()
        if self.last_turn:
            self.last_turn.validate()
        if self.scheduled_task:
            self.scheduled_task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_turn is not None:
            result['activeTurn'] = self.active_turn.to_map()

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.cursor is not None:
            result['cursor'] = self.cursor

        if self.last_turn is not None:
            result['lastTurn'] = self.last_turn.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.scheduled_task is not None:
            result['scheduledTask'] = self.scheduled_task.to_map()

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.session_type is not None:
            result['sessionType'] = self.session_type

        if self.status is not None:
            result['status'] = self.status

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activeTurn') is not None:
            temp_model = main_models.GetCopilotSessionResponseBodyDataActiveTurn()
            self.active_turn = temp_model.from_map(m.get('activeTurn'))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')

        if m.get('lastTurn') is not None:
            temp_model = main_models.GetCopilotSessionResponseBodyDataLastTurn()
            self.last_turn = temp_model.from_map(m.get('lastTurn'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('scheduledTask') is not None:
            temp_model = main_models.GetCopilotSessionResponseBodyDataScheduledTask()
            self.scheduled_task = temp_model.from_map(m.get('scheduledTask'))

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('sessionType') is not None:
            self.session_type = m.get('sessionType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

class GetCopilotSessionResponseBodyDataScheduledTask(DaraModel):
    def __init__(
        self,
        run_id: str = None,
        scheduled_at: str = None,
        started_at: str = None,
        task_id: int = None,
        task_name: str = None,
        timezone: str = None,
    ):
        # The ID of this scheduled execution. It is used to associate with the scheduled execution record. Multiple triggers of the same scheduled task use different runIds.
        self.run_id = run_id
        # The scheduled trigger time, in ISO 8601 format with a time zone. This field is empty if no record exists.
        self.scheduled_at = scheduled_at
        # The time when the processing of this schedule started, in ISO 8601 format with a time zone.
        self.started_at = started_at
        # The ID of the associated scheduled task.
        self.task_id = task_id
        # The name of the scheduled task when this trigger occurred. Subsequent changes to the task name do not change this snapshot.
        self.task_name = task_name
        # The scheduling time zone of the scheduled task.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.scheduled_at is not None:
            result['scheduledAt'] = self.scheduled_at

        if self.started_at is not None:
            result['startedAt'] = self.started_at

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.task_name is not None:
            result['taskName'] = self.task_name

        if self.timezone is not None:
            result['timezone'] = self.timezone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('scheduledAt') is not None:
            self.scheduled_at = m.get('scheduledAt')

        if m.get('startedAt') is not None:
            self.started_at = m.get('startedAt')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        return self

class GetCopilotSessionResponseBodyDataLastTurn(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        finished_at: str = None,
        input_tokens: int = None,
        output_tokens: int = None,
        pending_input_id: str = None,
        status: str = None,
        turn_id: str = None,
        updated_at: str = None,
    ):
        # The time when the execution turn was created, in ISO 8601 format.
        self.created_at = created_at
        # The time when the execution turn ended, in ISO 8601 format. This field is empty if the execution has not ended.
        self.finished_at = finished_at
        # The cumulative number of input tokens in this execution turn.
        self.input_tokens = input_tokens
        # The cumulative number of output tokens in this execution turn.
        self.output_tokens = output_tokens
        # The ID of the form that is waiting for user input. It is used when you submit user input. This field is empty if no form needs to be filled out.
        self.pending_input_id = pending_input_id
        # The execution status.
        self.status = status
        # The ID of the execution turn. It is used when you submit user input, reconnect, or stop the execution.
        self.turn_id = turn_id
        # The time when the execution turn was last updated, in ISO 8601 format.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.finished_at is not None:
            result['finishedAt'] = self.finished_at

        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        if self.pending_input_id is not None:
            result['pendingInputId'] = self.pending_input_id

        if self.status is not None:
            result['status'] = self.status

        if self.turn_id is not None:
            result['turnId'] = self.turn_id

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('finishedAt') is not None:
            self.finished_at = m.get('finishedAt')

        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

        if m.get('pendingInputId') is not None:
            self.pending_input_id = m.get('pendingInputId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('turnId') is not None:
            self.turn_id = m.get('turnId')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

class GetCopilotSessionResponseBodyDataActiveTurn(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        finished_at: str = None,
        input_tokens: int = None,
        output_tokens: int = None,
        pending_input_id: str = None,
        status: str = None,
        turn_id: str = None,
        updated_at: str = None,
    ):
        # The time when the execution turn was created, in ISO 8601 format.
        self.created_at = created_at
        # The time when the execution turn ended, in ISO 8601 format. This field is empty if the execution has not ended.
        self.finished_at = finished_at
        # The cumulative number of input tokens in this execution turn.
        self.input_tokens = input_tokens
        # The cumulative number of output tokens in this execution turn.
        self.output_tokens = output_tokens
        # The ID of the form that is waiting for user input. It is used when you submit user input. This field is empty if no form needs to be filled out.
        self.pending_input_id = pending_input_id
        # The execution status.
        self.status = status
        # The ID of the execution turn. It is used when you submit user input, reconnect, or stop the execution.
        self.turn_id = turn_id
        # The time when the execution turn was last updated, in ISO 8601 format.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.finished_at is not None:
            result['finishedAt'] = self.finished_at

        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        if self.pending_input_id is not None:
            result['pendingInputId'] = self.pending_input_id

        if self.status is not None:
            result['status'] = self.status

        if self.turn_id is not None:
            result['turnId'] = self.turn_id

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('finishedAt') is not None:
            self.finished_at = m.get('finishedAt')

        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

        if m.get('pendingInputId') is not None:
            self.pending_input_id = m.get('pendingInputId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('turnId') is not None:
            self.turn_id = m.get('turnId')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

