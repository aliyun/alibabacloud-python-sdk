# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConvertPlaybookRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        role_for: int = None,
        role_type: str = None,
        taskflow: str = None,
    ):
        # Language type for request and response messages. Values:
        # 
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # User ID for the administrator to switch to another member\\"s perspective.
        self.role_for = role_for
        # View type. Values:
        # 
        # - 0: Current Alibaba Cloud account view.
        # - 1: View for all accounts under the enterprise.
        self.role_type = role_type
        # XML configuration information for playbook orchestration.
        # 
        # This parameter is required.
        self.taskflow = taskflow

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.taskflow is not None:
            result['Taskflow'] = self.taskflow

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('Taskflow') is not None:
            self.taskflow = m.get('Taskflow')

        return self

