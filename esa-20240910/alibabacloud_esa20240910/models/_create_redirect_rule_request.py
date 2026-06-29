# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRedirectRuleRequest(DaraModel):
    def __init__(
        self,
        reserve_query_string: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_id: int = None,
        site_version: int = None,
        status_code: str = None,
        target_url: str = None,
        type: str = None,
    ):
        # Specifies whether to preserve the query string. Valid values:
        # 
        # - on: Enabled.
        # - off: Disabled.
        # 
        # This parameter is required.
        self.reserve_query_string = reserve_query_string
        # The rule content, which uses a conditional expression to match user requests. You do not need to set this parameter when adding a global configuration. Two scenarios are supported:
        # - Match all incoming requests: Set the value to true.
        # - Match specified requests: Set the value to a custom expression, such as (http.host eq \\"video.example.com\\").
        self.rule = rule
        # The rule switch. You do not need to set this parameter when adding a global configuration. Valid values:
        # - on: Enabled.
        # - off: Disabled.
        self.rule_enable = rule_enable
        # The rule name. You do not need to set this parameter when adding a global configuration.
        self.rule_name = rule_name
        # The rule execution order. A smaller value indicates a higher priority.
        self.sequence = sequence
        # The site ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The version number of the site configuration. For sites with configuration version management enabled, you can use this parameter to specify the site version on which the configuration takes effect. The default value is version 0.
        self.site_version = site_version
        # The response status code used by the node when responding to the client with the redirect address. Valid values:
        # 
        # - 301
        # - 302
        # - 303
        # - 307
        # - 308.
        # 
        # This parameter is required.
        self.status_code = status_code
        # The target URL after redirection.
        # 
        # This parameter is required.
        self.target_url = target_url
        # The redirect type. Valid values:
        # 
        # - static: Static pattern.
        # - dynamic: Dynamic pattern.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reserve_query_string is not None:
            result['ReserveQueryString'] = self.reserve_query_string

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

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.target_url is not None:
            result['TargetUrl'] = self.target_url

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReserveQueryString') is not None:
            self.reserve_query_string = m.get('ReserveQueryString')

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

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('TargetUrl') is not None:
            self.target_url = m.get('TargetUrl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

