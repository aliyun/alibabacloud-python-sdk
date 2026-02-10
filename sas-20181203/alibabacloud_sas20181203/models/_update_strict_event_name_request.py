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
        # List of strict alarms to be operated on. This list is a complete list, and any strict alarms not included in this list will have the opposite operation performed.
        # > You can call [DescribeStrictEventName](~~DescribeStrictEventName~~) to get the list of all strict mode alarms.
        # > -
        self.event_name_list = event_name_list
        # Sets the language type for requests and received messages, default is **zh**. Values:
        # 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Operation rule determination operator:
        # - *on*: Turn on the alarm
        # - *off*: Turn off the alarm
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

