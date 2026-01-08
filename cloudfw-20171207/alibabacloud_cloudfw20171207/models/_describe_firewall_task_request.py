# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeFirewallTaskRequest(DaraModel):
    def __init__(
        self,
        child_instance_id: str = None,
        lang: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        self.child_instance_id = child_instance_id
        self.lang = lang
        self.task_id = task_id
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

