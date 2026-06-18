# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateHttpRequestHeaderModificationRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        request_header_modification_shrink: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_id: int = None,
        site_version: int = None,
    ):
        # An array of objects that define Request Header modifications. Supported operations include add, del, and modify.
        # 
        # This parameter is required.
        self.request_header_modification_shrink = request_header_modification_shrink
        # The content of the Rule, which uses a Conditional Expression to match user requests. This parameter is not required when you add a global configuration. Supports two Use Cases:
        # 
        # - To match all incoming requests, set the value to true.
        # 
        # - To match specific requests, set the value to a custom expression, for example, (http.host eq "video.example.com").
        self.rule = rule
        # Specifies whether to enable the Rule. This parameter is not required when you add a global configuration. Valid values are:
        # 
        # - on: Enables the Rule.
        # 
        # - off: Disables the Rule.
        self.rule_enable = rule_enable
        # The name of the Rule. This parameter is not required when you add a global configuration.
        self.rule_name = rule_name
        # The execution order of the Rule. A smaller value indicates a higher priority.
        self.sequence = sequence
        # The ID of the Site. You can get this ID by calling the [ListSites](~~ListSites~~) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The Version of the Site configuration. For a Site with configuration versioning enabled, this parameter specifies the configuration\\"s target Version. The default value is 0.
        self.site_version = site_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        return self

