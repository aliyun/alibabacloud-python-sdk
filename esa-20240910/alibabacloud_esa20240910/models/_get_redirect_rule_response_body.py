# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRedirectRuleResponseBody(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        config_type: str = None,
        request_id: str = None,
        reserve_query_string: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_version: int = None,
        status_code: str = None,
        target_url: str = None,
        type: str = None,
    ):
        # Configuration ID.
        self.config_id = config_id
        # Configuration type. Possible values:
        # - global: Global configuration.
        # - rule: Rule-based configuration.
        self.config_type = config_type
        # Request ID.
        self.request_id = request_id
        # Preserve query string. Possible values:
        # - on: Enabled.
        # - off: Disabled.
        self.reserve_query_string = reserve_query_string
        # Rule content, using conditional expressions to match user requests. This parameter is not required when adding a global configuration. There are two usage scenarios:
        # - Match all incoming requests: Set the value to true
        # - Match specific requests: Set the value to a custom expression, e.g., (http.host eq \\"video.example.com\\")
        self.rule = rule
        # Rule switch. This parameter is not required when adding a global configuration. Possible values:
        # - on: Enabled.
        # - off: Disabled.
        self.rule_enable = rule_enable
        # Rule name. This parameter is not required when adding a global configuration.
        self.rule_name = rule_name
        # Rule execution order. The smaller the value, the higher the priority.
        self.sequence = sequence
        # The version number of the site configuration. For sites with version management enabled, this parameter can specify the effective version of the site, defaulting to version 0.
        self.site_version = site_version
        # Response status code used by the node to respond to the client with the redirect address. Possible values:
        # - 301
        # - 302
        # - 303
        # - 307
        # - 308
        self.status_code = status_code
        # Target URL after redirection.
        self.target_url = target_url
        # Redirect type. Possible values:
        # - static: Static mode.
        # - dynamic: Dynamic mode.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

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

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('TargetUrl') is not None:
            self.target_url = m.get('TargetUrl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

