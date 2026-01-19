# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRecommendEventRuleRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        event_code: str = None,
        event_name: str = None,
        recommend_rule_ids_str: str = None,
        reg_id: str = None,
        task_id: int = None,
    ):
        # Set the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Event code.
        self.event_code = event_code
        # Event name.
        self.event_name = event_name
        # Strategy ID.
        self.recommend_rule_ids_str = recommend_rule_ids_str
        # Region code.
        self.reg_id = reg_id
        # Task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.event_name is not None:
            result['eventName'] = self.event_name

        if self.recommend_rule_ids_str is not None:
            result['recommendRuleIdsStr'] = self.recommend_rule_ids_str

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')

        if m.get('recommendRuleIdsStr') is not None:
            self.recommend_rule_ids_str = m.get('recommendRuleIdsStr')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

