# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRewriteUrlRuleRequest(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        query_string: str = None,
        rewrite_query_string_type: str = None,
        rewrite_uri_type: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_id: int = None,
        uri: str = None,
    ):
        # Configuration ID. It can be obtained by calling the [ListRewriteUrlRules](https://help.aliyun.com/document_detail/2867480.html) interface.
        # 
        # This parameter is required.
        self.config_id = config_id
        # The query string after rewriting.
        self.query_string = query_string
        # Query string rewrite type. Value range:
        # - static: Static mode.
        # - dynamic: Dynamic mode.
        self.rewrite_query_string_type = rewrite_query_string_type
        # URI rewrite type. Value range:
        # - static: Static mode.
        # - dynamic: Dynamic mode.
        self.rewrite_uri_type = rewrite_uri_type
        # Rule content, using conditional expressions to match user requests. This parameter is not required when adding a global configuration. There are two usage scenarios:
        # - Match all incoming requests: Set the value to true
        # - Match specific requests: Set the value to a custom expression, for example: (http.host eq \\"video.example.com\\")
        self.rule = rule
        # Rule switch. This parameter is not required when adding a global configuration. Value range:
        # - on: Enable.
        # - off: Disable.
        self.rule_enable = rule_enable
        # Rule name. This parameter is not required when adding a global configuration.
        self.rule_name = rule_name
        self.sequence = sequence
        # Site ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) interface.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The target URI after rewriting.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

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

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

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

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

