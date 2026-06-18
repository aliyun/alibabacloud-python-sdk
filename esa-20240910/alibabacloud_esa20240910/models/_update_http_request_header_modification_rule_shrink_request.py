# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateHttpRequestHeaderModificationRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        request_header_modification_shrink: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_id: int = None,
    ):
        # The configuration ID. Call the [ListHttpRequestHeaderModificationRules](https://help.aliyun.com/document_detail/2867483.html) operation to obtain it.
        # 
        # This parameter is required.
        self.config_id = config_id
        # Specifies the modifications for the request header. Supported operations include `add`, `del`, and `modify`.
        self.request_header_modification_shrink = request_header_modification_shrink
        # The Conditional Expression used to match User Requests. This parameter is not required for a Global Configuration. Use cases:
        # 
        # - To match all incoming requests, set the value to `true`.
        # 
        # - To match specific requests, use a custom expression, for example, `(http.host eq "video.example.com")`.
        self.rule = rule
        # Specifies whether the Rule is enabled. This parameter is not required for a Global Configuration. Valid values:
        # 
        # - `on`: Enable
        # 
        # - `off`: Disable
        self.rule_enable = rule_enable
        # The name of the Rule. This parameter is not required for a Global Configuration.
        self.rule_name = rule_name
        # The execution priority of the Rule. A smaller value indicates a higher priority.
        self.sequence = sequence
        # The site ID. Call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation to obtain it.
        # 
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.request_header_modification_shrink is not None:
            result['RequestHeaderModification'] = self.request_header_modification_shrink

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('RequestHeaderModification') is not None:
            self.request_header_modification_shrink = m.get('RequestHeaderModification')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

