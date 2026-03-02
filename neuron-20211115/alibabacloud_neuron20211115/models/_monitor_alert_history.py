# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MonitorAlertHistory(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        event_state: str = None,
        id: int = None,
        name: str = None,
        rule_desc: str = None,
        rule_name: str = None,
        start_time: str = None,
        type: str = None,
        uuid: str = None,
    ):
        self.end_time = end_time
        self.event_state = event_state
        self.id = id
        self.name = name
        self.rule_desc = rule_desc
        self.rule_name = rule_name
        self.start_time = start_time
        # This parameter is required.
        self.type = type
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.event_state is not None:
            result['eventState'] = self.event_state

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.rule_desc is not None:
            result['ruleDesc'] = self.rule_desc

        if self.rule_name is not None:
            result['ruleName'] = self.rule_name

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.type is not None:
            result['type'] = self.type

        if self.uuid is not None:
            result['uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('eventState') is not None:
            self.event_state = m.get('eventState')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('ruleDesc') is not None:
            self.rule_desc = m.get('ruleDesc')

        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')

        return self

