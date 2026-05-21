# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Event(DaraModel):
    def __init__(
        self,
        content: str = None,
        event_id: str = None,
        event_type: str = None,
        function: str = None,
        is_truncated: bool = None,
        object_id: str = None,
        object_type: str = None,
        trigger_tenant_id: str = None,
        trigger_time: str = None,
        trigger_user_id: str = None,
        triggered_by: str = None,
    ):
        self.content = content
        self.event_id = event_id
        self.event_type = event_type
        self.function = function
        self.is_truncated = is_truncated
        self.object_id = object_id
        self.object_type = object_type
        self.trigger_tenant_id = trigger_tenant_id
        self.trigger_time = trigger_time
        self.trigger_user_id = trigger_user_id
        self.triggered_by = triggered_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.function is not None:
            result['Function'] = self.function

        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.trigger_tenant_id is not None:
            result['TriggerTenantId'] = self.trigger_tenant_id

        if self.trigger_time is not None:
            result['TriggerTime'] = self.trigger_time

        if self.trigger_user_id is not None:
            result['TriggerUserId'] = self.trigger_user_id

        if self.triggered_by is not None:
            result['TriggeredBy'] = self.triggered_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('Function') is not None:
            self.function = m.get('Function')

        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('TriggerTenantId') is not None:
            self.trigger_tenant_id = m.get('TriggerTenantId')

        if m.get('TriggerTime') is not None:
            self.trigger_time = m.get('TriggerTime')

        if m.get('TriggerUserId') is not None:
            self.trigger_user_id = m.get('TriggerUserId')

        if m.get('TriggeredBy') is not None:
            self.triggered_by = m.get('TriggeredBy')

        return self

