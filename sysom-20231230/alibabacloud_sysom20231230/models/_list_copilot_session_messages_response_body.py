# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class ListCopilotSessionMessagesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListCopilotSessionMessagesResponseBodyData = None,
        max_results: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The returned status code. Success indicates that the request is successful. Other values indicate that the request failed.
        self.code = code
        # The returned data.
        self.data = data
        # A field retained for historical compatibility, which may be omitted. Use data.maxResults instead.
        self.max_results = max_results
        # The error message. If the code is Success, this field is empty. Otherwise, this field contains the error message of the request.
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
            temp_model = main_models.ListCopilotSessionMessagesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListCopilotSessionMessagesResponseBodyData(DaraModel):
    def __init__(
        self,
        cursor: str = None,
        has_more: bool = None,
        max_results: int = None,
        messages: List[main_models.ListCopilotSessionMessagesResponseBodyDataMessages] = None,
        next_token: str = None,
        session: main_models.ListCopilotSessionMessagesResponseBodyDataSession = None,
    ):
        # The cursor of the last event on the current page, returned as a decimal string. The value is 0 for an empty page. This is not the pagination nextToken and does not indicate that a round of execution has finished.
        self.cursor = cursor
        # Indicates whether there are subsequent historical events. Valid values:
        # - true: Yes.
        # - false: No.
        self.has_more = has_more
        # The page size used for the current request.
        self.max_results = max_results
        # The history event records on the current page, sorted in ascending order by eventId. A record does not necessarily represent a complete chat message and may be a chunk of text or a tool calling (invoke) event.
        self.messages = messages
        # The token for the next page. Pass this value back as is in the next request. An empty value indicates that there is no next page.
        self.next_token = next_token
        # The session summary of the current user. This object does not contain the active execution summary. To query the execution status, call GetCopilotSession.
        self.session = session

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()
        if self.session:
            self.session.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cursor is not None:
            result['cursor'] = self.cursor

        if self.has_more is not None:
            result['hasMore'] = self.has_more

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        result['messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['messages'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.session is not None:
            result['session'] = self.session.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')

        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        self.messages = []
        if m.get('messages') is not None:
            for k1 in m.get('messages'):
                temp_model = main_models.ListCopilotSessionMessagesResponseBodyDataMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('session') is not None:
            temp_model = main_models.ListCopilotSessionMessagesResponseBodyDataSession()
            self.session = temp_model.from_map(m.get('session'))

        return self

class ListCopilotSessionMessagesResponseBodyDataSession(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        created_at: str = None,
        id: str = None,
        name: str = None,
        scheduled_task: main_models.ListCopilotSessionMessagesResponseBodyDataSessionScheduledTask = None,
        session_id: str = None,
        session_type: str = None,
        updated_at: str = None,
        user_id: str = None,
    ):
        # The agent identifier in the session summary, which does not represent the current executor. The current executor is subject to activeTurn.agentId.
        self.agent_id = agent_id
        # The time when the session was created, in ISO 8601 format.
        self.created_at = created_at
        # The session ID, which is the same as sessionId. We recommend using sessionId to initiate subsequent requests.
        self.id = id
        # The session title.
        self.name = name
        # The snapshot information when the scheduled task is triggered. This field is returned only for scheduled task sessions and is empty for sessions from other sources. Subsequent renaming or deletion of the task does not change the historical snapshot.
        self.scheduled_task = scheduled_task
        # The session ID. Use this value when you send follow-up questions, query history, or delete the session.
        self.session_id = session_id
        # The source from which the session was created. Valid values:
        # - openapi: Active call.
        # - cron: Scheduled task.
        # - im_dingtalk: DingTalk.
        # - im_feishu: Lark.
        # - alert: Alert.
        # This value is determined by the server and is not changed by follow-up questions.
        self.session_type = session_type
        # The time when the session was last updated, in ISO 8601 format.
        self.updated_at = updated_at
        # The ID of the user to whom the session belongs. This value is determined by the server based on the caller identity and is not used as a parameter for the client to specify the identity.
        self.user_id = user_id

    def validate(self):
        if self.scheduled_task:
            self.scheduled_task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('scheduledTask') is not None:
            temp_model = main_models.ListCopilotSessionMessagesResponseBodyDataSessionScheduledTask()
            self.scheduled_task = temp_model.from_map(m.get('scheduledTask'))

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('sessionType') is not None:
            self.session_type = m.get('sessionType')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class ListCopilotSessionMessagesResponseBodyDataSessionScheduledTask(DaraModel):
    def __init__(
        self,
        run_id: str = None,
        scheduled_at: str = None,
        started_at: str = None,
        task_id: int = None,
        task_name: str = None,
        timezone: str = None,
    ):
        # The ID of this scheduled execution. Different runIds are used for multiple triggers of the same scheduled task.
        self.run_id = run_id
        # The scheduled trigger time, in ISO 8601 format with time zone. This field is empty if there is no record.
        self.scheduled_at = scheduled_at
        # The time when Copilot started processing this schedule, in ISO 8601 format with time zone. This is not the time when the model outputs the first token.
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

class ListCopilotSessionMessagesResponseBodyDataMessages(DaraModel):
    def __init__(
        self,
        content: List[main_models.ListCopilotSessionMessagesResponseBodyDataMessagesContent] = None,
        created_at: str = None,
        event_id: str = None,
        finished_at: str = None,
        id: str = None,
        metadata: Any = None,
        name: str = None,
        role: str = None,
        turn_id: str = None,
        usage: Any = None,
    ):
        # The human-readable content summary of the event. To restore the complete interactive interface, use the original event in metadata.
        self.content = content
        # The time when the historical event record was created, in ISO 8601 format.
        self.created_at = created_at
        # The position of the event within the session, used for sorting and deduplication.
        self.event_id = event_id
        # Currently, an empty string is returned. This field is not used to determine whether the execution has finished.
        self.finished_at = finished_at
        # The ID of the historical event record.
        self.id = id
        # The complete original event object. The internal fields retain their original protocol names, without recursive naming conversion or the need for further JSON string parsing.
        self.metadata = metadata
        # Currently, an empty string is returned. This field is not used to identify the event type.
        self.name = name
        # The role in the original event. An empty string is returned if the event does not contain a role.
        self.role = role
        # The ID of the associated execution. This field is empty if there is no associated execution.
        self.turn_id = turn_id
        # The token usage per event. This data is not currently returned. To query the cumulative usage of an execution, call GetCopilotSession.
        self.usage = usage

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['content'].append(k1.to_map() if k1 else None)

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.event_id is not None:
            result['eventId'] = self.event_id

        if self.finished_at is not None:
            result['finishedAt'] = self.finished_at

        if self.id is not None:
            result['id'] = self.id

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.name is not None:
            result['name'] = self.name

        if self.role is not None:
            result['role'] = self.role

        if self.turn_id is not None:
            result['turnId'] = self.turn_id

        if self.usage is not None:
            result['usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('content') is not None:
            for k1 in m.get('content'):
                temp_model = main_models.ListCopilotSessionMessagesResponseBodyDataMessagesContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')

        if m.get('finishedAt') is not None:
            self.finished_at = m.get('finishedAt')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('turnId') is not None:
            self.turn_id = m.get('turnId')

        if m.get('usage') is not None:
            self.usage = m.get('usage')

        return self

class ListCopilotSessionMessagesResponseBodyDataMessagesContent(DaraModel):
    def __init__(
        self,
        text: str = None,
        type: str = None,
    ):
        # The readable text content in the event. This field is empty if no readable string is available.
        self.text = text
        # The event type, such as USER_MESSAGE, TEXT_MESSAGE_CONTENT, or TOOL_CALL_ARGS. This is not fixed to text.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text is not None:
            result['text'] = self.text

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

