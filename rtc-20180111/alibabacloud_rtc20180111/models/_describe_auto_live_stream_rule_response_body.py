# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeAutoLiveStreamRuleResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rules: List[main_models.DescribeAutoLiveStreamRuleResponseBodyRules] = None,
    ):
        self.request_id = request_id
        self.rules = rules

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeAutoLiveStreamRuleResponseBodyRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class DescribeAutoLiveStreamRuleResponseBodyRules(DaraModel):
    def __init__(
        self,
        call_back: str = None,
        channel_id_prefixes: List[str] = None,
        channel_ids: List[str] = None,
        create_time: str = None,
        media_encode: int = None,
        play_domain: str = None,
        rule_id: int = None,
        rule_name: str = None,
        status: str = None,
    ):
        self.call_back = call_back
        self.channel_id_prefixes = channel_id_prefixes
        self.channel_ids = channel_ids
        self.create_time = create_time
        self.media_encode = media_encode
        self.play_domain = play_domain
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_back is not None:
            result['CallBack'] = self.call_back

        if self.channel_id_prefixes is not None:
            result['ChannelIdPrefixes'] = self.channel_id_prefixes

        if self.channel_ids is not None:
            result['ChannelIds'] = self.channel_ids

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode

        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallBack') is not None:
            self.call_back = m.get('CallBack')

        if m.get('ChannelIdPrefixes') is not None:
            self.channel_id_prefixes = m.get('ChannelIdPrefixes')

        if m.get('ChannelIds') is not None:
            self.channel_ids = m.get('ChannelIds')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')

        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

