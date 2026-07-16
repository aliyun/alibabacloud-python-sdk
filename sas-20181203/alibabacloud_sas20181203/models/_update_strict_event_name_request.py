# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateStrictEventNameRequest(DaraModel):
    def __init__(
        self,
        event_name_list: List[str] = None,
        lang: str = None,
        operator: str = None,
    ):
        # The list of strict mode alerts to operate on. This is a full list. Strict mode alerts not included in this list will have the opposite action applied.
        # > Call [DescribeStrictEventName](~~DescribeStrictEventName~~) to obtain the list of all strict mode alerts.
        # > -.
        self.event_name_list = event_name_list
        # The language of the request and response. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The operator for the rule action. Valid values:
        # - *on*: enables alerting
        # - *off*: disables alerting.
        # 
        # This parameter is required.
        self.operator = operator

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_name_list is not None:
            result['EventNameList'] = self.event_name_list

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.operator is not None:
            result['Operator'] = self.operator

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventNameList') is not None:
            self.event_name_list = m.get('EventNameList')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        return self

