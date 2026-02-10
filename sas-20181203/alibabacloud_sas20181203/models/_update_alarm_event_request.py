# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateAlarmEventRequest(DaraModel):
    def __init__(
        self,
        alarm_event_id_list: List[int] = None,
        lang: str = None,
        operation_code: str = None,
    ):
        # The IDs of the alert events.
        self.alarm_event_id_list = alarm_event_id_list
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The operation that you want to perform on the alert events. Valid values:
        # 
        # *   **manual_handled**: handle the alert events.
        # *   **ignore**: igore the alert events.
        # *   **cancel_ignore**: remove the alert events from the whitelist.
        self.operation_code = operation_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_event_id_list is not None:
            result['AlarmEventIdList'] = self.alarm_event_id_list

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.operation_code is not None:
            result['OperationCode'] = self.operation_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmEventIdList') is not None:
            self.alarm_event_id_list = m.get('AlarmEventIdList')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('OperationCode') is not None:
            self.operation_code = m.get('OperationCode')

        return self

