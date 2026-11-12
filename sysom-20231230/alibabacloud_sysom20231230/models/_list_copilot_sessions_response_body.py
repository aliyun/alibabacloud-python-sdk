# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class ListCopilotSessionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListCopilotSessionsResponseBodyData = None,
        max_results: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The returned status code. Success indicates that the request is successful. Other values indicate that the request failed.
        self.code = code
        # The returned data.
        self.data = data
        # The page size used for the current request.
        self.max_results = max_results
        # The error message. If code is Success, this field is empty. Otherwise, this field contains the request error message.
        self.message = message
        # The request ID, which can be used for end-to-end diagnostics.
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

        if self.max_results is not None:
            result['maxResults'] = self.max_results

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
            temp_model = main_models.ListCopilotSessionsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListCopilotSessionsResponseBodyData(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        sessions: List[main_models.ListCopilotSessionsResponseBodyDataSessions] = None,
    ):
        # The page size used for the current request.
        self.max_results = max_results
        # The pagination token for the next page. Pass this value back as is in the next request. An empty value indicates that no more pages are available.
        self.next_token = next_token
        # The session list.
        self.sessions = sessions

    def validate(self):
        if self.sessions:
            for v1 in self.sessions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        result['sessions'] = []
        if self.sessions is not None:
            for k1 in self.sessions:
                result['sessions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        self.sessions = []
        if m.get('sessions') is not None:
            for k1 in m.get('sessions'):
                temp_model = main_models.ListCopilotSessionsResponseBodyDataSessions()
                self.sessions.append(temp_model.from_map(k1))

        return self

class ListCopilotSessionsResponseBodyDataSessions(DaraModel):
    def __init__(
        self,
        active_turn: main_models.ListCopilotSessionsResponseBodyDataSessionsActiveTurn = None,
        active_turn_id: str = None,
        agent_id: str = None,
        created_at: str = None,
        id: str = None,
        name: str = None,
        scheduled_task: main_models.ListCopilotSessionsResponseBodyDataSessionsScheduledTask = None,
        session_id: str = None,
        session_type: str = None,
        status: str = None,
        updated_at: str = None,
        user_id: str = None,
    ):
        # The information about the execution that currently occupies the session.
        self.active_turn = active_turn
        # The ID of the execution that currently occupies the session. This field is empty when no active execution exists.
        self.active_turn_id = active_turn_id
        # The Agent tag of the session. The current executor is subject to activeTurn.agentId.
        self.agent_id = agent_id
        # The time when the session was created, in ISO 8601 format.
        self.created_at = created_at
        # The session ID.
        self.id = id
        # The session title.
        self.name = name
        # The snapshot information when the scheduled task is triggered. This field is returned only for scheduled task sessions and is empty for sessions from other sources.
        self.scheduled_task = scheduled_task
        # The session ID. Use this value when you send questions, query history, and delete sessions later.
        self.session_id = session_id
        # The source from which the session was created. Valid values:
        # - openapi: API call.
        # - cron: Scheduled task.
        # - im_dingtalk: DingTalk.
        # - im_feishu: Lark.
        # - alert: Alert.
        # This value is determined by the server and is not changed by subsequent follow-up questions.
        self.session_type = session_type
        # The session status. Valid values:
        # - active: Not archived.
        # - archived: Archived.
        # This field does not indicate whether the execution has ended.
        self.status = status
        # The time when the session was last updated, in ISO 8601 format.
        self.updated_at = updated_at
        # The ID of the user to whom the session belongs. This value is determined by the server based on the caller identity and is not used as a parameter for the client to specify the identity.
        self.user_id = user_id

    def validate(self):
        if self.active_turn:
            self.active_turn.validate()
        if self.scheduled_task:
            self.scheduled_task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_turn is not None:
            result['activeTurn'] = self.active_turn.to_map()

        if self.active_turn_id is not None:
            result['activeTurnId'] = self.active_turn_id

        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.id is not None:
            result['id'] = self.id

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

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activeTurn') is not None:
            temp_model = main_models.ListCopilotSessionsResponseBodyDataSessionsActiveTurn()
            self.active_turn = temp_model.from_map(m.get('activeTurn'))

        if m.get('activeTurnId') is not None:
            self.active_turn_id = m.get('activeTurnId')

        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('scheduledTask') is not None:
            temp_model = main_models.ListCopilotSessionsResponseBodyDataSessionsScheduledTask()
            self.scheduled_task = temp_model.from_map(m.get('scheduledTask'))

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('sessionType') is not None:
            self.session_type = m.get('sessionType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class ListCopilotSessionsResponseBodyDataSessionsScheduledTask(DaraModel):
    def __init__(
        self,
        run_id: str = None,
        scheduled_at: str = None,
        started_at: str = None,
        task_id: int = None,
        task_name: str = None,
        timezone: str = None,
    ):
        # The ID of the current scheduled execution. Different runIds are used for multiple triggers of the same scheduled task.
        self.run_id = run_id
        # The scheduled trigger time, in ISO 8601 format with time zone. This field is empty when no record exists.
        self.scheduled_at = scheduled_at
        # The time when Copilot started processing the current schedule, in ISO 8601 format with time zone. This is not the time when the model outputs the first token.
        self.started_at = started_at
        # The ID of the associated scheduled task.
        self.task_id = task_id
        # The name of the scheduled task at the time of this trigger.
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

class ListCopilotSessionsResponseBodyDataSessionsActiveTurn(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        created_at: str = None,
        finished_at: str = None,
        input_tokens: int = None,
        output_tokens: int = None,
        pending_input_id: str = None,
        status: str = None,
        turn_id: str = None,
        updated_at: str = None,
    ):
        # The Agent ID bound to the current execution round.
        self.agent_id = agent_id
        # The time when the current execution round was created, in ISO 8601 format.
        self.created_at = created_at
        # The time when the execution ended, in ISO 8601 format. This field is empty if the execution has not ended.
        self.finished_at = finished_at
        # The cumulative number of input tokens in the current round, which is not the incremental usage of the current event.
        self.input_tokens = input_tokens
        # The cumulative number of output tokens in the current round.
        self.output_tokens = output_tokens
        # The ID of the form that is currently waiting for the user to fill out. This field is used when user input is submitted. This field is empty when no form needs to be filled out.
        self.pending_input_id = pending_input_id
        # The execution status. Valid values:
        # - running: The execution is in progress.
        # - waiting_input: Waiting for user input.
        # - cancelling: The execution is being canceled.
        # - completed: The execution is completed.
        # - failed: The execution failed.
        # - cancelled: The execution is canceled.
        # - outcome_unknown: The result is unknown, and the session may still be occupied. The execution should not be automatically rerun.
        self.status = status
        # The ID of the current execution round, which is used to submit user input, reconnect, or stop the execution.
        self.turn_id = turn_id
        # The time when the current execution round was last updated, in ISO 8601 format.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

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
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

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

