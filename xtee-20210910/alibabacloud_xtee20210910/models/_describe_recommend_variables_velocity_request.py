# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRecommendVariablesVelocityRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        reg_id: str = None,
        task_id: int = None,
        variable_ids_str: str = None,
    ):
        # Set the language type for request and response, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Region Code
        self.reg_id = reg_id
        # Task ID
        # 
        # This parameter is required.
        self.task_id = task_id
        # Variable IDs
        self.variable_ids_str = variable_ids_str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.variable_ids_str is not None:
            result['variableIdsStr'] = self.variable_ids_str

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('variableIdsStr') is not None:
            self.variable_ids_str = m.get('variableIdsStr')

        return self

