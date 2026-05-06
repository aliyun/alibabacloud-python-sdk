# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAutomaticFrequencyControlConfigResponseBody(DaraModel):
    def __init__(
        self,
        action_type: str = None,
        enable: str = None,
        interval: int = None,
        level: str = None,
        punish_time: int = None,
        request_id: str = None,
        rule_id: int = None,
        threshold: int = None,
    ):
        self.action_type = action_type
        self.enable = enable
        self.interval = interval
        self.level = level
        self.punish_time = punish_time
        self.request_id = request_id
        self.rule_id = rule_id
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.level is not None:
            result['Level'] = self.level

        if self.punish_time is not None:
            result['PunishTime'] = self.punish_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('PunishTime') is not None:
            self.punish_time = m.get('PunishTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

