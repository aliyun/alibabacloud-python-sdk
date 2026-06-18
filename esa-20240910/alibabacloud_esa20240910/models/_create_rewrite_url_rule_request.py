# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRewriteUrlRuleRequest(DaraModel):
    def __init__(
        self,
        query_string: str = None,
        rewrite_query_string_type: str = None,
        rewrite_uri_type: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_id: int = None,
        site_version: int = None,
        uri: str = None,
    ):
        # The query string after the rewrite.
        self.query_string = query_string
        # The query string rewrite mode. Valid values:
        # 
        # - `static`: Static mode.
        # 
        # - `dynamic`: Dynamic mode.
        self.rewrite_query_string_type = rewrite_query_string_type
        # The URI rewrite mode. Valid values:
        # 
        # - `static`: Static mode.
        # 
        # - `dynamic`: Dynamic mode.
        self.rewrite_uri_type = rewrite_uri_type
        # The conditional expression used to match user requests. This parameter is not required when you add a global configuration. Two use cases are supported:
        # 
        # - To match all inbound requests, set the value to `true`.
        # 
        # - To match specific requests, set the value to a custom expression, such as `(http.host eq "video.example.com")`.
        self.rule = rule
        # This parameter is not required when you add a global configuration. Valid values:
        # 
        # - `on`: Enables the rule.
        # 
        # - `off`: Disables the rule.
        self.rule_enable = rule_enable
        # The rule name. This parameter is not required when you add a global configuration.
        self.rule_name = rule_name
        # The execution priority of the rule. A lower value indicates a higher priority.
        self.sequence = sequence
        # The site ID. Obtain it by calling the [ListSites](~~ListSites~~) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # If configuration versioning is enabled for the site, this parameter specifies the target version. The default value is 0.
        self.site_version = site_version
        # The target URI after the rewrite.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.query_string is not None:
            result['QueryString'] = self.query_string

        if self.rewrite_query_string_type is not None:
            result['RewriteQueryStringType'] = self.rewrite_query_string_type

        if self.rewrite_uri_type is not None:
            result['RewriteUriType'] = self.rewrite_uri_type

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

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryString') is not None:
            self.query_string = m.get('QueryString')

        if m.get('RewriteQueryStringType') is not None:
            self.rewrite_query_string_type = m.get('RewriteQueryStringType')

        if m.get('RewriteUriType') is not None:
            self.rewrite_uri_type = m.get('RewriteUriType')

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

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

