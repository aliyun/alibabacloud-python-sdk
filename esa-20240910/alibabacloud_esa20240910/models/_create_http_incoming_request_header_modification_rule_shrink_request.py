# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateHttpIncomingRequestHeaderModificationRuleShrinkRequest(DaraModel):
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
        # The configurations of modifying request headers. You can add, delete, or modify a request header.
        # 
        # This parameter is required.
        self.request_header_modification_shrink = request_header_modification_shrink
        # The content of the rule. A conditional expression is used to match a user request. You do not need to set this parameter when you add global configuration. Use cases:
        # 
        # *   true: Match all incoming requests.
        # *   Set the value to a custom expression, for example: (http.host eq "video.example.com"): Match the specified request
        self.rule = rule
        # Specifies whether to enable the rule. Valid values: You do not need to set this parameter when you add global configuration. Valid values:
        # 
        # *   on
        # *   off
        self.rule_enable = rule_enable
        # The rule name. You do not need to set this parameter when you add global configuration.
        self.rule_name = rule_name
        # The order in which the rule is executed. A smaller value gives priority to the rule.
        self.sequence = sequence
        # The website ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The version number of the website configurations. You can use this parameter to specify a version of your website to apply the feature settings. By default, version 0 is used.
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

