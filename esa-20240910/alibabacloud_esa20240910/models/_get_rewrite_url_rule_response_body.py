# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRewriteUrlRuleResponseBody(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        config_type: str = None,
        query_string: str = None,
        request_id: str = None,
        rewrite_query_string_type: str = None,
        rewrite_uri_type: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_version: int = None,
        uri: str = None,
    ):
        self.config_id = config_id
        self.config_type = config_type
        self.query_string = query_string
        self.request_id = request_id
        self.rewrite_query_string_type = rewrite_query_string_type
        self.rewrite_uri_type = rewrite_uri_type
        self.rule = rule
        self.rule_enable = rule_enable
        self.rule_name = rule_name
        self.sequence = sequence
        self.site_version = site_version
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

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.query_string is not None:
            result['QueryString'] = self.query_string

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('QueryString') is not None:
            self.query_string = m.get('QueryString')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

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

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

