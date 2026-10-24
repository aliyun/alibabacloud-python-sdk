# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class SandboxLifecycleEvent(DaraModel):
    def __init__(
        self,
        action: str = None,
        build_id: str = None,
        description: str = None,
        event_data: Dict[str, Any] = None,
        event_id: str = None,
        event_type: str = None,
        level: str = None,
        occurred_at: str = None,
        reason: str = None,
        sandbox_id: str = None,
        team_id: str = None,
        template_id: str = None,
    ):
        # The action that triggered the event.
        self.action = action
        # The template build ID. This field is not returned if there is no associated build.
        self.build_id = build_id
        # The event description.
        self.description = description
        # The event data as a JSON object. The specific fields vary depending on the event type.
        self.event_data = event_data
        # The event ID.
        self.event_id = event_id
        # The event type.
        self.event_type = event_type
        # The event category. Valid values: INFO and WARNING.
        self.level = level
        # The time when the event occurred. The time is in UTC RFC3339 format and supports fractional seconds.
        self.occurred_at = occurred_at
        # The reason for the event. This field is not returned if there is no reason.
        self.reason = reason
        # The instance ID.
        self.sandbox_id = sandbox_id
        # The ID of the team to which the event belongs.
        self.team_id = team_id
        # The template ID.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.build_id is not None:
            result['buildID'] = self.build_id

        if self.description is not None:
            result['description'] = self.description

        if self.event_data is not None:
            result['eventData'] = self.event_data

        if self.event_id is not None:
            result['eventID'] = self.event_id

        if self.event_type is not None:
            result['eventType'] = self.event_type

        if self.level is not None:
            result['level'] = self.level

        if self.occurred_at is not None:
            result['occurredAt'] = self.occurred_at

        if self.reason is not None:
            result['reason'] = self.reason

        if self.sandbox_id is not None:
            result['sandboxID'] = self.sandbox_id

        if self.team_id is not None:
            result['teamID'] = self.team_id

        if self.template_id is not None:
            result['templateID'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('buildID') is not None:
            self.build_id = m.get('buildID')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('eventData') is not None:
            self.event_data = m.get('eventData')

        if m.get('eventID') is not None:
            self.event_id = m.get('eventID')

        if m.get('eventType') is not None:
            self.event_type = m.get('eventType')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('occurredAt') is not None:
            self.occurred_at = m.get('occurredAt')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('sandboxID') is not None:
            self.sandbox_id = m.get('sandboxID')

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        if m.get('templateID') is not None:
            self.template_id = m.get('templateID')

        return self

