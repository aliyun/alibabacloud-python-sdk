# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class UpdateCopilotSessionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateCopilotSessionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The returned status code. A value of Success indicates that the request is successful. Other values indicate that the request failed.
        self.code = code
        # The returned data.
        self.data = data
        # The error message. If the code is Success, this field is empty. Otherwise, this field contains the error message of the request.
        self.message = message
        # The request ID. You can use this ID for end-to-end diagnostics.
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
            temp_model = main_models.UpdateCopilotSessionResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class UpdateCopilotSessionResponseBodyData(DaraModel):
    def __init__(
        self,
        active_turn: main_models.UpdateCopilotSessionResponseBodyDataActiveTurn = None,
        created_at: str = None,
        cursor: str = None,
        last_turn: main_models.UpdateCopilotSessionResponseBodyDataLastTurn = None,
        name: str = None,
        scheduled_task: main_models.UpdateCopilotSessionResponseBodyDataScheduledTask = None,
        session_id: str = None,
        session_type: str = None,
        status: str = None,
        updated_at: str = None,
    ):
        # The summary of the execution that currently occupies the session. This field is empty when no active execution is in progress. An execution with an unknown outcome may still occupy the session.
        self.active_turn = active_turn
        # The time when the session was created. The time is in the ISO 8601 format.
        self.created_at = created_at
        # The latest persisted event cursor for the current session, returned as a decimal string. The value is 0 when no events exist. This value does not represent the position consumed by the client.
        self.cursor = cursor
        # The summary of the most recent execution. This field is empty if no execution has ever occurred. If the most recent execution has not ended, this field may point to the same execution as activeTurn.
        self.last_turn = last_turn
        # The session title.
        self.name = name
        # The snapshot information when the scheduled task is triggered. This field is returned only for scheduled task sessions and is empty for sessions from other sources. Subsequent renaming or deletion of the task does not change the historical snapshot.
        self.scheduled_task = scheduled_task
        # The session ID.
        self.session_id = session_id
        # The source from which the session was created. Valid values: openapi (proactive call), cron (scheduled task), im_dingtalk (DingTalk), im_feishu (Lark), and alert (alert). This value is determined by the server and is not changed by subsequent follow-up questions.
        self.session_type = session_type
        # The session status. Valid values: active (not archived) and archived (archived). This field does not indicate whether the execution has ended.
        self.status = status
        # The time when the session was last updated. The time is in the ISO 8601 format.
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
            temp_model = main_models.UpdateCopilotSessionResponseBodyDataActiveTurn()
            self.active_turn = temp_model.from_map(m.get('activeTurn'))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')

        if m.get('lastTurn') is not None:
            temp_model = main_models.UpdateCopilotSessionResponseBodyDataLastTurn()
            self.last_turn = temp_model.from_map(m.get('lastTurn'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('scheduledTask') is not None:
            temp_model = main_models.UpdateCopilotSessionResponseBodyDataScheduledTask()
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

class UpdateCopilotSessionResponseBodyDataScheduledTask(DaraModel):
    def __init__(
        self,
        run_id: str = None,
        scheduled_at: str = None,
        started_at: str = None,
        task_id: int = None,
        task_name: str = None,
        timezone: str = None,
    ):
        # The ID of this scheduled execution. Multiple triggers of the same scheduled task use different runIds.
        self.run_id = run_id
        # The scheduled trigger time. The time is in the ISO 8601 format with a time zone. This field is empty when no record exists.
        self.scheduled_at = scheduled_at
        # The time when Copilot started processing this schedule. The time is in the ISO 8601 format with a time zone. This is not the time when the model outputs the first token.
        self.started_at = started_at
        # The ID of the associated scheduled task.
        self.task_id = task_id
        # The name of the scheduled task at the time of this trigger.
        self.task_name = task_name
        # The scheduling time zone of the scheduled task, such as Asia/Shanghai.
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

class UpdateCopilotSessionResponseBodyDataLastTurn(DaraModel):
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
        # The time when the current execution turn was created. The time is in the ISO 8601 format.
        self.created_at = created_at
        # The time when the execution ended. The time is in the ISO 8601 format. This field is empty if the execution has not ended.
        self.finished_at = finished_at
        # The cumulative number of input tokens for the current turn. This is not the incremental usage for the current event.
        self.input_tokens = input_tokens
        # The cumulative number of output tokens for the current turn.
        self.output_tokens = output_tokens
        # The ID of the form that is currently waiting for user input. This ID is used when user input is submitted. This field is empty when no form is pending.
        self.pending_input_id = pending_input_id
        # The execution status. Valid values: running (in progress), waiting_input (waiting for user input), cancelling (being canceled), completed (completed), failed (failed), cancelled (canceled), and outcome_unknown (the outcome is unknown, the session may still be occupied, and the execution should not be automatically rerun).
        self.status = status
        # The ID of the current execution turn. You can use this ID to submit user input, reconnect, or stop the execution.
        self.turn_id = turn_id
        # The time when the current execution turn was last updated. The time is in the ISO 8601 format.
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

class UpdateCopilotSessionResponseBodyDataActiveTurn(DaraModel):
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
        # The time when the current execution turn was created. The time is in the ISO 8601 format.
        self.created_at = created_at
        # The time when the execution ended. The time is in the ISO 8601 format. This field is empty if the execution has not ended.
        self.finished_at = finished_at
        # The cumulative number of input tokens for the current turn. This is not the incremental usage for the current event.
        self.input_tokens = input_tokens
        # The cumulative number of output tokens for the current turn.
        self.output_tokens = output_tokens
        # The ID of the form that is currently waiting for user input. This ID is used when user input is submitted. This field is empty when no form is pending.
        self.pending_input_id = pending_input_id
        # The execution status. Valid values: running (in progress), waiting_input (waiting for user input), cancelling (being canceled), completed (completed), failed (failed), cancelled (canceled), and outcome_unknown (the outcome is unknown, the session may still be occupied, and the execution should not be automatically rerun).
        self.status = status
        # The ID of the current execution turn. You can use this ID to submit user input, reconnect, or stop the execution.
        self.turn_id = turn_id
        # The time when the current execution turn was last updated. The time is in the ISO 8601 format.
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

