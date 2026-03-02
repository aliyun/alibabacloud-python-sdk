# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AbbrevMonitorAlertRule(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        id: int = None,
        name: str = None,
        trigger_content: str = None,
        trigger_rule: str = None,
    ):
        self.create_time = create_time
        self.id = id
        self.name = name
        self.trigger_content = trigger_content
        self.trigger_rule = trigger_rule

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.trigger_content is not None:
            result['triggerContent'] = self.trigger_content

        if self.trigger_rule is not None:
            result['triggerRule'] = self.trigger_rule

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('triggerContent') is not None:
            self.trigger_content = m.get('triggerContent')

        if m.get('triggerRule') is not None:
            self.trigger_rule = m.get('triggerRule')

        return self

