# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLiveStreamWatermarkRuleRequest(DaraModel):
    def __init__(
        self,
        app: str = None,
        domain: str = None,
        owner_id: int = None,
        region_id: str = None,
        rule_id: str = None,
        stream: str = None,
    ):
        # The name of the application to which the live stream belongs.
        self.app = app
        # The streaming domain.
        # 
        # This parameter is required.
        self.domain = domain
        self.owner_id = owner_id
        self.region_id = region_id
        # The ID of the watermark rule.
        # 
        # >  You can obtain the rule ID by checking the value of the RuleId parameter that is returned by the [AddLiveStreamWatermarkRule](https://help.aliyun.com/document_detail/2848100.html) operation.
        self.rule_id = rule_id
        # The name of the stream. The following matching rules apply:
        # 
        # *   A stream name can be exactly matched, Example: liveStreamA.
        # *   Fuzzy match is also supported. The use of an asterisk (`*`) allows all approximate matches to be found.
        # *   You can place the asterisk before or after an approximate string.
        # 
        # > 
        # 
        # *   Fuzzy match: Only one asterisk (`*`) before or after an approximate string is allowed. The approximate string must be enclosed in `()`. Separate multiple strings with vertical bars (`|`).
        # 
        # *   For example, `*(t1|t2)` matches all streams whose name has the `t1` or `t2` suffix, and `(abc|123)*` matches all streams whose name has the `abc` or `123` prefix.
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app is not None:
            result['App'] = self.app

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.stream is not None:
            result['Stream'] = self.stream

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        return self

