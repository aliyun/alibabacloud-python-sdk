# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEventRuleAttributeRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        rule_name: str = None,
        silence_time: str = None,
    ):
        self.region_id = region_id
        # The name of the event-triggered alert rule.
        # 
        # For information about how to obtain the name of an event-triggered alert rule, see [DescribeEventRuleList](https://help.aliyun.com/document_detail/114996.html).
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The mute period during which new alert notifications are not sent even if the trigger conditions are met.
        # 
        # Unit: seconds. Default value: 86400, which indicates one day.
        # 
        # >  Only one alert notification is sent during each mute period even if the metric value exceeds the alert threshold several times.
        self.silence_time = silence_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')

        return self

