# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class DeleteEventsRequest(DaraModel):
    def __init__(
        self,
        body: main_models.DeleteEventsRequestBody = None,
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
            temp_model = main_models.DeleteEventsRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class DeleteEventsRequestBody(DaraModel):
    def __init__(
        self,
        event_ids: List[str] = None,
        scope: main_models.DeleteEventsRequestBodyScope = None,
    ):
        # A list of 1 to 100 unique event IDs. Only events owned by the current session are deleted.
        # 
        # This parameter is required.
        self.event_ids = event_ids
        # The scope for precise session location.
        # 
        # This parameter is required.
        self.scope = scope

    def validate(self):
        if self.scope:
            self.scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_ids is not None:
            result['eventIds'] = self.event_ids

        if self.scope is not None:
            result['scope'] = self.scope.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventIds') is not None:
            self.event_ids = m.get('eventIds')

        if m.get('scope') is not None:
            temp_model = main_models.DeleteEventsRequestBodyScope()
            self.scope = temp_model.from_map(m.get('scope'))

        return self

class DeleteEventsRequestBodyScope(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        session_id: str = None,
        team_id: str = None,
        user_id: str = None,
    ):
        # The business agent ID.
        self.agent_id = agent_id
        # The ID of the precisely located session.
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

