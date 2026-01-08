# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVpcFirewallTaskRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        lang: str = None,
        priority: str = None,
        task_action: str = None,
    ):
        self.content = content
        self.lang = lang
        self.priority = priority
        # This parameter is required.
        self.task_action = task_action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.task_action is not None:
            result['TaskAction'] = self.task_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')

        return self

