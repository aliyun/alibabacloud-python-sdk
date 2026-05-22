# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListRewriteUrlRulesResponseBody(DaraModel):
    def __init__(
        self,
        configs: List[main_models.ListRewriteUrlRulesResponseBodyConfigs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        # List of rewrite URL configurations.
        self.configs = configs
        # The current page number.
        self.page_number = page_number
        # The size of the page.
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # The total number of items.
        self.total_count = total_count
        # Total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.configs:
            for v1 in self.configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Configs'] = []
        if self.configs is not None:
            for k1 in self.configs:
                result['Configs'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k1 in m.get('Configs'):
                temp_model = main_models.ListRewriteUrlRulesResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class ListRewriteUrlRulesResponseBodyConfigs(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        config_type: str = None,
        query_string: str = None,
        rewrite_query_string_type: str = None,
        rewrite_uri_type: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_version: int = None,
        uri: str = None,
    ):
        # Configuration ID.
        self.config_id = config_id
        # Configuration type. Value range:
        # - global: Global configuration;
        # - rule: Rule configuration;
        self.config_type = config_type
        # The rewritten query string.
        self.query_string = query_string
        # Query string rewrite type. Value range:
        # - static: Static mode.
        # - dynamic: Dynamic mode.
        self.rewrite_query_string_type = rewrite_query_string_type
        # URI rewrite type. Value range:
        # - static: Static mode.
        # - dynamic: Dynamic mode.
        self.rewrite_uri_type = rewrite_uri_type
        # Rule content, using conditional expressions to match user requests. Not required when adding a global configuration. There are two usage scenarios:
        # - Match all incoming requests: Set the value to true
        # - Match specific requests: Set the value to a custom expression, e.g., (http.host eq \\"video.example.com\\")
        self.rule = rule
        # Rule switch. Not required when adding a global configuration. Value range:
        # - on: Enabled.
        # - off: Disabled.
        self.rule_enable = rule_enable
        # Rule name. Not required when adding a global configuration.
        self.rule_name = rule_name
        # Rule execution order. The smaller the value, the higher the priority.
        self.sequence = sequence
        # Version number of the site configuration. For sites with version management enabled, you can use this parameter to specify the effective version of the configuration, defaulting to version 0.
        self.site_version = site_version
        # Target URI after rewriting.
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

