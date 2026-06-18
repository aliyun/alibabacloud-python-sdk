# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateHttpResponseHeaderModificationRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        response_header_modification_shrink: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_id: int = None,
    ):
        # The ID of the Configuration. You can get this value by calling the [ListHttpResponseHeaderModificationRules](https://help.aliyun.com/document_detail/2867483.html) API.
        # 
        # This parameter is required.
        self.config_id = config_id
        # A list of objects, each defining a modification to a Response Header. Supported operations are `add`, `del`, and `modify`.
        self.response_header_modification_shrink = response_header_modification_shrink
        # The matching condition for the Rule, written as a Conditional Expression. This parameter is optional for global Configurations. Use cases:
        # 
        # - To match all incoming requests, set the value to `true`.
        # 
        # - To match specific requests, set the value to a custom expression, such as `(http.host eq "video.example.com")`.
        self.rule = rule
        # Specifies whether the rule is enabled. This parameter is optional for a global Configuration. Valid values:
        # 
        # - `on`: Enables the Rule.
        # 
        # - `off`: Disables the Rule.
        self.rule_enable = rule_enable
        # The name of the Rule. This parameter is optional for a global Configuration.
        self.rule_name = rule_name
        # The execution order for the Rule. A lower value indicates a higher priority.
        self.sequence = sequence
        # The ID of the Site. You can get this value by calling the [ListSites](~~ListSites~~) API.
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

        if self.response_header_modification_shrink is not None:
            result['ResponseHeaderModification'] = self.response_header_modification_shrink

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

        if m.get('ResponseHeaderModification') is not None:
            self.response_header_modification_shrink = m.get('ResponseHeaderModification')

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

