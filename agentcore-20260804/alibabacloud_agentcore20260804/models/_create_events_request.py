# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateEventsRequest(DaraModel):
    def __init__(
        self,
        body: main_models.CreateEventsRequestBody = None,
    ):
        # The JSON request body.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.CreateEventsRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class CreateEventsRequestBody(DaraModel):
    def __init__(
        self,
        events: List[main_models.CreateEventsRequestBodyEvents] = None,
        scope: main_models.CreateEventsRequestBodyScope = None,
        session: main_models.CreateEventsRequestBodySession = None,
    ):
        # A list of 1 to 100 events. The request body cannot exceed 1 MiB.
        # 
        # This parameter is required.
        self.events = events
        # The exact session to which all events belong.
        # 
        # This parameter is required.
        self.scope = scope
        # The information saved when the first event is successfully written. It is not overwritten by subsequent writes.
        self.session = session

    def validate(self):
        if self.events:
            for v1 in self.events:
                 if v1:
                    v1.validate()
        if self.scope:
            self.scope.validate()
        if self.session:
            self.session.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['events'] = []
        if self.events is not None:
            for k1 in self.events:
                result['events'].append(k1.to_map() if k1 else None)

        if self.scope is not None:
            result['scope'] = self.scope.to_map()

        if self.session is not None:
            result['session'] = self.session.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('events') is not None:
            for k1 in m.get('events'):
                temp_model = main_models.CreateEventsRequestBodyEvents()
                self.events.append(temp_model.from_map(k1))

        if m.get('scope') is not None:
            temp_model = main_models.CreateEventsRequestBodyScope()
            self.scope = temp_model.from_map(m.get('scope'))

        if m.get('session') is not None:
            temp_model = main_models.CreateEventsRequestBodySession()
            self.session = temp_model.from_map(m.get('session'))

        return self

class CreateEventsRequestBodySession(DaraModel):
    def __init__(
        self,
        metadata: Dict[str, str] = None,
        title: str = None,
    ):
        # The JSON metadata of the session.
        self.metadata = metadata
        # The session title. It can be up to 256 characters in length.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class CreateEventsRequestBodyScope(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        session_id: str = None,
        team_id: str = None,
        user_id: str = None,
    ):
        # The business agent ID.
        self.agent_id = agent_id
        # The exact session ID.
        # 
        # This parameter is required.
        self.session_id = session_id
        # The business team ID.
        self.team_id = team_id
        # The business user ID. This is not the platform tenant identity.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.team_id is not None:
            result['teamId'] = self.team_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('teamId') is not None:
            self.team_id = m.get('teamId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class CreateEventsRequestBodyEvents(DaraModel):
    def __init__(
        self,
        data: main_models.CreateEventsRequestBodyEventsData = None,
        timestamp: int = None,
        type: str = None,
    ):
        # The event-specific data. Use the corresponding fields based on the type. For conditional requirements, refer to the description of each field.
        # 
        # This parameter is required.
        self.data = data
        # The actual occurrence time provided by the client as a Unix timestamp in milliseconds. This is the only source for business sorting. Identical values do not indicate a known sequence, and the array position does not imply a business order.
        # 
        # This parameter is required.
        self.timestamp = timestamp
        # The event type. This determines the applicable fields and conditional requirements for the data.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.CreateEventsRequestBodyEventsData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateEventsRequestBodyEventsData(DaraModel):
    def __init__(
        self,
        call_id: str = None,
        content: List[main_models.CreateEventsRequestBodyEventsDataContent] = None,
        event_ids: List[str] = None,
        parent_event_id: str = None,
        parent_scope: main_models.CreateEventsRequestBodyEventsDataParentScope = None,
        role: str = None,
        summary: str = None,
    ):
        # The call ID. This field is required for tool_call and tool_result events, or message events with the role set to tool. It associates the call intent, actual execution, and feedback.
        self.call_id = call_id
        # The ordered content blocks. This field is required for message and tool_result events. Use a text block for plain text. This can be an empty array if the tool has no output.
        self.content = content
        # The list of visible event IDs referenced by the summary. This list cannot be empty.
        self.event_ids = event_ids
        # The anchor event ID of the parent session. This field is required for session_fork events. The child session continues from the valid context at this anchor and does not inherit interactions after the anchor.
        self.parent_event_id = parent_event_id
        # The business scope of the parent session. This field is required for session_fork events. The event is written to the child session, and the requested scope is the child session.
        self.parent_scope = parent_scope
        # The message role. This field is required for message events.
        self.role = role
        # The human-readable summary. This field is optional for context_update events.
        self.summary = summary

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()
        if self.parent_scope:
            self.parent_scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_id is not None:
            result['callId'] = self.call_id

        result['content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['content'].append(k1.to_map() if k1 else None)

        if self.event_ids is not None:
            result['eventIds'] = self.event_ids

        if self.parent_event_id is not None:
            result['parentEventId'] = self.parent_event_id

        if self.parent_scope is not None:
            result['parentScope'] = self.parent_scope.to_map()

        if self.role is not None:
            result['role'] = self.role

        if self.summary is not None:
            result['summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('callId') is not None:
            self.call_id = m.get('callId')

        self.content = []
        if m.get('content') is not None:
            for k1 in m.get('content'):
                temp_model = main_models.CreateEventsRequestBodyEventsDataContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('eventIds') is not None:
            self.event_ids = m.get('eventIds')

        if m.get('parentEventId') is not None:
            self.parent_event_id = m.get('parentEventId')

        if m.get('parentScope') is not None:
            temp_model = main_models.CreateEventsRequestBodyEventsDataParentScope()
            self.parent_scope = temp_model.from_map(m.get('parentScope'))

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('summary') is not None:
            self.summary = m.get('summary')

        return self

class CreateEventsRequestBodyEventsDataParentScope(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        session_id: str = None,
        team_id: str = None,
        user_id: str = None,
    ):
        # The business agent ID.
        self.agent_id = agent_id
        # The exact session ID.
        # 
        # This parameter is required.
        self.session_id = session_id
        # The business team ID.
        self.team_id = team_id
        # The business user ID. This is not the platform tenant identity.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.team_id is not None:
            result['teamId'] = self.team_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('teamId') is not None:
            self.team_id = m.get('teamId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class CreateEventsRequestBodyEventsDataContent(DaraModel):
    def __init__(
        self,
        arguments: Any = None,
        call_id: str = None,
        format: str = None,
        name: str = None,
        text: str = None,
        type: str = None,
        value: Any = None,
    ):
        # The JSON parameter values. This field is required for tool_call blocks. Unparsed raw strings can be retained.
        self.arguments = arguments
        # The logical call ID. This field is required for tool_call blocks.
        self.call_id = call_id
        # The access format identifier. This field is required for opaque blocks. Saving the format does not mean that its content can be interpreted or used across platforms.
        self.format = format
        # The tool name. This field is required for tool_call blocks. This content block only expresses the call intent.
        self.name = name
        # The actual text. This field is required for text and reasoning blocks.
        self.text = text
        # The content block type. This field determines the required fields.
        # 
        # This parameter is required.
        self.type = type
        # The JSON value. This field is required for json and opaque blocks. The data field is not used for opaque blocks.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arguments is not None:
            result['arguments'] = self.arguments

        if self.call_id is not None:
            result['callId'] = self.call_id

        if self.format is not None:
            result['format'] = self.format

        if self.name is not None:
            result['name'] = self.name

        if self.text is not None:
            result['text'] = self.text

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arguments') is not None:
            self.arguments = m.get('arguments')

        if m.get('callId') is not None:
            self.call_id = m.get('callId')

        if m.get('format') is not None:
            self.format = m.get('format')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

